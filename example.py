import requests

BASE_URL = "http://sosmedboost.com/api/service"

def connect(payload: dict, endpoint: str):
    headers = {
        "apiKey": "Your apikey..",
        "secretKey": "Your screetKey",
        "Content-Type": "application/json"
    }

    # pastikan endpoint nggak ada slash dobel
    url = f"{BASE_URL}?type={endpoint}"

    try:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code != 200:
            print("Status Code:", response.status_code)
            print("Response Text:", response.text)

        return response.json()
    except requests.exceptions.RequestException as e:
        print("Request Error:", str(e))
        return None
    except ValueError:
        # kalau JSON decode gagal
        print("Invalid JSON response")
        print("Response Text:", response.text)
        return None

def layanan():
    payload = {"lang": "id"}
    resp = connect(payload, "layanan")  
    print(resp)


def check_layanan_detail(code: str):
    payload = {"lang": "id", "code": code}
    resp = connect(payload, "get-layanan-detail")  
    print(resp)


def check_balance():
    payload = {"lang": "id"}
    resp = connect(payload, "get-balance")  #
    print(resp)

def check_order_detail(trx: str):
    payload = {"lang": "id", "trx": trx}
    resp = connect(payload, "get-order-detail")  
    print(resp)


def order_product(product_id: str, data: str, quantity: int):
    payload = {
        "lang": "id",
        "product_id": product_id,
        "data": data,
        "quantity": quantity
    }
    resp = connect(payload, "order-product")  
    print(resp)

if __name__ == "__main__":
    layanan() 
    check_layanan_detail("ttvtlike")
    check_balance()
    check_order_detail("VH-TRX456*****") 
    order_product("9989","https://vt.tiktok.com/ZSABqQ5ah/",100)
