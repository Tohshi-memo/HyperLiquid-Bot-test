# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T07:07:25.185792+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14747`

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

- `news_risk_high->unknown_24h` score `50.3933` n `50` status `ready` deltaP `11.5717` edge `4.1223` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.5708` n `50` status `ready` deltaP `37.6235` edge `1.1742` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.58` n `50` status `ready` deltaP `26.4695` edge `0.8818` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.3822` n `50` status `ready` deltaP `26.3143` edge `0.3659` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.9127` n `50` status `ready` deltaP `45.6585` edge `0.0307` maxDD `-0.0559`
- `news_risk_high->metal_24h` score `3.4126` n `50` status `ready` deltaP `40.487` edge `0.0187` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `3.4008` n `137` status `ready` deltaP `25.1702` edge `0.1563` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.9716` n `50` status `ready` deltaP `32.0415` edge `0.0491` maxDD `-0.2064`
- `news_risk_high->unknown_1h` score `2.864` n `50` status `ready` deltaP `16.0778` edge `0.1671` maxDD `-0.8495`
- `market_context_high->unknown_1h` score `1.4922` n `137` status `ready` deltaP `13.4501` edge `0.0797` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `1.4186` n `50` status `ready` deltaP `19.1557` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.3321` n `50` status `ready` deltaP `17.4132` edge `0.0228` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.261` n `50` status `ready` deltaP `20.0549` edge `0.0477` maxDD `-2.105`
- `market_context_high->unknown_24h` score `1.2492` n `136` status `ready` deltaP `5.6893` edge `0.1394` maxDD `-3.1917`
- `news_risk_high->commodity_1h` score `0.5814` n `50` status `ready` deltaP `15.3473` edge `0.0035` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.181` n `50` status `ready` deltaP `8.2575` edge `0.0021` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0719` n `50` status `ready` deltaP `5.1018` edge `-0.0022` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.0687` n `50` status `ready` deltaP `6.4756` edge `0.0022` maxDD `-0.1719`
- `market_context_high->fx_1h` score `-0.357` n `137` status `ready` deltaP `4.09` edge `0.0002` maxDD `-0.8587`
- `news_risk_high->metal_4h` score `-0.3574` n `50` status `ready` deltaP `5.3293` edge `-0.0122` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
