# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T04:07:20.531580+00:00`
- Price records: `672`
- Market context records: `2106`
- Flow alert records: `7957`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9146`

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

- `market_context_high->crypto_alt_4h` score `10.8801` n `175` status `ready` deltaP `31.2961` edge `0.8125` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `10.6408` n `175` status `ready` deltaP `37.9242` edge `0.6869` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.7812` n `175` status `ready` deltaP `23.6376` edge `0.3991` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.219` n `175` status `ready` deltaP `22.8345` edge `0.3088` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.5515` n `175` status `ready` deltaP `19.0627` edge `0.1539` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.3974` n `174` status `ready` deltaP `11.8979` edge `0.2433` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `2.2617` n `175` status `ready` deltaP `15.8238` edge `0.1816` maxDD `-3.2225`
- `market_context_high->unknown_24h` score `2.2138` n `174` status `ready` deltaP `23.2987` edge `0.5612` maxDD `-35.8966`
- `market_context_high->crypto_alt_1h` score `2.0947` n `175` status `ready` deltaP `12.8298` edge `0.2004` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.6405` n `174` status `ready` deltaP `23.1377` edge `0.4723` maxDD `-33.1875`
- `market_context_high->metal_4h` score `1.3579` n `175` status `ready` deltaP `16.7064` edge `0.1924` maxDD `-8.9164`
- `market_context_high->equity_1h` score `0.8501` n `175` status `ready` deltaP `10.8418` edge `0.0774` maxDD `-2.6402`
- `market_context_high->crypto_major_24h` score `0.2975` n `174` status `ready` deltaP `20.8309` edge `0.7445` maxDD `-62.3533`
- `market_context_high->index_1h` score `0.15` n `175` status `ready` deltaP `6.0804` edge `0.031` maxDD `-1.3898`
- `market_context_high->unknown_1h` score `0.055` n `175` status `ready` deltaP `5.0471` edge `0.0429` maxDD `-3.0902`
- `market_context_high->fx_24h` score `-0.0752` n `174` status `ready` deltaP `14.8749` edge `0.0305` maxDD `-2.811`
- `market_context_high->metal_1h` score `-0.1686` n `175` status `ready` deltaP `6.5038` edge `0.0371` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.5874` n `175` status `ready` deltaP `-2.0` edge `0.0008` maxDD `-0.3548`
- `market_context_high->metal_24h` score `-0.8103` n `174` status `ready` deltaP `9.8993` edge `0.2566` maxDD `-23.2095`
- `market_context_high->fx_4h` score `-1.0745` n `175` status `ready` deltaP `-6.9921` edge `-0.003` maxDD `-1.0513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
