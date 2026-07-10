# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T13:22:30.788652+00:00`
- Price records: `672`
- Market context records: `6286`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11100`

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

- `news_risk_high->crypto_alt_24h` score `15.231` n `32` status `ready` deltaP `43.2292` edge `0.9958` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9593` n `32` status `ready` deltaP `50.5208` edge `0.1598` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1865` n `32` status `ready` deltaP `43.8262` edge `0.0613` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.1274` n `32` status `ready` deltaP `16.6667` edge `0.496` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.7495` n `32` status `ready` deltaP `26.2153` edge `0.0749` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3727` n `32` status `ready` deltaP `28.5928` edge `0.021` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.4463` n `206` status `ready` deltaP `0.2457` edge `0.2197` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3977` n `32` status `ready` deltaP `14.128` edge `0.1317` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8737` n `32` status `ready` deltaP `11.4708` edge `0.0817` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.4887` n `194` status `ready` deltaP `-2.7219` edge `0.3121` maxDD `-11.925`
- `market_context_high->equity_4h` score `0.3399` n `194` status `ready` deltaP `6.8613` edge `0.0743` maxDD `-2.671`
- `market_context_high->metal_24h` score `-0.2636` n `182` status `ready` deltaP `18.6832` edge `0.0985` maxDD `-11.8809`
- `market_context_high->metal_4h` score `-0.2862` n `194` status `ready` deltaP `6.041` edge `0.0322` maxDD `-2.7056`
- `news_risk_high->index_24h` score `-0.3081` n `32` status `ready` deltaP `7.1181` edge `0.0002` maxDD `-2.3058`
- `market_context_high->commodity_1h` score `-0.4872` n `206` status `ready` deltaP `0.4084` edge `0.0027` maxDD `-0.682`
- `market_context_high->fx_1h` score `-0.5737` n `206` status `ready` deltaP `-0.2907` edge `-0.0013` maxDD `-0.5659`
- `news_risk_high->metal_1h` score `-0.7052` n `32` status `ready` deltaP `-2.5449` edge `-0.0237` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7156` n `206` status `ready` deltaP `2.7949` edge `-0.0005` maxDD `-1.8877`
- `market_context_high->commodity_4h` score `-0.7606` n `194` status `ready` deltaP `-2.4972` edge `0.0092` maxDD `-1.2054`
- `market_context_high->crypto_alt_1h` score `-0.8645` n `206` status `ready` deltaP `5.4939` edge `0.0278` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
