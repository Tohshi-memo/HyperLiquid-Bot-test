# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T22:52:29.071827+00:00`
- Price records: `672`
- Market context records: `6438`
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

- `news_risk_high->crypto_alt_24h` score `11.6264` n `32` status `ready` deltaP `29.6875` edge `0.7857` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `8.7693` n `146` status `ready` deltaP `21.3304` edge `0.9186` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.4277` n `32` status `ready` deltaP `53.6458` edge `0.178` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1096` n `32` status `ready` deltaP `42.7591` edge `0.062` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.0806` n `32` status `ready` deltaP `35.0694` edge `0.1268` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.2212` n `32` status `ready` deltaP `11.2847` edge `0.4157` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4326` n `32` status `ready` deltaP `29.3413` edge `0.021` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.482` n `190` status `ready` deltaP `-4.7999` edge `0.2456` maxDD `-3.2083`
- `news_risk_high->crypto_major_1h` score `1.4555` n `32` status `ready` deltaP `13.5292` edge `0.1431` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.838` n `32` status `ready` deltaP `9.6744` edge `0.0891` maxDD `-1.6923`
- `market_context_high->index_4h` score `0.0319` n `190` status `ready` deltaP `7.1695` edge `0.0225` maxDD `-0.4108`
- `market_context_high->metal_4h` score `-0.2084` n `190` status `ready` deltaP `7.6733` edge `0.0403` maxDD `-2.7056`
- `news_risk_high->unknown_1h` score `-0.2861` n `32` status `ready` deltaP `6.6804` edge `-0.0339` maxDD `-0.7581`
- `market_context_high->metal_1h` score `-0.5504` n `190` status `ready` deltaP `0.8257` edge `0.0017` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.5643` n `32` status `ready` deltaP `0.2994` edge `-0.0246` maxDD `-1.6464`
- `market_context_high->metal_24h` score `-0.5846` n `146` status `ready` deltaP `13.4846` edge `0.092` maxDD `-11.8809`
- `market_context_high->commodity_1h` score `-0.6364` n `190` status `ready` deltaP `-1.497` edge `-0.0033` maxDD `-2.1314`
- `market_context_high->equity_4h` score `-0.6365` n `190` status `ready` deltaP `6.3415` edge `0.046` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.7213` n `190` status `ready` deltaP `-0.9219` edge `-0.0016` maxDD `-0.8555`
- `news_risk_high->index_24h` score `-0.7256` n `32` status `ready` deltaP `0.6944` edge `-0.0105` maxDD `-2.3058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
