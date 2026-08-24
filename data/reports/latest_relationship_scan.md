# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T03:07:27.863908+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14856`

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

- `news_risk_high->unknown_24h` score `52.4398` n `50` status `ready` deltaP `17.1875` edge `4.2554` maxDD `0.0`
- `news_risk_high->equity_24h` score `15.1275` n `50` status `ready` deltaP `41.8056` edge `1.0565` maxDD `-3.6331`
- `news_risk_high->unknown_4h` score `13.0025` n `51` status `ready` deltaP `23.4965` edge `0.9315` maxDD `-0.0348`
- `news_risk_high->index_24h` score `6.0915` n `50` status `ready` deltaP `50.6736` edge `0.1795` maxDD `-0.109`
- `risk_on_high->unknown_1h` score `4.3893` n `33` status `ready` deltaP `-12.221` edge `0.6891` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `4.3893` n `33` status `ready` deltaP `-12.221` edge `0.6891` maxDD `-1.5916`
- `news_risk_high->fx_4h` score `3.1579` n `51` status `ready` deltaP `37.1682` edge `0.0288` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `3.0661` n `51` status `ready` deltaP `24.4889` edge `0.1693` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `2.9131` n `51` status `ready` deltaP `15.5864` edge `0.1693` maxDD `-0.7693`
- `news_risk_high->crypto_alt_24h` score `2.4384` n `50` status `ready` deltaP `26.9097` edge `0.0238` maxDD `0.0`
- `risk_on_high->metal_4h` score `2.2277` n `33` status `ready` deltaP `29.4947` edge `-0.0022` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.2277` n `33` status `ready` deltaP `29.4947` edge `-0.0022` maxDD `-0.0367`
- `risk_on_high->equity_4h` score `2.1863` n `33` status `ready` deltaP `-0.4665` edge `0.2283` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `2.1863` n `33` status `ready` deltaP `-0.4665` edge `0.2283` maxDD `-0.773`
- `news_risk_high->metal_24h` score `2.0869` n `50` status `ready` deltaP `37.2361` edge `-0.0701` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `2.0296` n `145` status `ready` deltaP `21.3194` edge `0.0407` maxDD `-0.0956`
- `market_context_high->unknown_1h` score `1.6823` n `157` status `ready` deltaP `10.3036` edge `0.1164` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.2805` n `51` status `ready` deltaP `17.4445` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.826` n `51` status `ready` deltaP `16.9954` edge `0.029` maxDD `-0.9128`
- `market_context_high->commodity_24h` score `0.7837` n `93` status `ready` deltaP `-0.5264` edge `0.1163` maxDD `-0.7984`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
