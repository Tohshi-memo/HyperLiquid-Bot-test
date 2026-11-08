# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T18:07:28.436621+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `56`

- Symbol pattern count: `5773`

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

- `market_context_high->unknown_4h` score `57.2146` n `39` status `ready` deltaP `-4.6591` edge `4.8437` maxDD `-0.9139`
- `market_context_high->equity_24h` score `5.8656` n `37` status `ready` deltaP `13.6778` edge `0.8271` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.3979` n `39` status `ready` deltaP `12.8858` edge `0.2432` maxDD `-2.3425`
- `market_context_high->fx_4h` score `2.7562` n `39` status `ready` deltaP `29.5302` edge `0.0418` maxDD `-0.0521`
- `market_context_high->index_4h` score `1.8845` n `39` status `ready` deltaP `24.789` edge `0.0388` maxDD `-2.4279`
- `market_context_high->crypto_alt_1h` score `1.2125` n `39` status `ready` deltaP `14.3636` edge `0.0868` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.1633` n `39` status `ready` deltaP `12.1181` edge `0.0747` maxDD `-3.0172`
- `market_context_high->index_24h` score `1.0604` n `37` status `ready` deltaP `13.1288` edge `0.1115` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.7934` n `37` status `ready` deltaP `10.9422` edge `0.002` maxDD `-0.0397`
- `market_context_high->fx_1h` score `0.4944` n `39` status `ready` deltaP `8.1146` edge `0.0142` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.2511` n `39` status `ready` deltaP `3.2282` edge `0.0377` maxDD `-0.1621`
- `market_context_high->commodity_24h` score `0.2502` n `37` status `ready` deltaP `3.0875` edge `0.131` maxDD `-6.5601`
- `market_context_high->commodity_1h` score `0.0699` n `39` status `ready` deltaP `8.0954` edge `0.0096` maxDD `-1.7019`
- `market_context_high->metal_1h` score `-0.0191` n `39` status `ready` deltaP `2.1803` edge `0.0158` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.1492` n `39` status `ready` deltaP `0.4925` edge `0.023` maxDD `-1.633`
- `market_context_high->equity_4h` score `-0.5923` n `39` status `ready` deltaP `23.1669` edge `0.0976` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.7817` n `39` status `ready` deltaP `-3.0566` edge `-0.0348` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-0.9541` n `39` status `ready` deltaP `16.1664` edge `0.0142` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-1.9242` n `37` status `ready` deltaP `4.7485` edge `-0.1367` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.863` n `39` status `ready` deltaP `1.794` edge `-0.1089` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
