from django.contrib import admin
# from .models import SPResult
# from .models import test
# # Register your models here.
#
#
# class Change_status(admin.ModelAdmin):
#     list_display = [ 'AccountID', 'AccountName', 'Status', 'CreateDate']
#     #Hiển thị danh sách
#
#
#     list_editable = ['Status']  # Cho phép chỉnh sửa trạng thái trực tiếp từ danh sách
#
#     actions = ['change_status_to_pending', 'change_status_to_not_gift','change_status_to_recieve_gift']
#     #Tạo ra option lựa chọn trong Select test to change trên giao diện Admin
#
#     # def status_color(self,color):
#     #     if color.status == 1:
#     #         color = 'red'
#     #     if color.status == 2:
#     #         color = 'yellow'
#     #         return f'<span style="color: {color};">{color.get_Status_display()}</span>'
#     #
#     # status_color.short_description = 'Status'
#     # status_color.allow_tags = True
#
#     def change_status_to_not_gift(self, request, queryset):
#         queryset.update(Status=0)  # Đặt trạng thái của các bản ghi được chọn thành 'Chưa nhận quà'
#     #hàm
#
#     def change_status_to_recieve_gift(self, request, queryset):
#         queryset.update(Status=1)  # Đặt trạng thái của các bản ghi được chọn thành 'Đã nhận quà'
#
#     def change_status_to_pending(self,request,queryset):
#         queryset.update(Status=2)   # Đặt trạng thái của các bản ghi được chọn thành 'Đang xử lí'
#     change_status_to_not_gift.short_description = "Change selected items to 'Chưa nhận quà'"
#     change_status_to_recieve_gift.short_description = "Change selected items to 'Đã nhận quà'"
#     change_status_to_pending.short_description = "Change selected items to 'Đang chờ xử lí'"
# admin.site.register(test,Change_status)
# admin.site.resgister(test)
# class SPAdmind(admin.ModelAdmin):
#     list = ['ID','AccountID','AccountName','Status','Create']
# admin.site.register(SPResult,SPAdmind)