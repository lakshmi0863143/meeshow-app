from ._anvil_designer import BorrowTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Borrow(BorrowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('arrow-circle-left')

  def text_area_2_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
   

  def text_area_1_change(self, **event_args):
    """This method is called when the text in this text area is edited"""

  def text_area_3_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
   




