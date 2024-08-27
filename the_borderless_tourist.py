# The Borderless Trousist is my first project in Python. 
# It functions as "an online application that gives you the power to find the parts of the city that fit the pace of your life" (Codecademy). 




# Data Lists
destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

attractions = [[] for attraction in destinations]

# logic to find traveler destinations and convert to internal data
def get_destination_index(destination):
    return destinations.index(destination)

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    return get_destination_index(traveler_destination)

# Attractions and functionality for adding new attractions
def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    attractions[destination_index].append(attraction)

test_destination_index = get_traveler_location(test_traveler)

add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


# Function to generate message for traveler and present attractions they might be interested in.
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]

    attractions_with_interest = []

    for possible_attraction in attractions_in_city:
        attraction_name = possible_attraction[0]
        attraction_tags = possible_attraction[1]

        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(attraction_name)
                break
    return attractions_with_interest

la_arts = find_attractions('Los Angeles, USA', ['art'])

def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    interests_string = 'Hi '
    interests_string += traveler[0]
    interests_string += ", we think you'll like these places around "
    interests_string += traveler_destination
    interests_string += ": "
    for attraction in traveler_attractions:
        interests_string += attraction + ", "
    return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)
