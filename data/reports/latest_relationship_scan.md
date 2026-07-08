# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T07:52:32.018297+00:00`
- Price records: `672`
- Market context records: `6066`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11108`

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

- `news_risk_high->fx_24h` score `8.1486` n `30` status `ready` deltaP `72.7431` edge `0.1941` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.4084` n `30` status `ready` deltaP `45.6402` edge `0.0677` maxDD `-0.0345`
- `news_risk_high->crypto_alt_24h` score `3.1329` n `30` status `ready` deltaP `28.9236` edge `0.083` maxDD `-0.5131`
- `news_risk_high->fx_1h` score `2.435` n `32` status `ready` deltaP `29.1916` edge `0.0222` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4749` n `206` status `ready` deltaP `8.7941` edge `0.156` maxDD `-2.671`
- `news_risk_high->commodity_24h` score `1.4461` n `30` status `ready` deltaP `21.5625` edge `-0.0027` maxDD `-0.3101`
- `news_risk_high->crypto_major_1h` score `1.1411` n `32` status `ready` deltaP `13.5292` edge `0.1028` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.5581` n `32` status `ready` deltaP `8.7762` edge `0.0592` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0797` n `30` status `ready` deltaP `9.2361` edge `0.0358` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4586` n `206` status `ready` deltaP `2.8312` edge `0.0022` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.5318` n `206` status `ready` deltaP `0.3081` edge `-0.0007` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.7446` n `206` status `ready` deltaP `-2.2818` edge `-0.0022` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.8457` n `206` status `ready` deltaP `4.7003` edge `0.037` maxDD `-9.807`
- `news_risk_high->metal_1h` score `-0.8549` n `32` status `ready` deltaP `-2.994` edge `-0.0399` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.8586` n `206` status `ready` deltaP `4.2556` edge `0.0368` maxDD `-9.3536`
- `market_context_high->index_4h` score `-0.9421` n `206` status `ready` deltaP `1.9581` edge `0.0195` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-1.0151` n `32` status `ready` deltaP `-8.3271` edge `-0.0183` maxDD `-1.1725`
- `market_context_high->equity_1h` score `-1.0541` n `206` status `ready` deltaP `0.7805` edge `0.0198` maxDD `-4.3608`
- `market_context_high->metal_4h` score `-1.12` n `206` status `ready` deltaP `3.5712` edge `0.0016` maxDD `-3.4996`
- `market_context_high->commodity_4h` score `-1.2772` n `206` status `ready` deltaP `-4.9506` edge `-0.0238` maxDD `-2.5555`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
