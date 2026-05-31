# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T22:52:23.797669+00:00`
- Price records: `672`
- Market context records: `2504`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9280`

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

- `market_context_high->unknown_24h` score `5.4391` n `124` status `ready` deltaP `19.8869` edge `0.3535` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.4537` n `151` status `ready` deltaP `21.5756` edge `0.4952` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.7675` n `151` status `ready` deltaP `17.8596` edge `0.3759` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.1484` n `124` status `ready` deltaP `12.78` edge `0.5795` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.7863` n `151` status `ready` deltaP `11.0745` edge `0.18` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.5666` n `158` status `ready` deltaP `6.8332` edge `0.1204` maxDD `-6.1656`
- `market_context_high->crypto_alt_24h` score `0.5042` n `124` status `ready` deltaP `3.0129` edge `0.7403` maxDD `-43.6595`
- `market_context_high->crypto_major_1h` score `0.4312` n `158` status `ready` deltaP `7.1326` edge `0.1078` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.1504` n `124` status `ready` deltaP `4.3514` edge `0.0816` maxDD `-2.5127`
- `market_context_high->index_4h` score `-0.1245` n `151` status `ready` deltaP `6.9264` edge `0.0276` maxDD `-2.3986`
- `market_context_high->equity_24h` score `-0.1293` n `124` status `ready` deltaP `18.4084` edge `0.0192` maxDD `-6.8828`
- `market_context_high->fx_1h` score `-0.2936` n `158` status `ready` deltaP `1.7149` edge `0.0044` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.485` n `158` status `ready` deltaP `2.0011` edge `0.0182` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.5732` n `158` status `ready` deltaP `-0.6253` edge `0.0058` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.5868` n `158` status `ready` deltaP `-0.4017` edge `0.0034` maxDD `-3.0759`
- `market_context_high->commodity_1h` score `-0.6092` n `158` status `ready` deltaP `3.8657` edge `0.0113` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.6918` n `151` status `ready` deltaP `-1.6081` edge `0.008` maxDD `-0.8774`
- `market_context_high->fx_24h` score `-0.9026` n `124` status `ready` deltaP `2.8506` edge `0.0038` maxDD `-2.7484`
- `market_context_high->equity_1h` score `-0.9234` n `158` status `ready` deltaP `-0.5836` edge `0.0108` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-0.9555` n `151` status `ready` deltaP `1.8929` edge `0.0465` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
