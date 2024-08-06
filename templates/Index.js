const elem = document.getElementById('city-input');
const resultDiv = document.getElementById('weather-result');

function getweather() {
    const city = elem.value.trim();
    if (!city) {
        alert('Please enter the city name');
        return;
    }
    fetch(`http://127.0.0.1:8000/weather/${city}`)
    .then((response) => response.json())
    .then((data)=> {
       resultDiv.innerText = `City: ${data.city}\nTemperature: ${data.temperature}°C\nDescription: ${data.description}`;
        })
    .catch((err)=>console.log("err",err));
    resultDiv.innerText = "Failed to fetch weather data"
    }


const button = document.getElementById("fetch-weather-button");
button-addEventListener('click',getweather);
