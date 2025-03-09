import requests

def fetch_api_data():
    url = "https://api.freeapi.app/api/v1/public/youtube/channel"
    response = requests.get(url)
    data_api = response.json()

    if data_api["success"] and "data" in data_api:
        user_data = data_api["data"]
        user_channel = user_data["info"]["snippet"]["brandingSettings"]["channel"]
        user_title = user_channel["title"]
        user_desc = user_channel["description"]

        return user_title, user_desc
    
    else:
        raise Exception("failed to fetch")
    
def main():
    try:
        title, desc = fetch_api_data()
        print(f"Username: {title} \nuser description: {desc}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()