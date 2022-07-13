from flask import Flask, render_template
import os


app = Flask(__name__)
picFolder = os.path.join('static', 'pics')

app.config['UPLOAD_FOLDER'] = picFolder

@app.route("/")
def index():
    logo=os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    pic1=os.path.join(app.config['UPLOAD_FOLDER'], 'pic1.jpeg')
    pic2=os.path.join(app.config['UPLOAD_FOLDER'], 'pic2.jpeg')
    pic3=os.path.join(app.config['UPLOAD_FOLDER'], 'pic3.mp4')
    return render_template ('index.html', user_image=logo, user_image1=pic1, user_image2=pic2, user_image3=pic3)

@app.route("/aboutus")
def aboutus():
    profile1=os.path.join(app.config['UPLOAD_FOLDER'], 'profile1.jpg')
    profile2=os.path.join(app.config['UPLOAD_FOLDER'], 'profile2.jpg')
    profile3=os.path.join(app.config['UPLOAD_FOLDER'], 'profile3.jpg')
    profile4=os.path.join(app.config['UPLOAD_FOLDER'], 'profile4.jpg')
    profile5=os.path.join(app.config['UPLOAD_FOLDER'], 'profile5.jpg')
    profile6=os.path.join(app.config['UPLOAD_FOLDER'], 'profile6.jpg')
    logo=os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    return render_template ('aboutus.html', user_image=logo, user_imagep1=profile1, user_imagep2=profile2, user_imagep3=profile3 , user_imagep4=profile4, user_imagep5=profile5, user_imagep6=profile6)

@app.route("/completed-project")
def completedproject():
    
    shelter2=os.path.join(app.config['UPLOAD_FOLDER'], 'shelter2.jpeg')
    shelter3=os.path.join(app.config['UPLOAD_FOLDER'], 'shelter3.jpeg')
    shelter4=os.path.join(app.config['UPLOAD_FOLDER'], 'shelter4.jpeg')
    
    logo=os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    shop1=os.path.join(app.config['UPLOAD_FOLDER'], 'shop1.jpg')
    shop2=os.path.join(app.config['UPLOAD_FOLDER'], 'shop2.jpg')
    shop3=os.path.join(app.config['UPLOAD_FOLDER'], 'shop3.jpg')

    punagam1=os.path.join(app.config['UPLOAD_FOLDER'], 'punagam1.jpeg')
    punagam2=os.path.join(app.config['UPLOAD_FOLDER'], 'punagam2.jpeg')
    punagam3=os.path.join(app.config['UPLOAD_FOLDER'], 'punagam3.jpeg')

    house1=os.path.join(app.config['UPLOAD_FOLDER'], 'house1.jpg')
    house2=os.path.join(app.config['UPLOAD_FOLDER'], 'house2.jpeg')
    house3=os.path.join(app.config['UPLOAD_FOLDER'], 'house3.jpg')

    sport1=os.path.join(app.config['UPLOAD_FOLDER'], 'sport1.JPG')
    sport2=os.path.join(app.config['UPLOAD_FOLDER'], 'sport2.JPG')
    sport3=os.path.join(app.config['UPLOAD_FOLDER'], 'sport3.JPG')

    hospital1=os.path.join(app.config['UPLOAD_FOLDER'], 'hospital1.jpg')
    hospital2=os.path.join(app.config['UPLOAD_FOLDER'], 'hospital2.jpg')
    hospital3=os.path.join(app.config['UPLOAD_FOLDER'], 'hospital3.jpg')

    ind1=os.path.join(app.config['UPLOAD_FOLDER'], 'ind1.jpg')
    ind2=os.path.join(app.config['UPLOAD_FOLDER'], 'ind2.jpg')

    staff1=os.path.join(app.config['UPLOAD_FOLDER'], 'staff1.jpg')


    return render_template ('completedproject.html', user_image=logo,  user_image2=shelter2, user_image3=shelter3, user_image4=shelter4, user_imagea1=shop1, user_imagea2=shop2, user_imagea3=shop3, user_imageb1=punagam1, user_imageb2=punagam2, user_imageb3=punagam3, user_imagec1=house1, user_imagec2=house2, user_imagec3=house3,  user_imaged1=sport1, user_imaged2=sport2, user_imaged3=sport3, user_imagee1=hospital1, user_imagee2=hospital2, user_imagee3=hospital3, user_imagef1=ind1, user_imagef2=ind2, user_imageg1=staff1)

@app.route("/running-project")
def runningproject():
    logo=os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    return render_template ('runningproject.html', user_image=logo)

@app.route("/career")
def career():
    logo=os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    return render_template ('career.html', user_image=logo)


 

if __name__== "__main__":
    app.run(debug=True)