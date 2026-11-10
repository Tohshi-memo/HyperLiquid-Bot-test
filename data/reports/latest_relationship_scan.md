# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T17:22:35.554197+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11460`

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

- `market_context_high->unknown_4h` score `52.6553` n `88` status `ready` deltaP `7.0676` edge `4.3856` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.9576` n `88` status `ready` deltaP `33.7344` edge `2.9287` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `5.5926` n `88` status `ready` deltaP `25.8941` edge `1.0538` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.5711` n `88` status `ready` deltaP `27.0915` edge `0.3299` maxDD `-2.3671`
- `market_context_high->metal_24h` score `1.1` n `88` status `ready` deltaP `21.2364` edge `0.0054` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3053` n `88` status `ready` deltaP `4.2461` edge `0.0139` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4269` n `88` status `ready` deltaP `2.089` edge `-0.0004` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.4701` n `88` status `ready` deltaP `3.5615` edge `0.0266` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.5887` n `88` status `ready` deltaP `3.8525` edge `-0.0034` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9753` n `88` status `ready` deltaP `-7.206` edge `0.0061` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0283` n `88` status `ready` deltaP `-0.5959` edge `0.0105` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2471` n `88` status `ready` deltaP `-13.0103` edge `-0.0047` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.534` n `88` status `ready` deltaP `-7.206` edge `0.036` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.7581` n `88` status `ready` deltaP `1.6807` edge `-0.0387` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.844` n `88` status `ready` deltaP `-2.0371` edge `-0.0047` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.0246` n `88` status `ready` deltaP `0.9532` edge `-0.0151` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-2.8362` n `88` status `ready` deltaP `-2.715` edge `-0.0832` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.278` n `88` status `ready` deltaP `0.9146` edge `-0.1481` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.4273` n `88` status `ready` deltaP `3.9219` edge `-0.2166` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.2452` n `88` status `ready` deltaP `-23.4698` edge `-0.0616` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
