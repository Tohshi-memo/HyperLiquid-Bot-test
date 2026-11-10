# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T22:22:34.762701+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11740`

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

- `market_context_high->unknown_4h` score `59.0735` n `88` status `ready` deltaP `7.525` edge `4.9174` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.2844` n `88` status `ready` deltaP `33.6489` edge `2.9565` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `6.7123` n `88` status `ready` deltaP `29.2929` edge `1.1747` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.9762` n `88` status `ready` deltaP `30.4608` edge `0.3412` maxDD `-2.3671`
- `market_context_high->metal_24h` score `2.1028` n `88` status `ready` deltaP `24.6054` edge `0.0665` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3545` n `88` status `ready` deltaP `3.797` edge `0.0128` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3568` n `88` status `ready` deltaP `3.2866` edge `0.0006` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.5381` n `88` status `ready` deltaP `4.6147` edge `-0.002` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.5422` n `88` status `ready` deltaP `3.1042` edge `0.0204` maxDD `-4.182`
- `market_context_high->index_1h` score `-0.9901` n `88` status `ready` deltaP `-7.5054` edge `0.0062` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0308` n `88` status `ready` deltaP `-0.7483` edge `0.0112` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2167` n `88` status `ready` deltaP `-12.4115` edge `-0.0048` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.541` n `88` status `ready` deltaP `-7.3557` edge `0.0361` maxDD `-8.1039`
- `market_context_high->fx_24h` score `-1.6948` n `88` status `ready` deltaP `4.3403` edge `-0.0102` maxDD `-3.4642`
- `market_context_high->crypto_alt_1h` score `-1.8064` n `88` status `ready` deltaP `1.2316` edge `-0.0419` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.8148` n `88` status `ready` deltaP `-1.5798` edge `-0.004` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-2.946` n `88` status `ready` deltaP `-3.7629` edge `-0.0903` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-5.9607` n `88` status `ready` deltaP `2.2866` edge `-0.1308` maxDD `-25.16`
- `market_context_high->crypto_major_24h` score `-7.2324` n `88` status `ready` deltaP `6.108` edge `0.5191` maxDD `-80.6681`
- `market_context_high->crypto_alt_4h` score `-8.2177` n `88` status `ready` deltaP `4.5316` edge `-0.2032` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
