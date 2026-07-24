# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T10:37:28.849740+00:00`
- Price records: `672`
- Market context records: `7767`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `6.3102` n `132` status `ready` deltaP `25.1451` edge `0.4924` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.1029` n `133` status `ready` deltaP `11.1881` edge `0.2264` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `0.923` n `133` status `ready` deltaP `12.5591` edge `0.0373` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.5651` n `132` status `ready` deltaP `21.5263` edge `0.0377` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `0.4323` n `133` status `ready` deltaP `12.3647` edge `0.1254` maxDD `-6.7444`
- `market_context_high->equity_1h` score `0.4286` n `133` status `ready` deltaP `7.5955` edge `0.071` maxDD `-4.2072`
- `market_context_high->equity_4h` score `0.3642` n `133` status `ready` deltaP `1.6636` edge `0.2269` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.323` n `133` status `ready` deltaP `8.3441` edge `0.0143` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `0.1992` n `133` status `ready` deltaP `6.8276` edge `0.0828` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `0.098` n `133` status `ready` deltaP `4.1286` edge `0.0239` maxDD `-1.4603`
- `market_context_high->commodity_4h` score `0.0799` n `133` status `ready` deltaP `5.5517` edge `0.029` maxDD `-1.0817`
- `market_context_high->commodity_1h` score `-0.0535` n `133` status `ready` deltaP `4.7461` edge `0.0098` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2821` n `133` status `ready` deltaP `10.2527` edge `0.0413` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.399` n `133` status `ready` deltaP `0.8242` edge `0.0` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.9058` n `133` status `ready` deltaP `0.968` edge `0.0184` maxDD `-0.6936`
- `market_context_high->commodity_24h` score `-1.1792` n `132` status `ready` deltaP `7.6022` edge `0.0094` maxDD `-7.0012`
- `market_context_high->fx_4h` score `-1.4753` n `133` status `ready` deltaP `-3.8559` edge `-0.0006` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.6514` n `133` status `ready` deltaP `-0.2339` edge `0.0694` maxDD `-1.4368`
- `market_context_high->index_24h` score `-2.029` n `132` status `ready` deltaP `-13.7499` edge `0.0418` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.3147` n `133` status `ready` deltaP `-1.8729` edge `-0.1214` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
