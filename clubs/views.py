from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import User
from .models import Club, Membership, Project, Event
from .forms import ClubForm, EventForm, ProjectForm, ProjectStatusForm


# Create your views here.
@login_required
def club_list(request):
    
    user_logged = request.user
    
    clubs_advisor = user_logged.advised_clubs.all().order_by('name')

    member_clubs = user_logged.joined_clubs.exclude(pk__in=clubs_advisor).order_by('name')

    context = {
        'clubs_advisor': clubs_advisor,
        'member_clubs': member_clubs,
    }
    return render(request, 'clubs/club_list.html', context)

@login_required
def club_detail(request, pk):

    club = get_object_or_404(Club, pk=pk)

    is_owner = (request.user == club.advisor)

    if request.method == 'POST' and is_owner:
        username_to_add = request.POST.get('username')
        try:
            user_to_add = User.objects.get(username=username_to_add)
            
            # Verifica se ele JÁ é membro
            is_already_member = Membership.objects.filter(club=club, user=user_to_add).exists()
            
            if is_already_member:
                messages.error(request, f'O usuário "{username_to_add}" já é membro deste clube.')
            else:
                Membership.objects.create(club=club, user=user_to_add, position='Member')
                messages.success(request, f'"{username_to_add}" foi adicionado ao clube com sucesso!')
            
            #Redireciona para a mesma página (para limpar o formulário)
            return redirect('club-detail', pk=club.pk)

        except User.DoesNotExist:
            messages.error(request, f'Usuário "{username_to_add}" não encontrado.')

    projects = club.projects.all().order_by('-start_date') 
    events = club.events.all().order_by('-event_date')
    members = Membership.objects.filter(club=club).order_by('user__first_name')

    context = {
        'club': club,
        'projects': projects,
        'events': events,
        'members': members,
        'is_owner': is_owner,
    }
    
    return render(request, 'clubs/club_detail.html', context)

@login_required
def club_create(request):

    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES)    

        if form.is_valid():
            new_club = form.save(commit=False)
            new_club.advisor = request.user
            new_club.save()
            return redirect('club_detail', pk=new_club.pk)

    else:
        form = ClubForm()

    context = {
        'form': form,
        }   
    return render(request, 'clubs/club_create.html', context) 

@login_required
def delete_member(request, pk, membership_id):
    club = get_object_or_404(Club, pk=pk)
    membership = get_object_or_404(Membership, pk=membership_id)

    if request.user != club.advisor or membership.club != club:
        messages.error(request, 'Você não tem permissão para realizar esta ação.')
        return redirect('club-detail', pk=club.pk)
    

    if request.method == 'POST':
        member_name = membership.user.username
        membership.delete()
        messages.success(request, f'Membro "{member_name}" removido com sucesso do clube.')
        return redirect('club-detail', pk=club.pk)

    return redirect('club-detail', pk=club.pk)    


@login_required
def club_edit(request, pk):
    club = get_object_or_404(Club, pk=pk)
    if request.user != club.advisor:
        messages.error(request, 'ERRO: Você não tem permissão para editar este clube.')
        return redirect('club-detail', pk=club.pk)
    
    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES, instance=club)

        if form.is_valid():
            form.save()
            messages.success(request, 'Informações do clube atualizadas com sucesso!')
            return redirect('club-detail', pk=club.pk)
        
    else:
        form = ClubForm(instance=club)

    context = {
        'form': form,
        'club': club,
    }

    return render(request, 'clubs/club_edit.html', context)


@login_required
def club_delete(request, pk):
    club = get_object_or_404(Club, pk=pk)
    if request.user != club.advisor:
        messages.error(request, 'ERRO: Você não tem permissão para deletar este clube.')
        return redirect('club-detail', pk=club.pk)
    
    if request.method == 'POST':
        club_name = club.name
        club.delete()
        messages.success(request, f'Clube "{club_name}" deletado com sucesso!')
        return redirect('club-list')
    
    context = {
        'club': club,
    }
    return render(request, 'clubs/club_delete_confirm.html', context)

login_required
def add_event(request, pk):
    club = get_object_or_404(Club, pk=pk)

    if request.user != club.advisor:
        messages.error(request, 'ERRO: Você não tem permissão para adicionar eventos a este clube.')
        return redirect('club-detail', pk=club.pk)
    
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.club = club
            event.create_by = request.user
            event.save()
            messages.success(request, 'Evento adicionado com sucesso!')
            return redirect('club-detail', pk=club.pk)

    else:
        form = EventForm()

    context = {
        'form': form,
        'club': club,
    }

    return render(request, 'clubs/add_event.html', context)        

login_required
def project_create(request, pk):
    club = get_object_or_404(Club, pk=pk)

    if request.user != club.advisor:
        messages.error(request, 'ERRO: Você não tem permissão para adicionar projetos a este clube.')
        return redirect('club-detail', pk=club.pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)            
            project.club = club
            project.save()
            messages.success(request, 'Novo projeto criado com sucesso!')
            
            return redirect('club-detail', pk=club.pk)

    else:
        form = ProjectForm()

    context = {
        'form': form,
        'club': club,
    }
    return render(request, 'clubs/project_create.html', context)


    
login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    club = project.club

    is_advisor = (request.user == club.advisor)
    is_member = Membership.objects.filter(club=club, user=request.user).exists()

    if not (is_advisor or is_member):
        messages.error(request, 'Você não tem permissão para ver este projeto.')
        return redirect('club-detail', pk=club.pk)
    
    if request.method == 'POST' and is_advisor:
        status_form = ProjectStatusForm(request.POST, instance=project)
        if status_form.is_valid():
            status_form.save()
            messages.success(request, 'Status do projeto atualizado com sucesso!')
            return redirect('project-detail', pk=project.pk)
        
    else:
        status_form = ProjectStatusForm(instance=project)    
    

    context = {
            'project': project,
            'is_advisor': is_advisor,
            'status_form': status_form,
        }
    return render(request, 'clubs/project_detail.html', context)