from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect

from .models import Customer


def authentication_check(request, required_roles=None, required_GET=None):
    """
    :param request: page request
    :param required_roles: role values of users allowed to view the page
    :param required_GET: GET values that the page needs to function properly
    :return: A redirect request if there's a problem, None otherwise
    """
    # Authentication check. Users not logged in cannot view the page
    if not request.user.is_authenticated:
        request.session['alert_danger'] = "You must be logged in to view the page."
        return HttpResponseRedirect('/login/')
    # Sanity Check. Users without accounts cannot interact with virtual clinic
    try:
        request.user.account
    except ObjectDoesNotExist:
        request.session['alert_danger'] = "Your account was not properly created, please try a different account."
        return HttpResponseRedirect('/logout/')
    # Permission check
    if required_roles and request.user.account.role not in required_roles:
        request.session['alert_danger'] = "You don't have permission to view the page."
        return HttpResponseRedirect('/error/denied/')
    # Validation check. Make sure this page has any required GET keys
    if required_GET:
        for key in required_GET:
            if key not in request.GET:
                request.session['alert_danger'] = "Looks like you tried to use a malformed URL."
                return HttpResponseRedirect('/error/denied/')


def register_user(email, password, first_name, last_name, phone):
    user = User.objects.create_user(
        email.lower(),
        email.lower(),
        password,
    )
    customer = Customer(
        firstname=first_name,
        lastname=last_name,
        phone=phone,
    )
    customer.save()

    return user
