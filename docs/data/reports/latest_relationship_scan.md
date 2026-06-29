# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T04:52:36.334069+00:00`
- Price records: `672`
- Market context records: `5111`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10328`

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

- `market_context_high->unknown_24h` score `21.7121` n `74` status `ready` deltaP `28.4253` edge `1.6541` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `8.026` n `113` status `ready` deltaP `22.4477` edge `0.6214` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `7.4659` n `125` status `ready` deltaP `5.7006` edge `0.6483` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `5.3144` n `113` status `ready` deltaP `15.2075` edge `0.5014` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.5549` n `113` status `ready` deltaP `13.59` edge `0.4662` maxDD `-14.0065`
- `market_context_high->crypto_alt_1h` score `0.8778` n `125` status `ready` deltaP `6.3461` edge `0.127` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.4683` n `125` status `ready` deltaP `8.4982` edge `0.0627` maxDD `-2.745`
- `market_context_high->crypto_major_1h` score `0.4018` n `125` status `ready` deltaP `7.2395` edge `0.1278` maxDD `-6.9639`
- `market_context_high->metal_1h` score `0.2459` n `125` status `ready` deltaP `8.2922` edge `0.0259` maxDD `-1.3057`
- `market_context_high->equity_4h` score `0.1892` n `113` status `ready` deltaP `6.5441` edge `0.1445` maxDD `-7.4425`
- `market_context_high->index_1h` score `-0.0219` n `125` status `ready` deltaP `5.3497` edge `0.0119` maxDD `-1.0296`
- `market_context_high->metal_4h` score `-0.4287` n `113` status `ready` deltaP `3.6397` edge `0.0618` maxDD `-4.6157`
- `market_context_high->index_4h` score `-0.5094` n `113` status `ready` deltaP `3.2754` edge `0.0246` maxDD `-2.9391`
- `market_context_high->fx_1h` score `-0.6824` n `125` status `ready` deltaP `-3.4036` edge `-0.0007` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.7527` n `125` status `ready` deltaP `1.7473` edge `0.0014` maxDD `-2.062`
- `market_context_high->commodity_24h` score `-0.856` n `74` status `ready` deltaP `11.036` edge `0.0572` maxDD `-12.2414`
- `market_context_high->fx_4h` score `-1.0147` n `113` status `ready` deltaP `-3.5546` edge `0.0009` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.4602` n `74` status `ready` deltaP `-2.318` edge `-0.008` maxDD `-1.5252`
- `market_context_high->commodity_4h` score `-2.1304` n `113` status `ready` deltaP `2.4795` edge `-0.0231` maxDD `-7.3435`
- `market_context_high->metal_24h` score `-3.8004` n `74` status `ready` deltaP `-4.7204` edge `0.0243` maxDD `-29.4045`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
