import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Replace 'YOUR_YELP_API_KEY' with your actual Yelp API key
YELP_API_KEY = 'i3XimU32UigfvPKtHvh_MrVvV4alXZpugMZsMY0PtXdyWAfUy5dKsB6tkOgEjPLWW2jY-dgRFsPhW7TOPIqAWpmxdla5qc4yVOiBCOsOKxJ1kTqKrn_TW2SCk9ObZ3Yx'
HEADERS = {'Authorization': f'Bearer {YELP_API_KEY}'}

def search_street_food(location):
    url = "https://api.yelp.com/v3/businesses/search"
    params = {
        "term": "street food",
        "location": location,
        "limit": 10,
        "categories": "foodtrucks,streetvendors"
    }
    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code == 200:
        return response.json().get("businesses", [])
    return []

@app.route('/', methods=['GET', 'POST'])
def index():
    food_spots = []
    if request.method == 'POST':
        location = request.form.get('location')
        if location:
            food_spots = search_street_food(location)
    return render_template('index.html', food_spots=food_spots)

if __name__ == '__main__':
    app.run(debug=True)
