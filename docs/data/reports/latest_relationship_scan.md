# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T02:22:24.250135+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14779`

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

- `news_risk_high->unknown_24h` score `49.3469` n `50` status `ready` deltaP `11.5717` edge `4.0351` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.2559` n `50` status `ready` deltaP `36.5872` edge `0.9882` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.2571` n `50` status `ready` deltaP `25.4024` edge `0.862` maxDD `-0.1276`
- `news_risk_high->equity_24h` score `6.278` n `50` status `ready` deltaP `29.4231` edge `0.4203` maxDD `-4.7964`
- `news_risk_high->fx_4h` score `3.8141` n `50` status `ready` deltaP `44.5915` edge `0.0296` maxDD `-0.0559`
- `news_risk_high->index_24h` score `3.5443` n `50` status `ready` deltaP `36.1865` edge `0.0693` maxDD `-0.2147`
- `market_context_high->unknown_4h` score `3.0997` n `137` status `ready` deltaP `24.1031` edge `0.1383` maxDD `-0.5878`
- `news_risk_high->metal_24h` score `2.8332` n `50` status `ready` deltaP `37.2055` edge `-0.0077` maxDD `-0.0053`
- `news_risk_high->unknown_1h` score `2.664` n `50` status `ready` deltaP `15.479` edge `0.1544` maxDD `-0.8474`
- `news_risk_high->fx_1h` score `1.4438` n `50` status `ready` deltaP `19.4551` edge `0.0076` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.3151` n `50` status `ready` deltaP `17.2635` edge `0.0224` maxDD `-0.2319`
- `market_context_high->unknown_1h` score `1.2961` n `137` status `ready` deltaP `12.8513` edge `0.0673` maxDD `-1.5974`
- `news_risk_high->equity_4h` score `1.2665` n `50` status `ready` deltaP `19.75` edge `0.0504` maxDD `-2.1218`
- `market_context_high->unknown_24h` score `0.6722` n `134` status `ready` deltaP `5.6016` edge `0.0918` maxDD `-3.1835`
- `news_risk_high->commodity_1h` score `0.5347` n `50` status `ready` deltaP `14.5988` edge `0.0025` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.1466` n `50` status `ready` deltaP `7.2378` edge `0.0037` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.1443` n `50` status `ready` deltaP `7.509` edge `0.0024` maxDD `-0.0505`
- `news_risk_high->metal_1h` score `0.0002` n `50` status `ready` deltaP `3.9042` edge `-0.0034` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.2806` n `50` status `ready` deltaP `6.2439` edge `-0.0119` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.3406` n `137` status `ready` deltaP `4.3894` edge `0.0003` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
