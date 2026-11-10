# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T01:37:33.679268+00:00`
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

- `market_context_high->unknown_4h` score `37.8191` n `88` status `ready` deltaP `7.525` edge `3.1462` maxDD `-0.9153`
- `market_context_high->equity_24h` score `20.8991` n `66` status `ready` deltaP `29.959` edge `2.7201` maxDD `-16.9034`
- `market_context_high->index_24h` score `3.4937` n `66` status `ready` deltaP `24.6258` edge `0.33` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `2.2565` n `66` status `ready` deltaP `15.2434` edge `0.6971` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.3126` n `66` status `ready` deltaP `13.5838` edge `-0.0092` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3724` n `88` status `ready` deltaP `3.6473` edge `0.0123` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.553` n `88` status `ready` deltaP `-0.3062` edge `-0.0006` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.8167` n `88` status `ready` deltaP `-1.4689` edge `0.0157` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.8264` n `88` status `ready` deltaP `0.3464` edge `-0.0105` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0579` n `88` status `ready` deltaP `-8.5533` edge `0.0045` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.1781` n `88` status `ready` deltaP `-2.5776` edge `0.0045` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3779` n `88` status `ready` deltaP `-15.2558` edge `-0.0065` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7336` n `88` status `ready` deltaP `-8.2539` edge `0.0174` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9218` n `88` status `ready` deltaP `0.7825` edge `-0.0537` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.2015` n `88` status `ready` deltaP `-7.9823` edge `-0.0109` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.5048` n `66` status `ready` deltaP `-16.9319` edge `-0.0483` maxDD `-3.4627`
- `market_context_high->commodity_24h` score `-2.9657` n `66` status `ready` deltaP `-17.8326` edge `0.0282` maxDD `-11.8292`
- `market_context_high->crypto_major_1h` score `-3.1924` n `88` status `ready` deltaP `-5.2599` edge `-0.1119` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.4031` n `88` status `ready` deltaP `-2.439` edge `-0.2195` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.117` n `88` status `ready` deltaP `2.245` edge `-0.2629` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
