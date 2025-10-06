from django.shortcuts import render , redirect , get_list_or_404,get_object_or_404
from .models import Contact


# contact view function
def contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_page.html', { "contacts" : contacts })



# new contact add function
def add_contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        company = request.POST.get("company")

        Contact.objects.create(
            name = name,
            email = email,
            phone = phone,
            company = company
        )
        return redirect("contacts")
    
    return render(request, 'add_new_contact.html')



# contact edit function
def update_contact(request, id): 

    contact = get_object_or_404(Contact, id=id)

    if request.method == "POST":
        contact.name = request.POST.get("name")
        contact.email = request.POST.get("email")
        contact.phone = request.POST.get("phone")
        contact.company = request.POST.get("company")
        contact.save()
        return redirect("contacts")
    
    return render(request, 'update_contact_page.html' , {"contact": contact})


# contact remove/delete function
def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        contact.delete()
        return redirect("contacts")
    return render(request, 'contact_page.html')
    