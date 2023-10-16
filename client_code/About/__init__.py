from ._anvil_designer import AboutTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class About(AboutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def text_area_2_change(self, **event_args):
    """This method is called when the text in this text area is edited"""

  def text_area_3_change(self, **event_args):
    """This method is called when the text in this text area is edited"""

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Home')

    
  

    

   

