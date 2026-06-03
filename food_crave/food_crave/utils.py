from geopy.geocoders import nominatim

def geocode_address(address):

    geolocator=nominatim(user_agent="food_crave")

    location = geolocator.geocode(address)
    
    if location:
        
        return(
            location.latitude,
            location.longitude   
            )
    return(None,None)