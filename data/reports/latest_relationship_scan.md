# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T07:37:15.725295+00:00`
- Price records: `672`
- Market context records: `1198`
- Flow alert records: `5356`
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

- `market_context_high->crypto_major_24h` score `18.5585` n `134` status `ready` deltaP `44.2553` edge `1.3647` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.447` n `134` status `ready` deltaP `22.0668` edge `0.6751` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `5.6479` n `134` status `ready` deltaP `4.0362` edge `0.5654` maxDD `-6.7322`
- `market_context_high->metal_24h` score `4.172` n `134` status `ready` deltaP `-4.2625` edge `0.5428` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `3.3734` n `134` status `ready` deltaP `-3.182` edge `0.5903` maxDD `-18.0378`
- `market_context_high->equity_4h` score `2.8237` n `134` status `ready` deltaP `14.7206` edge `0.2035` maxDD `-3.6396`
- `market_context_high->index_24h` score `1.9964` n `134` status `ready` deltaP `16.6355` edge `0.1641` maxDD `-5.3574`
- `market_context_high->equity_24h` score `1.558` n `134` status `ready` deltaP `16.8791` edge `0.3199` maxDD `-14.2815`
- `market_context_high->index_4h` score `0.9374` n `134` status `ready` deltaP `10.4273` edge `0.0769` maxDD `-2.1308`
- `market_context_high->fx_24h` score `0.4779` n `134` status `ready` deltaP `9.0174` edge `0.0556` maxDD `-2.7379`
- `market_context_high->index_1h` score `0.4676` n `134` status `ready` deltaP `8.1687` edge `0.0162` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3827` n `134` status `ready` deltaP `3.9838` edge `0.0431` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `-0.0956` n `134` status `ready` deltaP `6.4593` edge `0.1368` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.1119` n `134` status `ready` deltaP `5.3624` edge `0.0005` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.1902` n `134` status `ready` deltaP `8.4883` edge `-0.0114` maxDD `-2.2164`
- `market_context_high->crypto_major_1h` score `-0.3223` n `134` status `ready` deltaP `3.7269` edge `0.0104` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.3605` n `134` status `ready` deltaP `0.8781` edge `0.0322` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.8652` n `134` status `ready` deltaP `-3.137` edge `0.0103` maxDD `-2.252`
- `market_context_high->metal_4h` score `-0.9429` n `134` status `ready` deltaP `8.6116` edge `-0.0352` maxDD `-6.4478`
- `market_context_high->crypto_alt_4h` score `-1.0523` n `134` status `ready` deltaP `5.3217` edge `0.1261` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
