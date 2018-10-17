from model import model

class present:
	def __init__(self, vw):
		self.p_view = vw
		self.p_model = model()

	def fill_routes_table(self):
		routes = self.p_model.get_routes()
		self.p_view.insert_into_route_table(routes)