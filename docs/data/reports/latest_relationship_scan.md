# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T06:07:28.202266+00:00`
- Price records: `672`
- Market context records: `7850`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `10.5258` n `132` status `ready` deltaP `28.5507` edge `0.821` maxDD `-6.0681`
- `market_context_high->commodity_24h` score `1.22` n `132` status `ready` deltaP `21.1225` edge `0.1192` maxDD `-7.0012`
- `market_context_high->equity_4h` score `1.2194` n `133` status `ready` deltaP `4.263` edge `0.3192` maxDD `-6.9701`
- `market_context_high->crypto_major_1h` score `1.0358` n `133` status `ready` deltaP `12.7088` edge `0.0457` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `1.0167` n `133` status `ready` deltaP `13.2794` edge `0.168` maxDD `-6.7444`
- `market_context_high->metal_24h` score `0.973` n `133` status `ready` deltaP `8.8584` edge `0.2311` maxDD `-2.3927`
- `market_context_high->fx_24h` score `0.8359` n `132` status `ready` deltaP `25.2187` edge `0.0478` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.725` n `133` status `ready` deltaP `7.8958` edge `0.0937` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.615` n `133` status `ready` deltaP `7.2849` edge `0.1144` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.5647` n `133` status `ready` deltaP `9.5272` edge `0.0429` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.401` n `133` status `ready` deltaP `8.9447` edge `0.0168` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1868` n `133` status `ready` deltaP `4.2783` edge `0.0303` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0966` n `133` status `ready` deltaP `6.0975` edge `0.0133` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.119` n `133` status `ready` deltaP `11.9347` edge `0.051` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3354` n `133` status `ready` deltaP `1.5749` edge `0.0003` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.7644` n `133` status `ready` deltaP `2.465` edge `0.0202` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.1994` n `132` status `ready` deltaP `-4.9658` edge `0.0896` maxDD `-2.1544`
- `market_context_high->metal_4h` score `-1.2579` n `133` status `ready` deltaP `3.4247` edge `0.0778` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.3723` n `133` status `ready` deltaP `-2.174` edge `0.0014` maxDD `-1.6936`
- `market_context_high->crypto_alt_24h` score `-1.8328` n `133` status `ready` deltaP `15.2631` edge `0.1928` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
