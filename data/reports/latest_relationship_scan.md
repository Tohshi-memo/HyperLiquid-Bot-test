# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T12:37:28.214230+00:00`
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

- `news_risk_high->unknown_24h` score `1158.2748` n `139` status `ready` deltaP `1.2153` edge `96.5148` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.4369` n `139` status `ready` deltaP `20.6085` edge `0.7942` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `3.768` n `139` status `ready` deltaP `16.3868` edge `0.6482` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `3.2802` n `139` status `ready` deltaP `19.8591` edge `0.3966` maxDD `-11.1179`
- `news_risk_high->index_24h` score `2.591` n `139` status `ready` deltaP `25.4909` edge `0.1155` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `1.8032` n `139` status `ready` deltaP `22.9053` edge `0.1585` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.4754` n `139` status `ready` deltaP `20.3013` edge `0.1731` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.7427` n `139` status `ready` deltaP `7.5836` edge `0.2773` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.5751` n `139` status `ready` deltaP `6.8679` edge `0.0932` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.2862` n `139` status `ready` deltaP `6.9552` edge `0.0065` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `0.2383` n `139` status `ready` deltaP `5.6079` edge `0.0486` maxDD `-1.957`
- `news_risk_high->index_4h` score `-0.4064` n `139` status `ready` deltaP `4.5239` edge `0.0213` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.516` n `139` status `ready` deltaP `1.4905` edge `0.01` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.7181` n `139` status `ready` deltaP `-0.4513` edge `0.0392` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1313` n `139` status `ready` deltaP `-8.2196` edge `-0.0022` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.1534` n `139` status `ready` deltaP `11.2015` edge `-0.0012` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.5346` n `139` status `ready` deltaP `-10.6806` edge `0.0239` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-2.0365` n `139` status `ready` deltaP `-11.8662` edge `-0.0145` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.1068` n `139` status `ready` deltaP `-6.7677` edge `0.0465` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-4.0719` n `139` status `ready` deltaP `-12.999` edge `-0.0108` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
