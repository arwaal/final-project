from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout as auth_logout
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

from main.models import Users, Recommendation, BusinessSubmission, Category, Comment
from main.forms import BusinessSignUp, BusinessSubmissionForm, UserLogin, BusinessLogin, Comments, UserSignUp
import requests

from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from ratings.handlers import ratings
from django.conf import settings

# from default_settings import RATINGS_VOTES_PER_IP

from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def home(request):
    context = {}
    categories = Category.objects.all()
    context['categories'] = categories
    recommendations = Recommendation.objects.all()
    context['recommendations'] = recommendations

    return render(request, 'home.html', context)


def category_detail(request, pk):
    context = {}
    category = Category.objects.get(pk=pk)
    context['category'] = category

    return render(request, 'category_detail.html', context)


def recommendation_detail(request, pk):
    context = {}
    recommendation = Recommendation.objects.get(pk=pk)
    context['recommendation'] = recommendation

    return render(request, 'recommendation_detail.html', context)


def category_list(request):
    context = {}
    categories = Category.objects.all()
    context['categories'] = categories

    return render(request, 'category_list.html', context)


def cat_recommendations(request, pk):
    context = {}
    category = Category.objects.get(pk=pk)
    context['category'] = category

    return render(request, 'cat_recoms_list.html', context)


def location(request, pk):
    context = {}
    recommendation = Recommendation.objects.get(pk=pk)
    context['recommendation'] = recommendation

    return render(request, 'location.html', context)

@csrf_exempt
def submit_email(request):
    name = request.POST.get("name", None)
    email = request.POST.get("email", None)
    phone = request.POST.get("phone", None)
    message = request.POST.get("message", None)
    send_mail('users messages - %s' % name, message, email, ['recoms.com@gmail.com'], fail_silently=False)

    return HttpResponse('success')


def user_signup_view(request):
    print "AA"
    context = {}
    form = UserSignUp()
    context['form'] = form
    print form
    print "BB"
    if request.method == 'POST':
        form = UserSignUp(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            confirm_email = form.cleaned_data['confirm_email']
            
            if email != None:
                splite = email.split('@')
                try:
                    r = requests.get('http://%s' % splite[1])
                    if r.status_code == 200:
                        the_user = User.objects.create_user(username, email, password)
                        reg_user, created = Users.objects.get_or_create(regular_user=the_user)
                        # reg_user.recomendation = recomendation
                        reg_user.save()
                        auth_user = authenticate(username=username, password=password)
                        login(request, auth_user)

                    return HttpResponseRedirect('/user_profile/')
                except Exception, e:
                    print e
                    return HttpResponseRedirect('/user_signup/')
            else:
                context['form'] = form
                return render_to_response('user_signup.html', context, context_instatnce=RequestContext(request))

    elif request.method == 'GET':
        context['valid'] = form.errors

    else:
        return HttpResponse('Error')

    return render_to_response('user_signup.html', context, context_instance=RequestContext(request))


def business_signup_view(request):
    context = {}
    form = BusinessSignUp()
    context['form'] = form
    # print form
    if request.method == 'POST':
        form = BusinessSignUp(request.POST)
        context['form'] = form
        if form.is_valid():
            business_name = form.cleaned_data['business_name']
            password = form.cleaned_data['password']
            company = form.cleaned_data['company']
            mobile = form.cleaned_data['mobile']
            phone = form.cleaned_data['phone']
            if mobile == "" and phone == "":
                print "ph err"
                context['phone_error'] = "You Must Include a Mobile or Land Phone"
                return render_to_response('business_signup.html', context, context_instance=RequestContext(request))
            email = form.cleaned_data['email']
            confirm_email = form.cleaned_data['confirm_email']
            if email != None:
                splite = email.split('@')
                try:
                    r = requests.get('http://%s' % splite[1])
                    if r.status_code == 200:
                        the_user = User.objects.create_user(business_name, email, password)
                        buss_user, created = Users.objects.get_or_create(regular_user=the_user, business_user=True, mobile=mobile, phone=phone, company=company)
                        # buss_user.business_user = business_user(True)
                        # buss_user.address = address
                        buss_user.save()

                        auth_user = authenticate(username=business_name, password=password)
                        login(request, auth_user)
                    return HttpResponseRedirect('/home/')

                except Exception, e:
                    print e
                    return HttpResponseRedirect('/business_signup/')

            else:
                context['form'] = form
                return render_to_response('business_signup.html', context, context_instance=RequestContext(request))
    elif request.method == 'GET':
            context['valid'] = form.errors

    else:
        return HttpResponse('Error')
    return render_to_response('business_signup.html', context, context_instance=RequestContext(request))

@login_required
def business_submission_view(request):
    if not request.user.users.business_user:
        return HttpResponseRedirect('/home/')
    context = {}
    form = BusinessSubmissionForm(initial={'business_user':request.user.pk})
    context['form'] = form
    if request.method == 'POST':
        form = BusinessSubmissionForm(request.POST, request.FILES)
        context['form'] = form
        if form.is_valid():
            the_user = User.objects.get(pk=request.user.pk)
            users_obj = Users.objects.get(regular_user=the_user, business_user=True)
            business_name = form.cleaned_data['business_user']
            address = form.cleaned_data['address']
            mobile = form.cleaned_data['mobile']
            info = form.cleaned_data['info']
            email = form.cleaned_data['email']
            # if email != None:
            #     splite = email.split('@')
            #     try:
            #         r = requests.get('http:// %s' % splite[1])
            #         if r.status_code == 200:
            business_submission, created = BusinessSubmission.objects.get_or_create(user=users_obj, mobile=mobile, address=address, email=email)
            business_submission.save()
            recommendation, created = Recommendation.objects.get_or_create(name=business_name, info=info, address=address, mobile_number=mobile)
            recommendation.image1 = form.cleaned_data['image1']
            recommendation.image2 = form.cleaned_data['image2']
            recommendation.image3 = form.cleaned_data['image3']
            recommendation.image4 = form.cleaned_data['image4']
            recommendation.image5 = form.cleaned_data['image5']
            recommendation.image6 = form.cleaned_data['image6']
            recommendation.image7 = form.cleaned_data['image7']
            recommendation.image8 = form.cleaned_data['image8']
            recommendation.image9 = form.cleaned_data['image9']
            recommendation.image10 = form.cleaned_data['image10']
            recommendation.save()
            return HttpResponseRedirect('/business_profile/%s' % the_user.pk)
                # except Exception, e:
                #     print "email error %s" % splite[1]
                #     print e
                #     return render_to_response('business_submission.html', context, context_instance=RequestContext(request))
    
            # else:
            #     return render_to_response('business_submission.html', context, context_instance=RequestContext(request))
   
        else:
            return render_to_response('business_submission.html', context, context_instance=RequestContext(request))
    elif request.method == 'GET':
        context['valid'] = form.errors

    else:
        return HttpResponse('Error')
    return render_to_response('business_submission.html', context, context_instance=RequestContext(request))

# {% if user.business_user %}
#
#   <a hrf=/link/to/business_sub>Submit Image</a>
#
# {% endif %}


def user_login(request):
    context = {}
    form = UserLogin()
    context['form'] = form
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            auth_user = authenticate(username=username, password=password)
            login(request, auth_user)
            print "went through YAY"
            return HttpResponseRedirect('/user_profile/%s' % auth_user.pk)

    elif request.method == 'GET':
            context['valid'] = form.errors

    return render_to_response('user_login.html', context, context_instance=RequestContext(request))


def business_login(request):
    context = {}
    form = BusinessLogin()
    context['form'] = form
    if request.method == 'POST':
        form = BusinessLogin(request.POST)
        if form.is_valid():
            business_name = form.cleaned_data['business_name']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=business_name, password=password)
            login(request, auth_user)

            if auth_user.business_user:
                return HttpResponseRedirect('/business_profile/%s' % auth_user.pk)
            else:
                return HttpResponseRedirect('/user_profile/%s' % auth_user.pk)

    elif request.method == 'GET':
        context['valid'] = form.errors
    return render_to_response('business_login.html', context, context_instance=RequestContext(request))


