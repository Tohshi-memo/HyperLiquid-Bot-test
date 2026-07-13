# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T14:07:31.484529+00:00`
- Price records: `672`
- Market context records: `6610`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9808`

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

- `market_context_high->unknown_24h` score `3.3578` n `171` status `ready` deltaP `2.0711` edge `0.5572` maxDD `-13.2952`
- `market_context_high->unknown_1h` score `2.1112` n `206` status `ready` deltaP `-5.6799` edge `0.3039` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.206` n `171` status `ready` deltaP `7.2584` edge `0.1556` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.2775` n `206` status `ready` deltaP `2.2135` edge `0.0004` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4006` n `206` status `ready` deltaP `7.2045` edge `0.0272` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.5325` n `206` status `ready` deltaP `0.4404` edge `-0.0029` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.5544` n `206` status `ready` deltaP `-0.4084` edge `0.0036` maxDD `-0.7564`
- `market_context_high->crypto_alt_1h` score `-0.654` n `206` status `ready` deltaP `4.4779` edge `0.0176` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.8727` n `206` status `ready` deltaP `9.9737` edge `0.0096` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.1636` n `206` status `ready` deltaP `1.8284` edge `0.0012` maxDD `-4.1619`
- `market_context_high->commodity_4h` score `-1.2011` n `206` status `ready` deltaP `0.0888` edge `-0.0051` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.3242` n `206` status `ready` deltaP `-4.1379` edge `-0.0026` maxDD `-2.0797`
- `market_context_high->unknown_4h` score `-1.5596` n `206` status `ready` deltaP `-17.6844` edge `0.2285` maxDD `-10.5788`
- `market_context_high->fx_4h` score `-1.6231` n `206` status `ready` deltaP `2.1179` edge `-0.001` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.6989` n `206` status `ready` deltaP `7.4621` edge `0.0639` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.078` n `206` status `ready` deltaP `4.4814` edge `0.0439` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1485` n `206` status `ready` deltaP `-1.2003` edge `0.0186` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.0754` n `206` status `ready` deltaP `7.6545` edge `-0.0184` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-3.4948` n `171` status `ready` deltaP `-0.6597` edge `0.0549` maxDD `-11.8838`
- `market_context_high->fx_24h` score `-5.7614` n `171` status `ready` deltaP `-6.715` edge `-0.0006` maxDD `-9.1136`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
