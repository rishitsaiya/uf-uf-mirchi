

class Connection(object):
	"""docstring for connection"""
	def __init__(self):
		super(Connection, self).__init__()

	def cursor(self):
		return operator()
			

class operator(object):
	"""docstring for operator"""
	def __init__(self):
		super(operator, self).__init__()
	
	def execute(self, query, **kwargs):
		if 'id' in kwargs:
			return kwargs['object'].objects.get(id=kwargs['id'])
		elif 'author' in kwargs:
			return kwargs['object'].objects.filter(author=kwargs['author'])
		elif 'username' in kwargs:
			return kwargs['object'].objects.get(username=kwargs['username'])
		elif 'user' in kwargs:
			return kwargs['object'].objects.get(user=kwargs['user'])
		else:
			return kwargs['object'].objects.all()

	def excute(self, query, **kwargs):
		kwargs['object'].save()

class transaction(object):
	"""docstring for transaction"""
	def __init__(self):
		super(transaction, self).__init__()
		
connection = Connection()