# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T18:07:32.190733+00:00`
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

- `market_context_high->equity_24h` score `2.094` n `136` status `ready` deltaP `5.5026` edge `0.4512` maxDD `-21.0709`
- `market_context_high->commodity_4h` score `0.787` n `172` status `ready` deltaP `11.4223` edge `0.0609` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7342` n `180` status `ready` deltaP `9.867` edge `0.0297` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.6879` n `136` status `ready` deltaP `18.7634` edge `0.013` maxDD `-1.4613`
- `market_context_high->index_24h` score `-0.1082` n `136` status `ready` deltaP `5.119` edge `0.11` maxDD `-5.9181`
- `market_context_high->fx_4h` score `-0.1222` n `172` status `ready` deltaP `6.3883` edge `0.0072` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1356` n `180` status `ready` deltaP `4.1218` edge `0.0003` maxDD `-0.613`
- `market_context_high->index_1h` score `-0.593` n `180` status `ready` deltaP `-3.7225` edge `-0.0035` maxDD `-0.8168`
- `market_context_high->metal_24h` score `-0.704` n `136` status `ready` deltaP `1.5585` edge `0.0591` maxDD `-2.9193`
- `market_context_high->metal_1h` score `-0.8353` n `180` status `ready` deltaP `-4.9634` edge `-0.0104` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-0.9961` n `180` status `ready` deltaP `-3.0439` edge `-0.0156` maxDD `-5.0113`
- `market_context_high->index_4h` score `-1.1776` n `172` status `ready` deltaP `-1.4074` edge `-0.0105` maxDD `-1.26`
- `market_context_high->crypto_alt_1h` score `-1.8011` n `180` status `ready` deltaP `-10.1563` edge `-0.0463` maxDD `-6.3518`
- `market_context_high->metal_4h` score `-2.071` n `172` status `ready` deltaP `-7.5334` edge `-0.0389` maxDD `-6.1111`
- `market_context_high->crypto_major_24h` score `-2.9808` n `136` status `ready` deltaP `1.7892` edge `-0.0109` maxDD `-14.2873`
- `market_context_high->equity_4h` score `-3.1307` n `172` status `ready` deltaP `-10.8905` edge `-0.1097` maxDD `-8.5254`
- `market_context_high->crypto_alt_24h` score `-3.632` n `136` status `ready` deltaP `-9.6544` edge `-0.094` maxDD `-4.5445`
- `market_context_high->crypto_major_1h` score `-3.9317` n `180` status `ready` deltaP `-10.8782` edge `-0.0647` maxDD `-11.9002`
- `market_context_high->crypto_alt_4h` score `-5.8394` n `172` status `ready` deltaP `-11.3195` edge `-0.1354` maxDD `-15.3937`
- `market_context_high->commodity_24h` score `-8.9006` n `136` status `ready` deltaP `-6.0684` edge `-0.2291` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
