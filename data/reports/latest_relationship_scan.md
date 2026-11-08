# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T20:07:26.590788+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `56`

- Symbol pattern count: `5619`

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

- `market_context_high->unknown_4h` score `70.1734` n `39` status `ready` deltaP `-4.6591` edge `5.9236` maxDD `-0.9139`
- `market_context_high->equity_24h` score `5.4257` n `37` status `ready` deltaP `12.2889` edge `0.7997` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.1803` n `45` status `ready` deltaP `12.6713` edge `0.2265` maxDD `-2.3425`
- `market_context_high->fx_4h` score `2.6782` n `39` status `ready` deltaP `28.6156` edge `0.0414` maxDD `-0.0521`
- `market_context_high->index_4h` score `1.7762` n `39` status `ready` deltaP `23.5694` edge `0.0379` maxDD `-2.4279`
- `market_context_high->index_24h` score `1.1114` n `37` status `ready` deltaP `13.8232` edge `0.1134` maxDD `-2.7123`
- `market_context_high->crypto_alt_1h` score `0.8971` n `45` status `ready` deltaP `10.346` edge `0.0873` maxDD `-3.1881`
- `market_context_high->fx_24h` score `0.827` n `37` status `ready` deltaP `10.9422` edge `0.0048` maxDD `-0.0397`
- `market_context_high->crypto_major_1h` score `0.7039` n `45` status `ready` deltaP `8.1005` edge `0.0632` maxDD `-3.0172`
- `market_context_high->index_1h` score `0.6072` n `45` status `ready` deltaP `6.4538` edge `0.0346` maxDD `-0.1621`
- `market_context_high->metal_1h` score `0.4004` n `45` status `ready` deltaP `7.7778` edge `0.0143` maxDD `-0.6226`
- `market_context_high->commodity_24h` score `0.1145` n `37` status `ready` deltaP `3.0875` edge `0.1136` maxDD `-6.5601`
- `market_context_high->commodity_1h` score `-0.0078` n `45` status `ready` deltaP `7.006` edge `0.0069` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `-0.0773` n `39` status `ready` deltaP `1.5596` edge `0.0251` maxDD `-1.633`
- `market_context_high->fx_1h` score `-0.1835` n `45` status `ready` deltaP `0.1664` edge `0.0107` maxDD `-0.1681`
- `market_context_high->equity_4h` score `-0.6932` n `39` status `ready` deltaP `21.9473` edge `0.0928` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.8165` n `39` status `ready` deltaP `-3.6664` edge `-0.0352` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-1.0011` n `39` status `ready` deltaP `15.8615` edge `0.0102` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-1.7579` n `37` status `ready` deltaP `6.1374` edge `-0.1321` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.8956` n `39` status `ready` deltaP `1.6416` edge `-0.1106` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
