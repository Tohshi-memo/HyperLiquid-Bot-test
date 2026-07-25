# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T09:37:26.055643+00:00`
- Price records: `672`
- Market context records: `7865`
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

- `market_context_high->equity_24h` score `11.8934` n `124` status `ready` deltaP `29.0407` edge `0.9317` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.9041` n `125` status `ready` deltaP `12.1012` edge `0.2507` maxDD `-2.1494`
- `market_context_high->equity_4h` score `1.8844` n `125` status `ready` deltaP `7.3651` edge `0.3415` maxDD `-6.2546`
- `market_context_high->crypto_major_4h` score `1.4498` n `125` status `ready` deltaP `16.3232` edge `0.1838` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.3865` n `124` status `ready` deltaP `21.6887` edge `0.1293` maxDD `-7.0012`
- `market_context_high->crypto_major_1h` score `1.1755` n `125` status `ready` deltaP `13.3497` edge `0.0489` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `1.0936` n `125` status `ready` deltaP `10.3427` edge `0.1339` maxDD `-3.9374`
- `market_context_high->fx_24h` score `0.9486` n `124` status `ready` deltaP `27.2959` edge `0.0484` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.6201` n `125` status `ready` deltaP `9.2492` edge `0.0996` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.4162` n `125` status `ready` deltaP `8.0612` edge `0.0403` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.3543` n `125` status `ready` deltaP `5.2467` edge `0.0378` maxDD `-1.4603`
- `market_context_high->index_1h` score `0.1973` n `125` status `ready` deltaP `7.8018` edge `0.0163` maxDD `-0.7743`
- `market_context_high->commodity_1h` score `0.0752` n `125` status `ready` deltaP `5.6949` edge `0.0142` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2178` n `125` status `ready` deltaP `10.0355` edge `0.051` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3063` n `125` status `ready` deltaP `-0.048` edge `-0.0002` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8874` n `125` status `ready` deltaP `0.7928` edge `0.0211` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-0.9793` n `125` status `ready` deltaP `3.6012` edge `0.0829` maxDD `-1.4149`
- `market_context_high->index_24h` score `-1.03` n `124` status `ready` deltaP `-4.4684` edge `0.0989` maxDD `-2.0929`
- `market_context_high->fx_4h` score `-1.3947` n `125` status `ready` deltaP `-2.5431` edge `0.0006` maxDD `-1.6629`
- `market_context_high->crypto_alt_24h` score `-1.5195` n `125` status `ready` deltaP `15.139` edge `0.2338` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
