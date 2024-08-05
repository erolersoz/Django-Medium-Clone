from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from user_profile.models import Profile
from blog.forms import BlogPostModelForm
from .forms import ProfileModelForm
from slugify import slugify
from blog.models import BlogPost

@login_required(login_url='user:login_view')
def user_fav_view(request):
    ids = request.user.userpostfav_set.filter(is_deleted=False).values_list('post_id',flat=True).order_by('-updated_at')
    context = dict(
        title="Favorilerim",
        favs=BlogPost.objects.filter(id__in=ids,is_active=True)

    )   
    return render(request,'blog/post_list.html',context)



@login_required(login_url='user:login_view')
def profile_edit_view(request):
    user = request.user
    initial_data=dict(
        first_name=user.first_name,
        last_name=user.last_name,
    )
    form = ProfileModelForm(instance = user.profile,initial=initial_data)

    if request.method =="POST":
        form = ProfileModelForm(
            request.POST or None,
            request.FILES or None,
            instance = user.profile
        ) 
        if form.is_valid():
            f = form.save(commit=False)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            f.save()
            messages.success(request,'Profiliniz Guncelledi')
            return redirect('user:profile_edit_view')


    title="Profili düzenle"
    context=dict(
        form=form,
        title=title
    )
    return render(request,'common_components/form.html',context)




def login_view(request):

    if request.user.is_authenticated:
        messages.info(request,f'{request.user.username} daha önce login olmuşsun')
        return redirect('home_view')
        
    context=dict()
    if request.method=="POST":
        # print(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        #bu bilgileri doğru aldık mı
        if len(username)<6 or len(password)<6:
            messages.warning(request,f'Lütfen kullanıcı adı veya şifreyi doğru girinniz... 6 karakterde küçük olmamalı')
            # return redirect('home_view') burası anlaman içib buda çalışır logini tekrar dönderdik
            return redirect('user_profile:login_view')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request,f'{request.user.username} Login Başarılı')
            return redirect('home_view')
 
    return render (request,'user_profile/login.html',context)
def logout_view(request):
    messages.info(request,f'{request.user.username} Oturumun Sonlandırıldı')
    logout(request)
    return redirect('home_view')#anasayfaya geç


def register_view(request):
    context=dict()
    if request.method == "POST":
        post_info = request.POST
        email = post_info.get('email')
        email_confirm = post_info.get('email_confirm')
        first_name = post_info.get('first_name')
        last_name = post_info.get('last_name')
        password = post_info.get('password')
        password_confirm = post_info.get('password_confirm')
        instagram = post_info.get('instagram')
        print('*',30)
        print(email,email_confirm,password,password_confirm,first_name,last_name,instagram)
        if len(first_name) < 3 or len(last_name) < 3 or len(email) < 3 or len(password) <3:
            messages.warning(request,"Bilgiler En az 3 karakterden oluşmnalı")
            return redirect('user_profile:register_view')
        if email !=email_confirm:
            messages.warning(request,"Lüfen email Bilgisini Doğru Giriniz")
            return redirect('user_profile:register_view')
        if password !=password_confirm:
            messages.warning(request,"Lüfen password Bilgisini Doğru Giriniz")
            return redirect('user_profile:register_view')
        

        user, created=User.objects.get_or_create(username=email)
        #eğer kullanıcı create değilse kullanıcı daha önce sisteme kayıtlıdır
        if not created:
            user_login = authenticate(request,username=email,password=password)
            if user is not None:
                messages.success(request,"Daha önce kayıt olmuşsunuz ana sayfaya yönlendirildiniz")
                #kullanıcıyı login ettik
                login(request, user_login)
                return redirect('home_view')
            messages.warning(request,f'{email} adres sisteme kayıtlı ama login olmadınız login sayfasına yönlendiriyorsunuz')
            return redirect('user_profile:login_view')
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)

        profile, profile_created=Profile.objects.get_or_create(user=user)
        profile.imstagram = instagram
        profile.slug=slugify(f"{first_name}-{last_name}")
        user.save()
        profile.save()

        messages.success(request,f'{user.first_name} sisteme kaydedildiniz')
        user_login = authenticate(request,username=email,password=password)
        login(request, user_login)
        return redirect('home_view')

    return render(request,'user_profile/register.html')