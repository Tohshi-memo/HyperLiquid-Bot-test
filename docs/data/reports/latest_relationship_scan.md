# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T13:52:32.260234+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9232`

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

- `market_context_high->equity_24h` score `7.1875` n `34` status `ready` deltaP `12.306` edge `0.7542` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `1.9716` n `34` status `ready` deltaP `4.1463` edge `0.1954` maxDD `-1.6995`
- `market_context_high->index_24h` score `0.9963` n `34` status `ready` deltaP `11.2337` edge `0.0991` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.5999` n `34` status `ready` deltaP `9.8141` edge `-0.0048` maxDD `-0.1843`
- `market_context_high->metal_1h` score `-0.3688` n `88` status `ready` deltaP `3.6473` edge `0.0126` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4696` n `88` status `ready` deltaP `0.7417` edge `0.0031` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.4996` n `88` status `ready` deltaP `4.005` edge `0.007` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.7636` n `88` status `ready` deltaP `-1.4689` edge `0.0225` maxDD `-4.182`
- `market_context_high->index_1h` score `-0.9294` n `88` status `ready` deltaP `-6.6072` edge `0.008` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-0.9307` n `88` status `ready` deltaP `0.4712` edge `0.0159` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2712` n `88` status `ready` deltaP `-13.3097` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.3592` n `88` status `ready` deltaP `-6.9066` edge `0.0554` maxDD `-8.0225`
- `market_context_high->crypto_alt_1h` score `-1.8579` n `88` status `ready` deltaP `1.2316` edge `-0.0485` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-1.9622` n `34` status `ready` deltaP `-2.6042` edge `-0.1789` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.1424` n `88` status `ready` deltaP `-7.2201` edge `-0.0084` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.0926` n `88` status `ready` deltaP `-4.5114` edge `-0.1041` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-5.0938` n `88` status `ready` deltaP `0.9146` edge `-0.0526` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-6.6261` n `34` status `ready` deltaP `-6.5257` edge `-0.0456` maxDD `-30.3789`
- `market_context_high->crypto_alt_4h` score `-8.4006` n `88` status `ready` deltaP `3.1597` edge `-0.2093` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-10.658` n `34` status `ready` deltaP `-20.2104` edge `-0.244` maxDD `-33.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
