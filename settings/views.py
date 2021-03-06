from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

from profiles.models import UserProfile, CompanyProfile
from .models import Team, Shift
from .forms import CompanyProfileForm, TeamsForm, ShiftForm

import stripe
import datetime


@login_required
def settings_global(request):
    """
    Show the global settings According to the company id
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    # make sure only admins can change the company settings
    if profile.level == 'admin':

        company = get_object_or_404(CompanyProfile, company_id=profile.company_id)

        if request.method == 'POST':
            form = CompanyProfileForm(request.POST, instance=company)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully')
            else:
                messages.error(request, 'Update failed. Please ensure the form is valid.')

        else:
            form = CompanyProfileForm(instance=company)

        template = 'settings/settings_global.html'
        context = {
            'profile': profile,
            'company': company,
            'form_company': form,
        }

        return render(request, template, context)

    else:
        messages.info(request, 'Only Admins can edit the Global Settings.')

    return redirect(reverse('planning', ))


@login_required
def change_plan(request):
    """
    Change the sign-up plan
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    # make sure only admins can change the subscription plan
    if profile.level == 'admin':

        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY

        company = get_object_or_404(CompanyProfile, company_id=profile.company_id)

        if request.method == 'POST':
            data = request.POST
            company.plan = data['plan']
            company.payment = data['payment']
            company.renewal_date = datetime.date.today()
            company.save()
            messages.info(request, "The plan is successfully changed")

        else:
            form = CompanyProfileForm(instance=company)

        # Something needs to happen here
        stripe_total = 100

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        template = 'settings/change_plan.html'
        context = {
            'profile': profile,
            'company': company,
            'form_company': form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)

    else:
        messages.info(request, "Sorry, only Admins can change the plan.")

    return redirect(reverse('settings_global', ))


@login_required
def teams(request):
    """
    Show all teams related to the company
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    teams = Team.objects.filter(company_id=profile.company_id)

    template = 'settings/teams.html'
    context = {
        'teams': teams,
        'profile': profile
    }
    return render(request, template, context)


@login_required
def add_team(request):
    """
    Add a new team
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    # make sure only managers and admins can add a team
    if profile.level == 'admin' or profile.level == 'manager':

        if request.method == 'POST':
            form = TeamsForm(request.POST)
            if form.is_valid():
                team = form.save(commit=False)
                team.company_id = profile.company_id
                team.save()
                messages.success(request, 'Team added successfully')

            else:
                messages.error(request, 'Update failed. Please ensure the form is valid.')

            teams = Team.objects.filter(company_id=profile.company_id)

            template = 'settings/teams.html'
            context = {
                'teams': teams,
                'profile': profile
            }
            return render(request, template, context)

        else:
            teams = Team.objects.filter(company_id=profile.company_id)
            """
            Here will be an if-statemen once stripe is working, otherwise it's hard to check the functionality:
            company = get_object_or_404(CompanyProfile, company_id=profile.company_id)
            if company.plan == 'starter' and len(teams) == 1:
            if company.plan == 'basic' and len(teams) == 2:
            if company.plan == 'advanced' and len(teams) == 4:
            if company.plan == 'max' and len(teams) == 12:
            """
            form = TeamsForm()

            template = 'settings/add_team.html'
            context = {
                'form': form,
                'profile': profile,
                'teams': teams
            }

            return render(request, template, context)

    else:
        messages.info(request, "Sorry, you are not authorized to add teams. Ask a Manager or Admin.")

    return redirect(reverse('teams', ))


