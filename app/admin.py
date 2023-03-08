from app import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

class ProductView(ModelView): #kế thừa ModalView đã import ở trên
    column_display_pk = True #hiện khóa sản phẩm
    can_view_details = True #xuất hiện thêm biểu tượng mắt
    can_export = True #Nút tải về danh sách về file csv
    column_searchable_list = ['name', 'description'] #thanh tìm kiếm
    column_filters = ['name', 'price'] #tìm kiếm riêng bằng filter
    column_exclude_list = ['image', 'active', 'created_date'] #không muốn hiển thị cột "image", "active", "created_date"
    column_labels = { #đặt tên tiêu đề của bảng
        'name': 'Nom du produit',
        'description': 'Description',
        'price': 'Prix',
        'image': 'Photo du produit',
        'category': 'Category'
    }
    column_sortable_list = ['id', 'name', 'price']#sắp xếp là mặc định cho tất cả các cột nhưng chức năng này dùng để chỉ định cột muốn sắp xếp

admin = admin = Admin(app=app, name='E-commerce Administration', template_mode='bootstrap4')


