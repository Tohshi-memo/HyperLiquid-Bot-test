# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T18:07:25.157961+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11754`

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

- `market_context_high->unknown_4h` score `52.3037` n `88` status `ready` deltaP `7.0676` edge `4.3563` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.038` n `88` status `ready` deltaP `33.7344` edge `2.9354` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `5.8138` n `88` status `ready` deltaP `26.414` edge `1.0787` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.633` n `88` status `ready` deltaP `27.6114` edge `0.3316` maxDD `-2.3671`
- `market_context_high->metal_24h` score `1.2364` n `88` status `ready` deltaP `21.7563` edge `0.0133` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3065` n `88` status `ready` deltaP `4.2461` edge `0.0138` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4004` n `88` status `ready` deltaP `2.5381` edge `0.0` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.4841` n `88` status `ready` deltaP `3.5615` edge `0.0248` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.5863` n `88` status `ready` deltaP `3.8525` edge `-0.0031` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9566` n `88` status `ready` deltaP `-6.9066` edge `0.0065` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0221` n `88` status `ready` deltaP `-0.5959` edge `0.0113` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2478` n `88` status `ready` deltaP `-13.0103` edge `-0.0048` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.4904` n `88` status `ready` deltaP `-6.7569` edge `0.0386` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.7721` n `88` status `ready` deltaP `1.531` edge `-0.0395` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.8171` n `88` status `ready` deltaP `-1.5798` edge `-0.0043` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-1.971` n `88` status `ready` deltaP `1.4731` edge `-0.0141` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-2.8478` n `88` status `ready` deltaP `-2.8647` edge `-0.0837` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.2188` n `88` status `ready` deltaP `1.2195` edge `-0.1452` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.3577` n `88` status `ready` deltaP `3.9219` edge `-0.2108` maxDD `-34.2787`
- `market_context_high->crypto_major_24h` score `-9.0572` n `88` status `ready` deltaP `3.2023` edge `0.3864` maxDD `-80.6681`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
