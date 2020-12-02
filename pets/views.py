import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.decorators import user_required
from common.forms import CommentForm
from common.models import Comment
from pets.forms import PetForm
from pets.models import Pet, Like


def list_pets(request):
    context = {"pets": Pet.objects.all()}
    return render(request, 'pets/pet_list.html', context)


@login_required
def pet_create(request):
    if request.method == 'POST':
        pet = PetForm(request.POST, request.FILES)
        if pet.is_valid():
            pet.save()
        return redirect('list pets')
    else:
        context = {'form': PetForm()}
        return render(request, 'pets/pet_create.html', context)


@login_required
def pet_delete(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {"pet": pet}
        return render(request, 'pets/pet_delete.html', context)
    else:
        pet.delete()
        return redirect('list pets')


@user_required
def pets_edit(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        old_image = pet.image
        pet = PetForm(request.POST, request.FILES, instance=pet)
        if pet.is_valid():
            if old_image:
                os.remove(old_image.path)  # !!! delete old image before saving the new one
            pet.save()
            # # if we want to delete likes of this editable object
            # Like.objects.filter(pet_id=pet.id).delete()
        return redirect('pet details', pk)
    else:
        context = {"pet": pet, 'form': PetForm(instance=pet)}
        return render(request, 'pets/pet_edit.html', context)


@login_required
def pets_like(request, pk):
    like = Like.objects.filter(user_id=request.user.userprofile, pet_id=pk).first()
    if like:
        like.delete()
    else:
        pet = Pet.objects.get(pk=pk)
        like = Like(test=str(pk), user=request.user.userprofile)
        like.pet = pet
        like.save()
    return redirect('pet details', pk)


@login_required
def show_pets_details_and_commits(request, pk):
    pet = Pet.objects.get(pk=pk)
    context = {
        "pet": pet,
        "comment": CommentForm(),
        'is_owner': request.user == pet.user.user,
        'has_liked': pet.like_set.filter(user_id=request.user.userprofile.id).exists(),
    }
    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comment = comment.clean()['comment']
            com = Comment(pet=pet, comment=comment, user=request.user.userprofile)
            com.save()
            context = {"pet": pet, "comment": CommentForm()}

    return render(request, 'pets/pet_detail.html', context)
