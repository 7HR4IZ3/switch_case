class switch:
	def __init__(self, match, _return=False, args=[], kwargs={}):
		self.match, self._return, self.cases = match, _return, {}
		self.args, self.kwargs = args, kwargs
		self.cases = {}

	def default(self, func, args=[], kwargs={}):
		self.cases["default"] = {
			"func": func,
			"args": self.args+args,
			"kwargs": dict(**self.kwargs, **kwargs)
		}
		return self.make()

	def make(self):
		matched = False
		for case in self.cases:
			if self.match == case:
				matched = True
				if self._return:return self.cases[case]['func'](*self.cases[case]['args'], **self.cases[case]['kwargs'])
				else:self.cases[case]['func'](*self.cases[case]['args'], **self.cases[case]['kwargs'])
				break
		
		if not matched:
			if self._return:return self.cases["default"]['func'](*self.cases[case]['args'], **self.cases[case]['kwargs'])
			else:self.cases["default"]['func'](*self.cases[case]['args'], **self.cases[case]['kwargs'])

	def case(self, case, call, args=[], kwargs={}):
		self.cases[f"{case}"] = {
			"func": call,
			"args": self.args+args,
			"kwargs": dict(**self.kwargs, **kwargs)
		}
		return self
