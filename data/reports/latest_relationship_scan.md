# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T16:07:33.528921+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7782`

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

- `news_risk_high->unknown_24h` score `2596.566` n `139` status `ready` deltaP `1.2153` edge `216.3724` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `7.7099` n `139` status `ready` deltaP `22.6919` edge `0.8864` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `4.9176` n `139` status `ready` deltaP `18.8174` edge `0.7278` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `4.6783` n `139` status `ready` deltaP `22.2896` edge `0.4969` maxDD `-11.1179`
- `news_risk_high->index_24h` score `2.9354` n `139` status `ready` deltaP `27.9214` edge `0.128` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `2.1976` n `139` status `ready` deltaP `24.4297` edge `0.1812` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.7816` n `139` status `ready` deltaP `20.6485` edge `0.1963` maxDD `-6.8392`
- `news_risk_high->crypto_alt_1h` score `0.701` n `139` status `ready` deltaP `7.1673` edge `0.1017` maxDD `-4.2849`
- `news_risk_high->crypto_alt_4h` score `0.5112` n `139` status `ready` deltaP `6.6689` edge `0.2641` maxDD `-15.9436`
- `news_risk_high->equity_1h` score `0.5044` n `139` status `ready` deltaP `7.1049` edge `0.0608` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4479` n `139` status `ready` deltaP `8.6019` edge `0.009` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.2513` n `139` status `ready` deltaP `5.7434` edge `0.0261` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5244` n `139` status `ready` deltaP `1.3408` edge `0.0103` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.6269` n `139` status `ready` deltaP `0.1475` edge `0.0469` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1889` n `139` status `ready` deltaP `-9.2675` edge `-0.0026` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.1962` n `139` status `ready` deltaP `10.4393` edge `-0.0016` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.5204` n `139` status `ready` deltaP `-10.5281` edge `0.0247` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-2.0463` n `139` status `ready` deltaP `-6.1579` edge `0.0502` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0716` n `139` status `ready` deltaP `-12.3153` edge `-0.016` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.9881` n `139` status `ready` deltaP `-12.2368` edge `-0.0089` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
