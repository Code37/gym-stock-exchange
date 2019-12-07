from gym.envs.registration import register

register(
    id='game-stock-exchange-v0',
    entry_point='gym_exchange.envs:StockExchangeDiscrete',
)

register(
    id='game-stock-exchange-continuous-v0',
    entry_point='gym_exchange.envs:StockExchangeContinuous',
)
