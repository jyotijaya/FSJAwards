from django.core.exceptions import PermissionDenied
def is_coordinator(usr):
    user = get_FSJ_user(usr)
    if not isinstance(user, Coordinator):
        raise PermissionDenied
    return True
# Contains the decordator to ensure the user is logged into the system and a test to ensure the user accessing the page is valid.
@login_required
@user_passes_test(is_coordinator)
def coordinator_home(request, FSJ_user):
    context = get_standard_context(FSJ_user)   
    template = loader.get_template("FSJ/home.html")
    return HttpResponse(template.render(context, request))