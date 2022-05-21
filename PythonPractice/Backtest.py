import numpy as np
import pandas as pd
from numbers import Number
from utils_trade import read_file, assert_msg, crossover, SMA

class Backtest:
    """
    Backtest回测类，用于读取历史行情数据、执行策略、模拟交易并估计收益。
    
    初始化的时候调用Baskettest.run来时回测
    instance, or ·backtesting.backtesing.Backtest.optimize· to
    optimize it
    """
    
    def __init__(self,
                 data: pd)