from flask import Blueprint, flash, render_template, request
from website import rento

views=Blueprint('views',__name__)


# func run whenever we got to / (root page)
@views.route('/', methods=['GET','POST'])
def home():
    cities = ["Manhattan", "Queens", "Brooklyn"]
    home=[]
    data=request.form
    size=data.get('size_sqft')
    bedrooms=data.get('bedrooms')
    bathrooms=data.get('bathrooms')
    city=data.get('city')
    if size is None or size=='':
        size=0
    if bedrooms is None or bedrooms=='':
        bedrooms=0
    if bathrooms is None or bathrooms=='':
        bathrooms=0
    if city is None:
        city="Manhattan"
    home.append(size)
    home.append(bedrooms)
    home.append(bathrooms)
    home.append(city)

    rent=rento(home)
    print(rent[0][0][0])
    print(rent[1]*100)
    # flash("Your Rent Predictions is:" ,category="calculated")
    


    return render_template("Home.html", cities=cities,cvalue=round(rent[0][0][0],2),caccuracy=round(rent[1]*100,2))
    

