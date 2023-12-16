from django.shortcuts import render, HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from projects.models import Deprem,Sel,ResponsePlan,ResponseCat
from projects.forms import *
from django.contrib import messages
from django.urls import reverse
from math import sqrt,exp,pow
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import copy
from django.forms import modelformset_factory, inlineformset_factory, formset_factory
import pandas as pd




def about(request):
    return render(request, 'projects/aboutUs.html')


def depremAllProject(request):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':

            prjs_list = Deprem.objects.order_by('-crtDate')

            return render(request, 'projects/depremAllPrj.html', {'prjDpr': prjs_list})
        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')


def allProject(request):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':

            projectsDeprem = Deprem.objects.order_by('-crtDate')
            projectsSel = Sel.objects.order_by('-crtDate')

            context = {
                'prjDpr': projectsDeprem,
                'prjSel': projectsSel
            }

            return render(request, 'projects/allPrj.html', context)
        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')
    
    
    
    
    
def selAllProject(request):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':

            prjs_list = Sel.objects.order_by('-crtDate')

            return render(request, 'projects/selAllPrj.html', {'prjSel': prjs_list})
        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')
    
    
    
    

def depremView(request,id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':
            proje = get_object_or_404(Deprem,id=id)


            projectResponses = proje.responses.response.order_by('-time')

            context = {
                'project': proje,
                'responses': projectResponses
            }
            return render(request, 'projects/depremView.html',context)
        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')
    
    
    
def selView(request,id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':

            proje = get_object_or_404(Sel,id=id)

            projectResponses = proje.responses.response.order_by('-time')

            context = {
                'project': proje,
                'responses': projectResponses

            }
            return render(request, 'projects/selView.html',context)
        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')


def depremInfView(request,id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':

            project = get_object_or_404(Deprem,id=id)


            context = {
                'project': project,

            }
            return render(request, 'projects/depremInfView.html',context)
        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')

def selInfView(request,id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':

            project = get_object_or_404(Sel,id=id)


            context = {
                'project': project,
            }
            return render(request, 'projects/selInfView.html',context)
        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')





def depremUpdate(request,id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':
            project = get_object_or_404(Deprem, id=id)
            projectResponses = project.responses.response.order_by('-time')

            context = {
                'project': project,
                'responses': projectResponses

            }
            return render(request, 'projects/depremProjectUpdate.html', context)
        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')
    
    
    
    

def selUpdate(request,id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':
            project = get_object_or_404(Sel, id=id)
            projectResponses = project.responses.response.order_by('-time')

            context = {
                'project': project,
                'responses': projectResponses
            }
            return render(request, 'projects/selProjectUpdate.html', context)
        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')
    
    
    

def depremProjectDelete(request,id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[0].name == 'Disaster Manager':
            project = get_object_or_404(Deprem, id=id)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/notPermission.html')
            else:
                project.delete()
                return redirect("projects:depremAllProject")
        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')
    
    
def selProjectDelete(request,id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[0].name == 'Disaster Manager':
            project = get_object_or_404(Sel, id=id)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/notPermission.html')
            else:
                project.delete()
                return redirect("projects:selAllProject")
        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')
    
    
    
    

def depremProjectInfUpdate(request,id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[0].name == 'Disaster Manager':
            project = get_object_or_404(Deprem, id=id)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/notPermission.html')
            else:
                form = depremInfForm(request.POST or None,instance=project)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(project.get_update_url())

                context = {
                    'form':form,
                    'project':project
                }
                return render(request, 'projects/depremUpdate.html', context)
        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')
    
    
    
def selProjectInfUpdate(request,id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[0].name == 'Disaster Manager':
            project = get_object_or_404(Sel, id=id)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/notPermission.html')
            else:
                form = selInfForm(request.POST or None,instance=project)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(project.get_update_url())

                context = {
                    'form':form,
                    'project':project
                }
                return render(request, 'projects/selUpdate.html', context)
        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')
    
    
    
def depremFeatureUpdate(request,id):

    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[0].name == 'Disaster Manager':
            project = get_object_or_404(Deprem, id=id)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/notPermission.html')
            else:
                form = depremFeatureForm(request.POST or None,instance=project)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(reverse('projects:depremCalculateResponses', kwargs={'id': project.id}))

                context = {
                    'form': form,
                    'project': project
                }
                return render(request, 'projects/depremUpdate.html', context)
        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')
    
    
    
    
def selFeatureUpdate(request,id):

    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[0].name == 'Disaster Manager':
            project = get_object_or_404(Sel, id=id)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/notPermission.html')
            else:
                form = selFeatureForm(request.POST or None,instance=project)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(reverse('projects:selCalculateResponses', kwargs={'id': project.id}))

                context = {
                    'form': form,
                    'project': project
                }
                return render(request, 'projects/selUpdate.html', context)
        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')




def newResponseDpr(request,pId,rId):

    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[0].name == 'Disaster Manager':
            project = get_object_or_404(Deprem, id=pId)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/notPermission.html')
            else:
                objects = project.responses.response.all()

                for obj in objects:
                    if obj.id == rId:
                        obj.save()

                        form = responseForm(request.POST or None, instance=obj)
                        if form.is_valid():
                            obj = form.save()

                            return HttpResponseRedirect(reverse('projects:depremView', kwargs={'id': project.id}))
                        context = {
                        'form': form,
                        }
                        return render(request, 'projects/depremUpdate.html', context)

        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')


def newResponseSel(request,pId,rId):

    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[0].name == 'Disaster Manager':
            project = get_object_or_404(Sel, id=pId)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/notPermission.html')
            else:
                objects = project.responses.response.all()

                for obj in objects:
                    if obj.id == rId:
                        obj.save()

                        form = responseForm(request.POST or None, instance=obj)
                        if form.is_valid():
                            obj = form.save()

                            return HttpResponseRedirect(reverse('projects:selView', kwargs={'id': project.id}))

                        context = {
                        'form': form,
                        }
                        return render(request, 'projects/selUpdate.html', context)

        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')


def viewResponseDpr(request,pId,rId):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':
            project = get_object_or_404(Deprem, id=pId)
            objects = project.responses.response.all()
            for obj in objects:
                if obj.id == rId:
                    context = {
                        'response': obj,
                    }
                    return render(request, 'projects/viewResponseDpr.html', context)
        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')




def viewResponseSel(request,pId,rId):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':
            project = get_object_or_404(Sel, id=pId)
            objects = project.responses.response.all()
            for obj in objects:
                if obj.id == rId:
                    context = {
                        'response': obj,
                    }
                    return render(request, 'projects/viewResponseSel.html', context)
        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')



def addResponseDpr(request,pId):

    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[0].name == 'Disaster Manager':
            project = get_object_or_404(Deprem, id=pId)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/notPermission.html')
            else:
                dummyPrjResponses = project.responses
                newResponse = ResponsePlan()
                newResponse.id = None
                form = responseForm(request.POST or None)
                if form.is_valid():
                    data = form.cleaned_data
                    newResponse.reaction = data['reaction']
                    newResponse.time = data['time']
                    newResponse.date = data['date']
                    newResponse.effect = data['effect']
                    newResponse.responsible = data['responsible']
                    newResponse.save()
                    dummyPrjResponses.save()
                    dummyPrjResponses.response.add(newResponse)
                    project.save()
                    project.responses = dummyPrjResponses

                    return HttpResponseRedirect(reverse('projects:depremView', kwargs={'id': project.id}))
                context = {
                    'form': form,
                }
                return render(request, 'projects/depremAddRsp.html', context)

        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')



def addResponseSel(request,pId):

    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[
            0].name == 'Disaster Manager':
            project = get_object_or_404(Sel, id=pId)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/notPermission.html')
            else:
                dummyPrjResponses = project.responses
                newResponse = ResponsePlan()
                newResponse.id = None
                form = responseForm(request.POST or None)
                if form.is_valid():
                    data = form.cleaned_data
                    newResponse.reaction = data['reaction']
                    newResponse.time = data['time']
                    newResponse.date = data['date']
                    newResponse.effect = data['effect']
                    newResponse.responsible = data['responsible']
                    newResponse.save()
                    dummyPrjResponses.save()
                    dummyPrjResponses.response.add(newResponse)
                    project.save()
                    project.responses = dummyPrjResponses

                    return HttpResponseRedirect(reverse('projects:selView', kwargs={'id': project.id}))
                context = {
                    'form': form,
                }
                return render(request, 'projects/selAddRsp.html', context)

        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')





def deleteResponseDpr(request,pId,rId):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':
            project = get_object_or_404(Deprem, id=pId)


            objects = project.responses.response.all()
            for obj in objects:
                if obj.id == rId:
                    obj.delete()

            projectResponses = project.responses.response.order_by('-time')

            context = {
                'project': project,
                'responses': projectResponses
            }
            return render(request, 'projects/depremView.html',context)
        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')


def deleteResponseSel(request,pId,rId):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':
            project = get_object_or_404(Sel, id=pId)


            objects = project.responses.response.all()
            for obj in objects:
                if obj.id == rId:
                    obj.delete()

            projectResponses = project.responses.response.order_by('-time')

            context = {
                'project': project,
                'responses': projectResponses
            }
            return render(request, 'projects/depremView.html',context)
        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')




def depremTermPrj(request,id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[0].name == 'Disaster Manager':
            project = get_object_or_404(Deprem, id=id)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/notPermission.html')
            else:

                project.terminate = True
                project.save()

                projectResponses = project.responses.response.order_by('-time')

                context = {
                    'project': project,
                    'responses': projectResponses
                }

                return render(request, 'projects/depremView.html', context)

        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')
    
    
    
def selTermPrj(request,id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[0].name == 'Disaster Manager':
            project = get_object_or_404(Sel, id=id)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/notPermission.html')
            else:

                project.terminate = True
                project.save()

                projectResponses = project.responses.response.order_by('-time')

                context = {
                    'project': project,
                    'responses': projectResponses
                }
                return render(request, 'projects/selView.html', context)

        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')
    


def depremProjectCreate(request):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name=='Disaster Specialist' or request.user.groups.all()[0].name=='Disaster Manager':
            form = depremForm(request.POST or None)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = request.user

                catlg = get_object_or_404(ResponseCat, catId=1)

                project.responses = catlg
                project.save()

                return HttpResponseRedirect(reverse('projects:depremCalculateResponses', kwargs={'id': project.id}))

            context = {
                'form': form,
            }
            return render(request, 'projects/depremCreate.html', context)
        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')



def selProjectCreate(request):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name=='Disaster Specialist' or request.user.groups.all()[0].name=='Disaster Manager':
            form = selForm(request.POST or None)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = request.user

                catlg = get_object_or_404(ResponseCat, catId=1)

                project.responses = catlg
                project.save()

                return HttpResponseRedirect(reverse('projects:selCalculateResponses', kwargs={'id': project.id}))

            context = {
                'form': form,
            }
            return render(request, 'projects/selCreate.html', context)
        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')



def depremCalculateResponses(request,id):

    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[ 0].name == 'Disaster Manager':
            prj = get_object_or_404(Deprem, pk=id)
            if request.user.groups.all()[0].name != 'Disaster Manager' and prj.user != request.user:
                return render(request, 'accounts/notPermission.html')
            else:
                maxTable, maxValues = depremSimilarityAlgorithm(request, prj.id)
                i = 0
                cnt = len(maxTable)
                simProjects = []
                simValues = []
                while i < 5:
                    tmp = get_object_or_404(Deprem, id=maxTable[i])
                    simProjects.append(tmp)
                    simValues.append(maxValues[i])
                    i = i + 1

                dummyPrjResponses = ResponseCat()
                dummyPrjResponses.catId = id
                # benzer projelerin responsları ekleniyor burda

                for project in simProjects:
                    tmpResponses = project.responses.response.all()
                    for obj in tmpResponses:
                        newResponse = ResponsePlan()
                        newResponse.id = None
                        newResponse.reaction = obj.reaction
                        newResponse.time = obj.time
                        newResponse.date = obj.date
                        newResponse.effect = obj.effect
                        newResponse.responsible = obj.responsible
                        newResponse.save()
                        dummyPrjResponses.save()
                        dummyPrjResponses.response.add(newResponse)
                        prj.save()
                        prj.responses = dummyPrjResponses

                firstFive = []
                i = 0
                while i < 5:
                    similars = []
                    similars.append(simProjects[i].id)
                    similars.append(simProjects[i].projectName)
                    similars.append(simProjects[i].summary)
                    similars.append(simProjects[i].crtDate)
                    similars.append(simProjects[i].user)
                    similars.append(round(simValues[i], 4))
                    firstFive.append(similars)

                    i = i + 1

                context = {
                    'project': prj,
                    'simProjects': firstFive,

                }
                return render(request, 'projects/depremSimilarProject.html', context)


        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')




def selCalculateResponses(request,id):

    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[ 0].name == 'Disaster Manager':
            prj = get_object_or_404(Sel, pk=id)
            if request.user.groups.all()[0].name != 'Disaster Manager' and prj.user != request.user:
                return render(request, 'accounts/notPermission.html')
            else:

                maxTable,maxValues = selSimilarityAlgorithm(request, prj.id)
                print("hata burda", prj.projectName)
                i = 0
                cnt = len(maxTable)
                simProjects = []
                simValues = []
                while i<5:
                    tmp = get_object_or_404(Sel, id=maxTable[i])
                    simProjects.append(tmp)
                    simValues.append(maxValues[i])
                    i = i+1

                dummyPrjResponses = ResponseCat()
                dummyPrjResponses.catId = id
                # benzer projelerin responsları ekleniyor burda

                for project in simProjects:
                    tmpResponses = project.responses.response.all()
                    for obj in tmpResponses:
                        newResponse = ResponsePlan()
                        newResponse.reaction = obj.reaction
                        newResponse.time = obj.time
                        newResponse.date = obj.date
                        newResponse.effect = obj.effect
                        newResponse.responsible = obj.responsible
                        newResponse.save()
                        dummyPrjResponses.save()
                        dummyPrjResponses.response.add(newResponse)
                        prj.save()
                        prj.responses = dummyPrjResponses

                firstFive = []
                i = 0
                while i < 5:
                    similars = []
                    similars.append(simProjects[i].id)
                    similars.append(simProjects[i].projectName)
                    similars.append(simProjects[i].summary)
                    similars.append(simProjects[i].crtDate)
                    similars.append(simProjects[i].user)
                    similars.append(round(simValues[i], 4))
                    firstFive.append(similars)

                    i = i + 1

                context = {
                    'project': prj,
                    'simProjects': firstFive,

                }
                return render(request, 'projects/selSimilarProject.html', context)


        else:
            return render(request, 'accounts/notPermission.html')
    else:
        return render(request, 'accounts/notLogin.html')




def depremSimilarityAlgorithm(request, id):

    project = get_object_or_404(Deprem, id=id)
    maxTable = []
    maxValues = []

    varMaxDel = depremDeltaMaxes(id)

    i = 0
    while i< 5:
        maxSim = -1
        maxSimId = -1
        projects = Deprem.objects.all()
        for prjCurr in projects:
            if prjCurr.terminate != False :
                if prjCurr.id not in maxTable and prjCurr.id != project.id:
                    dummySim = depremCalculateSim(project.id,prjCurr.id,varMaxDel)
                    if maxSim < dummySim:
                        maxSim = dummySim
                        maxSimId = prjCurr.id
        maxTable.append(maxSimId)
        maxValues.append(maxSim)
        i = i+1

    return maxTable,maxValues


def selSimilarityAlgorithm(request, id):

    project = get_object_or_404(Sel, id=id)
    maxTable = []
    maxValues = []


    varMaxDel = selDeltaMaxes(id)

    i = 0
    while i< 5:
        maxSim = -1
        maxSimId = -1
        projects = Sel.objects.all()
        for prjCurr in projects:
            if prjCurr.terminate != False :
                if prjCurr.id not in maxTable and prjCurr.id != project.id:
                    dummySim = selCalculateSim(project.id,prjCurr.id,varMaxDel)
                    if maxSim < dummySim:
                        maxSim = dummySim
                        maxSimId = prjCurr.id
        maxTable.append(maxSimId)
        maxValues.append(maxSim)
        i = i+1

    return maxTable,maxValues


def depremCalculateSim(id1,id2,maxDelta):




    # symbol
    EmergencyTimeWght = 0.060048557026748
    EmergencyLocationWght = 0.030232148195847
    PotentialSecondaryDisastersWght = 0.062363092070137

    # number
    MagnitudeWght = 0.067161779905293
    FocalDepthWght = 0.063638474772217
    BuildingCollapseRateWght = 0.031913883946852
    PopulationDensityWght = 0.031781599687703


    # fuzzy
    WeatherConditionWght = 0.030081208076213
    BuildingDensityWght = 0.032759984926028
    PotentialHazardousWght = 0.031765056356517
    EmergencyResourceCompWght = 0.059906821029412
    EmergencyResourceDurWght = 0.057857988923343
    InitialResponseWght = 0.0597062885185
    RoadTranspWght = 0.0281
    AirTranspWght = 0.0271
    RailwayTranspWght = 0.0258
    MaritimeTranspWght = 0.0251
    HealthInfrWght = 0.0285
    WaterSupplyWght = 0.0273
    CommunicationInfrWght = 0.0279
    NaturalgasWght = 0.0251
    PowergridWght = 0.0269
    SufficiencyTemporaryWght = 0.054276635356218
    CapacityWasteWght = 0.029860927040779





    similarity = 0

    project1 = get_object_or_404(Deprem, id=id1)
    project2 = get_object_or_404(Deprem, id=id2)

    choseVar = depremFuzziesChose(project1,project2)
    WeatherConditionChose = choseVar[0]
    BuildingDensityChose = choseVar[1]
    PotentialHazardousChose = choseVar[2]
    EmergencyResourceCompChose = choseVar[3]
    EmergencyResourceDurChose = choseVar[4]
    InitialResponseChose = choseVar[5]
    RoadTranspChose = choseVar[6]
    AirTranspChose = choseVar[7]
    RailwayTranspChose = choseVar[8]
    MaritimeTranspChose = choseVar[9]
    HealthInfrChose = choseVar[10]
    WaterSupplyChose = choseVar[11]
    CommunicationInfrChose = choseVar[12]
    NaturalgasChose = choseVar[13]
    PowergridChose = choseVar[14]
    SufficiencyTemporaryChose = choseVar[15]
    CapacityWasteChose = choseVar[16]


    # numberMax
    MagnitudeMax = maxDelta[0]
    FocalDepthMax = maxDelta[1]
    BuildingCollapseRateMax = maxDelta[2]
    PopulationDensityMax = maxDelta[3]

    # fuzzyMax
    WeatherConditionMax = maxDelta[4]
    BuildingDensityMax = maxDelta[5]
    PotentialHazardousMax = maxDelta[6]
    EmergencyResourceCompMax = maxDelta[7]
    EmergencyResourceDurMax = maxDelta[8]
    InitialResponseMax = maxDelta[9]
    RoadTranspMax = maxDelta[10]
    AirTranspMax = maxDelta[11]
    RailwayTranspMax= maxDelta[12]
    MaritimeTranspMax= maxDelta[13]
    HealthInfrMax = maxDelta[14]
    WaterSupplyMax = maxDelta[15]
    CommunicationInfrMax = maxDelta[16]
    NaturalgasMax = maxDelta[17]
    PowergridMax = maxDelta[18]
    SufficiencyTemporaryMax = maxDelta[19]
    CapacityWasteMax = maxDelta[20]



    # symbol
    if project1.EmergencyTime == project2.EmergencyTime:
        similarity = similarity + EmergencyTimeWght*1

    if project1.EmergencyLocation == project2.EmergencyLocation:
        similarity = similarity + EmergencyLocationWght*1

    if project1.PotentialSecondaryDisasters == project2.PotentialSecondaryDisasters:
        similarity = similarity + PotentialSecondaryDisastersWght*1


    # number
    if MagnitudeMax == 0:
        similarity = similarity + MagnitudeWght * 1
    else:
        delta = (1/MagnitudeMax)*pow(sqrt(abs(project1.MagnitudeEarthquake - project2.MagnitudeEarthquake)),0.5)
        similarity = similarity + MagnitudeWght*exp(-delta)

    if FocalDepthMax == 0:
        similarity = similarity + FocalDepthWght * 1
    else :
        delta = (1 / FocalDepthMax) * pow(sqrt(abs(project1.FocalDepth - project2.FocalDepth)), 0.5)
        similarity = similarity + FocalDepthWght * exp(-delta)

    if BuildingCollapseRateMax == 0:
        similarity = similarity + BuildingCollapseRateWght*1
    else:
        delta = (1 / BuildingCollapseRateMax) * pow(sqrt(abs(project1.BuildingCollapseRate - project2.BuildingCollapseRate)), 0.5)
        similarity = similarity + BuildingCollapseRateWght * exp(-delta)

    if PopulationDensityMax == 0:
        similarity = similarity + PopulationDensityWght*1
    else :
        delta = (1 / PopulationDensityMax) * pow(sqrt(abs(project1.PopulationDensity - project2.PopulationDensity)), 0.5)
        similarity = similarity + PopulationDensityWght * exp(-delta)



    # fuzzy
    if WeatherConditionMax == 0:
        similarity = similarity + WeatherConditionWght*1
    else:
        delta = (1 / WeatherConditionMax) * WeatherConditionChose
        similarity = similarity + WeatherConditionWght * exp(-delta)

    if BuildingDensityMax == 0:
        similarity = similarity + BuildingDensityWght*1
    else :
        delta = (1 / BuildingDensityMax) * BuildingDensityChose
        similarity = similarity + BuildingDensityWght * exp(-delta)

    if PotentialHazardousMax == 0:
        similarity = similarity + PotentialHazardousWght*1
    else:
        delta = (1 / PotentialHazardousMax) * PotentialHazardousChose
        similarity = similarity + PotentialHazardousWght * exp(-delta)

    if EmergencyResourceCompMax == 0:
        similarity = similarity +EmergencyResourceCompWght*1
    else:
        delta = (1 / EmergencyResourceCompMax) * EmergencyResourceCompChose
        similarity = similarity + EmergencyResourceCompWght * exp(-delta)

    if EmergencyResourceDurMax == 0:
        similarity = similarity + EmergencyResourceDurWght*1
    else :
        delta = (1 / EmergencyResourceDurMax) * EmergencyResourceDurChose
        similarity = similarity + EmergencyResourceDurWght * exp(-delta)

    if InitialResponseMax == 0:
        similarity = similarity +InitialResponseWght*1
    else:
        delta = (1 / InitialResponseMax) * InitialResponseChose
        similarity = similarity + InitialResponseWght * exp(-delta)

    if RoadTranspMax == 0:
        similarity = similarity + RoadTranspWght*1
    else:
        delta = (1 / RoadTranspMax) * RoadTranspChose
        similarity = similarity + RoadTranspWght * exp(-delta)

    if AirTranspMax == 0:
        similarity = similarity + AirTranspWght*1
    else:
        delta = (1 / AirTranspMax) * AirTranspChose
        similarity = similarity + AirTranspWght * exp(-delta)

    if RailwayTranspMax == 0:
        similarity = similarity + RailwayTranspWght*1
    else:
        delta = (1 / RailwayTranspMax) * RailwayTranspChose
        similarity = similarity + RailwayTranspWght * exp(-delta)

    if MaritimeTranspMax == 0:
        similarity = similarity + MaritimeTranspWght*1
    else:
        delta = (1 / MaritimeTranspMax) * MaritimeTranspChose
        similarity = similarity + MaritimeTranspWght * exp(-delta)

    if HealthInfrMax == 0:
        similarity = similarity +HealthInfrWght*1
    else:
        delta = (1 / HealthInfrMax) * HealthInfrChose
        similarity = similarity + HealthInfrWght * exp(-delta)

    if WaterSupplyMax == 0:
        similarity = similarity + WaterSupplyWght*1
    else:
        delta = (1 / WaterSupplyMax) * WaterSupplyChose
        similarity = similarity + WaterSupplyWght * exp(-delta)

    if CommunicationInfrMax == 0:
        similarity = similarity + CommunicationInfrWght*1
    else:
        delta = (1 / CommunicationInfrMax) * CommunicationInfrChose
        similarity = similarity + CommunicationInfrWght * exp(-delta)

    if NaturalgasMax == 0:
        similarity = similarity + NaturalgasWght*1
    else:
        delta = (1 / NaturalgasMax) * NaturalgasChose
        similarity = similarity + NaturalgasWght * exp(-delta)

    if PowergridMax == 0:
        similarity = similarity + PowergridWght*1
    else:
        delta = (1 / PowergridMax) * PowergridChose
        similarity = similarity + PowergridWght * exp(-delta)

    if SufficiencyTemporaryMax == 0:
        similarity = similarity + SufficiencyTemporaryWght*1
    else:
        delta = (1 / SufficiencyTemporaryMax) * SufficiencyTemporaryChose
        similarity = similarity + SufficiencyTemporaryWght * exp(-delta)

    if CapacityWasteMax == 0:
        similarity = similarity + CapacityWasteWght*1
    else:
        delta = (1 / CapacityWasteMax) * CapacityWasteChose
        similarity = similarity + CapacityWasteWght * exp(-delta)


    return similarity



def selCalculateSim(id1,id2,maxDelta):


    # numberWeight
    MaxPrecipInteWght = 0.09199847853287
    SinglePrecipPerWght = 0.0782179871022
    AveragePrecipWght = 0.087023702223219
    MaxWaterDepWght = 0.083641707575501
    DamageAreaWght = 0.0653197367304
    RescueWorkWght = 0.105970439098994
    EmrResDurWght = 0.10641358242577
    AltituRegWght = 0.053525492358055
    SlopeRegWght = 0.060583319347845

    # fuzzyWeight
    CondRoadWght = 0.067601686879495
    EmrResCompWght = 0.133229850310478
    BuildDensWght = 0.066474017415173


    # numberMaxes
    MaxPrecipInteMax = maxDelta[0]
    SinglePrecipPerMax = maxDelta[1]
    AveragePrecipMax = maxDelta[2]
    MaxWaterDepMax = maxDelta[3]
    DamageAreaMax = maxDelta[4]
    RescueWorkMax = maxDelta[5]
    EmrResDurMax = maxDelta[6]
    AltituRegMax = maxDelta[7]
    SlopeRegMax = maxDelta[8]

    # fuzzyMaxes
    CondRoadMax = maxDelta[9]
    EmrResCompMax = maxDelta[10]
    BuildDensMax = maxDelta[11]



    similarity = 0

    project1 = get_object_or_404(Sel, id=id1)
    project2 = get_object_or_404(Sel, id=id2)

    choseVar = selFuzziesChose(project1,project2)
    CondRoadChose = choseVar[0]
    EmrResCompChose = choseVar[1]
    BuildDensChose = choseVar[2]




    if MaxPrecipInteMax == 0:
        similarity = similarity + MaxPrecipInteWght * 1
    else :
        delta = (1 / MaxPrecipInteMax) * pow(sqrt(abs(project1.MaximumPrecipitationIntensity - project2.MaximumPrecipitationIntensity)), 0.5)
        similarity = similarity + MaxPrecipInteWght * exp(-delta)

    if SinglePrecipPerMax == 0:
        similarity = similarity + SinglePrecipPerWght*1
    else:
        delta = (1 / SinglePrecipPerMax) * pow(sqrt(abs(project1.SinglePrecipitationPeriod - project2.SinglePrecipitationPeriod)), 0.5)
        similarity = similarity + SinglePrecipPerWght * exp(-delta)

    if AveragePrecipMax == 0:
        similarity = similarity + AveragePrecipWght*1
    else :
        delta = (1 / AveragePrecipMax) * pow(sqrt(abs(project1.AveragePrecipitation - project2.AveragePrecipitation)), 0.5)
        similarity = similarity + AveragePrecipWght * exp(-delta)

    if MaxWaterDepMax == 0:
        similarity = similarity + MaxWaterDepWght*1
    else :
        delta = (1 / MaxWaterDepMax) * pow(sqrt(abs(project1.MaximumWaterDepth - project2.MaximumWaterDepth)), 0.5)
        similarity = similarity + MaxWaterDepWght * exp(-delta)

    if DamageAreaMax == 0:
        similarity = similarity + DamageAreaWght*1
    else :
        delta = (1 / DamageAreaMax) * pow(sqrt(abs(project1.DamageArea - project2.DamageArea)), 0.5)
        similarity = similarity + DamageAreaWght * exp(-delta)

    if RescueWorkMax == 0:
        similarity = similarity + RescueWorkWght*1
    else :
        delta = (1 / RescueWorkMax) * pow(sqrt(abs(project1.RescueWorker - project2.RescueWorker)), 0.5)
        similarity = similarity + RescueWorkWght * exp(-delta)

    if EmrResDurMax == 0:
        similarity = similarity + EmrResDurWght*1
    else :
        delta = (1 / EmrResDurMax) * pow(sqrt(abs(project1.EmergencyResourceDuration - project2.EmergencyResourceDuration)), 0.5)
        similarity = similarity + EmrResDurWght * exp(-delta)

    if AltituRegMax == 0:
        similarity = similarity + AltituRegWght*1
    else :
        delta = (1 / AltituRegMax) * pow(sqrt(abs(project1.AltitudeRegion - project2.AltitudeRegion)), 0.5)
        similarity = similarity + AltituRegWght * exp(-delta)

    if SlopeRegMax == 0:
        similarity = similarity + SlopeRegWght*1
    else :
        delta = (1 / SlopeRegMax) * pow(sqrt(abs(project1.SlopeRegion - project2.SlopeRegion)), 0.5)
        similarity = similarity + SlopeRegWght * exp(-delta)

    if CondRoadMax == 0:
        similarity = similarity + CondRoadWght*1
    else:
        delta = (1 / CondRoadMax) * CondRoadChose
        similarity = similarity + CondRoadWght * exp(-delta)

    if EmrResCompMax == 0:
        similarity = similarity + EmrResCompWght*1
    else :
        delta = (1 / EmrResCompMax) * EmrResCompChose
        similarity = similarity + EmrResCompWght * exp(-delta)

    if BuildDensMax == 0:
        similarity = similarity + BuildDensWght*1
    else:
        delta = (1 / BuildDensMax) * BuildDensChose
        similarity = similarity + BuildDensWght * exp(-delta)

    return similarity



def depremDeltaMaxes(id):

    # number
    MagnitudeMax = 0
    FocalDepthMax = 0
    BuildingCollapseRateMax = 0
    PopulationDensityMax = 0

    # fuzzy
    WeatherConditionMax = 0
    BuildingDensityMax = 0
    PotentialHazardousMax = 0
    EmergencyResourceCompMax = 0
    EmergencyResourceDurMax = 0
    InitialResponseMax = 0
    RoadTranspMax = 0
    AirTranspMax = 0
    RailwayTranspMax = 0
    MaritimeTranspMax = 0
    HealthInfrMax = 0
    WaterSupplyMax = 0
    CommunicationInfrMax = 0
    NaturalgasMax = 0
    PowergridMax = 0
    SufficiencyTemporaryMax = 0
    CapacityWasteMax = 0

    project = get_object_or_404(Deprem, id=id)
    prjs = Deprem.objects.all()

    varMaxDel = []

    i = 0
    count = prjs.count()
    while (i<count):
        dummyProject = prjs.order_by('id')[i]
        if project.id != dummyProject.id:
            #number

            if MagnitudeMax < pow((sqrt(abs(project.MagnitudeEarthquake-dummyProject.MagnitudeEarthquake))),0.5):
                MagnitudeMax = pow((sqrt(abs(project.MagnitudeEarthquake-dummyProject.MagnitudeEarthquake))),0.5)

            if FocalDepthMax < pow((sqrt(abs(project.FocalDepth-dummyProject.FocalDepth))),0.5):
                FocalDepthMax = pow((sqrt(abs(project.FocalDepth-dummyProject.FocalDepth))),0.5)

            if BuildingCollapseRateMax < pow((sqrt(abs(project.BuildingCollapseRate-dummyProject.BuildingCollapseRate))),0.5):
                BuildingCollapseRateMax = pow((sqrt(abs(project.BuildingCollapseRate-dummyProject.BuildingCollapseRate))),0.5)

            if PopulationDensityMax < pow((sqrt(abs(project.PopulationDensity-dummyProject.PopulationDensity))),0.5):
                PopulationDensityMax = pow((sqrt(abs(project.PopulationDensity-dummyProject.PopulationDensity))),0.5)

            choseVar = depremFuzziesChose(project,dummyProject)

            WeatherConditionChose = choseVar[0]
            BuildingDensityChose = choseVar[1]
            PotentialHazardousChose = choseVar[2]
            EmergencyResourceCompChose = choseVar[3]
            EmergencyResourceDurChose = choseVar[4]
            InitialResponseChose = choseVar[5]
            RoadTranspChose = choseVar[6]
            AirTranspChose = choseVar[7]
            RailwayTranspChose = choseVar[8]
            MaritimeTranspChose = choseVar[9]
            HealthInfrChose = choseVar[10]
            WaterSupplyChose = choseVar[11]
            CommunicationInfrChose = choseVar[12]
            NaturalgasChose = choseVar[13]
            PowergridChose = choseVar[14]
            SufficiencyTemporaryChose = choseVar[15]
            CapacityWasteChose = choseVar[16]


            if WeatherConditionMax < WeatherConditionChose:
                WeatherConditionMax = WeatherConditionChose


            if BuildingDensityMax < BuildingDensityChose:
                BuildingDensityMax = BuildingDensityChose


            if PotentialHazardousMax < PotentialHazardousChose:
                PotentialHazardousMax = PotentialHazardousChose


            if EmergencyResourceCompMax < EmergencyResourceCompChose:
                EmergencyResourceCompMax = EmergencyResourceCompChose


            if EmergencyResourceDurMax < EmergencyResourceDurChose:
                EmergencyResourceDurMax = EmergencyResourceDurChose


            if InitialResponseMax < InitialResponseChose:
                InitialResponseMax = InitialResponseChose


            if RoadTranspMax < RoadTranspChose:
                RoadTranspMax = RoadTranspChose


            if AirTranspMax < AirTranspChose:
                AirTranspMax = AirTranspChose


            if RailwayTranspMax < RailwayTranspChose:
                RailwayTranspMax = RailwayTranspChose


            if MaritimeTranspMax < MaritimeTranspChose:
                MaritimeTranspMax = MaritimeTranspChose


            if HealthInfrMax < HealthInfrChose:
                HealthInfrMax = HealthInfrChose


            if WaterSupplyMax < WaterSupplyChose:
                WaterSupplyMax = WaterSupplyChose


            if CommunicationInfrMax < CommunicationInfrChose:
                CommunicationInfrMax = CommunicationInfrChose


            if NaturalgasMax < NaturalgasChose:
                NaturalgasMax = NaturalgasChose


            if PowergridMax < PowergridChose:
                PowergridMax = PowergridChose


            if SufficiencyTemporaryMax < SufficiencyTemporaryChose:
                SufficiencyTemporaryMax = SufficiencyTemporaryChose


            if CapacityWasteMax < CapacityWasteChose:
                CapacityWasteMax = CapacityWasteChose
        i = i+1

    varMaxDel.append(MagnitudeMax)
    varMaxDel.append(FocalDepthMax)
    varMaxDel.append(BuildingCollapseRateMax)
    varMaxDel.append(PopulationDensityMax)
    varMaxDel.append(WeatherConditionMax)
    varMaxDel.append(BuildingDensityMax)
    varMaxDel.append(PotentialHazardousMax)
    varMaxDel.append(EmergencyResourceCompMax)
    varMaxDel.append(EmergencyResourceDurMax)
    varMaxDel.append(InitialResponseMax)
    varMaxDel.append(RoadTranspMax)
    varMaxDel.append(AirTranspMax)
    varMaxDel.append(RailwayTranspMax)
    varMaxDel.append(MaritimeTranspMax)
    varMaxDel.append(HealthInfrMax)
    varMaxDel.append(WaterSupplyMax)
    varMaxDel.append(CommunicationInfrMax)
    varMaxDel.append(NaturalgasMax)
    varMaxDel.append(PowergridMax)
    varMaxDel.append(SufficiencyTemporaryMax)
    varMaxDel.append(CapacityWasteMax)

    return varMaxDel


def selDeltaMaxes(id):

    # number
    MaxPrecipInteMax = 0
    SinglePrecipPerMax = 0
    AveragePrecipMax = 0
    MaxWaterDepMax = 0
    DamageAreaMax = 0
    RescueWorkMax = 0
    EmrResDurMax = 0
    AltituRegMax = 0
    SlopeRegMax = 0

    # fuzzy
    CondRoadMax = 0
    EmrResCompMax = 0
    BuildDensMax = 0


    project = get_object_or_404(Sel, id=id)
    prjs = Sel.objects.all()

    varMaxDel = []

    i = 0
    count = prjs.count()
    while (i<count):
        dummyProject = prjs.order_by('id')[i]
        if project.id != dummyProject.id:

            #number
            if MaxPrecipInteMax < pow((sqrt(abs(project.MaximumPrecipitationIntensity-dummyProject.MaximumPrecipitationIntensity))),0.5):
                MaxPrecipInteMax = pow((sqrt(abs(project.MaximumPrecipitationIntensity-dummyProject.MaximumPrecipitationIntensity))),0.5)

            if SinglePrecipPerMax < pow((sqrt(abs(project.SinglePrecipitationPeriod-dummyProject.SinglePrecipitationPeriod))),0.5):
                SinglePrecipPerMax = pow((sqrt(abs(project.SinglePrecipitationPeriod-dummyProject.SinglePrecipitationPeriod))),0.5)

            if AveragePrecipMax < pow((sqrt(abs(project.AveragePrecipitation-dummyProject.AveragePrecipitation))),0.5):
                AveragePrecipMax = pow((sqrt(abs(project.AveragePrecipitation-dummyProject.AveragePrecipitation))),0.5)

            if MaxWaterDepMax < pow((sqrt(abs(project.MaximumWaterDepth-dummyProject.MaximumWaterDepth))),0.5):
                MaxWaterDepMax = pow((sqrt(abs(project.MaximumWaterDepth-dummyProject.MaximumWaterDepth))),0.5)

            if DamageAreaMax < pow((sqrt(abs(project.DamageArea-dummyProject.DamageArea))),0.5):
                DamageAreaMax = pow((sqrt(abs(project.DamageArea-dummyProject.DamageArea))),0.5)

            if RescueWorkMax < pow((sqrt(abs(project.RescueWorker-dummyProject.RescueWorker))),0.5):
                RescueWorkMax = pow((sqrt(abs(project.RescueWorker-dummyProject.RescueWorker))),0.5)

            if EmrResDurMax < pow((sqrt(abs(project.EmergencyResourceDuration-dummyProject.EmergencyResourceDuration))),0.5):
                EmrResDurMax = pow((sqrt(abs(project.EmergencyResourceDuration-dummyProject.EmergencyResourceDuration))),0.5)

            if AltituRegMax < pow((sqrt(abs(project.AltitudeRegion-dummyProject.AltitudeRegion))),0.5):
                AltituRegMax = pow((sqrt(abs(project.AltitudeRegion-dummyProject.AltitudeRegion))),0.5)

            if SlopeRegMax < pow((sqrt(abs(project.SlopeRegion-dummyProject.SlopeRegion))),0.5):
                SlopeRegMax = pow((sqrt(abs(project.SlopeRegion-dummyProject.SlopeRegion))),0.5)


            choseVar = selFuzziesChose(project,dummyProject)

            CondRoadChose = choseVar[0]
            EmrResCompChose = choseVar[1]
            BuildDensChose = choseVar[2]



            if CondRoadMax < CondRoadChose:
                CondRoadMax = CondRoadChose


            if EmrResCompMax < EmrResCompChose:
                EmrResCompMax = EmrResCompChose


            if BuildDensMax < BuildDensChose:
                BuildDensMax = BuildDensChose

        i = i+1


    varMaxDel.append(MaxPrecipInteMax)
    varMaxDel.append(SinglePrecipPerMax)
    varMaxDel.append(AveragePrecipMax)
    varMaxDel.append(MaxWaterDepMax)
    varMaxDel.append(DamageAreaMax)
    varMaxDel.append(RescueWorkMax)
    varMaxDel.append(EmrResDurMax)
    varMaxDel.append(AltituRegMax)
    varMaxDel.append(SlopeRegMax)
    varMaxDel.append(CondRoadMax)
    varMaxDel.append(EmrResCompMax)
    varMaxDel.append(BuildDensMax)

    return varMaxDel

def depremFuzziesChose(project,dummyProject):

    # fuzzy variables
    s1 = [0, 0, 0.17]
    s2 = [0, 0.17, 0.33]
    s3 = [0.17, 0.33, 0.5]
    s4 = [0.33, 0.5, 0.67]
    s5 = [0.5, 0.67, 0.83]
    s6 = [0.67, 0.83, 1]
    s7 = [0.83, 1, 1]


    widgetsChose = []

    # fuzzy-WeatherCondition
    if project.WeatherCondition == 1:
        x1 = s1[0]
        y1 = s1[1]
        z1 = s1[2]
    elif project.WeatherCondition == 2:
        x1 = s2[0]
        y1 = s2[1]
        z1 = s2[2]
    elif project.WeatherCondition == 3:
        x1 = s3[0]
        y1 = s3[1]
        z1 = s3[2]
    elif project.WeatherCondition == 4:
        x1 = s4[0]
        y1 = s4[1]
        z1 = s4[2]
    elif project.WeatherCondition == 5:
        x1 = s5[0]
        y1 = s5[1]
        z1 = s5[2]
    elif project.WeatherCondition == 6:
        x1 = s6[0]
        y1 = s6[1]
        z1 = s6[2]
    else:
        x1 = s7[0]
        y1 = s7[1]
        z1 = s7[2]

    if dummyProject.WeatherCondition == 1:
        x2 = s1[0]
        y2 = s1[1]
        z2 = s1[2]
    elif dummyProject.WeatherCondition == 2:
        x2 = s2[0]
        y2 = s2[1]
        z2 = s2[2]
    elif dummyProject.WeatherCondition == 3:
        x2 = s3[0]
        y2 = s3[1]
        z2 = s3[2]
    elif dummyProject.WeatherCondition == 4:
        x2 = s4[0]
        y2 = s4[1]
        z2 = s4[2]
    elif dummyProject.WeatherCondition == 5:
        x2 = s5[0]
        y2 = s5[1]
        z2 = s5[2]
    elif dummyProject.WeatherCondition == 6:
        x2 = s6[0]
        y2 = s6[1]
        z2 = s6[2]
    else:
        x2 = s7[0]
        y2 = s7[1]
        z2 = s7[2]

    WeatherConditionMax = pow((sqrt(x1 - x2) + sqrt(y1 - y2) + sqrt(z1 - z2)), 0.5)

    # fuzzy-BuildingDensityAccessibilityDisasterArea
    if project.BuildingDensityAccessibilityDisasterArea == 1:
        x1 = s1[0]
        y1 = s1[1]
        z1 = s1[2]
    elif project.BuildingDensityAccessibilityDisasterArea == 2:
        x1 = s2[0]
        y1 = s2[1]
        z1 = s2[2]
    elif project.BuildingDensityAccessibilityDisasterArea == 3:
        x1 = s3[0]
        y1 = s3[1]
        z1 = s3[2]
    elif project.BuildingDensityAccessibilityDisasterArea == 4:
        x1 = s4[0]
        y1 = s4[1]
        z1 = s4[2]
    elif project.BuildingDensityAccessibilityDisasterArea == 5:
        x1 = s5[0]
        y1 = s5[1]
        z1 = s5[2]
    elif project.BuildingDensityAccessibilityDisasterArea == 6:
        x1 = s6[0]
        y1 = s6[1]
        z1 = s6[2]
    else:
        x1 = s7[0]
        y1 = s7[1]
        z1 = s7[2]

    if dummyProject.BuildingDensityAccessibilityDisasterArea == 1:
        x2 = s1[0]
        y2 = s1[1]
        z2 = s1[2]
    elif dummyProject.BuildingDensityAccessibilityDisasterArea == 2:
        x2 = s2[0]
        y2 = s2[1]
        z2 = s2[2]
    elif dummyProject.BuildingDensityAccessibilityDisasterArea == 3:
        x2 = s3[0]
        y2 = s3[1]
        z2 = s3[2]
    elif dummyProject.BuildingDensityAccessibilityDisasterArea == 4:
        x2 = s4[0]
        y2 = s4[1]
        z2 = s4[2]
    elif dummyProject.BuildingDensityAccessibilityDisasterArea == 5:
        x2 = s5[0]
        y2 = s5[1]
        z2 = s5[2]
    elif dummyProject.BuildingDensityAccessibilityDisasterArea == 6:
        x2 = s6[0]
        y2 = s6[1]
        z2 = s6[2]
    else:
        x2 = s7[0]
        y2 = s7[1]
        z2 = s7[2]

    BuildingDensityMax = pow((sqrt(x1 - x2) + sqrt(y1 - y2) + sqrt(z1 - z2)), 0.5)

    # fuzzy-PotentialHazardousMaterial
    if project.PotentialHazardousMaterial == 1:
        x1 = s1[0]
        y1 = s1[1]
        z1 = s1[2]
    elif project.PotentialHazardousMaterial == 2:
        x1 = s2[0]
        y1 = s2[1]
        z1 = s2[2]
    elif project.PotentialHazardousMaterial == 3:
        x1 = s3[0]
        y1 = s3[1]
        z1 = s3[2]
    elif project.PotentialHazardousMaterial == 4:
        x1 = s4[0]
        y1 = s4[1]
        z1 = s4[2]
    elif project.PotentialHazardousMaterial == 5:
        x1 = s5[0]
        y1 = s5[1]
        z1 = s5[2]
    elif project.PotentialHazardousMaterial == 6:
        x1 = s6[0]
        y1 = s6[1]
        z1 = s6[2]
    else:
        x1 = s7[0]
        y1 = s7[1]
        z1 = s7[2]

    if dummyProject.PotentialHazardousMaterial == 1:
        x2 = s1[0]
        y2 = s1[1]
        z2 = s1[2]
    elif dummyProject.PotentialHazardousMaterial == 2:
        x2 = s2[0]
        y2 = s2[1]
        z2 = s2[2]
    elif dummyProject.PotentialHazardousMaterial == 3:
        x2 = s3[0]
        y2 = s3[1]
        z2 = s3[2]
    elif dummyProject.PotentialHazardousMaterial == 4:
        x2 = s4[0]
        y2 = s4[1]
        z2 = s4[2]
    elif dummyProject.PotentialHazardousMaterial == 5:
        x2 = s5[0]
        y2 = s5[1]
        z2 = s5[2]
    elif dummyProject.PotentialHazardousMaterial == 6:
        x2 = s6[0]
        y2 = s6[1]
        z2 = s6[2]
    else:
        x2 = s7[0]
        y2 = s7[1]
        z2 = s7[2]
    PotentialHazardousMax = pow((sqrt(x1 - x2) + sqrt(y1 - y2) + sqrt(z1 - z2)), 0.5)

    # fuzzy-EmergencyResourceCompleteness
    if project.EmergencyResourceCompleteness == 1:
        x1 = s1[0]
        y1 = s1[1]
        z1 = s1[2]
    elif project.EmergencyResourceCompleteness == 2:
        x1 = s2[0]
        y1 = s2[1]
        z1 = s2[2]
    elif project.EmergencyResourceCompleteness == 3:
        x1 = s3[0]
        y1 = s3[1]
        z1 = s3[2]
    elif project.EmergencyResourceCompleteness == 4:
        x1 = s4[0]
        y1 = s4[1]
        z1 = s4[2]
    elif project.EmergencyResourceCompleteness == 5:
        x1 = s5[0]
        y1 = s5[1]
        z1 = s5[2]
    elif project.EmergencyResourceCompleteness == 6:
        x1 = s6[0]
        y1 = s6[1]
        z1 = s6[2]
    else:
        x1 = s7[0]
        y1 = s7[1]
        z1 = s7[2]

    if dummyProject.EmergencyResourceCompleteness == 1:
        x2 = s1[0]
        y2 = s1[1]
        z2 = s1[2]
    elif dummyProject.EmergencyResourceCompleteness == 2:
        x2 = s2[0]
        y2 = s2[1]
        z2 = s2[2]
    elif dummyProject.EmergencyResourceCompleteness == 3:
        x2 = s3[0]
        y2 = s3[1]
        z2 = s3[2]
    elif dummyProject.EmergencyResourceCompleteness == 4:
        x2 = s4[0]
        y2 = s4[1]
        z2 = s4[2]
    elif dummyProject.EmergencyResourceCompleteness == 5:
        x2 = s5[0]
        y2 = s5[1]
        z2 = s5[2]
    elif dummyProject.EmergencyResourceCompleteness == 6:
        x2 = s6[0]
        y2 = s6[1]
        z2 = s6[2]
    else:
        x2 = s7[0]
        y2 = s7[1]
        z2 = s7[2]
    EmergencyResourceCompMax = pow((sqrt(x1 - x2) + sqrt(y1 - y2) + sqrt(z1 - z2)), 0.5)

    # fuzzy-EmergencyResourceDuration
    if project.EmergencyResourceDuration == 1:
        x1 = s1[0]
        y1 = s1[1]
        z1 = s1[2]
    elif project.EmergencyResourceDuration == 2:
        x1 = s2[0]
        y1 = s2[1]
        z1 = s2[2]
    elif project.EmergencyResourceDuration == 3:
        x1 = s3[0]
        y1 = s3[1]
        z1 = s3[2]
    elif project.EmergencyResourceDuration == 4:
        x1 = s4[0]
        y1 = s4[1]
        z1 = s4[2]
    elif project.EmergencyResourceDuration == 5:
        x1 = s5[0]
        y1 = s5[1]
        z1 = s5[2]
    elif project.EmergencyResourceDuration == 6:
        x1 = s6[0]
        y1 = s6[1]
        z1 = s6[2]
    else:
        x1 = s7[0]
        y1 = s7[1]
        z1 = s7[2]

    if dummyProject.EmergencyResourceDuration == 1:
        x2 = s1[0]
        y2 = s1[1]
        z2 = s1[2]
    elif dummyProject.EmergencyResourceDuration == 2:
        x2 = s2[0]
        y2 = s2[1]
        z2 = s2[2]
    elif dummyProject.EmergencyResourceDuration == 3:
        x2 = s3[0]
        y2 = s3[1]
        z2 = s3[2]
    elif dummyProject.EmergencyResourceDuration == 4:
        x2 = s4[0]
        y2 = s4[1]
        z2 = s4[2]
    elif dummyProject.EmergencyResourceDuration == 5:
        x2 = s5[0]
        y2 = s5[1]
        z2 = s5[2]
    elif dummyProject.EmergencyResourceDuration == 6:
        x2 = s6[0]
        y2 = s6[1]
        z2 = s6[2]
    else:
        x2 = s7[0]
        y2 = s7[1]
        z2 = s7[2]
    EmergencyResourceDurMax = pow((sqrt(x1 - x2) + sqrt(y1 - y2) + sqrt(z1 - z2)), 0.5)

    # fuzzy-InitialResponseLevel
    if project.InitialResponseLevel == 1:
        x1 = s1[0]
        y1 = s1[1]
        z1 = s1[2]
    elif project.InitialResponseLevel == 2:
        x1 = s2[0]
        y1 = s2[1]
        z1 = s2[2]
    elif project.InitialResponseLevel == 3:
        x1 = s3[0]
        y1 = s3[1]
        z1 = s3[2]
    elif project.InitialResponseLevel == 4:
        x1 = s4[0]
        y1 = s4[1]
        z1 = s4[2]
    elif project.InitialResponseLevel == 5:
        x1 = s5[0]
        y1 = s5[1]
        z1 = s5[2]
    elif project.InitialResponseLevel == 6:
        x1 = s6[0]
        y1 = s6[1]
        z1 = s6[2]
    else:
        x1 = s7[0]
        y1 = s7[1]
        z1 = s7[2]

    if dummyProject.InitialResponseLevel == 1:
        x2 = s1[0]
        y2 = s1[1]
        z2 = s1[2]
    elif dummyProject.InitialResponseLevel == 2:
        x2 = s2[0]
        y2 = s2[1]
        z2 = s2[2]
    elif dummyProject.InitialResponseLevel == 3:
        x2 = s3[0]
        y2 = s3[1]
        z2 = s3[2]
    elif dummyProject.InitialResponseLevel == 4:
        x2 = s4[0]
        y2 = s4[1]
        z2 = s4[2]
    elif dummyProject.InitialResponseLevel == 5:
        x2 = s5[0]
        y2 = s5[1]
        z2 = s5[2]
    elif dummyProject.InitialResponseLevel == 6:
        x2 = s6[0]
        y2 = s6[1]
        z2 = s6[2]
    else:
        x2 = s7[0]
        y2 = s7[1]
        z2 = s7[2]
    InitialResponseMax = pow((sqrt(x1 - x2) + sqrt(y1 - y2) + sqrt(z1 - z2)), 0.5)

    # fuzzy-ConditionRoadTransportation
    if project.ConditionRoadTransportation == 1:
        x1 = s1[0]
        y1 = s1[1]
        z1 = s1[2]
    elif project.ConditionRoadTransportation == 2:
        x1 = s2[0]
        y1 = s2[1]
        z1 = s2[2]
    elif project.ConditionRoadTransportation == 3:
        x1 = s3[0]
        y1 = s3[1]
        z1 = s3[2]
    elif project.ConditionRoadTransportation == 4:
        x1 = s4[0]
        y1 = s4[1]
        z1 = s4[2]
    elif project.ConditionRoadTransportation == 5:
        x1 = s5[0]
        y1 = s5[1]
        z1 = s5[2]
    elif project.ConditionRoadTransportation == 6:
        x1 = s6[0]
        y1 = s6[1]
        z1 = s6[2]
    else:
        x1 = s7[0]
        y1 = s7[1]
        z1 = s7[2]

    if dummyProject.ConditionRoadTransportation == 1:
        x2 = s1[0]
        y2 = s1[1]
        z2 = s1[2]
    elif dummyProject.ConditionRoadTransportation == 2:
        x2 = s2[0]
        y2 = s2[1]
        z2 = s2[2]
    elif dummyProject.ConditionRoadTransportation == 3:
        x2 = s3[0]
        y2 = s3[1]
        z2 = s3[2]
    elif dummyProject.ConditionRoadTransportation == 4:
        x2 = s4[0]
        y2 = s4[1]
        z2 = s4[2]
    elif dummyProject.ConditionRoadTransportation == 5:
        x2 = s5[0]
        y2 = s5[1]
        z2 = s5[2]
    elif dummyProject.ConditionRoadTransportation == 6:
        x2 = s6[0]
        y2 = s6[1]
        z2 = s6[2]
    else:
        x2 = s7[0]
        y2 = s7[1]
        z2 = s7[2]
    RoadTranspMax = pow((sqrt(x1 - x2) + sqrt(y1 - y2) + sqrt(z1 - z2)), 0.5)

    # fuzzy-ConditionAirTransportation
    if project.ConditionAirTransportation == 1:
        x1 = s1[0]
        y1 = s1[1]
        z1 = s1[2]
    elif project.ConditionAirTransportation == 2:
        x1 = s2[0]
        y1 = s2[1]
        z1 = s2[2]
    elif project.ConditionAirTransportation == 3:
        x1 = s3[0]
        y1 = s3[1]
        z1 = s3[2]
    elif project.ConditionAirTransportation == 4:
        x1 = s4[0]
        y1 = s4[1]
        z1 = s4[2]
    elif project.ConditionAirTransportation == 5:
        x1 = s5[0]
        y1 = s5[1]
        z1 = s5[2]
    elif project.ConditionAirTransportation == 6:
        x1 = s6[0]
        y1 = s6[1]
        z1 = s6[2]
    else:
        x1 = s7[0]
        y1 = s7[1]
        z1 = s7[2]

    if dummyProject.ConditionAirTransportation == 1:
        x2 = s1[0]
        y2 = s1[1]
        z2 = s1[2]
    elif dummyProject.ConditionAirTransportation == 2:
        x2 = s2[0]
        y2 = s2[1]
        z2 = s2[2]
    elif dummyProject.ConditionAirTransportation == 3:
        x2 = s3[0]
        y2 = s3[1]
        z2 = s3[2]
    elif dummyProject.ConditionAirTransportation == 4:
        x2 = s4[0]
        y2 = s4[1]
        z2 = s4[2]
    elif dummyProject.ConditionAirTransportation == 5:
        x2 = s5[0]
        y2 = s5[1]
        z2 = s5[2]
    elif dummyProject.ConditionAirTransportation == 6:
        x2 = s6[0]
        y2 = s6[1]
        z2 = s6[2]
    else:
        x2 = s7[0]
        y2 = s7[1]
        z2 = s7[2]
    AirTranspMax = pow((sqrt(x1 - x2) + sqrt(y1 - y2) + sqrt(z1 - z2)), 0.5)

    # fuzzy-ConditionRailwayTransportation
    if project.ConditionRailwayTransportation == 1:
        x1 = s1[0]
        y1 = s1[1]
        z1 = s1[2]
    elif project.ConditionRailwayTransportation == 2:
        x1 = s2[0]
        y1 = s2[1]
        z1 = s2[2]
    elif project.ConditionRailwayTransportation == 3:
        x1 = s3[0]
        y1 = s3[1]
        z1 = s3[2]
    elif project.ConditionRailwayTransportation == 4:
        x1 = s4[0]
        y1 = s4[1]
        z1 = s4[2]
    elif project.ConditionRailwayTransportation == 5:
        x1 = s5[0]
        y1 = s5[1]
        z1 = s5[2]
    elif project.ConditionRailwayTransportation == 6:
        x1 = s6[0]
        y1 = s6[1]
        z1 = s6[2]
    else:
        x1 = s7[0]
        y1 = s7[1]
        z1 = s7[2]

    if dummyProject.ConditionRailwayTransportation == 1:
        x2 = s1[0]
        y2 = s1[1]
        z2 = s1[2]
    elif dummyProject.ConditionRailwayTransportation == 2:
        x2 = s2[0]
        y2 = s2[1]
        z2 = s2[2]
    elif dummyProject.ConditionRailwayTransportation == 3:
        x2 = s3[0]
        y2 = s3[1]
        z2 = s3[2]
    elif dummyProject.ConditionRailwayTransportation == 4:
        x2 = s4[0]
        y2 = s4[1]
        z2 = s4[2]
    elif dummyProject.ConditionRailwayTransportation == 5:
        x2 = s5[0]
        y2 = s5[1]
        z2 = s5[2]
    elif dummyProject.ConditionRailwayTransportation == 6:
        x2 = s6[0]
        y2 = s6[1]
        z2 = s6[2]
    else:
        x2 = s7[0]
        y2 = s7[1]
        z2 = s7[2]
    RailwayTranspMax = pow((sqrt(x1 - x2) + sqrt(y1 - y2) + sqrt(z1 - z2)), 0.5)

    # fuzzy-ConditionMaritimeTransportation
    if project.ConditionMaritimeTransportation == 1:
        x1 = s1[0]
        y1 = s1[1]
        z1 = s1[2]
    elif project.ConditionMaritimeTransportation == 2:
        x1 = s2[0]
        y1 = s2[1]
        z1 = s2[2]
    elif project.ConditionMaritimeTransportation == 3:
        x1 = s3[0]
        y1 = s3[1]
        z1 = s3[2]
    elif project.ConditionMaritimeTransportation == 4:
        x1 = s4[0]
        y1 = s4[1]
        z1 = s4[2]
    elif project.ConditionMaritimeTransportation == 5:
        x1 = s5[0]
        y1 = s5[1]
        z1 = s5[2]
    elif project.ConditionMaritimeTransportation == 6:
        x1 = s6[0]
        y1 = s6[1]
        z1 = s6[2]
    else:
        x1 = s7[0]
        y1 = s7[1]
        z1 = s7[2]

    if dummyProject.ConditionMaritimeTransportation == 1:
        x2 = s1[0]
        y2 = s1[1]
        z2 = s1[2]
    elif dummyProject.ConditionMaritimeTransportation == 2:
        x2 = s2[0]
        y2 = s2[1]
        z2 = s2[2]
    elif dummyProject.ConditionMaritimeTransportation == 3:
        x2 = s3[0]
        y2 = s3[1]
        z2 = s3[2]
    elif dummyProject.ConditionMaritimeTransportation == 4:
        x2 = s4[0]
        y2 = s4[1]
        z2 = s4[2]
    elif dummyProject.ConditionMaritimeTransportation == 5:
        x2 = s5[0]
        y2 = s5[1]
        z2 = s5[2]
    elif dummyProject.ConditionMaritimeTransportation == 6:
        x2 = s6[0]
        y2 = s6[1]
        z2 = s6[2]
    else:
        x2 = s7[0]
        y2 = s7[1]
        z2 = s7[2]
    MaritimeTranspMax = pow((sqrt(x1 - x2) + sqrt(y1 - y2) + sqrt(z1 - z2)), 0.5)

    # fuzzy-ConditionHealthInfrastructure
    if project.ConditionHealthInfrastructure == 1:
        x1 = s1[0]
        y1 = s1[1]
        z1 = s1[2]
    elif project.ConditionHealthInfrastructure == 2:
        x1 = s2[0]
        y1 = s2[1]
        z1 = s2[2]
    elif project.ConditionHealthInfrastructure == 3:
        x1 = s3[0]
        y1 = s3[1]
        z1 = s3[2]
    elif project.ConditionHealthInfrastructure == 4:
        x1 = s4[0]
        y1 = s4[1]
        z1 = s4[2]
    elif project.ConditionHealthInfrastructure == 5:
        x1 = s5[0]
        y1 = s5[1]
        z1 = s5[2]
    elif project.ConditionHealthInfrastructure == 6:
        x1 = s6[0]
        y1 = s6[1]
        z1 = s6[2]
    else:
        x1 = s7[0]
        y1 = s7[1]
        z1 = s7[2]

    if dummyProject.ConditionHealthInfrastructure == 1:
        x2 = s1[0]
        y2 = s1[1]
        z2 = s1[2]
    elif dummyProject.ConditionHealthInfrastructure == 2:
        x2 = s2[0]
        y2 = s2[1]
        z2 = s2[2]
    elif dummyProject.ConditionHealthInfrastructure == 3:
        x2 = s3[0]
        y2 = s3[1]
        z2 = s3[2]
    elif dummyProject.ConditionHealthInfrastructure == 4:
        x2 = s4[0]
        y2 = s4[1]
        z2 = s4[2]
    elif dummyProject.ConditionHealthInfrastructure == 5:
        x2 = s5[0]
        y2 = s5[1]
        z2 = s5[2]
    elif dummyProject.ConditionHealthInfrastructure == 6:
        x2 = s6[0]
        y2 = s6[1]
        z2 = s6[2]
    else:
        x2 = s7[0]
        y2 = s7[1]
        z2 = s7[2]
    HealthInfrMax = pow((sqrt(x1 - x2) + sqrt(y1 - y2) + sqrt(z1 - z2)), 0.5)

    # fuzzy-ConditionWaterSupplySewage
    if project.ConditionWaterSupplySewage == 1:
        x1 = s1[0]
        y1 = s1[1]
        z1 = s1[2]
    elif project.ConditionWaterSupplySewage == 2:
        x1 = s2[0]
        y1 = s2[1]
        z1 = s2[2]
    elif project.ConditionWaterSupplySewage == 3:
        x1 = s3[0]
        y1 = s3[1]
        z1 = s3[2]
    elif project.ConditionWaterSupplySewage == 4:
        x1 = s4[0]
        y1 = s4[1]
        z1 = s4[2]
    elif project.ConditionWaterSupplySewage == 5:
        x1 = s5[0]
        y1 = s5[1]
        z1 = s5[2]
    elif project.ConditionWaterSupplySewage == 6:
        x1 = s6[0]
        y1 = s6[1]
        z1 = s6[2]
    else:
        x1 = s7[0]
        y1 = s7[1]
        z1 = s7[2]

    if dummyProject.ConditionWaterSupplySewage == 1:
        x2 = s1[0]
        y2 = s1[1]
        z2 = s1[2]
    elif dummyProject.ConditionWaterSupplySewage == 2:
        x2 = s2[0]
        y2 = s2[1]
        z2 = s2[2]
    elif dummyProject.ConditionWaterSupplySewage == 3:
        x2 = s3[0]
        y2 = s3[1]
        z2 = s3[2]
    elif dummyProject.ConditionWaterSupplySewage == 4:
        x2 = s4[0]
        y2 = s4[1]
        z2 = s4[2]
    elif dummyProject.ConditionWaterSupplySewage == 5:
        x2 = s5[0]
        y2 = s5[1]
        z2 = s5[2]
    elif dummyProject.ConditionWaterSupplySewage == 6:
        x2 = s6[0]
        y2 = s6[1]
        z2 = s6[2]
    else:
        x2 = s7[0]
        y2 = s7[1]
        z2 = s7[2]
    WaterSupplyMax = pow((sqrt(x1 - x2) + sqrt(y1 - y2) + sqrt(z1 - z2)), 0.5)

    # fuzzy-ConditionCommunicationInfrastructure
    if project.ConditionCommunicationInfrastructure == 1:
        x1 = s1[0]
        y1 = s1[1]
        z1 = s1[2]
    elif project.ConditionCommunicationInfrastructure == 2:
        x1 = s2[0]
        y1 = s2[1]
        z1 = s2[2]
    elif project.ConditionCommunicationInfrastructure == 3:
        x1 = s3[0]
        y1 = s3[1]
        z1 = s3[2]
    elif project.ConditionCommunicationInfrastructure == 4:
        x1 = s4[0]
        y1 = s4[1]
        z1 = s4[2]
    elif project.ConditionCommunicationInfrastructure == 5:
        x1 = s5[0]
        y1 = s5[1]
        z1 = s5[2]
    elif project.ConditionCommunicationInfrastructure == 6:
        x1 = s6[0]
        y1 = s6[1]
        z1 = s6[2]
    else:
        x1 = s7[0]
        y1 = s7[1]
        z1 = s7[2]

    if dummyProject.ConditionCommunicationInfrastructure == 1:
        x2 = s1[0]
        y2 = s1[1]
        z2 = s1[2]
    elif dummyProject.ConditionCommunicationInfrastructure == 2:
        x2 = s2[0]
        y2 = s2[1]
        z2 = s2[2]
    elif dummyProject.ConditionCommunicationInfrastructure == 3:
        x2 = s3[0]
        y2 = s3[1]
        z2 = s3[2]
    elif dummyProject.ConditionCommunicationInfrastructure == 4:
        x2 = s4[0]
        y2 = s4[1]
        z2 = s4[2]
    elif dummyProject.ConditionCommunicationInfrastructure == 5:
        x2 = s5[0]
        y2 = s5[1]
        z2 = s5[2]
    elif dummyProject.ConditionCommunicationInfrastructure == 6:
        x2 = s6[0]
        y2 = s6[1]
        z2 = s6[2]
    else:
        x2 = s7[0]
        y2 = s7[1]
        z2 = s7[2]
    CommunicationInfrMax = pow((sqrt(x1 - x2) + sqrt(y1 - y2) + sqrt(z1 - z2)), 0.5)

    # fuzzy-ConditionNaturalgas
    if project.ConditionNaturalgas == 1:
        x1 = s1[0]
        y1 = s1[1]
        z1 = s1[2]
    elif project.ConditionNaturalgas == 2:
        x1 = s2[0]
        y1 = s2[1]
        z1 = s2[2]
    elif project.ConditionNaturalgas == 3:
        x1 = s3[0]
        y1 = s3[1]
        z1 = s3[2]
    elif project.ConditionNaturalgas == 4:
        x1 = s4[0]
        y1 = s4[1]
        z1 = s4[2]
    elif project.ConditionNaturalgas == 5:
        x1 = s5[0]
        y1 = s5[1]
        z1 = s5[2]
    elif project.ConditionNaturalgas == 6:
        x1 = s6[0]
        y1 = s6[1]
        z1 = s6[2]
    else:
        x1 = s7[0]
        y1 = s7[1]
        z1 = s7[2]

    if dummyProject.ConditionNaturalgas == 1:
        x2 = s1[0]
        y2 = s1[1]
        z2 = s1[2]
    elif dummyProject.ConditionNaturalgas == 2:
        x2 = s2[0]
        y2 = s2[1]
        z2 = s2[2]
    elif dummyProject.ConditionNaturalgas == 3:
        x2 = s3[0]
        y2 = s3[1]
        z2 = s3[2]
    elif dummyProject.ConditionNaturalgas == 4:
        x2 = s4[0]
        y2 = s4[1]
        z2 = s4[2]
    elif dummyProject.ConditionNaturalgas == 5:
        x2 = s5[0]
        y2 = s5[1]
        z2 = s5[2]
    elif dummyProject.ConditionNaturalgas == 6:
        x2 = s6[0]
        y2 = s6[1]
        z2 = s6[2]
    else:
        x2 = s7[0]
        y2 = s7[1]
        z2 = s7[2]
    NaturalgasMax = pow((sqrt(x1 - x2) + sqrt(y1 - y2) + sqrt(z1 - z2)), 0.5)

    # fuzzy-ConditionPowergrid
    if project.ConditionPowergrid == 1:
        x1 = s1[0]
        y1 = s1[1]
        z1 = s1[2]
    elif project.ConditionPowergrid == 2:
        x1 = s2[0]
        y1 = s2[1]
        z1 = s2[2]
    elif project.ConditionPowergrid == 3:
        x1 = s3[0]
        y1 = s3[1]
        z1 = s3[2]
    elif project.ConditionPowergrid == 4:
        x1 = s4[0]
        y1 = s4[1]
        z1 = s4[2]
    elif project.ConditionPowergrid == 5:
        x1 = s5[0]
        y1 = s5[1]
        z1 = s5[2]
    elif project.ConditionPowergrid == 6:
        x1 = s6[0]
        y1 = s6[1]
        z1 = s6[2]
    else:
        x1 = s7[0]
        y1 = s7[1]
        z1 = s7[2]

    if dummyProject.ConditionPowergrid == 1:
        x2 = s1[0]
        y2 = s1[1]
        z2 = s1[2]
    elif dummyProject.ConditionPowergrid == 2:
        x2 = s2[0]
        y2 = s2[1]
        z2 = s2[2]
    elif dummyProject.ConditionPowergrid == 3:
        x2 = s3[0]
        y2 = s3[1]
        z2 = s3[2]
    elif dummyProject.ConditionPowergrid == 4:
        x2 = s4[0]
        y2 = s4[1]
        z2 = s4[2]
    elif dummyProject.ConditionPowergrid == 5:
        x2 = s5[0]
        y2 = s5[1]
        z2 = s5[2]
    elif dummyProject.ConditionPowergrid == 6:
        x2 = s6[0]
        y2 = s6[1]
        z2 = s6[2]
    else:
        x2 = s7[0]
        y2 = s7[1]
        z2 = s7[2]
    PowergridMax = pow((sqrt(x1 - x2) + sqrt(y1 - y2) + sqrt(z1 - z2)), 0.5)

    # fuzzy-SufficiencyTemporaryResidential
    if project.SufficiencyTemporaryResidential == 1:
        x1 = s1[0]
        y1 = s1[1]
        z1 = s1[2]
    elif project.SufficiencyTemporaryResidential == 2:
        x1 = s2[0]
        y1 = s2[1]
        z1 = s2[2]
    elif project.SufficiencyTemporaryResidential == 3:
        x1 = s3[0]
        y1 = s3[1]
        z1 = s3[2]
    elif project.SufficiencyTemporaryResidential == 4:
        x1 = s4[0]
        y1 = s4[1]
        z1 = s4[2]
    elif project.SufficiencyTemporaryResidential == 5:
        x1 = s5[0]
        y1 = s5[1]
        z1 = s5[2]
    elif project.SufficiencyTemporaryResidential == 6:
        x1 = s6[0]
        y1 = s6[1]
        z1 = s6[2]
    else:
        x1 = s7[0]
        y1 = s7[1]
        z1 = s7[2]

    if dummyProject.SufficiencyTemporaryResidential == 1:
        x2 = s1[0]
        y2 = s1[1]
        z2 = s1[2]
    elif dummyProject.SufficiencyTemporaryResidential == 2:
        x2 = s2[0]
        y2 = s2[1]
        z2 = s2[2]
    elif dummyProject.SufficiencyTemporaryResidential == 3:
        x2 = s3[0]
        y2 = s3[1]
        z2 = s3[2]
    elif dummyProject.SufficiencyTemporaryResidential == 4:
        x2 = s4[0]
        y2 = s4[1]
        z2 = s4[2]
    elif dummyProject.SufficiencyTemporaryResidential == 5:
        x2 = s5[0]
        y2 = s5[1]
        z2 = s5[2]
    elif dummyProject.SufficiencyTemporaryResidential == 6:
        x2 = s6[0]
        y2 = s6[1]
        z2 = s6[2]
    else:
        x2 = s7[0]
        y2 = s7[1]
        z2 = s7[2]
    SufficiencyTemporaryMax = pow((sqrt(x1 - x2) + sqrt(y1 - y2) + sqrt(z1 - z2)), 0.5)

    # fuzzy-CapacityWasteLandfills
    if project.CapacityWasteLandfills == 1:
        x1 = s1[0]
        y1 = s1[1]
        z1 = s1[2]
    elif project.CapacityWasteLandfills == 2:
        x1 = s2[0]
        y1 = s2[1]
        z1 = s2[2]
    elif project.CapacityWasteLandfills == 3:
        x1 = s3[0]
        y1 = s3[1]
        z1 = s3[2]
    elif project.CapacityWasteLandfills == 4:
        x1 = s4[0]
        y1 = s4[1]
        z1 = s4[2]
    elif project.CapacityWasteLandfills == 5:
        x1 = s5[0]
        y1 = s5[1]
        z1 = s5[2]
    elif project.CapacityWasteLandfills == 6:
        x1 = s6[0]
        y1 = s6[1]
        z1 = s6[2]
    else:
        x1 = s7[0]
        y1 = s7[1]
        z1 = s7[2]

    if dummyProject.CapacityWasteLandfills == 1:
        x2 = s1[0]
        y2 = s1[1]
        z2 = s1[2]
    elif dummyProject.CapacityWasteLandfills == 2:
        x2 = s2[0]
        y2 = s2[1]
        z2 = s2[2]
    elif dummyProject.CapacityWasteLandfills == 3:
        x2 = s3[0]
        y2 = s3[1]
        z2 = s3[2]
    elif dummyProject.CapacityWasteLandfills == 4:
        x2 = s4[0]
        y2 = s4[1]
        z2 = s4[2]
    elif dummyProject.CapacityWasteLandfills == 5:
        x2 = s5[0]
        y2 = s5[1]
        z2 = s5[2]
    elif dummyProject.CapacityWasteLandfills == 6:
        x2 = s6[0]
        y2 = s6[1]
        z2 = s6[2]
    else:
        x2 = s7[0]
        y2 = s7[1]
        z2 = s7[2]
    CapacityWasteMax = pow((sqrt(x1 - x2) + sqrt(y1 - y2) + sqrt(z1 - z2)), 0.5)

    widgetsChose.append(WeatherConditionMax)
    widgetsChose.append(BuildingDensityMax)
    widgetsChose.append(PotentialHazardousMax)
    widgetsChose.append(EmergencyResourceCompMax)
    widgetsChose.append(EmergencyResourceDurMax)
    widgetsChose.append(InitialResponseMax)
    widgetsChose.append(RoadTranspMax)
    widgetsChose.append(AirTranspMax)
    widgetsChose.append(RailwayTranspMax)
    widgetsChose.append(MaritimeTranspMax)
    widgetsChose.append(HealthInfrMax)
    widgetsChose.append(WaterSupplyMax)
    widgetsChose.append(CommunicationInfrMax)
    widgetsChose.append(NaturalgasMax)
    widgetsChose.append(PowergridMax)
    widgetsChose.append(SufficiencyTemporaryMax)
    widgetsChose.append(CapacityWasteMax)


    return widgetsChose




def selFuzziesChose(project,dummyProject):

    # fuzzy variables
    s1 = [0, 0, 0.17]
    s2 = [0, 0.17, 0.33]
    s3 = [0.17, 0.33, 0.5]
    s4 = [0.33, 0.5, 0.67]
    s5 = [0.5, 0.67, 0.83]
    s6 = [0.67, 0.83, 1]
    s7 = [0.83, 1, 1]

    widgetsChose = []

    # fuzzy-ConditionRoadTransportation
    if project.ConditionRoadTransportation == 1:
        x1 = s1[0]
        y1 = s1[1]
        z1 = s1[2]
    elif project.ConditionRoadTransportation == 2:
        x1 = s2[0]
        y1 = s2[1]
        z1 = s2[2]
    elif project.ConditionRoadTransportation == 3:
        x1 = s3[0]
        y1 = s3[1]
        z1 = s3[2]
    elif project.ConditionRoadTransportation == 4:
        x1 = s4[0]
        y1 = s4[1]
        z1 = s4[2]
    elif project.ConditionRoadTransportation == 5:
        x1 = s5[0]
        y1 = s5[1]
        z1 = s5[2]
    elif project.ConditionRoadTransportation == 6:
        x1 = s6[0]
        y1 = s6[1]
        z1 = s6[2]
    else:
        x1 = s7[0]
        y1 = s7[1]
        z1 = s7[2]

    if dummyProject.ConditionRoadTransportation == 1:
        x2 = s1[0]
        y2 = s1[1]
        z2 = s1[2]
    elif dummyProject.ConditionRoadTransportation == 2:
        x2 = s2[0]
        y2 = s2[1]
        z2 = s2[2]
    elif dummyProject.ConditionRoadTransportation == 3:
        x2 = s3[0]
        y2 = s3[1]
        z2 = s3[2]
    elif dummyProject.ConditionRoadTransportation == 4:
        x2 = s4[0]
        y2 = s4[1]
        z2 = s4[2]
    elif dummyProject.ConditionRoadTransportation == 5:
        x2 = s5[0]
        y2 = s5[1]
        z2 = s5[2]
    elif dummyProject.ConditionRoadTransportation == 6:
        x2 = s6[0]
        y2 = s6[1]
        z2 = s6[2]
    else:
        x2 = s7[0]
        y2 = s7[1]
        z2 = s7[2]

    CondRoadMax = pow((sqrt(x1 - x2) + sqrt(y1 - y2) + sqrt(z1 - z2)), 0.5)

    # fuzzy-EmergencyResourceCompletenessReadiness
    if project.EmergencyResourceCompletenessReadiness == 1:
        x1 = s1[0]
        y1 = s1[1]
        z1 = s1[2]
    elif project.EmergencyResourceCompletenessReadiness == 2:
        x1 = s2[0]
        y1 = s2[1]
        z1 = s2[2]
    elif project.EmergencyResourceCompletenessReadiness == 3:
        x1 = s3[0]
        y1 = s3[1]
        z1 = s3[2]
    elif project.EmergencyResourceCompletenessReadiness == 4:
        x1 = s4[0]
        y1 = s4[1]
        z1 = s4[2]
    elif project.EmergencyResourceCompletenessReadiness == 5:
        x1 = s5[0]
        y1 = s5[1]
        z1 = s5[2]
    elif project.EmergencyResourceCompletenessReadiness == 6:
        x1 = s6[0]
        y1 = s6[1]
        z1 = s6[2]
    else:
        x1 = s7[0]
        y1 = s7[1]
        z1 = s7[2]

    if dummyProject.EmergencyResourceCompletenessReadiness == 1:
        x2 = s1[0]
        y2 = s1[1]
        z2 = s1[2]
    elif dummyProject.EmergencyResourceCompletenessReadiness == 2:
        x2 = s2[0]
        y2 = s2[1]
        z2 = s2[2]
    elif dummyProject.EmergencyResourceCompletenessReadiness == 3:
        x2 = s3[0]
        y2 = s3[1]
        z2 = s3[2]
    elif dummyProject.EmergencyResourceCompletenessReadiness == 4:
        x2 = s4[0]
        y2 = s4[1]
        z2 = s4[2]
    elif dummyProject.EmergencyResourceCompletenessReadiness == 5:
        x2 = s5[0]
        y2 = s5[1]
        z2 = s5[2]
    elif dummyProject.EmergencyResourceCompletenessReadiness == 6:
        x2 = s6[0]
        y2 = s6[1]
        z2 = s6[2]
    else:
        x2 = s7[0]
        y2 = s7[1]
        z2 = s7[2]

    EmrResCompMax = pow((sqrt(x1 - x2) + sqrt(y1 - y2) + sqrt(z1 - z2)), 0.5)

    # fuzzy-BuildingDensityAccessibility
    if project.BuildingDensityAccessibility == 1:
        x1 = s1[0]
        y1 = s1[1]
        z1 = s1[2]
    elif project.BuildingDensityAccessibility == 2:
        x1 = s2[0]
        y1 = s2[1]
        z1 = s2[2]
    elif project.BuildingDensityAccessibility == 3:
        x1 = s3[0]
        y1 = s3[1]
        z1 = s3[2]
    elif project.BuildingDensityAccessibility == 4:
        x1 = s4[0]
        y1 = s4[1]
        z1 = s4[2]
    elif project.BuildingDensityAccessibility == 5:
        x1 = s5[0]
        y1 = s5[1]
        z1 = s5[2]
    elif project.BuildingDensityAccessibility == 6:
        x1 = s6[0]
        y1 = s6[1]
        z1 = s6[2]
    else:
        x1 = s7[0]
        y1 = s7[1]
        z1 = s7[2]

    if dummyProject.BuildingDensityAccessibility == 1:
        x2 = s1[0]
        y2 = s1[1]
        z2 = s1[2]
    elif dummyProject.BuildingDensityAccessibility == 2:
        x2 = s2[0]
        y2 = s2[1]
        z2 = s2[2]
    elif dummyProject.BuildingDensityAccessibility == 3:
        x2 = s3[0]
        y2 = s3[1]
        z2 = s3[2]
    elif dummyProject.BuildingDensityAccessibility == 4:
        x2 = s4[0]
        y2 = s4[1]
        z2 = s4[2]
    elif dummyProject.BuildingDensityAccessibility == 5:
        x2 = s5[0]
        y2 = s5[1]
        z2 = s5[2]
    elif dummyProject.BuildingDensityAccessibility == 6:
        x2 = s6[0]
        y2 = s6[1]
        z2 = s6[2]
    else:
        x2 = s7[0]
        y2 = s7[1]
        z2 = s7[2]
    BuildDensMax = pow((sqrt(x1 - x2) + sqrt(y1 - y2) + sqrt(z1 - z2)), 0.5)


    widgetsChose.append(CondRoadMax)
    widgetsChose.append(EmrResCompMax)
    widgetsChose.append(BuildDensMax)

    return widgetsChose





#############
#############
##############
################
#### Turkish ####


def depremCalculateResponsesTr(request,id):

    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[ 0].name == 'Disaster Manager':
            prj = get_object_or_404(Deprem, pk=id)
            if request.user.groups.all()[0].name != 'Disaster Manager' and prj.user != request.user:
                return render(request, 'accounts/Turkish/notPermissionTr.html')
            else:
                maxTable, maxValues = depremSimilarityAlgorithm(request, prj.id)
                i = 0
                cnt = len(maxTable)
                simProjects = []
                simValues = []
                while i < 5:
                    tmp = get_object_or_404(Deprem, id=maxTable[i])
                    simProjects.append(tmp)
                    simValues.append(maxValues[i])
                    i = i + 1

                dummyPrjResponses = ResponseCat()
                dummyPrjResponses.catId = id
                # benzer projelerin responsları ekleniyor burda

                for project in simProjects:
                    tmpResponses = project.responses.response.all()
                    for obj in tmpResponses:
                        newResponse = ResponsePlan()
                        newResponse.id = None
                        newResponse.reaction = obj.reaction
                        newResponse.time = obj.time
                        newResponse.date = obj.date
                        newResponse.effect = obj.effect
                        newResponse.responsible = obj.responsible
                        newResponse.save()
                        dummyPrjResponses.save()
                        dummyPrjResponses.response.add(newResponse)
                        prj.save()
                        prj.responses = dummyPrjResponses


                firstFive = []
                i = 0
                while i < 5:
                    similars = []
                    similars.append(simProjects[i].id)
                    similars.append(simProjects[i].projectName)
                    similars.append(simProjects[i].summary)
                    similars.append(simProjects[i].crtDate)
                    similars.append(simProjects[i].user)
                    similars.append(round(simValues[i], 4))
                    firstFive.append(similars)

                    i = i+1


                context = {
                    'project': prj,
                    'simProjects': firstFive,

                }
                return render(request, 'projects/Turkish/depremSimilarProjectTr.html', context)


        else:
            return render(request, 'accounts/Turkish/notPermission.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')





def selCalculateResponsesTr(request,id):

    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[ 0].name == 'Disaster Manager':
            prj = get_object_or_404(Sel, pk=id)
            if request.user.groups.all()[0].name != 'Disaster Manager' and prj.user != request.user:
                return render(request, 'accounts/Turkish/notPermissionTr.html')
            else:

                maxTable, maxValues = selSimilarityAlgorithm(request, prj.id)
                print("hata burda", prj.projectName)
                i = 0
                cnt = len(maxTable)
                simProjects = []
                simValues = []
                while i < 5:
                    tmp = get_object_or_404(Sel, id=maxTable[i])
                    simProjects.append(tmp)
                    simValues.append(maxValues[i])
                    i = i + 1

                dummyPrjResponses = ResponseCat()
                dummyPrjResponses.catId = id
                # benzer projelerin responsları ekleniyor burda

                for project in simProjects:
                    tmpResponses = project.responses.response.all()
                    for obj in tmpResponses:
                        newResponse = ResponsePlan()
                        newResponse.reaction = obj.reaction
                        newResponse.time = obj.time
                        newResponse.date = obj.date
                        newResponse.effect = obj.effect
                        newResponse.responsible = obj.responsible
                        newResponse.save()
                        dummyPrjResponses.save()
                        dummyPrjResponses.response.add(newResponse)
                        prj.save()
                        prj.responses = dummyPrjResponses

                firstFive = []
                i = 0
                while i < 5:
                    similars = []
                    similars.append(simProjects[i].id)
                    similars.append(simProjects[i].projectName)
                    similars.append(simProjects[i].summary)
                    similars.append(simProjects[i].crtDate)
                    similars.append(simProjects[i].user)
                    similars.append(round(simValues[i], 4))
                    firstFive.append(similars)

                    i = i + 1

                context = {
                    'project': prj,
                    'simProjects': firstFive,

                }
                return render(request, 'projects/Turkish/selSimilarProjectTr.html', context)


        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')


def depremAllProjectTr(request):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':

            prjs_list = Deprem.objects.order_by('-crtDate')

            return render(request, 'projects/Turkish/depremAllPrjTr.html', {'prjDpr': prjs_list})
        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')


def allProjectTr(request):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':

            projectsDeprem = Deprem.objects.order_by('-crtDate')
            projectsSel = Sel.objects.order_by('-crtDate')

            context = {
                'prjDpr': projectsDeprem,
                'prjSel': projectsSel
            }

            return render(request, 'projects/Turkish/allPrjTr.html', context)
        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')


def selAllProjectTr(request):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':

            prjs_list = Sel.objects.order_by('-crtDate')

            return render(request, 'projects/Turkish/selAllPrjTr.html', {'prjSel': prjs_list})
        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')


def depremViewTr(request, id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':
            proje = get_object_or_404(Deprem, id=id)

            projectResponses = proje.responses.response.order_by('-time')

            context = {
                'project': proje,
                'responses': projectResponses
            }
            return render(request, 'projects/Turkish/depremViewTr.html', context)
        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')


def selViewTr(request, id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':

            proje = get_object_or_404(Sel, id=id)

            projectResponses = proje.responses.response.order_by('-time')

            context = {
                'project': proje,
                'responses': projectResponses

            }
            return render(request, 'projects/Turkish/selViewTr.html', context)
        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')




def depremProjectCreateTr(request):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name=='Disaster Specialist' or request.user.groups.all()[0].name=='Disaster Manager':
            form = depremFormTr(request.POST or None)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = request.user

                catlg = get_object_or_404(ResponseCat, catId=1)

                project.responses = catlg
                project.save()

                return HttpResponseRedirect(reverse('projects:depremCalculateResponsesTr', kwargs={'id': project.id}))

            context = {
                'form': form,
            }
            return render(request, 'projects/Turkish/depremCreateTr.html', context)
        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')



def selProjectCreateTr(request):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name=='Disaster Specialist' or request.user.groups.all()[0].name=='Disaster Manager':
            form = selFormTr(request.POST or None)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = request.user

                catlg = get_object_or_404(ResponseCat, catId=1)

                project.responses = catlg
                project.save()

                return HttpResponseRedirect(reverse('projects:selCalculateResponsesTr', kwargs={'id': project.id}))

            context = {
                'form': form,
            }
            return render(request, 'projects/Turkish/selCreateTr.html', context)
        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')


def depremUpdateTr(request, id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':
            project = get_object_or_404(Deprem, id=id)
            projectResponses = project.responses.response.order_by('-time')

            context = {
                'project': project,
                'responses': projectResponses

            }
            return render(request, 'projects/Turkish/depremProjectUpdateTr.html', context)
        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')


def selUpdateTr(request, id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':
            project = get_object_or_404(Sel, id=id)
            projectResponses = project.responses.response.order_by('-time')

            context = {
                'project': project,
                'responses': projectResponses
            }
            return render(request, 'projects/Turkish/selProjectUpdateTr.html', context)
        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')


def depremProjectDeleteTr(request, id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[
            0].name == 'Disaster Manager':
            project = get_object_or_404(Deprem, id=id)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/Turkish/notPermissionTr.html')
            else:
                project.delete()
                return redirect("projects:depremAllProjectTr")
        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')


def selProjectDeleteTr(request, id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[
            0].name == 'Disaster Manager':
            project = get_object_or_404(Sel, id=id)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/Turkish/notPermissionTr.html')
            else:
                project.delete()
                return redirect("projects:selAllProjectTr")
        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')


def depremProjectInfUpdateTr(request, id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[
            0].name == 'Disaster Manager':
            project = get_object_or_404(Deprem, id=id)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/Turkish/notPermissionTr.html')
            else:
                form = depremInfFormTr(request.POST or None, instance=project)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(project.get_update_urlTr())

                context = {
                    'form': form,
                    'project': project
                }
                return render(request, 'projects/Turkish/depremUpdateTr.html', context)
        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')


def selProjectInfUpdateTr(request, id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[
            0].name == 'Disaster Manager':
            project = get_object_or_404(Sel, id=id)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/Turkish/notPermissionTr.html')
            else:
                form = selInfFormTr(request.POST or None, instance=project)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(project.get_update_urlTr())

                context = {
                    'form': form,
                    'project': project
                }
                return render(request, 'projects/Turkish/selUpdateTr.html', context)
        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')


def depremFeatureUpdateTr(request, id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[
            0].name == 'Disaster Manager':
            project = get_object_or_404(Deprem, id=id)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/Turkish/notPermissionTr.html')
            else:
                form = depremFeatureFormTr(request.POST or None, instance=project)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(reverse('projects:depremCalculateResponsesTr', kwargs={'id': project.id}))

                context = {
                    'form': form,
                    'project': project
                }
                return render(request, 'projects/Turkish/depremUpdateTr.html', context)
        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')


def selFeatureUpdateTr(request, id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[
            0].name == 'Disaster Manager':
            project = get_object_or_404(Sel, id=id)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/Turkish/notPermissionTr.html')
            else:
                form = selFeatureFormTr(request.POST or None, instance=project)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(reverse('projects:selCalculateResponsesTr', kwargs={'id': project.id}))

                context = {
                    'form': form,
                    'project': project
                }
                return render(request, 'projects/Turkish/selUpdateTr.html', context)
        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')


def depremTermPrjTr(request, id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[
            0].name == 'Disaster Manager':
            project = get_object_or_404(Deprem, id=id)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/Turkish/notPermissionTr.html')
            else:

                project.terminate = True
                project.save()

                projectResponses = project.responses.response.order_by('-time')

                context = {
                    'project': project,
                    'responses': projectResponses
                }

                return render(request, 'projects/Turkish/depremViewTr.html', context)

        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')


def selTermPrjTr(request, id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[
            0].name == 'Disaster Manager':
            project = get_object_or_404(Sel, id=id)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/Turkish/notPermissionTr.html')
            else:

                project.terminate = True
                project.save()

                projectResponses = project.responses.response.order_by('-time')

                context = {
                    'project': project,
                    'responses': projectResponses
                }
                return render(request, 'projects/Turkish/selViewTr.html', context)

        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')



def depremDeltaMaxesTr(id):

    # number
    MagnitudeMax = 0
    FocalDepthMax = 0
    BuildingCollapseRateMax = 0
    PopulationDensityMax = 0

    # fuzzy
    WeatherConditionMax = 0
    BuildingDensityMax = 0
    PotentialHazardousMax = 0
    EmergencyResourceCompMax = 0
    EmergencyResourceDurMax = 0
    InitialResponseMax = 0
    RoadTranspMax = 0
    AirTranspMax = 0
    RailwayTranspMax = 0
    MaritimeTranspMax = 0
    HealthInfrMax = 0
    WaterSupplyMax = 0
    CommunicationInfrMax = 0
    NaturalgasMax = 0
    PowergridMax = 0
    SufficiencyTemporaryMax = 0
    CapacityWasteMax = 0

    project = get_object_or_404(Deprem, id=id)
    prjs = Deprem.objects.all()

    varMaxDel = []

    i = 0
    count = prjs.count()
    while (i<count):
        dummyProject = prjs.order_by('id')[i]
        if project.id != dummyProject.id:
            #number

            if MagnitudeMax < pow((sqrt(abs(project.MagnitudeEarthquake-dummyProject.MagnitudeEarthquake))),0.5):
                MagnitudeMax = pow((sqrt(abs(project.MagnitudeEarthquake-dummyProject.MagnitudeEarthquake))),0.5)

            if FocalDepthMax < pow((sqrt(abs(project.FocalDepth-dummyProject.FocalDepth))),0.5):
                FocalDepthMax = pow((sqrt(abs(project.FocalDepth-dummyProject.FocalDepth))),0.5)

            if BuildingCollapseRateMax < pow((sqrt(abs(project.BuildingCollapseRate-dummyProject.BuildingCollapseRate))),0.5):
                BuildingCollapseRateMax = pow((sqrt(abs(project.BuildingCollapseRate-dummyProject.BuildingCollapseRate))),0.5)

            if PopulationDensityMax < pow((sqrt(abs(project.PopulationDensity-dummyProject.PopulationDensity))),0.5):
                PopulationDensityMax = pow((sqrt(abs(project.PopulationDensity-dummyProject.PopulationDensity))),0.5)

            choseVar = depremFuzziesChose(project,dummyProject)

            WeatherConditionChose = choseVar[0]
            BuildingDensityChose = choseVar[1]
            PotentialHazardousChose = choseVar[2]
            EmergencyResourceCompChose = choseVar[3]
            EmergencyResourceDurChose = choseVar[4]
            InitialResponseChose = choseVar[5]
            RoadTranspChose = choseVar[6]
            AirTranspChose = choseVar[7]
            RailwayTranspChose = choseVar[8]
            MaritimeTranspChose = choseVar[9]
            HealthInfrChose = choseVar[10]
            WaterSupplyChose = choseVar[11]
            CommunicationInfrChose = choseVar[12]
            NaturalgasChose = choseVar[13]
            PowergridChose = choseVar[14]
            SufficiencyTemporaryChose = choseVar[15]
            CapacityWasteChose = choseVar[16]


            if WeatherConditionMax < WeatherConditionChose:
                WeatherConditionMax = WeatherConditionChose


            if BuildingDensityMax < BuildingDensityChose:
                BuildingDensityMax = BuildingDensityChose


            if PotentialHazardousMax < PotentialHazardousChose:
                PotentialHazardousMax = PotentialHazardousChose


            if EmergencyResourceCompMax < EmergencyResourceCompChose:
                EmergencyResourceCompMax = EmergencyResourceCompChose


            if EmergencyResourceDurMax < EmergencyResourceDurChose:
                EmergencyResourceDurMax = EmergencyResourceDurChose


            if InitialResponseMax < InitialResponseChose:
                InitialResponseMax = InitialResponseChose


            if RoadTranspMax < RoadTranspChose:
                RoadTranspMax = RoadTranspChose


            if AirTranspMax < AirTranspChose:
                AirTranspMax = AirTranspChose


            if RailwayTranspMax < RailwayTranspChose:
                RailwayTranspMax = RailwayTranspChose


            if MaritimeTranspMax < MaritimeTranspChose:
                MaritimeTranspMax = MaritimeTranspChose


            if HealthInfrMax < HealthInfrChose:
                HealthInfrMax = HealthInfrChose


            if WaterSupplyMax < WaterSupplyChose:
                WaterSupplyMax = WaterSupplyChose


            if CommunicationInfrMax < CommunicationInfrChose:
                CommunicationInfrMax = CommunicationInfrChose


            if NaturalgasMax < NaturalgasChose:
                NaturalgasMax = NaturalgasChose


            if PowergridMax < PowergridChose:
                PowergridMax = PowergridChose


            if SufficiencyTemporaryMax < SufficiencyTemporaryChose:
                SufficiencyTemporaryMax = SufficiencyTemporaryChose


            if CapacityWasteMax < CapacityWasteChose:
                CapacityWasteMax = CapacityWasteChose
        i = i+1

    varMaxDel.append(MagnitudeMax)
    varMaxDel.append(FocalDepthMax)
    varMaxDel.append(BuildingCollapseRateMax)
    varMaxDel.append(PopulationDensityMax)
    varMaxDel.append(WeatherConditionMax)
    varMaxDel.append(BuildingDensityMax)
    varMaxDel.append(PotentialHazardousMax)
    varMaxDel.append(EmergencyResourceCompMax)
    varMaxDel.append(EmergencyResourceDurMax)
    varMaxDel.append(InitialResponseMax)
    varMaxDel.append(RoadTranspMax)
    varMaxDel.append(AirTranspMax)
    varMaxDel.append(RailwayTranspMax)
    varMaxDel.append(MaritimeTranspMax)
    varMaxDel.append(HealthInfrMax)
    varMaxDel.append(WaterSupplyMax)
    varMaxDel.append(CommunicationInfrMax)
    varMaxDel.append(NaturalgasMax)
    varMaxDel.append(PowergridMax)
    varMaxDel.append(SufficiencyTemporaryMax)
    varMaxDel.append(CapacityWasteMax)

    return varMaxDel


def selDeltaMaxesTr(id):

    # number
    MaxPrecipInteMax = 0
    SinglePrecipPerMax = 0
    AveragePrecipMax = 0
    MaxWaterDepMax = 0
    DamageAreaMax = 0
    RescueWorkMax = 0
    EmrResDurMax = 0
    AltituRegMax = 0
    SlopeRegMax = 0

    # fuzzy
    CondRoadMax = 0
    EmrResCompMax = 0
    BuildDensMax = 0


    project = get_object_or_404(Sel, id=id)
    prjs = Sel.objects.all()

    varMaxDel = []

    i = 0
    count = prjs.count()
    while (i<count):
        dummyProject = prjs.order_by('id')[i]
        if project.id != dummyProject.id:

            #number
            if MaxPrecipInteMax < pow((sqrt(abs(project.MaximumPrecipitationIntensity-dummyProject.MaximumPrecipitationIntensity))),0.5):
                MaxPrecipInteMax = pow((sqrt(abs(project.MaximumPrecipitationIntensity-dummyProject.MaximumPrecipitationIntensity))),0.5)

            if SinglePrecipPerMax < pow((sqrt(abs(project.SinglePrecipitationPeriod-dummyProject.SinglePrecipitationPeriod))),0.5):
                SinglePrecipPerMax = pow((sqrt(abs(project.SinglePrecipitationPeriod-dummyProject.SinglePrecipitationPeriod))),0.5)

            if AveragePrecipMax < pow((sqrt(abs(project.AveragePrecipitation-dummyProject.AveragePrecipitation))),0.5):
                AveragePrecipMax = pow((sqrt(abs(project.AveragePrecipitation-dummyProject.AveragePrecipitation))),0.5)

            if MaxWaterDepMax < pow((sqrt(abs(project.MaximumWaterDepth-dummyProject.MaximumWaterDepth))),0.5):
                MaxWaterDepMax = pow((sqrt(abs(project.MaximumWaterDepth-dummyProject.MaximumWaterDepth))),0.5)

            if DamageAreaMax < pow((sqrt(abs(project.DamageArea-dummyProject.DamageArea))),0.5):
                DamageAreaMax = pow((sqrt(abs(project.DamageArea-dummyProject.DamageArea))),0.5)

            if RescueWorkMax < pow((sqrt(abs(project.RescueWorker-dummyProject.RescueWorker))),0.5):
                RescueWorkMax = pow((sqrt(abs(project.RescueWorker-dummyProject.RescueWorker))),0.5)

            if EmrResDurMax < pow((sqrt(abs(project.EmergencyResourceDuration-dummyProject.EmergencyResourceDuration))),0.5):
                EmrResDurMax = pow((sqrt(abs(project.EmergencyResourceDuration-dummyProject.EmergencyResourceDuration))),0.5)

            if AltituRegMax < pow((sqrt(abs(project.AltitudeRegion-dummyProject.AltitudeRegion))),0.5):
                AltituRegMax = pow((sqrt(abs(project.AltitudeRegion-dummyProject.AltitudeRegion))),0.5)

            if SlopeRegMax < pow((sqrt(abs(project.SlopeRegion-dummyProject.SlopeRegion))),0.5):
                SlopeRegMax = pow((sqrt(abs(project.SlopeRegion-dummyProject.SlopeRegion))),0.5)


            choseVar = selFuzziesChose(project,dummyProject)

            CondRoadChose = choseVar[0]
            EmrResCompChose = choseVar[1]
            BuildDensChose = choseVar[2]



            if CondRoadMax < CondRoadChose:
                CondRoadMax = CondRoadChose


            if EmrResCompMax < EmrResCompChose:
                EmrResCompMax = EmrResCompChose


            if BuildDensMax < BuildDensChose:
                BuildDensMax = BuildDensChose

        i = i+1


    varMaxDel.append(MaxPrecipInteMax)
    varMaxDel.append(SinglePrecipPerMax)
    varMaxDel.append(AveragePrecipMax)
    varMaxDel.append(MaxWaterDepMax)
    varMaxDel.append(DamageAreaMax)
    varMaxDel.append(RescueWorkMax)
    varMaxDel.append(EmrResDurMax)
    varMaxDel.append(AltituRegMax)
    varMaxDel.append(SlopeRegMax)
    varMaxDel.append(CondRoadMax)
    varMaxDel.append(EmrResCompMax)
    varMaxDel.append(BuildDensMax)

    return varMaxDel




def newResponseDprTr(request,pId,rId):

    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[0].name == 'Disaster Manager':
            project = get_object_or_404(Deprem, id=pId)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/Turkish/notPermissionTr.html')
            else:
                objects = project.responses.response.all()

                for obj in objects:
                    if obj.id == rId:
                        obj.save()

                        form = responseFormTr(request.POST or None, instance=obj)
                        if form.is_valid():
                            obj = form.save()

                            return HttpResponseRedirect(reverse('projects:depremViewTr', kwargs={'id': project.id}))
                        context = {
                        'form': form,
                        }
                        return render(request, 'projects/Turkish/depremUpdateTr.html', context)

        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')


def newResponseSelTr(request,pId,rId):

    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[0].name == 'Disaster Manager':
            project = get_object_or_404(Sel, id=pId)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/Turkish/notPermissionTr.html')
            else:
                objects = project.responses.response.all()

                for obj in objects:
                    if obj.id == rId:
                        obj.save()

                        form = responseFormTr(request.POST or None, instance=obj)
                        if form.is_valid():
                            obj = form.save()

                            return HttpResponseRedirect(reverse('projects:selViewTr', kwargs={'id': project.id}))

                        context = {
                        'form': form,
                        }
                        return render(request, 'projects/Turkish/selUpdateTr.html', context)

        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')



def viewResponseDprTr(request,pId,rId):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':
            project = get_object_or_404(Deprem, id=pId)
            objects = project.responses.response.all()
            for obj in objects:
                if obj.id == rId:
                    context = {
                        'response': obj,
                    }
                    return render(request, 'projects/Turkish/viewResponseDprTr.html', context)
        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')




def viewResponseSelTr(request,pId,rId):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':
            project = get_object_or_404(Sel, id=pId)
            objects = project.responses.response.all()
            for obj in objects:
                if obj.id == rId:
                    context = {
                        'response': obj,
                    }
                    return render(request, 'projects/Turkish/viewResponseSelTr.html', context)
        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')



def deleteResponseDprTr(request,pId,rId):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':
            project = get_object_or_404(Deprem, id=pId)


            objects = project.responses.response.all()
            for obj in objects:
                if obj.id == rId:
                    obj.delete()

            projectResponses = project.responses.response.order_by('-time')

            context = {
                'project': project,
                'responses': projectResponses
            }
            return render(request, 'projects/Turkish/depremViewTr.html',context)
        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')



def deleteResponseSelTr(request,pId,rId):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':
            project = get_object_or_404(Sel, id=pId)


            objects = project.responses.response.all()
            for obj in objects:
                if obj.id == rId:
                    obj.delete()

            projectResponses = project.responses.response.order_by('-time')

            context = {
                'project': project,
                'responses': projectResponses
            }
            return render(request, 'projects/Turkish/depremViewTr.html',context)
        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')


def addResponseDprTr(request,pId):

    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[0].name == 'Disaster Manager':
            project = get_object_or_404(Deprem, id=pId)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/Turkish/notPermission.html')
            else:
                dummyPrjResponses = project.responses
                newResponse = ResponsePlan()
                newResponse.id = None
                form = responseFormTr(request.POST or None)
                if form.is_valid():
                    data = form.cleaned_data
                    newResponse.reaction = data['reaction']
                    newResponse.time = data['time']
                    newResponse.date = data['date']
                    newResponse.effect = data['effect']
                    newResponse.responsible = data['responsible']
                    newResponse.save()
                    dummyPrjResponses.save()
                    dummyPrjResponses.response.add(newResponse)
                    project.save()
                    project.responses = dummyPrjResponses

                    return HttpResponseRedirect(reverse('projects:depremViewTr', kwargs={'id': project.id}))
                context = {
                    'form': form,
                }
                return render(request, 'projects/Turkish/depremAddRspTr.html', context)

        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')



def addResponseSelTr(request,pId):

    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'Disaster Specialist' or request.user.groups.all()[
            0].name == 'Disaster Manager':
            project = get_object_or_404(Sel, id=pId)
            if request.user.groups.all()[0].name != 'Disaster Manager' and project.user != request.user:
                return render(request, 'accounts/Turkish/notPermissionTr.html')
            else:
                dummyPrjResponses = project.responses
                newResponse = ResponsePlan()
                newResponse.id = None
                form = responseFormTr(request.POST or None)
                if form.is_valid():
                    data = form.cleaned_data
                    newResponse.reaction = data['reaction']
                    newResponse.time = data['time']
                    newResponse.date = data['date']
                    newResponse.effect = data['effect']
                    newResponse.responsible = data['responsible']
                    newResponse.save()
                    dummyPrjResponses.save()
                    dummyPrjResponses.response.add(newResponse)
                    project.save()
                    project.responses = dummyPrjResponses

                    return HttpResponseRedirect(reverse('projects:selViewTr', kwargs={'id': project.id}))
                context = {
                    'form': form,
                }
                return render(request, 'projects/Turkish/selAddRspTr.html', context)

        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')



def depremInfViewTr(request,id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':

            project = get_object_or_404(Deprem,id=id)


            context = {
                'project': project,

            }
            return render(request, 'projects/Turkish/depremInfViewTr.html',context)
        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')


def selInfViewTr(request,id):
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name != 'New Member':

            project = get_object_or_404(Sel,id=id)


            context = {
                'project': project,
            }
            return render(request, 'projects/Turkish/selInfViewTr.html',context)
        else:
            return render(request, 'accounts/Turkish/notPermissionTr.html')
    else:
        return render(request, 'accounts/Turkish/notLoginTr.html')



def aboutTr(request):
    return render(request, 'projects/Turkish/aboutUsTr.html')