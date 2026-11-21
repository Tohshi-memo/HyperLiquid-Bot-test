# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T10:07:39.943033+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2674`

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

- `market_context_high->unknown_1h` score `10030.2821` n `126` status `ready` deltaP `1.0146` edge `835.8699` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6116.4213` n `126` status `ready` deltaP `-0.3145` edge `509.7344` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.1649` n `126` status `ready` deltaP `4.5504` edge `0.015` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2991` n `126` status `ready` deltaP `2.8585` edge `0.0038` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5162` n `126` status `ready` deltaP `11.7958` edge `0.0358` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4154` n `126` status `ready` deltaP `-9.1056` edge `-0.0013` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.7868` n `126` status `ready` deltaP `6.2874` edge `0.0151` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.8828` n `126` status `ready` deltaP `-6.2693` edge `0.002` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.2044` n `126` status `ready` deltaP `-7.3235` edge `-0.0217` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.4359` n `126` status `ready` deltaP `-3.794` edge `-0.0144` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.5435` n `126` status `ready` deltaP `2.5591` edge `0.0028` maxDD `-13.8788`
- `market_context_high->crypto_major_24h` score `-3.1713` n `114` status `ready` deltaP `23.2365` edge `0.7745` maxDD `-98.212`
- `market_context_high->crypto_alt_1h` score `-3.2734` n `126` status `ready` deltaP `-4.194` edge `-0.0171` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.4702` n `126` status `ready` deltaP `-1.2607` edge `0.1282` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-6.3885` n `114` status `ready` deltaP `11.0289` edge `0.1155` maxDD `-47.7124`
- `market_context_high->fx_24h` score `-6.4111` n `114` status `ready` deltaP `-14.4371` edge `-0.0066` maxDD `-5.8465`
- `market_context_high->commodity_4h` score `-6.809` n `126` status `ready` deltaP `-17.9007` edge `-0.0788` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.7531` n `126` status `ready` deltaP `-2.3278` edge `0.0507` maxDD `-46.5016`
- `market_context_high->crypto_alt_24h` score `-11.111` n `114` status `ready` deltaP `11.102` edge `0.46` maxDD `-108.1279`
- `market_context_high->index_24h` score `-13.4921` n `114` status `ready` deltaP `-26.6812` edge `-0.1185` maxDD `-34.9038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
