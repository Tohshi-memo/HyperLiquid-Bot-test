# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T19:52:34.272214+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10206`

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

- `market_context_high->equity_24h` score `9.6652` n `43` status `ready` deltaP `17.8026` edge `1.3609` maxDD `-16.9034`
- `market_context_high->unknown_4h` score `5.2353` n `88` status `ready` deltaP `7.043` edge `0.4341` maxDD `-0.9153`
- `market_context_high->index_24h` score `1.7588` n `43` status `ready` deltaP `14.9006` edge `0.1724` maxDD `-2.3671`
- `market_context_high->commodity_24h` score `0.1965` n `43` status `ready` deltaP `-6.4206` edge `0.144` maxDD `-2.414`
- `market_context_high->metal_1h` score `-0.3509` n `88` status `ready` deltaP `3.797` edge `0.0131` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5756` n `88` status `ready` deltaP `-0.6056` edge `-0.0015` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.7991` n `88` status `ready` deltaP `0.7351` edge `-0.0096` maxDD `-2.4871`
- `market_context_high->fx_24h` score `-0.8536` n `43` status `ready` deltaP `-1.9991` edge `-0.0315` maxDD `-1.5016`
- `market_context_high->commodity_4h` score `-0.9809` n `88` status `ready` deltaP `-3.5163` edge `0.0083` maxDD `-4.182`
- `market_context_high->metal_4h` score `-1.0436` n `88` status `ready` deltaP `-1.1311` edge `0.0121` maxDD `-4.0688`
- `market_context_high->index_1h` score `-1.0579` n `88` status `ready` deltaP `-8.5533` edge `0.0045` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.3101` n `88` status `ready` deltaP `-14.0582` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7079` n `88` status `ready` deltaP `-7.9545` edge `0.0187` maxDD `-8.1039`
- `market_context_high->metal_24h` score `-1.9095` n `43` status `ready` deltaP `3.7927` edge `-0.1291` maxDD `-1.4245`
- `market_context_high->crypto_alt_1h` score `-2.0402` n `88` status `ready` deltaP `-0.4151` edge `-0.0609` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.0899` n `88` status `ready` deltaP `-6.2249` edge `-0.0083` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.2337` n `88` status `ready` deltaP `-5.5593` edge `-0.1152` maxDD `-15.9848`
- `market_context_high->crypto_alt_24h` score `-6.3796` n `43` status `ready` deltaP `-6.4649` edge `0.0209` maxDD `-33.4213`
- `market_context_high->equity_4h` score `-7.3573` n `88` status `ready` deltaP `-2.5114` edge `-0.2152` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.3718` n `88` status `ready` deltaP `0.6348` edge `-0.2734` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
