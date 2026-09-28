# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T16:22:33.618887+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7792`

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

- `news_risk_high->unknown_24h` score `2679.0168` n `139` status `ready` deltaP `1.2153` edge `223.2433` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `7.7874` n `139` status `ready` deltaP `22.8655` edge `0.8917` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `4.9687` n `139` status `ready` deltaP `18.991` edge `0.7309` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `4.7666` n `139` status `ready` deltaP `22.4632` edge `0.5031` maxDD `-11.1179`
- `news_risk_high->index_24h` score `2.9565` n `139` status `ready` deltaP `28.095` edge `0.1286` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `2.2254` n `139` status `ready` deltaP `24.5822` edge `0.1825` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.7996` n `139` status `ready` deltaP `20.6485` edge `0.1978` maxDD `-6.8392`
- `news_risk_high->crypto_alt_1h` score `0.6411` n `139` status `ready` deltaP `7.0176` edge `0.0977` maxDD `-4.2849`
- `news_risk_high->crypto_alt_4h` score `0.5232` n `139` status `ready` deltaP `6.6689` edge `0.2651` maxDD `-15.9436`
- `news_risk_high->equity_1h` score `0.4769` n `139` status `ready` deltaP `6.9552` edge `0.0595` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4455` n `139` status `ready` deltaP `8.6019` edge `0.0088` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.2367` n `139` status `ready` deltaP `5.8958` edge `0.0263` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.54` n `139` status `ready` deltaP `1.1911` edge `0.01` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.6527` n `139` status `ready` deltaP `-0.0022` edge `0.0446` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1889` n `139` status `ready` deltaP `-9.2675` edge `-0.0026` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.197` n `139` status `ready` deltaP `10.4393` edge `-0.0017` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.5188` n `139` status `ready` deltaP `-10.5281` edge `0.0249` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-2.0307` n `139` status `ready` deltaP `-6.1579` edge `0.0522` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0599` n `139` status `ready` deltaP `-12.1656` edge `-0.0155` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.9687` n `139` status `ready` deltaP `-12.0844` edge `-0.0083` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
