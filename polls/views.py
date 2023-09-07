from django.shortcuts import render

def all_popup_view(request):
    return render(request, 'dist/pages/all-popup.html')

def nhan_qua_view(request):
    return render(request, 'dist/pages/nhanqua.html')

def dang_ki_thong_tin(request):
    return render(request, 'dist/pages/dangkithongtin.html')
def dang_ki_thong_tin2(request):
    return render(request,'dist/pages/dangkithongtin2.html')

def trang_chu(request):
    return render(request,'dist/pages/index.html')

def the_le(request):
    return render(request,'dist/pages/thele.html')
def kiem_tra(request):
    context = {'nội dung':'hello'}
    return render(request,'dist/pages/kiemtra.html',context)
def nhan_qua(request):
    return render(request,'dist/pages/nhaqua.html')

def home(request):
    context = {'message': 'Xin chào từ Django!'}
    return render(request, 'dist/pages/test.html', context)
def test(request):
    return render(request,'dist/pages/test.html')