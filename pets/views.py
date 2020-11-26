from django.shortcuts import render, redirect

from common.forms import CommentForm
from common.models import Comment
from pets.forms import PetForm
from pets.models import Pet, Like


def list_pets(request):
    context = {"pets": Pet.objects.all()}
    return render(request, 'pets/pet_list.html', context)


def pet_create(request):
    if request.method == 'POST':
        pet = PetForm(request.POST)
        if pet.is_valid():
            pet.save()
        return redirect('list pets')
    else:
        context = {'form': PetForm()}
        return render(request, 'pets/pet_create.html', context)


def pet_delete(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {"pet": pet}
        return render(request, 'pets/pet_delete.html', context)
    else:
        pet.delete()
        return redirect('list pets')


def pets_edit(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        pet = PetForm(request.POST, instance=pet)
        if pet.is_valid():
            pet.save()
            pet = Pet.objects.get(pk=pk)
        return redirect('pet details', pk)
    else:
        context = {"pet": pet, 'form': PetForm(instance=pet)}
        return render(request, 'pets/pet_edit.html', context)


def pets_like(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(test=str(pk))
    like.pet = pet
    like.save()
    return redirect('list pets')


def show_pets_details_and_commits(request, pk):
    pet = Pet.objects.get(pk=pk)
    context = {"pet": pet, "comment": CommentForm()}
    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comment = comment.clean()['comment']
            com = Comment(pet=pet, comment=comment)
            com.save()
            context = {"pet": pet, "comment": CommentForm()}

    return render(request, 'pets/pet_detail.html', context)


