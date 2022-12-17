# Weather

## Forecast process:
1. Get geocode(lat/lon coordinates) by location
    - By address: https://positionstack.com/documentation
    - By gridsquare: https://github.com/space-physics/maidenhead
2. Get forecast URLs for local weather office by geocode: https://api.weather.gov/points/43.6394,-70.7374
3. Get forecast for weather office: https://api.weather.gov/gridpoints/GYX/60,54/forecast

## Gridsquare example
```sh
pip install maidenhead 5.8K
python3 -m maidenhead fn43pp
43.6250 -70.7500
```

## Warnings by state:
https://api.weather.gov/alerts/active?area=ME
Search areaDesc for county