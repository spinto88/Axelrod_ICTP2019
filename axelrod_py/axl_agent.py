import os
import ctypes as C
import random as rand

libc = C.CDLL(os.getcwd() + '/axelrod_py/libc.so')

class Axl_agent(C.Structure):

	"""
	Axelrod agent: it is caracterized by a cultural vector feat, with f features, which each can adopt q different traits.
	"""

	_fields_ = [('f', C.c_int),('q', C.c_int),('feat', C.POINTER(C.c_int)),('degree', C.c_int),('neighbors', C.POINTER(C.c_int)),('label', C.c_int)]

	def __init__(self, f, q):
		"""
		Constructor: f number of features, q number of traits per feature, q_z number of traits of the first feature only.
		"""
		self.f = f
		self.q = q

		# Initialize the agent's state with a random one.
		self.feat = (C.c_int * self.f)()
        	    
		for i in range(self.f):
			self.feat[i] = rand.randint(0, self.q-1)
      
	def homophily(self, other):
		"""
		This method returns the homophily of an agent respect to other one.
		"""
		libc.homophily.argtypes = [Axl_agent, Axl_agent]
		libc.homophily.restype = C.c_double

		return libc.homophily(self, other)

class Axl_mass_media(C.Structure):
	"""
	Axelrod agent: it is caracterized by a cultural vector feat, with f features, which each can adopt q different traits.
	"""

	_fields_ = [('f', C.c_int),('q', C.c_int),('feat', C.POINTER(C.c_int)),('phi', C.c_double)]

	def __init__(self, f, q, phi):
		"""
		Constructor: f number of features, q number of traits per feature, q_z number of traits of the first feature only.
		"""
		self.f = f
		self.q = q
		self.phi = phi

		# Initialize the agent's state with a random one.
		self.feat = (C.c_int * self.f)()
        	    
		for i in range(self.f):
			self.feat[i] = rand.randint(0, self.q-1)
      
	def homophily(self, other):
		"""
		This method returns the homophily of an agent respect to other one.
		"""
		libc.homophily_with_mm.argtypes = [Axl_agent, Axl_mass_media]
		libc.homophily_with_mm.restype = C.c_double

		return libc.homophily_with_mm(other, self)
