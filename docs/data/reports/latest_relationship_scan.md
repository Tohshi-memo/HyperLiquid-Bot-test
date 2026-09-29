# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T16:37:33.673286+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7160`

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

- `news_risk_high->unknown_24h` score `2588.004` n `139` status `ready` deltaP `1.2153` edge `215.6589` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.2579` n `139` status `ready` deltaP `31.546` edge `1.5397` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.9707` n `139` status `ready` deltaP `33.9216` edge `0.8594` maxDD `-11.039`
- `news_risk_high->crypto_major_24h` score `8.0233` n `139` status `ready` deltaP `24.8938` edge `0.9461` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.1714` n `139` status `ready` deltaP `38.5117` edge `0.1604` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.7606` n `139` status `ready` deltaP `31.586` edge `0.2883` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.8125` n `142` status `ready` deltaP `28.5899` edge `0.2039` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `1.3643` n `142` status `ready` deltaP `9.5479` edge `0.316` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.9444` n `142` status `ready` deltaP `7.5694` edge `0.1193` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6695` n `142` status `ready` deltaP `8.0016` edge `0.0684` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.509` n `142` status `ready` deltaP `9.0495` edge `0.0111` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.1304` n `142` status `ready` deltaP `9.7497` edge `0.0312` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.2886` n `142` status `ready` deltaP `2.7389` edge `0.073` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5169` n `142` status `ready` deltaP `1.0141` edge `0.0131` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2603` n `142` status `ready` deltaP `-7.0873` edge `0.0351` maxDD `-3.6214`
- `news_risk_high->fx_4h` score `-1.2858` n `142` status `ready` deltaP `9.4362` edge `-0.0064` maxDD `-3.0414`
- `news_risk_high->crypto_major_4h` score `-1.5898` n `142` status `ready` deltaP `-3.9205` edge `0.0938` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8193` n `142` status `ready` deltaP `-8.9947` edge `-0.0036` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.8939` n `142` status `ready` deltaP `-9.7537` edge `-0.0103` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.3513` n `142` status `ready` deltaP `-9.6122` edge `0.0045` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
