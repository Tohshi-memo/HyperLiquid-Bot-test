# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T16:07:50.729433+00:00`
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

- `market_context_high->unknown_4h` score `54.1487` n `88` status `ready` deltaP `7.525` edge `4.507` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.7708` n `88` status `ready` deltaP `33.2145` edge `2.9166` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4904` n `88` status `ready` deltaP `26.3983` edge `0.3278` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `5.1926` n `88` status `ready` deltaP `25.0276` edge `1.0083` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.8831` n `88` status `ready` deltaP `20.3698` edge `-0.0069` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3269` n `88` status `ready` deltaP `4.0964` edge `0.0131` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4011` n `88` status `ready` deltaP `2.2387` edge `0.0019` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.456` n `88` status `ready` deltaP `3.5615` edge `0.0284` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.5926` n `88` status `ready` deltaP `3.8525` edge `-0.0039` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9878` n `88` status `ready` deltaP `-7.3557` edge `0.0055` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0408` n `88` status `ready` deltaP `-0.5959` edge `0.0089` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2805` n `88` status `ready` deltaP `-13.6091` edge `-0.005` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5878` n `88` status `ready` deltaP `-7.3557` edge `0.0301` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.8423` n `88` status `ready` deltaP `1.2316` edge `-0.0465` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.8922` n `88` status `ready` deltaP `-2.7993` edge `-0.0058` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.1179` n `88` status `ready` deltaP `0.0867` edge `-0.0171` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-2.9094` n `88` status `ready` deltaP `-3.1641` edge `-0.0896` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.3392` n `88` status `ready` deltaP `0.9146` edge `-0.1532` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.5643` n `88` status `ready` deltaP `3.7694` edge `-0.227` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.2188` n `88` status `ready` deltaP `-23.4698` edge `-0.0594` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
