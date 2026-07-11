# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T23:06:30.414312+00:00`
- Price records: `672`
- Market context records: `6439`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5875`

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

- `news_risk_high->crypto_alt_24h` score `11.5837` n `32` status `ready` deltaP `29.5139` edge `0.7833` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `8.8641` n `146` status `ready` deltaP `21.3304` edge `0.9265` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.4126` n `32` status `ready` deltaP `53.4722` edge `0.1779` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1096` n `32` status `ready` deltaP `42.7591` edge `0.062` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.0619` n `32` status `ready` deltaP `34.8958` edge `0.1264` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.1989` n `32` status `ready` deltaP `11.1111` edge `0.414` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4326` n `32` status `ready` deltaP `29.3413` edge `0.021` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.5287` n `189` status `ready` deltaP `-4.6962` edge `0.2488` maxDD `-3.2083`
- `news_risk_high->crypto_major_1h` score `1.4562` n `32` status `ready` deltaP `13.5292` edge `0.1432` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8404` n `32` status `ready` deltaP `9.6744` edge `0.0894` maxDD `-1.6923`
- `market_context_high->index_4h` score `0.0311` n `189` status `ready` deltaP `7.1437` edge `0.0226` maxDD `-0.4108`
- `market_context_high->metal_4h` score `-0.2142` n `189` status `ready` deltaP `7.6002` edge `0.0403` maxDD `-2.7056`
- `news_risk_high->unknown_1h` score `-0.3053` n `32` status `ready` deltaP `6.5307` edge `-0.0345` maxDD `-0.7581`
- `news_risk_high->metal_1h` score `-0.5636` n `32` status `ready` deltaP `0.2994` edge `-0.0245` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.5647` n `189` status `ready` deltaP `0.564` edge `0.0016` maxDD `-1.8877`
- `market_context_high->metal_24h` score `-0.6135` n `146` status `ready` deltaP `12.9733` edge `0.0917` maxDD `-11.8809`
- `market_context_high->equity_4h` score `-0.6177` n `189` status `ready` deltaP `6.659` edge `0.0463` maxDD `-8.2573`
- `market_context_high->commodity_1h` score `-0.6312` n `189` status `ready` deltaP `-1.3821` edge `-0.0034` maxDD `-2.1314`
- `news_risk_high->index_24h` score `-0.7158` n `32` status `ready` deltaP `0.8681` edge `-0.0104` maxDD `-2.3058`
- `market_context_high->unknown_4h` score `-0.7311` n `189` status `ready` deltaP `-14.8286` edge `0.2785` maxDD `-10.5788`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
