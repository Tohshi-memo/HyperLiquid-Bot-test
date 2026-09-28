# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T10:52:28.705145+00:00`
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

- `news_risk_high->unknown_24h` score `996.2976` n `139` status `ready` deltaP `1.2153` edge `83.0167` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `5.879` n `139` status `ready` deltaP `19.7405` edge `0.7535` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `3.1284` n `139` status `ready` deltaP `15.1716` edge `0.603` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `2.6838` n `139` status `ready` deltaP `18.6438` edge `0.355` maxDD `-11.1179`
- `news_risk_high->index_24h` score `2.4265` n `139` status `ready` deltaP `24.2756` edge `0.1099` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `1.6441` n `139` status `ready` deltaP `22.2956` edge `0.1493` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.3734` n `139` status `ready` deltaP `20.3013` edge `0.1646` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.8281` n `139` status `ready` deltaP `7.736` edge `0.2834` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6674` n `139` status `ready` deltaP `7.1673` edge `0.0989` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.315` n `139` status `ready` deltaP `7.2546` edge `0.0069` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `0.2838` n `139` status `ready` deltaP `5.9073` edge `0.0504` maxDD `-1.957`
- `news_risk_high->index_4h` score `-0.4536` n `139` status `ready` deltaP `4.219` edge `0.0194` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5855` n `139` status `ready` deltaP `0.742` edge `0.0092` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.6916` n `139` status `ready` deltaP `-0.4513` edge `0.0426` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1407` n `139` status `ready` deltaP `-8.3693` edge `-0.0024` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.1637` n `139` status `ready` deltaP `11.0491` edge `-0.0015` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.484` n `139` status `ready` deltaP `-9.9184` edge `0.0253` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-2.0396` n `139` status `ready` deltaP `-11.8662` edge `-0.0149` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.106` n `139` status `ready` deltaP `-6.7677` edge `0.0466` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.9459` n `139` status `ready` deltaP `-12.0844` edge `-0.0064` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
