from flask import Flask, request, render_template
import folium

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['POST'])
def location():
    data = request.json
    lat = data['latitude']
    lng = data['longitude']

    print(f"Lokasi diterima: {lat}, {lng}")

    # Buat peta dari lokasi
    map = folium.Map(location=[lat, lng], zoom_start=16)
    folium.Marker([lat, lng], popup="Lokasi HP").add_to(map)
    map.save("static/map.html")

    return {'status': 'OK'}

@app.route('/map')
def map_view():
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)