@login_required
def logout(request):
    logout(request)
    return HttpResponseRedirect('/home/')


@login_required
def comments_view(request):
    context = {}
    form = Comments(request.GET)
    context['form'] = form
    if form.is_valid():
        comment = form.cleaned_data['comment']
        reply = form.cleaned_data['reply']
        recomendation = form.cleaned_data['recomendation']
        comment, created = Comment.objects.get_or_create(comment=comment, reply=reply, recomendation=Recommendation.name)
        comment.save()
    else:
        return HttpResponseRedirect('/')
    return render(request, 'recommendation_detail.html', context)


@login_required
def user_profile_view(request, pk):
    context = {}
    regular_user = Users.objects.filter(pk=pk, business_user=False)
    context['regular_user'] = regular_user
    if regular_user.pk != None:
        return HttpResponseRedirect('/home/')
    
    return render_to_response('user_profile.html', context, context_instance=RequestContext(request))


@login_required
def business_profile_view(request, pk):
    context = {}
    business_user = Users.objects.filter(pk=pk, business_user=True)

    context['business_user'] = business_user
    return render_to_response('business_profile.html', context, context_instance=RequestContext(request))


@login_required
def voting(request, pk):
    user = Users.objects.get(pk=request.user.pk, business_user=False)
    vote_type = request.GET.get('vote_type', None)
    recomendation_object = Recommendation.objects.get(pk=pk)
    if vote_type == 'up':
        recomendation_object.up_votes.add(user)
        try:
            recomendation_object.down_votes.get(pk=request.user.pk)
            recomendation_object.down_votes.remove(user)
        except Exception, e:
            print e
        recomendation_object.save()

    elif vote_type == 'down':
        recomendation_object.down_votes.add(user)
        try:
            recomendation_object.up_votes.get(pk=request.user.pk)
            recomendation_object.up_votes.remove(user)
        except Exception, e:
            print e
        recomendation_object.save()
    return HttpResponseRedirect('/recommendation_detail/')

    return HttpResponse("%s, %s" % (recomendation_object.up_votes, recomendation_object.down_votes))


def terms_of_use(request):
    context = {}
    return render(request, 'terms_of_use_and_privacy_policy.html', context)


@login_required
@csrf_exempt
def rate_me(request):

    context = {}

    context['recommendation'] = Recommendation.objects.get(pk=1)

    return render_to_response('test_rec_detail.html', context, context_instance=RequestContext(request))













# @login_require
# def favorite(request, pk):
#     user = Users.objects.get(pk=request.user.pk, business_user=False)
#     fav_type = request.GET.get('fav_type', None)
#     recomendation_object = Recommendation.objects.get(pk=pk)
#     if fav_type == 'like':
#         recomendation_object.like