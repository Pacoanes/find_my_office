def find(ciu, metros):
    bd = df20[df20["ciudad"]==ciu]
    cd=[]
    for c in range(len(bd)):
        d={}
        coor=bd["oficina_principal"].values[c]['coordinates']
        query=db.limpio.find({"oficina_principal": {"$near": {"$geometry": {"type":"Point","coordinates":coor},"$maxDistance": metros,}}})
        num = query.count()
        coord=query[0]["oficina_principal"]["coordinates"]
        coordenada_buena=[coord[1],coord[0]]
        name=query[0]["name"]
        d.update(numero = num, donde = coordenada_buena, nombre = name)
        cd.append(d)
        nl = sorted(cd, key=lambda k: k['numero'], reverse=True)[0]
        
        res = req.get("https://maps.googleapis.com/maps/api/geocode/json?latlng={}, {}&key={}".format(nl["donde"][0], nl["donde"][1],g_key)).json()
        dirr= res["results"][0]["formatted_address"]
        
        #hacer mapa con folium
        mi = folium.Map(location=nl["donde"], zoom_start=17, control_scale=True)
        folium.Marker(location=nl["donde"], popup='{}: Hay {} empresas en un radio de {} metros'.format(dirr,nl["numero"],metros), icon=folium.Icon(color='blue', icon='home'),).add_to(mi)
        folium.Circle(location=nl["donde"], radius=nl["numero"]*30, color='blue', fill=True, fill_color='blue').add_to(mi)
        mi.save('index.html')
    return mi
    