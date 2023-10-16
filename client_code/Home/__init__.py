from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('About')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Borrow')

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('FAQs')

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Lender')

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Online_chat')

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('QuickFacts')

  def link_7_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('UnderFeedback')

  def link_8_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('working')

  def link_9_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Login')

  def text_area_1_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
  










 