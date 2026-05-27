# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T19:37:24.428269+00:00`
- Price records: `672`
- Market context records: `2069`
- Flow alert records: `7851`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9145`

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

- `market_context_high->crypto_major_4h` score `9.7066` n `206` status `ready` deltaP `34.4823` edge `0.632` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `9.0384` n `206` status `ready` deltaP `26.7553` edge `0.6893` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.6688` n `206` status `ready` deltaP `21.8328` edge `0.4851` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `6.0668` n `205` status `ready` deltaP `19.9367` edge `0.9047` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.5248` n `206` status `ready` deltaP `19.302` edge `0.2745` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.0414` n `206` status `ready` deltaP `15.4467` edge `0.1355` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.8258` n `206` status `ready` deltaP `14.005` edge `0.1574` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.75` n `205` status `ready` deltaP `20.8161` edge `0.4969` maxDD `-33.1875`
- `market_context_high->index_24h` score `1.4746` n `205` status `ready` deltaP `9.3181` edge `0.1836` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `1.4704` n `206` status `ready` deltaP `11.011` edge `0.1605` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `0.5198` n `205` status `ready` deltaP `21.0296` edge `0.7617` maxDD `-62.3533`
- `market_context_high->unknown_1h` score `0.4463` n `206` status `ready` deltaP `5.5578` edge `0.0721` maxDD `-3.0902`
- `market_context_high->equity_1h` score `0.4225` n `206` status `ready` deltaP `8.1217` edge `0.0599` maxDD `-2.6402`
- `market_context_high->index_1h` score `-0.0816` n `206` status `ready` deltaP `4.0565` edge `0.0252` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.2634` n `205` status `ready` deltaP `13.7176` edge `0.0259` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.5609` n `206` status `ready` deltaP `11.6741` edge `0.1377` maxDD `-11.9812`
- `market_context_high->metal_1h` score `-0.7536` n `206` status `ready` deltaP `4.1466` edge `0.0283` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8287` n `206` status `ready` deltaP `-1.0479` edge `0.0007` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.4225` n `206` status `ready` deltaP `-4.5451` edge `-0.0001` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.8266` n `205` status `ready` deltaP `11.0549` edge `0.1642` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
