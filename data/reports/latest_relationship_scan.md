# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T02:07:35.795456+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8664`

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

- `market_context_high->unknown_24h` score `1272.3789` n `34` status `ready` deltaP `3.9861` edge `106.005` maxDD `0.0`
- `news_risk_high->equity_24h` score `47.4957` n `50` status `ready` deltaP `50.565` edge `3.6915` maxDD `-3.6503`
- `market_context_high->unknown_4h` score `43.3579` n `64` status `ready` deltaP `8.9939` edge `3.5532` maxDD `0.0`
- `market_context_high->equity_24h` score `30.7746` n `34` status `ready` deltaP `33.1532` edge `2.4977` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `29.4605` n `34` status `ready` deltaP `53.0737` edge `2.2089` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `21.4211` n `50` status `ready` deltaP `42.5754` edge `2.5768` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.8816` n `50` status `ready` deltaP `37.2378` edge `0.8549` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `10.9814` n `34` status `ready` deltaP `13.9872` edge `1.2403` maxDD `-28.8081`
- `news_risk_high->crypto_alt_24h` score `9.0643` n `50` status `ready` deltaP `20.6031` edge `1.4753` maxDD `-29.0448`
- `news_risk_high->index_24h` score `6.8375` n `50` status `ready` deltaP `42.2461` edge `0.3185` maxDD `-0.4279`
- `market_context_high->index_24h` score `6.668` n `34` status `ready` deltaP `45.4226` edge `0.2615` maxDD `-0.0251`
- `news_risk_high->commodity_24h` score `6.262` n `50` status `ready` deltaP `41.0745` edge `0.248` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.9662` n `50` status `ready` deltaP `44.2317` edge `0.1566` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.3928` n `50` status `ready` deltaP `20.8415` edge `0.3647` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.2156` n `50` status `ready` deltaP `26.0793` edge `0.321` maxDD `-9.4848`
- `market_context_high->metal_24h` score `4.0707` n `34` status `ready` deltaP `51.3508` edge `0.2687` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.8785` n `50` status `ready` deltaP `20.2994` edge `0.2509` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.8255` n `50` status `ready` deltaP `34.8963` edge `0.1115` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4576` n `50` status `ready` deltaP `23.5793` edge `0.0826` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2425` n `50` status `ready` deltaP `25.2934` edge `0.0437` maxDD `-0.3692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
