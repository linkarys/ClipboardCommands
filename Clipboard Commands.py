# coding=utf8
import sublime_plugin, sublime, re
from html.parser import HTMLParser

class HTMLStripper(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.fed = []
	def handle_data(self, d):
		self.fed.append(d)
	def get_data(self):
		return ''.join(self.fed)

def clipboard():
	return sublime.get_clipboard()

def copy(data):
	sublime.set_clipboard(data)

# to transfer data to sublime text
def clean_paste(data):
	# clean word
	data = data.replace('”', '"').replace('“', '"').replace('’', "'")
	data = data.replace('________________________________________', '\n')
	# clean htmlentities
	data = HTMLParser().unescape(data)
	return data;

def strip_html_tags(data):
	s = HTMLStripper()
	data = re.sub('<br ?/?>', '\n', data, re.I)
	s.feed(data)
	return s.get_data()

# to transfer data from sublime text
def clean_copy(data):
	# clean html
	data = re.sub('<br ?/?>', '\n', data, re.I);
	data = re.sub('<[^>]*>', '', data);
	# clean htmlentities
	from html.parser import HTMLParser
	data = HTMLParser().unescape(data)
	return data;

# to transfer data from sublime text
def clean_line_number(data):
	# clean line number
	data = re.sub('(^|(?<=\n))[^\S\n]*\d+[^\S\n](?=[^\n]+)', '', data);
	return data;

# cut

class ClipboardCommandsCutAll(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command('select_all')
		self.view.run_command('cut')

class ClipboardCommandsCutPlainText(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command('cut')
		copy(clean_copy(clipboard()))

# copy

class ClipboardCommandsCopyAll(sublime_plugin.TextCommand):
	def run(self, edit):
		copy(self.view.substr(sublime.Region(0, self.view.size())))

class ClipboardCommandsCopyPlainText(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command('copy')
		copy(clean_copy(clipboard()))

# paste

class ClipboardCommandsPasteInAll(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command('select_all')
		self.view.run_command('paste')


class ClipboardCommandsPastePlainText(sublime_plugin.TextCommand):
	def run(self, edit):
		copy(clean_paste(clipboard()))
		self.view.run_command('paste')

class ClipboardCommandsPastePlainTextWithHtmlTagsStripOut(sublime_plugin.TextCommand):
	def run(self, edit):
		copy(strip_html_tags(clean_paste(clipboard())))
		self.view.run_command('paste')

class ClipboardCommandsPasteWithoutLineNumber(sublime_plugin.TextCommand):
	def run(self, edit):
		copy(clean_line_number(clipboard()))
		self.view.run_command('paste')

