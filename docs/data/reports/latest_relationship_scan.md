# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T15:52:31.214420+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4791`

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

- `market_context_high->unknown_4h` score `30.0562` n `39` status `ready` deltaP `-4.6591` edge `2.5805` maxDD `-0.9139`
- `market_context_high->equity_24h` score `6.0859` n `37` status `ready` deltaP `15.0667` edge `0.8362` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.3835` n `39` status `ready` deltaP `12.7361` edge `0.243` maxDD `-2.3425`
- `market_context_high->fx_4h` score `2.822` n `39` status `ready` deltaP `30.2924` edge `0.0422` maxDD `-0.0521`
- `market_context_high->index_4h` score `1.8893` n `39` status `ready` deltaP `24.789` edge `0.0392` maxDD `-2.4279`
- `market_context_high->crypto_alt_1h` score `1.1849` n `39` status `ready` deltaP `14.3636` edge `0.0845` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.1393` n `39` status `ready` deltaP `12.1181` edge `0.0727` maxDD `-3.0172`
- `market_context_high->index_24h` score `0.9464` n `37` status `ready` deltaP `11.5663` edge `0.1073` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.755` n `37` status `ready` deltaP `10.9422` edge `-0.0012` maxDD `-0.0397`
- `market_context_high->fx_1h` score `0.5207` n `39` status `ready` deltaP `8.414` edge `0.0144` maxDD `-0.1681`
- `market_context_high->commodity_24h` score `0.4657` n `37` status `ready` deltaP `4.65` edge `0.1482` maxDD `-6.5601`
- `market_context_high->index_1h` score `0.2581` n `39` status `ready` deltaP `3.3779` edge `0.0376` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.08` n `39` status `ready` deltaP `8.2451` edge `0.0099` maxDD `-1.7019`
- `market_context_high->metal_1h` score `-0.0191` n `39` status `ready` deltaP `2.1803` edge `0.0158` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.1334` n `39` status `ready` deltaP `0.7974` edge `0.023` maxDD `-1.633`
- `market_context_high->equity_4h` score `-0.5861` n `39` status `ready` deltaP `23.1669` edge `0.0984` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.7912` n `39` status `ready` deltaP `-3.2091` edge `-0.035` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-0.9182` n `39` status `ready` deltaP `16.1664` edge `0.0188` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-2.1308` n `37` status `ready` deltaP `3.186` edge `-0.1435` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.8342` n `39` status `ready` deltaP `1.794` edge `-0.1065` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
