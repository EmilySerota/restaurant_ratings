
def restaurant_ratings(document):
	"""function will take a document and return the restaurant name and rating"""

	new_restaurant = input("Please enter a new restaurant to add:")
	new_restaurant_rating = input("Please enter your new restaurant's rating:")
	ratings_dict = {}
	
	with open(document) as file:
		for line in file:
			restaurant, rating = line.strip().split(":")

			#creates a dictionary with the restaurant & rating as key value pairs
			ratings_dict[restaurant] = rating

			#adds the restaurant that was input by the user
			ratings_dict[new_restaurant] = new_restaurant_rating
			
		#create a list of tuples so you can easily sort
		ratings_tup = ratings_dict.items()
		
		#sort tuple list by the key
		sorted_restaurants = sorted(ratings_tup)
		
		#go through the sorted list and return restaurant in rating in the new format
		for restaurant in sorted_restaurants:
			print ("{} is rated at {}".format(restaurant[0], restaurant[1]))

		#ratings_dict[new_restaurant] = new_restaurant_rating
		return ratings_dict

restaurant_ratings("scores.txt")


#restaurant_ratings()
#print (restaurant_rating_dict)


