from django.shortcuts import render , redirect , get_list_or_404,get_object_or_404
from .models import Contact
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# contact view function
@login_required(login_url='login')
def contacts(request):
    if not request.user.is_authenticated:
        messages.error(request, "login fast")
        return redirect('login')
    contacts = Contact.objects.filter(user=request.user)
    return render(request, 'contact_page.html', { "contacts" : contacts })



# new contact add function
@login_required(login_url='login')
def add_contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        company = request.POST.get("company")

        Contact.objects.create(
            user = request.user,
            name = name,
            email = email,
            phone = phone,
            company = company
        )
        return redirect("contacts")
    
    return render(request, 'add_new_contact.html')



# contact edit function
@login_required(login_url='login')
def update_contact(request, id): 

    contact = get_object_or_404(Contact, id=id, user = request.user)

    if request.method == "POST":
        contact.name = request.POST.get("name")
        contact.email = request.POST.get("email")
        contact.phone = request.POST.get("phone")
        contact.company = request.POST.get("company")
        contact.save()
        return redirect("contacts")
    
    return render(request, 'update_contact_page.html' , {"contact": contact})


# contact remove/delete function
@login_required(login_url='login')

def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id, user = request.user)
    if request.method == "POST":
        contact.delete()
        return redirect("contacts")
    return render(request, 'contact_page.html')
    