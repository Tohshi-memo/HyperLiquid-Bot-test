# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T23:37:24.623276+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `9892`

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

- `market_context_high->unknown_4h` score `29.6359` n `88` status `ready` deltaP `7.2201` edge `2.4663` maxDD `-0.9153`
- `market_context_high->equity_24h` score `17.8415` n `58` status `ready` deltaP `26.8242` edge `2.349` maxDD `-16.9034`
- `market_context_high->index_24h` score `3.0935` n `58` status `ready` deltaP `22.1179` edge `0.2954` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `0.6741` n `58` status `ready` deltaP `9.7741` edge `0.5307` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.1285` n `58` status `ready` deltaP `11.4176` edge `-0.0101` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3904` n `88` status `ready` deltaP `3.4976` edge `0.0118` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5405` n `88` status `ready` deltaP `-0.0068` edge `-0.001` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.8485` n `88` status `ready` deltaP `0.0416` edge `-0.0113` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.8688` n `88` status `ready` deltaP `-2.2311` edge `0.0141` maxDD `-4.182`
- `market_context_high->index_1h` score `-1.1046` n `88` status `ready` deltaP `-9.3018` edge `0.0035` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.1364` n `88` status `ready` deltaP `-2.1203` edge `0.0068` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3358` n `88` status `ready` deltaP `-14.5073` edge `-0.0061` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7718` n `88` status `ready` deltaP `-8.4036` edge `0.0135` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9498` n `88` status `ready` deltaP `0.4831` edge `-0.0553` maxDD `-10.8319`
- `market_context_high->commodity_24h` score `-2.1021` n `58` status `ready` deltaP `-15.2483` edge `0.0509` maxDD `-8.8327`
- `market_context_high->fx_4h` score `-2.1249` n `88` status `ready` deltaP `-6.7628` edge `-0.0092` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.329` n `58` status `ready` deltaP `-14.4356` edge `-0.0528` maxDD `-3.2972`
- `market_context_high->crypto_major_1h` score `-3.2399` n `88` status `ready` deltaP `-5.709` edge `-0.115` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.4081` n `88` status `ready` deltaP `-2.5915` edge `-0.2189` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1158` n `88` status `ready` deltaP `2.245` edge `-0.2628` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
