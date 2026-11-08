# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T18:22:26.116392+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `56`

- Symbol pattern count: `5607`

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

- `market_context_high->unknown_4h` score `60.2518` n `39` status `ready` deltaP `-4.6591` edge `5.0968` maxDD `-0.9139`
- `market_context_high->equity_24h` score `5.8217` n `37` status `ready` deltaP `13.5042` edge `0.8246` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.3751` n `39` status `ready` deltaP `12.7361` edge `0.2423` maxDD `-2.3425`
- `market_context_high->fx_4h` score `2.7428` n `39` status `ready` deltaP `29.3777` edge `0.0417` maxDD `-0.0521`
- `market_context_high->index_4h` score `1.8711` n `39` status `ready` deltaP `24.6365` edge `0.0387` maxDD `-2.4279`
- `market_context_high->crypto_alt_1h` score `1.1861` n `39` status `ready` deltaP `14.2139` edge `0.0856` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.1405` n `39` status `ready` deltaP `11.9684` edge `0.0738` maxDD `-3.0172`
- `market_context_high->index_24h` score `1.0718` n `37` status `ready` deltaP `13.3024` edge `0.1118` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.7982` n `37` status `ready` deltaP `10.9422` edge `0.0024` maxDD `-0.0397`
- `market_context_high->fx_1h` score `0.4944` n `39` status `ready` deltaP `8.1146` edge `0.0142` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.2426` n `39` status `ready` deltaP `3.0785` edge `0.0376` maxDD `-0.1621`
- `market_context_high->commodity_24h` score `0.2346` n `37` status `ready` deltaP `3.0875` edge `0.129` maxDD `-6.5601`
- `market_context_high->commodity_1h` score `0.0722` n `39` status `ready` deltaP `8.0954` edge `0.0099` maxDD `-1.7019`
- `market_context_high->metal_1h` score `-0.0191` n `39` status `ready` deltaP `2.1803` edge `0.0158` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.1389` n `39` status `ready` deltaP `0.645` edge `0.0233` maxDD `-1.633`
- `market_context_high->equity_4h` score `-0.6057` n `39` status `ready` deltaP `23.0144` edge `0.0969` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.7817` n `39` status `ready` deltaP `-3.0566` edge `-0.0348` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-0.9714` n `39` status `ready` deltaP `16.014` edge `0.013` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-1.9019` n `37` status `ready` deltaP `4.9222` edge `-0.136` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.8836` n `39` status `ready` deltaP `1.6416` edge `-0.1096` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
