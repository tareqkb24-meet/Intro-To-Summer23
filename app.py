from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return '''<html>
    <h1>EVERYTHING YOU CAN THINK ABOUT</h1>
    <p>welocome to the a photo gallery containing three types of photos: food, pets, and outer space</p>
    <a href = "/food1">go to the first food photo</a>
    <a href = "/pet1">go to the first pet</a>
    <a href = "/space1">go to the first space pic</a></html>'''



@app.route("/food1")
def food1():
    return '''<html>
    <h1>ITS PIZZAAAAAA</h1>
    <img src="https://www.allrecipes.com/thmb/iXKYAl17eIEnvhLtb4WxM7wKqTc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/240376-homemade-pepperoni-pizza-Beauty-3x4-1-6ae54059c23348b3b9a703b6a3067a44.jpg" style="width: 600px">
    <a href='/home'>home</a>
    <a href='/food2'>food2</a>
    </html>'''





@app.route("/food2")
def food2():
    return '''<html>
    <h1>HAMBURGERRRR</h1>
    <img src="https://media.cnn.com/api/v1/images/stellar/prod/220428140436-04-classic-american-hamburgers.jpg?c=16x9&q=h_833,w_1480,c_fill" style="width: 600px">
    <a href='/home'>home</a>
    <a href='/food3'>food3</a>
    <a href='/food1'>food1</a>
    </html>'''






@app.route("/food3")
def food3():
    return '''<html>
    <h1>SHAWARMAAAA</h1>
    <img src="https://www.recipetineats.com/tachyon/2022/02/Chicken-Shawarma-Wrap_2-SQ.jpg" style="width: 600px">
    <a href='/home'>home</a>
    </html>'''



@app.route("/pet1")

def pet1():
    return '''<html>
    <h1>ITS a mouseee</h1>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQnr7Q6htX2ZVQ6TP-LpwW9ufdUfgSoNshOQ&s" style="width: 600px">
    <a href='/home'>home</a>
    <a href="/pet2">pet2</a>
    </html>'''



@app.route("/pet2")

def pet2():
    return '''<html>
    <h1>ITS A CAT</h1>
    <img src="https://s.w-x.co/util/image/w/in-kittens.jpg?v=at&w=532&h=532" style="width: 600px">
    <a href='/home'>home</a>
    <a href="/pet3">pet3</a>
    <a href="/pet1">pet1</a>
    </html>'''




@app.route("/pet3")

def pet3():
    return '''<html>
    <h1>DOOOOGGGG</h1>
    <img src="https://www.humanesociety.org/sites/default/files/styles/768x326/public/2022-10/dog-583007.jpg?h=c6dbd090&itok=1KrPn9Xm" style="width: 600px">
    <a href='/home'>home</a>
    <a href='/pet2'>pet2</a>
    </html>'''



@app.route("/space1")
def space1():
    return '''<html>
    <img src="https://img.freepik.com/free-photo/ultra-detailed-nebula-abstract-wallpaper-4_1562-749.jpg" style="width: 600px">
    <a href='/home'>home</a>
    <a href='/space2'>the second pic</a>
    </html>'''



@app.route("/space2")
def space2():
    return '''<html>
    <img src="https://res.cloudinary.com/momentum-media-group-pty-ltd/image/upload/c_fill,q_auto:best,f_auto,e_unsharp_mask:80,w_830,h_478/Space%20Connect%2Fspace-exploration-sc_fm1ysf" style="width: 600px">
    <a href='/home'>home</a>
    <a href='/space1'>return to the first pic</a>
    </html>'''









































if __name__ == '__main__':
    app.run(debug=True)

