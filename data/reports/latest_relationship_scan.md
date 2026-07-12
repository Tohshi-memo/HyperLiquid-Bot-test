# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T03:37:33.457408+00:00`
- Price records: `672`
- Market context records: `6458`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5875`

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

- `news_risk_high->crypto_alt_24h` score `11.8562` n `32` status `ready` deltaP `30.7292` edge `0.7979` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `7.5048` n `146` status `ready` deltaP `17.2398` edge `0.8405` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.3106` n `32` status `ready` deltaP `52.2569` edge `0.1775` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.084` n `32` status `ready` deltaP `42.4543` edge `0.0619` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.6412` n `32` status `ready` deltaP `32.2917` edge `0.1087` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.5166` n `32` status `ready` deltaP `13.0208` edge `0.442` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4458` n `32` status `ready` deltaP `29.491` edge `0.0211` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.5674` n `172` status `ready` deltaP `-5.6364` edge `0.2583` maxDD `-3.2083`
- `news_risk_high->crypto_major_1h` score `1.4267` n `32` status `ready` deltaP `12.9304` edge `0.1434` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.775` n `32` status `ready` deltaP `8.6265` edge `0.088` maxDD `-1.6923`
- `market_context_high->crypto_alt_4h` score `0.3704` n `172` status `ready` deltaP `8.8556` edge `0.1272` maxDD `-6.7632`
- `market_context_high->commodity_24h` score `0.3426` n `146` status `ready` deltaP `6.8208` edge `0.1699` maxDD `-5.2791`
- `market_context_high->unknown_4h` score `0.3079` n `172` status `ready` deltaP `-14.9355` edge `0.3658` maxDD `-10.5788`
- `market_context_high->index_4h` score `0.2992` n `172` status `ready` deltaP `9.8199` edge `0.0271` maxDD `-0.4108`
- `market_context_high->metal_4h` score `0.0701` n `172` status `ready` deltaP `10.6743` edge `0.0435` maxDD `-2.7056`
- `news_risk_high->unknown_1h` score `-0.2847` n `32` status `ready` deltaP `5.4828` edge `-0.0258` maxDD `-0.7581`
- `news_risk_high->index_24h` score `-0.5104` n `32` status `ready` deltaP `3.9931` edge `-0.0049` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.5223` n `32` status `ready` deltaP `1.0479` edge `-0.0242` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.5427` n `172` status `ready` deltaP `1.0479` edge `0.0012` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.5856` n `172` status `ready` deltaP `6.6151` edge `0.0507` maxDD `-8.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
