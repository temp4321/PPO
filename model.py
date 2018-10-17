import polyline
import gpxpy
import geopy.distance

class model:
	def __init__(self):
		self.routes = []

	def get_routes(self):
		return self.routes

	def print_routs(self):
		for i in range(len(self.routes)):
			print("Route name: ", end = "")
			print(self.routes[i][0])
			print("Route length: ", end = "")
			print(self.routes[i][1])
			print("Route random point: ", end = "")
			print(self.routes[i][2][2])
			print("Route polyline first 40 elements: ", end = "")
			print(self.routes[i][3][:40])
			print("--------------------------------------------")

	def add_route_from_file(self, file_list):
		for i in range(len(file_list)):
			with open(file_list[i], "r") as f:
				tmp_track = gpxpy.parse(f).tracks[0]
				tmp_points = []
				for segment in tmp_track.segments:
					for point in segment.points:
						tmp_points.append([point.latitude,\
			point.longitude, point.elevation, point.course])

				tmp_polyline = polyline.encode(tmp_points)

				tmp_dist = self.route_distanse(tmp_points)
				#print(tmp_dist)

				self.routes.append([tmp_track.name,\
				 tmp_dist, tmp_track.description, tmp_points, tmp_polyline])

	def add_route(self, route):
		self.routes.append(route)

	def remove_route(self, route_ind):
		self.routes.pop(route_ind)

	def edit_route_name(self, route_ind, new_name):
		self.routes[route_ind][0] = new_name

	def edit_route_description(self, route_ind, new_description):
		self.routes[route_ind][1] = new_description
	
	def remove_point(self, route_ind, point_ind):
		self.routes[route_ind][2].pop(point_ind)

	def edit_point(self, route_ind, point_ind, new_point):
		self.routes[route_ind][2][point_ind] = new_point

	def route_distanse(self, points):
		dist = 0
		
		for i in range(len(points) - 1):
			dist += geopy.distance.vincenty(points[i][:2], points[i+1][:2]).km

		return round(dist, 2)

'''
По поводу потяженности:
В desc всех файлов убираем расстояние
Либа или своя ф-ия для подсчета
В add_route считать, и пересчитывать во всех функциях с изменениями

По поводу карты высот - во View
'''

m = model()

m.add_route_from_file(["routes/route1.gpx"])
