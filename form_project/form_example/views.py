from django.shortcuts import render, redirect
from .forms import ExampleForm, CourseModelForm
from .models import Course
from django.contrib import messages


# Create your views here.
def form_example(request):
    form = ExampleForm()
    for name in request.POST:
        messages.success("{}: {}".format(name, request.POST.getlist(name)))
        print("{}: {}".format(name, request.POST.getlist(name)))

    return render(
        request, "form-example.html", {"method": request.method, "form": form}
    )


def course_form(request):
    # first, is this a returned (filled) form?
    if request.method == 'POST':
        # if it is, then take the information from the page and populate the Django form object
        form = CourseModelForm(request.POST)
        # is the data clean?
        if form.is_valid():
            #if yes, save to database
            form.save()
            messages.success(request, "Saved the course...")
        else:
            # couldn't save the data
            messages.error(request, "Failed to save...")


        return redirect("form_example")

    # not a POST, but a GET
    else:
        # make an empty form object
        form = CourseModelForm()
        # get all Course objects from database
        courses = Course.objects.all()
        return render(request, "course-form.html", {"form": form, "courses": courses})
