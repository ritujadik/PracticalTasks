from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "e3bb4b14e5b910014f5a29cc615106c4"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


@app.get("/weather/{city}")
def get_weather(city:str):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        weather = {
            "city" : city,
            "temperature":data["main"]["temp"],
            "description":data["weather"][0]["description"]
        }
        return weather
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500,detail=str(e))

    except KeyError:
        raise HTTPException(status_code=404, detail="City not found or API response format changed")





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)




