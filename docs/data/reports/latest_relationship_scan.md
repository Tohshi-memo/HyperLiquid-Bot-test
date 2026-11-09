# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T09:37:29.715547+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9226`

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

- `market_context_high->equity_24h` score `8.8184` n `32` status `ready` deltaP `16.4931` edge `0.8622` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.4053` n `32` status `ready` deltaP `7.8125` edge `0.2071` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.3444` n `32` status `ready` deltaP `16.6667` edge `0.1075` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.8586` n `32` status `ready` deltaP `12.3264` edge `-0.0018` maxDD `-0.0397`
- `market_context_high->metal_1h` score `-0.3113` n `88` status `ready` deltaP `4.2461` edge `0.0134` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.479` n `88` status `ready` deltaP `0.7417` edge `0.0019` maxDD `-1.7935`
- `market_context_high->metal_4h` score `-0.5671` n `82` status `ready` deltaP `2.439` edge `0.0215` maxDD `-3.5036`
- `market_context_high->commodity_4h` score `-0.8414` n `82` status `ready` deltaP `-3.3537` edge `0.0251` maxDD `-4.182`
- `market_context_high->index_1h` score `-0.8531` n `88` status `ready` deltaP `-5.2599` edge `0.0088` maxDD `-0.9814`
- `market_context_high->index_4h` score `-0.8669` n `82` status `ready` deltaP `2.8963` edge `0.0062` maxDD `-2.4866`
- `market_context_high->equity_1h` score `-1.2073` n `88` status `ready` deltaP `-5.4096` edge `0.0649` maxDD `-8.0225`
- `market_context_high->fx_1h` score `-1.2961` n `88` status `ready` deltaP `-13.7588` edge `-0.006` maxDD `-0.8088`
- `market_context_high->crypto_alt_1h` score `-1.7472` n `88` status `ready` deltaP `1.8304` edge `-0.0383` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-1.9143` n `32` status `ready` deltaP `-2.7778` edge `-0.1716` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.3918` n `82` status `ready` deltaP `-11.2805` edge `-0.0133` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.0528` n `88` status `ready` deltaP `-4.212` edge `-0.101` maxDD `-15.9848`
- `market_context_high->crypto_major_24h` score `-4.1362` n `32` status `ready` deltaP `-4.8611` edge `0.052` maxDD `-23.1423`
- `market_context_high->equity_4h` score `-5.017` n `82` status `ready` deltaP `0.9147` edge `-0.0462` maxDD `-24.9053`
- `market_context_high->crypto_alt_4h` score `-8.9856` n `82` status `ready` deltaP `0.1524` edge `-0.238` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-9.2278` n `32` status `ready` deltaP `-18.75` edge `-0.1861` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
