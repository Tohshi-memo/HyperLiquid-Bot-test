# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T06:22:30.690505+00:00`
- Price records: `672`
- Market context records: `8169`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11778`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `news_risk_high->unknown_24h` score `8493.4498` n `38` status `ready` deltaP `37.1528` edge `707.5398` maxDD `0.0`
- `market_context_high->equity_24h` score `18.8033` n `61` status `ready` deltaP `44.3505` edge `1.3623` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.2735` n `62` status `ready` deltaP `38.1245` edge `0.5421` maxDD `-0.5442`
- `news_risk_high->equity_4h` score `9.1617` n `43` status `ready` deltaP `34.5611` edge `0.5536` maxDD `-0.6428`
- `market_context_high->metal_24h` score `8.1165` n `61` status `ready` deltaP `41.6667` edge `0.3986` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.5499` n `43` status `ready` deltaP `20.7956` edge `0.3844` maxDD `-2.1767`
- `market_context_high->index_4h` score `4.0419` n `62` status `ready` deltaP `36.8411` edge `0.0955` maxDD `-0.0092`
- `market_context_high->equity_1h` score `3.5654` n `62` status `ready` deltaP `21.1995` edge `0.1761` maxDD `-0.6254`
- `news_risk_high->equity_1h` score `3.4495` n `47` status `ready` deltaP `25.7294` edge `0.1468` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.9428` n `43` status `ready` deltaP `24.688` edge `0.0997` maxDD `-0.191`
- `market_context_high->index_1h` score `1.8617` n `62` status `ready` deltaP `21.5665` edge `0.0252` maxDD `-0.1069`
- `market_context_high->index_24h` score `1.8533` n `61` status `ready` deltaP `18.0641` edge `0.1842` maxDD `-1.3621`
- `news_risk_high->metal_4h` score `1.8358` n `43` status `ready` deltaP `16.8711` edge `0.0873` maxDD `-0.7433`
- `market_context_high->metal_4h` score `1.6973` n `62` status `ready` deltaP `21.2972` edge `0.0617` maxDD `-0.979`
- `news_risk_high->crypto_major_1h` score `1.5514` n `47` status `ready` deltaP `8.7622` edge `0.1106` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.29` n `47` status `ready` deltaP `9.6604` edge `0.0865` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.1777` n `43` status `ready` deltaP `12.8651` edge `0.2044` maxDD `-5.8012`
- `market_context_high->commodity_24h` score `1.0425` n `61` status `ready` deltaP `27.8233` edge `0.2367` maxDD `-15.7497`
- `market_context_high->fx_24h` score `0.9733` n `61` status `ready` deltaP `21.3058` edge `0.0531` maxDD `-0.6283`
- `market_context_high->metal_1h` score `0.6281` n `62` status `ready` deltaP `10.3921` edge `0.0209` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
