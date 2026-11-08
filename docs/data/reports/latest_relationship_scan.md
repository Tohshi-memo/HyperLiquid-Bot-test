# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T13:37:26.075090+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4735`

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

- `market_context_high->unknown_4h` score `57.3153` n `37` status `ready` deltaP `-5.0057` edge `4.8544` maxDD `-0.9139`
- `market_context_high->equity_24h` score `6.1245` n `37` status `ready` deltaP `15.4139` edge `0.8371` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.3368` n `39` status `ready` deltaP `12.287` edge `0.2421` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.1461` n `37` status `ready` deltaP `33.9239` edge `0.045` maxDD `-0.0521`
- `market_context_high->index_4h` score `2.151` n `37` status `ready` deltaP `27.8799` edge `0.0404` maxDD `-2.4279`
- `market_context_high->crypto_alt_1h` score `1.2076` n `39` status `ready` deltaP `14.663` edge `0.0844` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.1105` n `39` status `ready` deltaP `11.9684` edge `0.0713` maxDD `-3.0172`
- `market_context_high->index_24h` score `0.8701` n `37` status `ready` deltaP `10.6982` edge `0.1033` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.7082` n `37` status `ready` deltaP `10.9422` edge `-0.0051` maxDD `-0.0397`
- `market_context_high->commodity_24h` score `0.6483` n `37` status `ready` deltaP `6.2125` edge `0.1612` maxDD `-6.5601`
- `market_context_high->fx_1h` score `0.4944` n `39` status `ready` deltaP `8.1146` edge `0.0142` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.2013` n `39` status `ready` deltaP `2.33` edge `0.0373` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.0652` n `39` status `ready` deltaP `7.9457` edge `0.01` maxDD `-1.7019`
- `market_context_high->metal_1h` score `-0.044` n `39` status `ready` deltaP `1.7312` edge `0.0156` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.0694` n `37` status `ready` deltaP `2.0724` edge `0.0227` maxDD `-1.633`
- `market_context_high->crypto_alt_4h` score `-0.6902` n `37` status `ready` deltaP `19.2156` edge `0.0277` maxDD `-17.5435`
- `market_context_high->metal_4h` score `-0.7122` n `37` status `ready` deltaP `-1.6151` edge `-0.0355` maxDD `-0.9363`
- `market_context_high->equity_4h` score `-0.7197` n `37` status `ready` deltaP `21.9471` edge `0.0894` maxDD `-24.9053`
- `market_context_high->metal_24h` score `-2.2501` n `37` status `ready` deltaP `2.1444` edge `-0.1465` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-4.3157` n `37` status `ready` deltaP `-0.3544` edge `-0.1323` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
