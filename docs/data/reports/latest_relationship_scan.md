# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T22:22:36.797674+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5932`

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

- `news_risk_high->unknown_24h` score `5188.5913` n `60` status `ready` deltaP `31.2882` edge `432.2161` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.8146` n `53` status `ready` deltaP `58.1374` edge `1.1367` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `4.8645` n `68` status `ready` deltaP `17.1359` edge `0.3675` maxDD `-3.4427`
- `market_context_high->commodity_24h` score `1.7657` n `53` status `ready` deltaP `27.4844` edge `0.229` maxDD `-10.2019`
- `news_risk_high->index_4h` score `1.7415` n `68` status `ready` deltaP `16.6786` edge `0.072` maxDD `-0.3783`
- `market_context_high->crypto_alt_4h` score `0.7892` n `53` status `ready` deltaP `9.9575` edge `0.1305` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.6672` n `68` status `ready` deltaP `9.4928` edge `0.0746` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.2058` n `53` status `ready` deltaP `13.5585` edge `0.0156` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.1274` n `68` status `ready` deltaP `5.165` edge `0.0295` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.0983` n `68` status `ready` deltaP `6.1818` edge `0.0396` maxDD `-3.1233`
- `market_context_high->fx_24h` score `-0.025` n `53` status `ready` deltaP `7.7531` edge `0.0431` maxDD `-2.506`
- `market_context_high->fx_1h` score `-0.052` n `53` status `ready` deltaP `6.7535` edge `0.0009` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.0528` n `68` status `ready` deltaP `2.6154` edge `0.0081` maxDD `-0.5845`
- `news_risk_high->fx_4h` score `-0.0613` n `68` status `ready` deltaP `10.3121` edge `0.0219` maxDD `-0.6604`
- `market_context_high->commodity_1h` score `-0.0667` n `53` status `ready` deltaP `4.3272` edge `0.0167` maxDD `-1.3282`
- `news_risk_high->fx_1h` score `-0.1354` n `68` status `ready` deltaP `1.6203` edge `0.0041` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.152` n `68` status `ready` deltaP `2.1663` edge `0.0064` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2132` n `68` status `ready` deltaP `1.9197` edge `0.0319` maxDD `-3.762`
- `market_context_high->commodity_4h` score `-0.3063` n `53` status `ready` deltaP `2.81` edge `0.0295` maxDD `-3.0005`
- `market_context_high->crypto_alt_1h` score `-0.6129` n `53` status `ready` deltaP `-4.4176` edge `0.0136` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
