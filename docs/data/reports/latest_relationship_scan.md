# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T10:37:33.585988+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11130`

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

- `market_context_high->unknown_4h` score `43.2001` n `88` status `ready` deltaP `7.6774` edge `3.5936` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.9946` n `88` status `ready` deltaP `33.0412` edge `2.9364` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4812` n `88` status `ready` deltaP `25.8783` edge `0.3305` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `4.4845` n `88` status `ready` deltaP `22.6012` edge `0.9337` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.0615` n `88` status `ready` deltaP `16.7303` edge `-0.0511` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.3738` n `88` status `ready` deltaP `2.2387` edge `0.0054` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.4127` n `88` status `ready` deltaP `3.1042` edge `0.037` maxDD `-4.182`
- `market_context_high->metal_1h` score `-0.4575` n `88` status `ready` deltaP `2.8988` edge `0.0102` maxDD `-1.4122`
- `market_context_high->index_4h` score `-0.7671` n `88` status `ready` deltaP `1.2611` edge `-0.009` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0509` n `88` status `ready` deltaP `-8.4036` edge `0.0044` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2203` n `88` status `ready` deltaP `-2.5776` edge `-0.0009` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3086` n `88` status `ready` deltaP `-14.0582` edge `-0.0056` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7858` n `88` status `ready` deltaP `-9.1521` edge `0.0167` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9428` n `88` status `ready` deltaP `0.7825` edge `-0.0564` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.0093` n `88` status `ready` deltaP `-4.7811` edge `-0.0076` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.5141` n `88` status `ready` deltaP `-3.7262` edge `-0.0247` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.1183` n `88` status `ready` deltaP `-4.5114` edge `-0.1074` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.2237` n `88` status `ready` deltaP `-1.9817` edge `-0.2076` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.9684` n `88` status `ready` deltaP `2.0926` edge `-0.2495` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.2212` n `88` status `ready` deltaP `-23.4698` edge `-0.0596` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
