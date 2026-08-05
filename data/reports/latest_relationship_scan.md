# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T11:37:40.540892+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11648`

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

- `market_context_high->unknown_24h` score `13.9898` n `89` status `ready` deltaP `9.4667` edge `1.107` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4131` n `92` status `ready` deltaP `2.2402` edge `0.5357` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.7565` n `92` status `ready` deltaP `18.286` edge `0.1091` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.1923` n `89` status `ready` deltaP `28.0548` edge `0.0864` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.8963` n `89` status `ready` deltaP `1.6268` edge `0.2209` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.4274` n `98` status `ready` deltaP `7.4423` edge `0.0276` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.0756` n `92` status `ready` deltaP `13.2887` edge `0.0071` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.0611` n `98` status `ready` deltaP `6.4891` edge `-0.0032` maxDD `-0.7973`
- `market_context_high->metal_1h` score `-0.559` n `98` status `ready` deltaP `-1.8789` edge `-0.0097` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.648` n `98` status `ready` deltaP `-1.662` edge `-0.0186` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.9061` n `92` status `ready` deltaP `1.5906` edge `-0.0033` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.9433` n `98` status `ready` deltaP `-4.2863` edge `-0.0213` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.423` n `89` status `ready` deltaP `0.8505` edge `-0.0438` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.568` n `92` status `ready` deltaP `-0.8749` edge `-0.0562` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7644` n `98` status `ready` deltaP `2.6641` edge `-0.0904` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1493` n `92` status `ready` deltaP `-13.3219` edge `-0.0613` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.4277` n `89` status `ready` deltaP `-10.4343` edge `-0.0222` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.1877` n `98` status `ready` deltaP `4.4483` edge `-0.2506` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6056` n `98` status `ready` deltaP `-13.1156` edge `-0.0757` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.0813` n `89` status `ready` deltaP `10.4771` edge `-0.0345` maxDD `-50.8663`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
