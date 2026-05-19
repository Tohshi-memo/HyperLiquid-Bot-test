# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T07:22:18.787419+00:00`
- Price records: `672`
- Market context records: `1197`
- Flow alert records: `5353`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `18.5717` n `134` status `ready` deltaP `44.2553` edge `1.3658` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.4362` n `134` status `ready` deltaP `22.0668` edge `0.6742` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `5.6347` n `134` status `ready` deltaP `4.0362` edge `0.5643` maxDD `-6.7322`
- `market_context_high->metal_24h` score `4.0969` n `134` status `ready` deltaP `-4.4362` edge `0.5377` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `3.4557` n `134` status `ready` deltaP `-3.0084` edge `0.596` maxDD `-18.0378`
- `market_context_high->equity_4h` score `2.8407` n `134` status `ready` deltaP `14.8731` edge `0.2039` maxDD `-3.6396`
- `market_context_high->index_24h` score `1.9381` n `134` status `ready` deltaP `16.4619` edge `0.1604` maxDD `-5.3574`
- `market_context_high->equity_24h` score `1.5123` n `134` status `ready` deltaP `16.7055` edge `0.3152` maxDD `-14.2815`
- `market_context_high->index_4h` score `0.9216` n `134` status `ready` deltaP `10.2748` edge `0.0766` maxDD `-2.1308`
- `market_context_high->fx_24h` score `0.5074` n `134` status `ready` deltaP `9.191` edge `0.0569` maxDD `-2.7379`
- `market_context_high->index_1h` score `0.4688` n `134` status `ready` deltaP `8.1687` edge `0.0163` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4055` n `134` status `ready` deltaP `4.1335` edge `0.044` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `-0.0932` n `134` status `ready` deltaP `6.4593` edge `0.1371` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.1238` n `134` status `ready` deltaP `5.2127` edge `0.0005` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.1854` n `134` status `ready` deltaP `8.4883` edge `-0.011` maxDD `-2.2164`
- `market_context_high->crypto_major_1h` score `-0.3083` n `134` status `ready` deltaP `3.8766` edge `0.0112` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.3598` n `134` status `ready` deltaP `0.8781` edge `0.0323` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.8676` n `134` status `ready` deltaP `-3.137` edge `0.0101` maxDD `-2.252`
- `market_context_high->metal_4h` score `-0.9375` n `134` status `ready` deltaP `8.6116` edge `-0.0345` maxDD `-6.4478`
- `market_context_high->crypto_alt_4h` score `-1.0531` n `134` status `ready` deltaP `5.3217` edge `0.126` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
