from django.shortcuts import render

def site_bilgileri():
    sozluk = {}
    return sozluk
# Create your views here.
def admin_homebase(request):
    content = site_bilgileri()
    return render(
        request=request,
        template_name="admin_temp/admin_index.html",
        context=content
        )