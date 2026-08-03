# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T01:52:27.911978+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `4557.4282` n `55` status `ready` deltaP `23.1092` edge `379.6737` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `14.4087` n `40` status `ready` deltaP `51.4583` edge `0.8974` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.2386` n `40` status `ready` deltaP `51.3194` edge `0.6072` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `3.9906` n `55` status `ready` deltaP `10.8925` edge `0.3363` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.624` n `55` status `ready` deltaP `15.5848` edge `0.0695` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `0.7584` n `43` status `ready` deltaP `10.0433` edge `0.1149` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.6035` n `55` status `ready` deltaP `8.9957` edge `0.0726` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.4139` n `43` status `ready` deltaP `17.6652` edge `0.0149` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.3751` n `47` status `ready` deltaP `7.7143` edge `0.0341` maxDD `-1.3282`
- `news_risk_high->metal_4h` score `0.318` n `55` status `ready` deltaP `8.1707` edge `0.0214` maxDD `-0.8085`
- `market_context_high->crypto_alt_4h` score `0.3156` n `43` status `ready` deltaP `5.5835` edge `0.0938` maxDD `-4.9116`
- `news_risk_high->index_1h` score `0.0277` n `55` status `ready` deltaP `4.1181` edge `0.0084` maxDD `-0.5845`
- `market_context_high->fx_1h` score `0.0079` n `47` status `ready` deltaP `7.2652` edge `-0.0085` maxDD `-0.7804`
- `news_risk_high->fx_4h` score `-0.2596` n `55` status `ready` deltaP `5.995` edge `0.0225` maxDD `-0.6604`
- `news_risk_high->crypto_alt_1h` score `-0.2642` n `55` status `ready` deltaP `5.4437` edge `0.0099` maxDD `-3.1233`
- `news_risk_high->metal_1h` score `-0.2823` n `55` status `ready` deltaP `-0.1388` edge `0.0009` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.4031` n `55` status `ready` deltaP `2.2564` edge `0.0053` maxDD `-3.762`
- `news_risk_high->fx_1h` score `-0.4124` n `55` status `ready` deltaP `-0.7812` edge `0.0031` maxDD `-0.2475`
- `market_context_high->fx_24h` score `-0.7259` n `40` status `ready` deltaP `0.6597` edge `0.0331` maxDD `-2.506`
- `news_risk_high->commodity_1h` score `-0.9417` n `55` status `ready` deltaP `1.4861` edge `-0.0206` maxDD `-2.0891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
