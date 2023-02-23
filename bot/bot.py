import pandas as pd
from td.client import TDClient
from td.utils import milliseconds_since_epochs

from datetime import datetime
from datetime import time
from datetime import timezone

from typing import List
from typing import Dict
from typing import Union

class PyRobot():
  def __init__(self, client_id: str, redirect_uri: str, credentials_path: str = None, trading_account: str = None) -> None:
    self.trading_account: str = trading_account
    self.client_id: str = client_id
    self.redirect_uri: str = redirect_uri
    self.credentials_path: str = credentials_path
    self.session: TDClient = self._create_session()
    self.trades: dict = {}
    self.historical_prices: dict = {}
    self.stock_frame = None

  def _create_session(self) -> TDClient:

    td_client = TDClient(
      client_id = self.client_id,
      
    ) 


  