@login_required
def edit_team(request, team_id):
    """
    Edit a team, out of teams
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    # make sure only managers and admins can edit a team
    if profile.level == 'admin' or profile.level == 'manager':

        team_selected = get_object_or_404(Team, pk=team_id)
        if request.method == 'POST':
            form = TeamsForm(request.POST, instance=team_selected)
            if form.is_valid():
                form.save()
                messages.success(request, 'Team edited successfully')
                teams = Team.objects.filter(company_id=profile.company_id)
                template = 'settings/teams.html'
                context = {
                    'teams': teams,
                    'profile': profile
                }
                return render(request, template, context)

            else:
                messages.error(request, 'Save failed. Please ensure the form is valid.')
        else:
            form = TeamsForm(instance=team_selected)

            teams = Team.objects.filter(company_id=profile.company_id)
            template = 'settings/edit_team.html'
            context = {
                'form': form,
                'teams': teams,
                'team_selected': team_selected,
                'profile': profile
            }

        return render(request, template, context)

    else:
        messages.info(request, "Sorry, you are not authorized to edit teams. Ask a Manager or Admin.")

    return redirect(reverse('teams', ))


def delete_team(request, team_id):
    """
    Delete a team after checking if no users are attached
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    # make sure only admins and managers can delete a team
    if profile.level == 'admin' or profile.level == 'manager':
        users = UserProfile.objects.filter(company_id=profile.company_id, team=team_id)
        if len(users) == 0:
            team = get_object_or_404(Team, pk=team_id)
            team.delete()
            messages.success(request, 'Team deleted!')

        else:
            messages.error(request, "Users are still part of this team. Attach users to a different team in 'User Management' or delete them.")

    else:
        messages.info(request, "Sorry, you are not authorized to delete teams. Ask a Manager or Admin.")

    return redirect(reverse('teams', ))


def shifts(request):
    """
    Show all shifts related to the company, sorted by team
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    shifts = Shift.objects.filter(company_id=profile.company_id)

    template = 'settings/shifts.html'
    context = {
        'shifts': shifts,
        'profile': profile
    }
    return render(request, template, context)


@login_required
def edit_shift(request, shift_id):
    """
    Edit shifts
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    # making sure only admins and managers can edit shifts
    if profile.level == 'admin' or profile.level == 'manager':
        shift_selected = get_object_or_404(Shift, pk=shift_id)
        if request.method == 'POST':
            form = ShiftForm(request.POST, instance=shift_selected)
            if form.is_valid():
                form.save()
                messages.success(request, 'Shift edited successfully')
                shifts = Shift.objects.filter(company_id=profile.company_id)
                template = 'settings/shifts.html'
                context = {
                    'shifts': shifts,
                    'profile': profile
                }
                return render(request, template, context)

            else:
                messages.error(request, 'Save failed. Please ensure the form is valid.')
        else:
            form = ShiftForm(instance=shift_selected)

        shifts = Shift.objects.filter(company_id=profile.company_id)
        template = 'settings/edit_shift.html'
        context = {
            'form': form,
            'shifts': shifts,
            'shift_selected': shift_selected,
            'profile': profile
        }

        return render(request, template, context)

    else:
        messages.info(request, "Sorry, you are not authorized to edit shifts. Ask a Manager or Admin.")

    return redirect(reverse('shifts', ))


@login_required
def add_shift(request):
    """
    Add a new role
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    # making sure only admins and managers can add shifts
    if profile.level == 'admin' or profile.level == 'manager':

        if request.method == 'POST':
            form = ShiftForm(request.POST)
            if form.is_valid():
                shift = form.save(commit=False)
                shift.company_id = profile.company_id
                shift.save()
                messages.success(request, 'Shift added successfully')

            else:
                messages.error(request, 'Save failed. Please ensure the form is valid.')

            shifts = Shift.objects.filter(company_id=profile.company_id)

            template = 'settings/shifts.html'
            context = {
                'shifts': shifts,
                'profile': profile
            }
            return render(request, template, context)

        else:
            form = ShiftForm()
            shifts = Shift.objects.filter(company_id=profile.company_id)

            template = 'settings/add_shift.html'
            context = {
                'form': form,
                'profile': profile,
                'shifts': shifts
            }

            return render(request, template, context)

    else:
        messages.info(request, "Sorry, you are not authorized to add shifts. Ask a Manager or Admin.")

    return redirect(reverse('shifts', ))
