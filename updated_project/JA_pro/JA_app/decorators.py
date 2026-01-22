from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from functools import wraps


def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not  request.user.is_authenticated:
            return  HttpResponseForbidden("يجب تسجيل الدخول")
    
        if not (request.user.is_superuser or request.user.role == 'admin'):
            return HttpResponseForbidden('غير مصرح لك(Admins فقط)')

        return view_func(request, *args, **kwargs)   

    return wrapper


# def staff_or_admin_required(view_func):
#     @wraps(view_func)
#     def wrapper(request, *args, **kwargs):
#         if not  request.user.is_authenticated:
#             return HttpResponseForbidden("يجب تسجيل الدخول")

#         if not (request.user.is_superuser or  request.user.role in ['admin','staff']):
#             return HttpResponseForbidden('غير مصرح لك.')

#         return view_func(request, *args, **kwargs) 
#     return wrapper   
      
