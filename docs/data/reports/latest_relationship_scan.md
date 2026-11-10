# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T00:37:29.349576+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `9892`

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

- `market_context_high->unknown_4h` score `38.4719` n `88` status `ready` deltaP `7.525` edge `3.2006` maxDD `-0.9153`
- `market_context_high->equity_24h` score `19.7246` n `62` status `ready` deltaP `28.4928` edge `2.5793` maxDD `-16.9034`
- `market_context_high->index_24h` score `3.3532` n `62` status `ready` deltaP `23.4528` edge `0.3198` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `1.7133` n `62` status `ready` deltaP `12.7774` edge `0.6439` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.3215` n `62` status `ready` deltaP `12.6153` edge `-0.002` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3605` n `88` status `ready` deltaP `3.797` edge `0.0123` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5662` n `88` status `ready` deltaP `-0.4559` edge `-0.0013` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.8287` n `88` status `ready` deltaP `0.3464` edge `-0.0108` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.8609` n `88` status `ready` deltaP `-2.0787` edge `0.0141` maxDD `-4.182`
- `market_context_high->index_1h` score `-1.0773` n `88` status `ready` deltaP `-8.8527` edge `0.004` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.1482` n `88` status `ready` deltaP `-2.2727` edge `0.0063` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3607` n `88` status `ready` deltaP `-14.9564` edge `-0.0063` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.778` n `88` status `ready` deltaP `-8.5533` edge `0.0137` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9226` n `88` status `ready` deltaP `0.7825` edge `-0.0538` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1636` n `88` status `ready` deltaP `-7.3725` edge `-0.0101` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.4157` n `62` status `ready` deltaP `-15.0836` edge `-0.0504` maxDD `-3.3667`
- `market_context_high->commodity_24h` score `-2.5458` n `62` status `ready` deltaP `-16.6685` edge `0.0387` maxDD `-10.3167`
- `market_context_high->crypto_major_1h` score `-3.2243` n `88` status `ready` deltaP `-5.5593` edge `-0.114` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.3887` n `88` status `ready` deltaP `-2.439` edge `-0.2183` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.099` n `88` status `ready` deltaP `2.245` edge `-0.2614` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
