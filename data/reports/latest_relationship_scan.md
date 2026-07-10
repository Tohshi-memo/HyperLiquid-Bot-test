# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T21:07:35.445187+00:00`
- Price records: `672`
- Market context records: `6322`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.4518` n `32` status `ready` deltaP `43.2292` edge `1.0142` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.0476` n `32` status `ready` deltaP `50.6944` edge `0.166` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.384` n `32` status `ready` deltaP `16.6667` edge `0.5289` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.2045` n `32` status `ready` deltaP `43.8262` edge `0.0628` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.3599` n `32` status `ready` deltaP `30.0347` edge `0.1003` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.4374` n `32` status `ready` deltaP `29.3413` edge `0.0214` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4998` n `32` status `ready` deltaP `14.8765` edge `0.1398` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9377` n `32` status `ready` deltaP `11.7702` edge `0.0879` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.149` n `208` status `ready` deltaP `-6.5954` edge `0.1572` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.0466` n `196` status `ready` deltaP `9.361` edge `0.0378` maxDD `-2.7056`
- `market_context_high->metal_24h` score `-0.2328` n `153` status `ready` deltaP `19.7406` edge `0.0954` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.3864` n `208` status `ready` deltaP `3.9181` edge `0.0021` maxDD `-1.8877`
- `market_context_high->index_4h` score `-0.5148` n `196` status `ready` deltaP `4.2652` edge `0.0196` maxDD `-1.1232`
- `news_risk_high->index_24h` score `-0.5438` n `32` status `ready` deltaP `3.125` edge `-0.0034` maxDD `-2.3058`
- `market_context_high->commodity_1h` score `-0.5733` n `208` status `ready` deltaP `-0.7485` edge `-0.0002` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.7228` n `208` status `ready` deltaP `-3.1207` edge `0.0021` maxDD `-0.9168`
- `news_risk_high->metal_1h` score `-0.7551` n `32` status `ready` deltaP `-3.2934` edge `-0.0251` maxDD `-1.6464`
- `market_context_high->fx_1h` score `-0.8121` n `208` status `ready` deltaP `-1.9087` edge `-0.0022` maxDD `-0.8865`
- `news_risk_high->unknown_1h` score `-0.827` n `32` status `ready` deltaP `5.1834` edge `-0.069` maxDD `-0.7581`
- `market_context_high->crypto_alt_1h` score `-1.0059` n `208` status `ready` deltaP `4.799` edge `0.0143` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
