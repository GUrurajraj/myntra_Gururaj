from django.urls import path
from . import views as v
from app.views import ProductRegister, ProductList, ProductRemove, ProductUpdate

urlpatterns = [
    path("", v.index, name="index"),
    path("ProductRegister/", ProductRegister.as_view(), name="ProductRegister"),
    path("ProductList/", ProductList.as_view(), name="ProductList"),
    path("ProductRemove/<int:pk>", ProductRemove.as_view(), name="ProductRemove"),
    path("ProductUpdate/<int:pk>", ProductUpdate.as_view(), name="ProductUpdate"),
    path("signin/", v.signin, name="signin"),
    path("signup/", v.signup, name="signup"),
    path("userlogout/", v.userlogout, name="userlogout"),
    path("mobilelist/",v.mobilelist, name="mobilelist"),
    path("clothslist",v.clothslist, name='clothslist'),
    path("shoeslist/",v.shoeslist, name="shoeslist"),
    path("electronicslist/",v.electronicslist, name="electronicslist"),
    path("showpricerange/", v.showpricerange, name="showpricerange"),
    path("sortingproduct/",v.sortingproduct, name="sortingproduct"),
    path("searchproduct/",v.searchproduct, name="searchproduct"),
    path("showcarts/",v.showcarts, name="showcarts"),
    path("addcart/<int:productid>",v.addcart, name="addcart"),
    path("removecart/<int:productid",v.removecart, name="removecart"),
    path('updateqty/<int:qv>/<int:productid>',v.updateqty, name="updateqty"),
]












