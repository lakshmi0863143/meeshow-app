from ._anvil_designer import LoginTemplate
from anvil import *

class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""

  def text_box_2_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    username = self.text_box_1.text
    password = self.text_box_2.text
    alert('login succesfully')
    open_form('Home')

    



