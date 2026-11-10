# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T01:52:28.155247+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `9966`

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

- `market_context_high->unknown_4h` score `37.4771` n `88` status `ready` deltaP `7.525` edge `3.1177` maxDD `-0.9153`
- `market_context_high->equity_24h` score `21.0743` n `67` status `ready` deltaP `30.2982` edge `2.7403` maxDD `-16.9034`
- `market_context_high->index_24h` score `3.5074` n `67` status `ready` deltaP `24.7239` edge `0.3311` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `2.3088` n `67` status `ready` deltaP `15.6807` edge `0.7009` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.2803` n `67` status `ready` deltaP `13.795` edge `-0.0133` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.388` n `88` status `ready` deltaP `3.4976` edge `0.012` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5428` n `88` status `ready` deltaP `-0.1565` edge `-0.0003` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.8064` n `88` status `ready` deltaP `-1.3165` edge `0.016` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.8256` n `88` status `ready` deltaP `0.3464` edge `-0.0104` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0579` n `88` status `ready` deltaP `-8.5533` edge `0.0045` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.182` n `88` status `ready` deltaP `-2.5776` edge `0.004` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3856` n `88` status `ready` deltaP `-15.4055` edge `-0.0065` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7422` n `88` status `ready` deltaP `-8.4036` edge `0.0173` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9265` n `88` status `ready` deltaP `0.7825` edge `-0.0543` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.211` n `88` status `ready` deltaP `-8.1347` edge `-0.0111` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.5203` n `67` status `ready` deltaP `-17.3465` edge `-0.0475` maxDD `-3.4642`
- `market_context_high->commodity_24h` score `-3.0737` n `67` status `ready` deltaP `-18.0889` edge `0.0254` maxDD `-12.2427`
- `market_context_high->crypto_major_1h` score `-3.2048` n `88` status `ready` deltaP `-5.4096` edge `-0.1125` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.4079` n `88` status `ready` deltaP `-2.439` edge `-0.2199` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1146` n `88` status `ready` deltaP `2.245` edge `-0.2627` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
