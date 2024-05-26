from django.urls import path
from. import views

app_name = "ekart_admin"

urlpatterns = [   
   path('',views.admin_home,name="admin_home"),
   path('category/add',views.add_category,name="add_category"),
   path('category/list',views.view_category,name="view_category"),
   path('sellers/list/pending',views.pending_sellers,name="pending_sellers"),
   path('sellers/list/approved',views.approved_sellers,name="approved_sellers"),
   path('customers/list',views.customers,name="customers"),
]