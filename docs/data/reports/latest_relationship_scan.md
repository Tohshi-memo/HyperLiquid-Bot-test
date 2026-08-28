# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T05:52:23.523693+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `news_risk_high->unknown_24h` score `52.8877` n `50` status `ready` deltaP `11.6118` edge `4.3299` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `28.2032` n `50` status `ready` deltaP `37.7678` edge `2.1426` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6027` n `50` status `ready` deltaP `24.5936` edge `0.8962` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `5.4059` n `50` status `ready` deltaP `49.4731` edge `0.1249` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `5.3359` n `50` status `ready` deltaP `30.1005` edge `0.3368` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.8758` n `50` status `ready` deltaP `45.2725` edge `0.0302` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.4634` n `128` status `ready` deltaP `5.3618` edge `0.3261` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.9316` n `50` status `ready` deltaP `16.1734` edge `0.1721` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.7077` n `50` status `ready` deltaP `30.2877` edge `0.0388` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.1597` n `148` status `ready` deltaP `17.7558` edge `0.1023` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.5947` n `50` status `ready` deltaP `21.3274` edge `0.0077` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.4357` n `50` status `ready` deltaP `18.843` edge `0.0219` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.427` n `50` status `ready` deltaP `21.8143` edge `0.0498` maxDD `-2.105`
- `market_context_high->unknown_1h` score `0.8082` n `148` status `ready` deltaP `8.4707` edge `0.0559` maxDD `-1.6015`
- `news_risk_high->crypto_major_24h` score `0.5516` n `50` status `ready` deltaP `17.9688` edge `-0.0245` maxDD `-2.6128`
- `news_risk_high->commodity_1h` score `0.5121` n `50` status `ready` deltaP `14.2242` edge `0.0021` maxDD `-0.5024`
- `news_risk_high->metal_4h` score `0.3263` n `50` status `ready` deltaP `11.2055` edge `0.0056` maxDD `-0.249`
- `news_risk_high->index_1h` score `0.2023` n `50` status `ready` deltaP `8.7862` edge `0.0013` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1699` n `50` status `ready` deltaP `6.5232` edge `0.0009` maxDD `-0.1413`
- `market_context_high->metal_24h` score `0.0175` n `128` status `ready` deltaP `13.9731` edge `0.0726` maxDD `-3.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
