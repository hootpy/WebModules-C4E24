from flask import Flask,render_template
app = Flask(__name__)
food_list=[
        {
            "Name": "Trà Sữa SayTea - Tây Sơn",
            "image": "https://images.foody.vn/res/g66/655637/prof/s576x330/foody-upload-api-foody-mobile-say-tea-jpg-180827142117.jpg",
            "link": "https://www.foody.vn/ha-noi/tra-sua-saytea-tay-son",
            "video": "https://www.youtube.com/embed/ZEwn6DwDUCI"
        },
        {
            "Name": "Chik’s House - Hainanese Chicken Rice & Hotpot",
            "image": "https://images.foody.vn/res/g81/804658/prof/s576x330/foody-upload-api-foody-mobile-ck-jpg-181221174423.jpg",
            "link": "https://www.foody.vn/ha-noi/chik-s-house-hainanese-chicken-rice-hotpot-tran-thai-tong",
            "video": "https://www.youtube.com/embed/XjH3Gr9-ffs"
        },
        {
            "Name": "Dezato - Japanese Desert, Cafe & Tea",
            "image": "https://images.foody.vn/res/g75/746446/prof/s576x330/foody-upload-api-foody-mobile-untitled-2-jpg-180907153116.jpg",
            "link": "https://www.foody.vn/ha-noi/dezato-japanese-desert-cafe-tea",
            "video": "https://www.youtube.com/embed/beD_X8WiEJA"
        }
    ]

@app.route('/')
def index():
    return "Hello"

@app.route('/characters')
def characters():
    c_list=[
        {
        "name": "Thanos",
        "image": "https://www.sideshowtoy.com/wp-content/uploads/2018/04/marvel-avengers-infinity-war-thanos-sixth-scale-figure-hot-toys-feature-903429-1.jpg",
        "link": "https://vi.wikipedia.org/wiki/Thanos"
    },
        {
        "name": "Iron Man",
        "image": "https://www.sideshowtoy.com/assets/products/903421-iron-man/lg/marvel-avengers-infinity-war-iron-man-sixth-scale-figure-hot-toys-903421-13.jpg",
        "link": "https://vi.wikipedia.org/wiki/Ng%C6%B0%E1%BB%9Di_S%E1%BA%AFt"
    },
    {
        "name": "Aquaman",
        "image": "https://chieuphimquocgia.com.vn/Content/Images/uploaded/2018/poster/Aquaman_DC_Comics_Banner_Home.jpg",
        "link": "https://en.wikipedia.org/wiki/Aquaman_(film)"
    }
    ]
    return render_template("characters-list.html",
                            character_list = c_list)

@app.route('/names')
def names():
    name_list = ["huy","quan","huong","tung"]
    return render_template("names.html", name_list=name_list)

@app.route('/food_items')
def food_items():
    return render_template("food_items.html", food_list=food_list)

@app.route('/food_detail/<int:pos>')
def food_detail(pos):
    video_link = food_list[pos]["video"]
    return render_template("food_detail.html", video_link=video_link)


if __name__ == '__main__':
  app.run(debug=True)