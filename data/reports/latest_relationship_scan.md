# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T11:52:30.445202+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7916`

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

- `news_risk_high->unknown_24h` score `1089.1776` n `139` status `ready` deltaP `1.2153` edge `90.7567` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.2092` n `139` status `ready` deltaP `20.0877` edge `0.7787` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `3.5079` n `139` status `ready` deltaP `15.866` edge `0.63` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `3.0394` n `139` status `ready` deltaP `19.3382` edge `0.38` maxDD `-11.1179`
- `news_risk_high->index_24h` score `2.5241` n `139` status `ready` deltaP `24.97` edge `0.1134` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `1.772` n `139` status `ready` deltaP `22.9053` edge `0.1559` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.4334` n `139` status `ready` deltaP `20.3013` edge `0.1696` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.8269` n `139` status `ready` deltaP `7.736` edge `0.2833` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6423` n `139` status `ready` deltaP `7.0176` edge `0.0978` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.3138` n `139` status `ready` deltaP `7.2546` edge `0.0068` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `0.279` n `139` status `ready` deltaP `5.9073` edge `0.05` maxDD `-1.957`
- `news_risk_high->index_4h` score `-0.4148` n `139` status `ready` deltaP `4.5239` edge `0.0206` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.528` n `139` status `ready` deltaP `1.3408` edge `0.01` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.6885` n `139` status `ready` deltaP `-0.3016` edge `0.042` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1235` n `139` status `ready` deltaP `-8.0699` edge `-0.0022` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.136` n `139` status `ready` deltaP `11.5064` edge `-0.001` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.503` n `139` status `ready` deltaP `-10.2232` edge `0.0249` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-2.0388` n `139` status `ready` deltaP `-11.8662` edge `-0.0148` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.0834` n `139` status `ready` deltaP `-6.7677` edge `0.0495` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-4.0295` n `139` status `ready` deltaP `-12.6941` edge `-0.0093` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
