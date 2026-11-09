# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T20:22:30.791992+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10180`

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

- `market_context_high->equity_24h` score `10.9205` n `45` status `ready` deltaP `19.353` edge `1.5115` maxDD `-16.9034`
- `market_context_high->unknown_4h` score `9.6501` n `88` status `ready` deltaP `7.043` edge `0.802` maxDD `-0.9153`
- `market_context_high->index_24h` score `1.9637` n `45` status `ready` deltaP `16.1409` edge `0.1904` maxDD `-2.3671`
- `market_context_high->commodity_24h` score `-0.1914` n `45` status `ready` deltaP `-8.0378` edge `0.1251` maxDD `-3.3513`
- `market_context_high->metal_1h` score `-0.3868` n `88` status `ready` deltaP `3.4976` edge `0.0121` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5592` n `88` status `ready` deltaP `-0.4559` edge `-0.0004` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.8212` n `88` status `ready` deltaP `0.4307` edge `-0.0104` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.9644` n `88` status `ready` deltaP `-3.3641` edge `0.0094` maxDD `-4.182`
- `market_context_high->metal_4h` score `-1.0649` n `88` status `ready` deltaP `-1.4356` edge `0.0114` maxDD `-4.0688`
- `market_context_high->index_1h` score `-1.0773` n `88` status `ready` deltaP `-8.8527` edge `0.004` maxDD `-0.9814`
- `market_context_high->fx_24h` score `-1.1081` n `45` status `ready` deltaP `-4.2364` edge `-0.0369` maxDD `-1.82`
- `market_context_high->fx_1h` score `-1.2938` n `88` status `ready` deltaP `-13.7588` edge `-0.0057` maxDD `-0.8088`
- `market_context_high->metal_24h` score `-1.5434` n `45` status `ready` deltaP `5.2031` edge `-0.108` maxDD `-1.4245`
- `market_context_high->equity_1h` score `-1.75` n `88` status `ready` deltaP `-8.2539` edge `0.0153` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-2.0465` n `88` status `ready` deltaP `-0.4151` edge `-0.0617` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.082` n `88` status `ready` deltaP `-6.0727` edge `-0.0083` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.2453` n `88` status `ready` deltaP `-5.709` edge `-0.1157` maxDD `-15.9848`
- `market_context_high->crypto_alt_24h` score `-5.3763` n `45` status `ready` deltaP `-3.6742` edge `0.0859` maxDD `-33.4213`
- `market_context_high->equity_4h` score `-7.4067` n `88` status `ready` deltaP `-2.6636` edge `-0.2183` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.3235` n `88` status `ready` deltaP `0.9392` edge `-0.2714` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
