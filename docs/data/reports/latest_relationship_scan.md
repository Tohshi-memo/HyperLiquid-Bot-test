# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T07:22:43.381232+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4221`

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

- `market_context_high->unknown_24h` score `1377.9345` n `98` status `ready` deltaP `2.9514` edge `114.8082` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.0805` n `98` status `ready` deltaP `43.7606` edge `1.9687` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `13.7389` n `98` status `ready` deltaP `29.6485` edge `1.7761` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.3154` n `98` status `ready` deltaP `1.7292` edge `0.0082` maxDD `-2.1461`
- `market_context_high->metal_24h` score `-0.6949` n `98` status `ready` deltaP `15.3557` edge `0.1622` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.7239` n `98` status `ready` deltaP `9.9428` edge `0.0041` maxDD `-6.1238`
- `market_context_high->crypto_alt_4h` score `-0.9117` n `98` status `ready` deltaP `-1.2569` edge `0.1725` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.9756` n `98` status `ready` deltaP `-3.822` edge `-0.0009` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2422` n `98` status `ready` deltaP `-2.4074` edge `0.0071` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3819` n `98` status `ready` deltaP `-8.8965` edge `-0.0012` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.5578` n `98` status `ready` deltaP `-4.2123` edge `0.1866` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.3034` n `98` status `ready` deltaP `-2.1355` edge `0.009` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.6836` n `98` status `ready` deltaP `-10.0641` edge `-0.0222` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.866` n `98` status `ready` deltaP `-15.2236` edge `-0.0326` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.2372` n `98` status `ready` deltaP `0.11` edge `-0.0519` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6558` n `98` status `ready` deltaP `-25.9115` edge `-0.011` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7912` n `98` status `ready` deltaP `-18.8138` edge `-0.0096` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.4872` n `98` status `ready` deltaP `-24.8195` edge `-0.1124` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.3448` n `98` status `ready` deltaP `-9.1305` edge `-0.0923` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.9487` n `98` status `ready` deltaP `-16.563` edge `-0.2832` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
