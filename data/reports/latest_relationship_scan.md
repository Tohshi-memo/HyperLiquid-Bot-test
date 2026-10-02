# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T18:37:39.510338+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4890`

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

- `market_context_high->unknown_1h` score `359.2486` n `50` status `ready` deltaP `10.8743` edge `29.8698` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.4881` n `50` status `ready` deltaP `10.3659` edge `24.3049` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.7658` n `73` status `ready` deltaP `40.1422` edge `1.0671` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `9.4405` n `50` status `ready` deltaP `16.8819` edge `0.8445` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `8.9682` n `50` status `ready` deltaP `31.8264` edge `0.6768` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `8.905` n `73` status `ready` deltaP `31.885` edge `0.578` maxDD `-2.8784`
- `market_context_high->crypto_major_4h` score `7.2339` n `50` status `ready` deltaP `17.6951` edge `0.5552` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.2774` n `50` status `ready` deltaP `15.8841` edge `0.4628` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `5.0984` n `116` status `ready` deltaP `21.7462` edge `0.4143` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `3.1858` n `50` status `ready` deltaP `14.8024` edge `0.2331` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.0707` n `50` status `ready` deltaP `14.4491` edge `0.2046` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7519` n `50` status `ready` deltaP `30.7073` edge `0.0381` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.4915` n `116` status `ready` deltaP `22.0984` edge `0.1299` maxDD `-2.9013`
- `market_context_high->equity_24h` score `1.6148` n `50` status `ready` deltaP `8.1042` edge `0.3392` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `1.4942` n `73` status `ready` deltaP `5.9908` edge `0.467` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4352` n `50` status `ready` deltaP `20.1916` edge `0.0114` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.3434` n `73` status `ready` deltaP `13.009` edge `0.2129` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `1.2714` n `116` status `ready` deltaP `14.3503` edge `0.2983` maxDD `-10.477`
- `news_risk_high->crypto_alt_1h` score `1.0383` n `116` status `ready` deltaP `5.699` edge `0.1046` maxDD `-2.4854`
- `market_context_high->fx_24h` score `0.7919` n `50` status `ready` deltaP `17.2083` edge `0.0886` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
