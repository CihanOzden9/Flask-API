from flask import Flask, request

#server başlatıyoruz
app = Flask(__name__) #dosya adı ile değişken adı aynı olmalıdır

#Örnek veriler oluşturuldu
stores = [
    {
        "name":"My store",
        "items":[
            {
                "name":"Chair",
                "price":14.99
            }
        ]
    }
]


# oluşturulan sayfaya örnek verileri "get" ediyoruz
@app.get("/store")
def get_stores():
    return {"stores":stores} 


#Sayfadan gönderilen verileri "store" verilerine ekliyoruz
@app.post("/store")
def create_store():
    request_data = request.get_json() #istek gönderildi
    new_store = {"name":request_data["name"], "items":[]} #veriler eklendi
    stores.append(new_store)
    return new_store, 201 #201 ile gönder ve kabul et return ediliyor


@app.post("/store/<string:name>/item") #belirlenen mağazanın altındaki itemlere eriş
def create_item(name):
    request_data = request.get_json() #json dosyasına erişim isteği gönder
    for store in stores:
        if store["name"] == name:
            new_item = {"name":request_data["name"],"price":request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201 #verileri item altına ekle
    return {"message":"Store not found!"}, 404 #Sayfa bulunamazsa hata döndür


@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message":"Store not found"}, 404

@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items":store["items"]}, {"message":"your rock"}
    return {"message":"Store not found"}, 404