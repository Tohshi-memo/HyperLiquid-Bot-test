# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T14:22:29.674268+00:00`
- Price records: `672`
- Market context records: `6399`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11091`

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

- `news_risk_high->crypto_alt_24h` score `13.7115` n `32` status `ready` deltaP `35.5903` edge `0.9201` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6255` n `32` status `ready` deltaP `55.7292` edge `0.1806` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.3725` n `32` status `ready` deltaP `37.8472` edge `0.1326` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `4.195` n `32` status `ready` deltaP `17.1875` edge `0.5012` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.0498` n `32` status `ready` deltaP `41.997` edge `0.0621` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4218` n `32` status `ready` deltaP `29.1916` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4398` n `32` status `ready` deltaP `13.6789` edge `0.1401` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8364` n `32` status `ready` deltaP `10.2732` edge `0.0849` maxDD `-1.6923`
- `market_context_high->unknown_24h` score `0.5117` n `146` status `ready` deltaP `7.0134` edge `0.3916` maxDD `-20.3241`
- `market_context_high->metal_4h` score `0.4898` n `216` status `ready` deltaP `11.9354` edge `0.0409` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.3985` n `218` status `ready` deltaP `-5.6062` edge `0.1714` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.07` n `216` status `ready` deltaP `7.8252` edge `0.0213` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.1997` n `32` status `ready` deltaP `6.9798` edge `-0.0287` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.3329` n `146` status `ready` deltaP `19.6205` edge `0.0983` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.4816` n `218` status `ready` deltaP `2.0134` edge `0.0026` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.4934` n `216` status `ready` deltaP `8.3898` edge `0.0507` maxDD `-8.2573`
- `news_risk_high->metal_1h` score `-0.6453` n `32` status `ready` deltaP `-1.1976` edge `-0.025` maxDD `-1.6464`
- `market_context_high->index_1h` score `-0.6823` n `218` status `ready` deltaP `-2.7331` edge `0.0027` maxDD `-0.7564`
- `market_context_high->fx_1h` score `-0.7294` n `218` status `ready` deltaP `-0.8543` edge `-0.0017` maxDD `-0.9376`
- `market_context_high->commodity_1h` score `-0.7395` n `218` status `ready` deltaP `-3.5104` edge `-0.0031` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
