# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T04:29:51.945332+00:00`
- Price records: `672`
- Market context records: `6156`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `12.2628` n `30` status `ready` deltaP `42.7267` edge `0.7518` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.6025` n `30` status `ready` deltaP `67.0711` edge `0.1864` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2308` n `32` status `ready` deltaP `44.0497` edge `0.0635` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4094` n `32` status `ready` deltaP `28.9611` edge `0.0216` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.7019` n `195` status `ready` deltaP `1.1912` edge `0.2347` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.2793` n `32` status `ready` deltaP `13.6071` edge `0.12` maxDD `-2.0691`
- `news_risk_high->crypto_major_24h` score `0.7996` n `30` status `ready` deltaP `13.42` edge `0.091` maxDD `-4.2368`
- `news_risk_high->crypto_alt_1h` score `0.6837` n `32` status `ready` deltaP `8.8518` edge `0.0748` maxDD `-1.6923`
- `market_context_high->equity_4h` score `-0.0042` n `195` status `ready` deltaP `2.7702` edge `0.0729` maxDD `-2.671`
- `market_context_high->unknown_4h` score `-0.1774` n `195` status `ready` deltaP `-1.6134` edge `0.2492` maxDD `-11.925`
- `market_context_high->metal_24h` score `-0.2084` n `195` status `ready` deltaP `18.8899` edge `0.1042` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2233` n `30` status `ready` deltaP `7.5794` edge `0.008` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.264` n `195` status `ready` deltaP `1.6534` edge `-0.0003` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.5702` n `195` status `ready` deltaP `4.2361` edge `0.0174` maxDD `-3.4996`
- `news_risk_high->commodity_24h` score `-0.6081` n `30` status `ready` deltaP `14.0497` edge `-0.1238` maxDD `-0.3101`
- `news_risk_high->metal_1h` score `-0.737` n `32` status `ready` deltaP `-2.6158` edge `-0.0273` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.7425` n `195` status `ready` deltaP `-1.911` edge `-0.0045` maxDD `-0.5708`
- `market_context_high->metal_1h` score `-0.7682` n `195` status `ready` deltaP `2.7688` edge `-0.0026` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.8799` n `195` status `ready` deltaP `-1.8237` edge `0.0109` maxDD `-4.2573`
- `market_context_high->crypto_alt_1h` score `-0.8922` n `195` status `ready` deltaP `3.8358` edge `0.0353` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
