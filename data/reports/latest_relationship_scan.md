# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T07:37:28.783241+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `news_risk_high->unknown_24h` score `56.8265` n `51` status `ready` deltaP `20.6086` edge `4.6066` maxDD `-0.3426`
- `news_risk_high->crypto_alt_24h` score `31.5868` n `51` status `ready` deltaP `44.6384` edge `2.4059` maxDD `-4.7006`
- `news_risk_high->crypto_major_24h` score `8.6345` n `51` status `ready` deltaP `26.4501` edge `0.6234` maxDD `-5.082`
- `market_context_high->unknown_24h` score `7.9475` n `120` status `ready` deltaP `15.9027` edge `0.6295` maxDD `-3.1917`
- `news_risk_high->equity_24h` score `6.9738` n `51` status `ready` deltaP `28.8807` edge `0.4914` maxDD `-5.5562`
- `news_risk_high->unknown_4h` score `6.3041` n `80` status `ready` deltaP `10.5183` edge `0.5142` maxDD `-1.7183`
- `news_risk_high->metal_24h` score `4.3044` n `51` status `ready` deltaP `42.6062` edge `0.0867` maxDD `-0.6303`
- `market_context_high->metal_24h` score `3.5395` n `120` status `ready` deltaP `29.8611` edge `0.1978` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.7292` n `80` status `ready` deltaP `5.524` edge `0.2263` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.596` n `120` status `ready` deltaP `19.685` edge `0.1258` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.3327` n `51` status `ready` deltaP `25.5106` edge `0.041` maxDD `-0.3341`
- `news_risk_high->fx_4h` score `2.2901` n `80` status `ready` deltaP `33.5976` edge `0.0218` maxDD `-0.3953`
- `market_context_high->unknown_1h` score `1.303` n `120` status `ready` deltaP `9.6907` edge `0.089` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6633` n `80` status `ready` deltaP `13.2934` edge `0.0055` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4828` n `80` status `ready` deltaP `13.2485` edge `0.0056` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.1431` n `120` status `ready` deltaP `9.4918` edge `0.0101` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.3164` n `120` status `ready` deltaP `4.9601` edge `-0.0004` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.3825` n `80` status `ready` deltaP `0.4566` edge `-0.0084` maxDD `-0.8275`
- `news_risk_high->index_4h` score `-0.5436` n `80` status `ready` deltaP `1.6159` edge `-0.0163` maxDD `-1.7996`
- `news_risk_high->commodity_4h` score `-0.553` n `80` status `ready` deltaP `7.8049` edge `0.0112` maxDD `-2.0635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
