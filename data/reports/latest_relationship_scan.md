# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T17:40:11.762157+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->equity_24h` score `1.7842` n `136` status `ready` deltaP `5.156` edge `0.4277` maxDD `-21.0709`
- `market_context_high->commodity_4h` score `0.7668` n `171` status `ready` deltaP `11.2591` edge `0.0603` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7354` n `180` status `ready` deltaP `9.867` edge `0.0298` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.6963` n `136` status `ready` deltaP `18.7634` edge `0.0137` maxDD `-1.4613`
- `market_context_high->fx_4h` score `-0.1153` n `171` status `ready` deltaP `6.4755` edge `0.0072` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1356` n `180` status `ready` deltaP `4.1218` edge `0.0003` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.1671` n `136` status `ready` deltaP `4.7724` edge `0.1074` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.6016` n `180` status `ready` deltaP `-3.8722` edge `-0.0036` maxDD `-0.8168`
- `market_context_high->metal_24h` score `-0.728` n `136` status `ready` deltaP `1.5585` edge `0.0571` maxDD `-2.9193`
- `market_context_high->metal_1h` score `-0.812` n `180` status `ready` deltaP `-4.664` edge `-0.0094` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-1.0077` n `180` status `ready` deltaP `-3.1936` edge `-0.0161` maxDD `-5.0113`
- `market_context_high->index_4h` score `-1.1837` n `171` status `ready` deltaP `-1.3791` edge `-0.0112` maxDD `-1.26`
- `market_context_high->crypto_alt_1h` score `-1.7987` n `180` status `ready` deltaP `-10.1563` edge `-0.046` maxDD `-6.3518`
- `market_context_high->metal_4h` score `-2.0696` n `171` status `ready` deltaP `-7.4767` edge `-0.0391` maxDD `-6.1111`
- `market_context_high->crypto_major_24h` score `-3.1393` n `136` status `ready` deltaP `1.4426` edge `-0.0218` maxDD `-14.2873`
- `market_context_high->equity_4h` score `-3.1915` n `171` status `ready` deltaP `-10.9132` edge `-0.1178` maxDD `-8.4888`
- `market_context_high->crypto_alt_24h` score `-3.7354` n `136` status `ready` deltaP `-10.0011` edge `-0.1003` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.818` n `171` status `ready` deltaP `-11.3456` edge `-0.1381` maxDD `-15.3937`
- `market_context_high->crypto_major_1h` score `-3.9257` n `180` status `ready` deltaP `-10.8782` edge `-0.0642` maxDD `-11.9002`
- `market_context_high->commodity_24h` score `-8.8343` n `136` status `ready` deltaP `-5.7218` edge `-0.2229` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
