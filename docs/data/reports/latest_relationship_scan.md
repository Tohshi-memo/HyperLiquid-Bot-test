# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T08:52:25.945533+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2674`

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

- `market_context_high->unknown_1h` score `10049.8109` n `126` status `ready` deltaP `1.0146` edge `837.4973` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6133.0773` n `126` status `ready` deltaP `-0.3145` edge `511.1224` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `1.1653` n `110` status `ready` deltaP `25.565` edge `0.9799` maxDD `-72.7411`
- `market_context_high->metal_1h` score `-0.1641` n `126` status `ready` deltaP `4.5504` edge `0.0151` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2991` n `126` status `ready` deltaP `2.8585` edge `0.0038` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5092` n `126` status `ready` deltaP `11.7958` edge `0.0367` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.3747` n `126` status `ready` deltaP `-8.6565` edge `-0.0009` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.8` n `126` status `ready` deltaP `6.1377` edge `0.015` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.9082` n `126` status `ready` deltaP `-6.7267` edge `0.0018` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.1661` n `126` status `ready` deltaP `-6.8744` edge `-0.0215` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.3799` n `126` status `ready` deltaP `-3.1843` edge `-0.0138` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.4704` n `126` status `ready` deltaP `3.0082` edge `0.0059` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.1871` n `126` status `ready` deltaP `-3.7449` edge `-0.0129` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.3086` n `126` status `ready` deltaP `-1.1082` edge `0.1479` maxDD `-47.4317`
- `market_context_high->crypto_alt_24h` score `-5.3268` n `110` status `ready` deltaP `12.8883` edge `0.6357` maxDD `-85.9083`
- `market_context_high->metal_24h` score `-6.0941` n `110` status `ready` deltaP `11.9539` edge `0.1151` maxDD `-46.211`
- `market_context_high->fx_24h` score `-6.3682` n `110` status `ready` deltaP `-14.6212` edge `-0.0059` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.8066` n `126` status `ready` deltaP `-17.9007` edge `-0.0786` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.5097` n `126` status `ready` deltaP `-1.5656` edge `0.0659` maxDD `-46.5016`
- `market_context_high->index_24h` score `-12.9341` n `110` status `ready` deltaP `-26.4899` edge `-0.115` maxDD `-32.8996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
