# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T20:37:16.590844+00:00`
- Price records: `672`
- Market context records: `1354`
- Flow alert records: `5814`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8794`

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

- `market_context_high->crypto_major_24h` score `13.5376` n `129` status `ready` deltaP `33.2889` edge `1.0194` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.6958` n `129` status `ready` deltaP `11.9994` edge `1.1447` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.4623` n `129` status `ready` deltaP `28.4036` edge `0.8008` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.0745` n `129` status `ready` deltaP `23.6959` edge `0.2902` maxDD `-5.3574`
- `market_context_high->commodity_24h` score `3.1199` n `129` status `ready` deltaP `-7.9861` edge `0.4614` maxDD `-6.8535`
- `market_context_high->equity_4h` score `2.3062` n `157` status `ready` deltaP `11.8912` edge `0.1834` maxDD `-3.6396`
- `market_context_high->equity_24h` score `1.8737` n `129` status `ready` deltaP `16.59` edge `0.3623` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.4846` n `129` status `ready` deltaP `16.1054` edge `0.0628` maxDD `-0.3831`
- `market_context_high->unknown_24h` score `0.2085` n `129` status `ready` deltaP `-4.8692` edge `0.3228` maxDD `-10.1706`
- `market_context_high->metal_4h` score `0.1035` n `157` status `ready` deltaP `13.068` edge `0.0646` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.0776` n `166` status `ready` deltaP `5.337` edge `0.0163` maxDD `-1.6329`
- `market_context_high->index_4h` score `-0.0016` n `157` status `ready` deltaP `4.8742` edge `0.0762` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.0558` n `166` status `ready` deltaP `2.0327` edge `0.0264` maxDD `-1.9017`
- `market_context_high->metal_1h` score `-0.2033` n `166` status `ready` deltaP `7.8638` edge `-0.0004` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.4204` n `166` status `ready` deltaP `2.1211` edge `-0.0036` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5983` n `166` status `ready` deltaP `0.1533` edge `0.0106` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.8892` n `166` status `ready` deltaP `-0.7268` edge `0.0178` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.1733` n `166` status `ready` deltaP `-3.6` edge `-0.0199` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.3165` n `157` status `ready` deltaP `8.4676` edge `0.1658` maxDD `-19.5565`
- `market_context_high->unknown_4h` score `-1.3868` n `157` status `ready` deltaP `1.4292` edge `0.0398` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
