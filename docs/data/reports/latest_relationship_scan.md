# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T06:52:28.734512+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11607`

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

- `news_risk_high->unknown_24h` score `52.9945` n `50` status `ready` deltaP `11.6118` edge `4.3388` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `28.6496` n `50` status `ready` deltaP `37.7678` edge `2.1798` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6934` n `50` status `ready` deltaP `25.2024` edge `0.8997` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `5.3776` n `50` status `ready` deltaP `49.2998` edge `0.1237` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `5.3287` n `50` status `ready` deltaP `30.1005` edge `0.3362` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.9183` n `50` status `ready` deltaP `45.7291` edge `0.0307` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.5702` n `128` status `ready` deltaP `5.3618` edge `0.335` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.9132` n `50` status `ready` deltaP `16.0778` edge `0.1712` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.6426` n `50` status `ready` deltaP `29.5945` edge `0.038` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2504` n `148` status `ready` deltaP `18.3646` edge `0.1058` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.6414` n `50` status `ready` deltaP `21.8503` edge `0.0081` maxDD `-0.0257`
- `news_risk_high->equity_4h` score `1.5501` n `50` status `ready` deltaP `22.4231` edge `0.056` maxDD `-2.105`
- `news_risk_high->equity_1h` score `1.4315` n `50` status `ready` deltaP `18.7605` edge `0.0221` maxDD `-0.2301`
- `news_risk_high->crypto_major_24h` score `0.89` n `50` status `ready` deltaP `17.9688` edge `0.0037` maxDD `-2.6128`
- `market_context_high->unknown_1h` score `0.7898` n `148` status `ready` deltaP `8.3751` edge `0.055` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5347` n `50` status `ready` deltaP `14.5988` edge `0.0025` maxDD `-0.5024`
- `news_risk_high->metal_4h` score `0.3347` n `50` status `ready` deltaP `11.2055` edge `0.0063` maxDD `-0.249`
- `news_risk_high->index_1h` score `0.1981` n `50` status `ready` deltaP `8.7066` edge `0.0013` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1692` n `50` status `ready` deltaP `6.5988` edge `0.0003` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.0448` n `50` status `ready` deltaP `6.4018` edge `0.0007` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
