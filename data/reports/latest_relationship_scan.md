# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T16:22:29.283390+00:00`
- Price records: `672`
- Market context records: `6408`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11095`

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

- `news_risk_high->crypto_alt_24h` score `13.2355` n `32` status `ready` deltaP `34.2014` edge `0.8897` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6883` n `32` status `ready` deltaP `56.4236` edge `0.1812` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.2301` n `32` status `ready` deltaP `36.4583` edge `0.13` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.1521` n `32` status `ready` deltaP `43.2165` edge `0.0625` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.9925` n `32` status `ready` deltaP `15.7986` edge `0.4845` maxDD `-4.2368`
- `market_context_high->unknown_24h` score `3.6468` n `146` status `ready` deltaP `11.104` edge `0.5599` maxDD `-15.0689`
- `news_risk_high->fx_1h` score `2.459` n `32` status `ready` deltaP `29.6407` edge `0.0212` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4671` n `32` status `ready` deltaP `14.128` edge `0.1406` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8434` n `32` status `ready` deltaP `10.2732` edge `0.0858` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.5875` n `210` status `ready` deltaP `-5.6744` edge `0.1876` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.3863` n `210` status `ready` deltaP `11.2369` edge `0.0411` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.0504` n `210` status `ready` deltaP `7.5204` edge `0.0217` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.3016` n `32` status `ready` deltaP `6.0816` edge `-0.0312` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.3882` n `146` status `ready` deltaP `19.1091` edge `0.0971` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.4604` n `210` status `ready` deltaP `2.4351` edge `0.0025` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.629` n `32` status `ready` deltaP `-0.8982` edge `-0.0249` maxDD `-1.6464`
- `market_context_high->fx_1h` score `-0.6695` n `210` status `ready` deltaP `-0.1212` edge `-0.0016` maxDD `-0.9376`
- `market_context_high->commodity_1h` score `-0.6995` n `210` status `ready` deltaP `-2.8301` edge `-0.0025` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.7271` n `210` status `ready` deltaP `-3.5786` edge `0.0026` maxDD `-0.7564`
- `news_risk_high->index_24h` score `-0.7557` n `32` status `ready` deltaP `0.5208` edge `-0.0132` maxDD `-2.3058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
