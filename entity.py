#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import personas
from persona import Persona


class Entity (Persona):

	####################################################################
	### Persona class extension to handle user arguments with prefix ###
	####################################################################

	def ask (self, *args, **kwargs):
		### @description: protected method for requesting input from user under a persona
		### @parameter: <args>, @type: <tuple>
		### @parameter: <kwargs>, @type: <dict>
		### @return: @type: <str>

		# set formatted request string for use in input request
		request = self.__format(kwargs.pop('request', 'please enter your selection'))
		# set formatted confirmation string for using in confirmation request
		confirm = self.__format(kwargs.pop('confirm', 'is {{%s}} the correct answer?'))
		# set formatted reject string for use to notify of failed input
		reject = self.__format(kwargs.pop('reject', '{{%s}} is not an accepted option'))
		# set option separator to break option listings
		separator = self.__format(kwargs.pop('separator', '/'))
		# set input divider to break user input from requests
		divider = self.__format(kwargs.pop('divider', ':'))
		# set null string to identify blank input
		null = self.__format(kwargs.pop('null', 'empty'))
		# set args to list
		args = list(args)
		# set accept string for confirmation request
		accept = kwargs.get('accept', 'YES')
		# set decline string for rejection request
		decline = kwargs.get('decline', 'NO')
		# set confirmations to list
		confirms = [accept, decline]
		# set clean string options
		selection_options = [super(Entity, self).Clean(self.__str(string)) for string in args]
		# set beautiful string options
		selection_beautiful = [super(Entity, self).Pretty(**self.__dict(option)) for option in args]
		# set confirmation string options
		confirmation_options = [super(Entity, self).Clean(self.__str(string)) for string in confirms]
		# set confirmation string options
		confirmation_beautiful = [super(Entity, self).Pretty(**self.__dict(option)) for option in confirms]		
		# get and return user input
		return self.__strin(request = request, confirm = confirm, reject = reject, null = null, separator = separator, divider = divider, selection_options = selection_options, selection_beautiful = selection_beautiful, confirmation_options = confirmation_options, confirmation_beautiful = confirmation_beautiful, accept = accept, decline = decline)

	def __strin (self, **kwargs):
		### @description: private method for requesting input to match selection options
		### @parameter: <kwargs>, @type: <dict>
		### @return: @type: <str>

		# set base options
		options = kwargs.get('selection_options')
		# set user input string
		user = str(self.__input(request = kwargs.get('request'), selection = kwargs.get('selection_options'), beautified = kwargs.get('selection_beautiful'), divider = kwargs.get('divider'), separator = kwargs.get('separator')) or kwargs.get('null'))
		# initialise loop to test strings against user input
		for i in range(0, len(options)):
			# confirm selection in options
			if user.upper() == options[i].upper():
				# set selection for handler
				return self.__strout(user, **kwargs)
		# notify that user input was not accepted
		print super(Entity, self).say(kwargs.get('reject') % user)
		# request user input
		return self.__strin(**kwargs)

	def __strout (self, arg, **kwargs):
		### @description: private method for confirming returned selection
		### @parameter: <arg>, @type: <str>
		### @parameter: <kwargs>, @type: <dict>
		### @return: @type: <str>

		# set base options
		options = kwargs.get('confirmation_options')
		# set user input string
		user = str(self.__input(request = kwargs.get('confirm') % arg, selection = kwargs.get('confirmation_options'), beautified = kwargs.get('confirmation_beautiful'), divider = kwargs.get('divider'), separator = kwargs.get('separator')) or kwargs.get('null'))
		# confirm user string matches confirmation string
		if user.upper() == options[0].upper():
			# set selection for handler
			return arg
		# confirm user string matches rejection string
		elif user.upper() == options[1].upper():
			# request new input
			return self.__strin(**kwargs)
		# notify that user input was not accepted
		print super(Entity, self).say(kwargs.get('reject') % user)
		# request user input
		return self.__strout(arg, **kwargs)
		
	def __input (self, **kwargs):
		### @description: private function for collecting user input 
		### @parameter: <kwargs>, @type: <dict>
		### @return: @type: <str>

		# set user input
		return raw_input(super(Entity, self).say(super(Entity, self).concat(kwargs.get('request'), super(Entity, self).cconcat([super(Entity, self).cconcat(kwargs.get('beautified'), kwargs.get('separator')), kwargs.get('divider'), ' ']))))

	def __format (self, arg = {}):
		### @description: private method for beautifying wildcard argument
		### @parameter: <arg>, @type: <dict/str>, @default: <dict>
		### @return: @type: <str>

		# set beautiful string
		return super(Entity, self).Pretty(**self.__dict(arg))

	def __dict (self, arg = 'sample'):
		### @description: private method for casting argument to string.pretty kwargs
		### @parameter: <arg>, @type: <dict/str>, @default: <str>
		### @return: @type: <dict>

		# cast argument to dict if argument is string otherwise assume dict
		return { 'string': str(arg), 'attributes': ['BOLD'] } if type(arg) is not dict else arg

	def __str (self, arg = { 'string': 'sample' }):
		### @description: private method for casting argument to string
		### @parameter: <arg>, @type: <dict/str>, @default: <dict>
		### @return: @type: <str>

		# cast dict to str if else assume str
		return arg['string'] if type(arg) is dict else arg

	def __init__ (self, **kwargs):
		### @descrption: class constructor
		### @parameters: <kwargs>, @type: <dict>

		# set call to inherited persona
		super(Entity, self).__init__(**kwargs)




if __name__ == '__main__':

	# entity named request
	print Entity(**Persona().__dict__).ask({ 'string': 'A', 'attributes': ['BOLD'], 'tag': True }, { 'string': 'B', 'attributes': ['BOLD'], 'tag': True }, request = 'please enter one option', confirm = Entity.cconcat(['user input', Entity.Pretty('{{%s}}', ['UNDERLINE']), 'correct?'], ' '), reject = Entity.cconcat(['user input', Entity.Pretty('{{%s}}', ['UNDERLINE']), 'is incorrect.'], ' '), accept = {'string': 'YES', 'attributes': ['GREEN','BOLD'], 'tag': True }, decline =  'NO')
