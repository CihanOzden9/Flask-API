from flask import Flask, request

#server başlatıyoruz
app = Flask(__name__) #dosya adı ile değişken adı aynı olmalıdır

#Örnek veriler oluşturuldu
stores = [
    {
        "name":"my store",
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