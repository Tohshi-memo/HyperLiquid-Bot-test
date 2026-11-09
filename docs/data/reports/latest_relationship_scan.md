# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T22:37:26.581764+00:00`
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

- `market_context_high->unknown_4h` score `29.3827` n `88` status `ready` deltaP `7.2201` edge `2.4452` maxDD `-0.9153`
- `market_context_high->equity_24h` score `15.99` n `54` status `ready` deltaP `24.9085` edge `2.1244` maxDD `-16.9034`
- `market_context_high->index_24h` score `2.8039` n `54` status `ready` deltaP `20.5854` edge `0.2685` maxDD `-2.3671`
- `market_context_high->metal_24h` score `-0.2357` n `54` status `ready` deltaP `9.9396` edge `-0.0306` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.4024` n `88` status `ready` deltaP `3.3479` edge `0.0118` maxDD `-1.4122`
- `market_context_high->crypto_alt_24h` score `-0.4295` n `54` status `ready` deltaP `6.3258` edge `0.4122` maxDD `-33.4213`
- `market_context_high->commodity_1h` score `-0.5576` n `88` status `ready` deltaP `-0.3062` edge `-0.0012` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.8477` n `88` status `ready` deltaP `0.0416` edge `-0.0112` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.9161` n `88` status `ready` deltaP `-2.8409` edge `0.0121` maxDD `-4.182`
- `market_context_high->metal_4h` score `-1.0915` n `88` status `ready` deltaP `-1.5105` edge `0.0085` maxDD `-4.0688`
- `market_context_high->index_1h` score `-1.1046` n `88` status `ready` deltaP `-9.3018` edge `0.0035` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.3023` n `88` status `ready` deltaP `-13.9085` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->commodity_24h` score `-1.553` n `54` status `ready` deltaP `-13.515` edge `0.0706` maxDD `-7.0347`
- `market_context_high->equity_1h` score `-1.771` n `88` status `ready` deltaP `-8.4036` edge `0.0136` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9522` n `88` status `ready` deltaP `0.4831` edge `-0.0556` maxDD `-10.8319`
- `market_context_high->fx_24h` score `-2.0155` n `54` status `ready` deltaP `-11.9359` edge `-0.0505` maxDD `-2.9328`
- `market_context_high->fx_4h` score `-2.0885` n `88` status `ready` deltaP `-6.153` edge `-0.0086` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.2041` n `88` status `ready` deltaP `-5.2599` edge `-0.1134` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.4009` n `88` status `ready` deltaP `-2.5915` edge `-0.2183` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1242` n `88` status `ready` deltaP `2.245` edge `-0.2635` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
