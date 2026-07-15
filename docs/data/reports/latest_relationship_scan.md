# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T19:59:33.067585+00:00`
- Price records: `672`
- Market context records: `6849`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `1.0605` n `176` status `ready` deltaP `-1.5467` edge `0.5215` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2523` n `223` status `ready` deltaP `2.169` edge `0.0017` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.3055` n `176` status `ready` deltaP `7.4495` edge `0.1117` maxDD `-5.2791`
- `market_context_high->crypto_alt_1h` score `-0.6144` n `223` status `ready` deltaP `1.7125` edge `0.0138` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.6454` n `223` status `ready` deltaP `3.6559` edge `0.012` maxDD `-4.2122`
- `market_context_high->commodity_1h` score `-0.6626` n `223` status `ready` deltaP `-1.8716` edge `-0.004` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.8912` n `223` status `ready` deltaP `-2.9148` edge `-0.0037` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.9807` n `223` status `ready` deltaP `-5.9014` edge `-0.0096` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-1.0136` n `213` status `ready` deltaP `10.5941` edge `0.0058` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4975` n `213` status `ready` deltaP `-4.186` edge `-0.0151` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6825` n `223` status `ready` deltaP `-3.2109` edge `-0.0287` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-2.0033` n `223` status `ready` deltaP `-0.527` edge `-0.0353` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.141` n `213` status `ready` deltaP `1.9173` edge `-0.0293` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.5708` n `213` status `ready` deltaP `-1.8256` edge `-0.0191` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.041` n `213` status `ready` deltaP `-0.5339` edge `-0.0536` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.2006` n `213` status `ready` deltaP `-0.7472` edge `-0.047` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.2067` n `213` status `ready` deltaP `-9.3253` edge `0.0315` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4888` n `176` status `ready` deltaP `-9.7853` edge `-0.0052` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.8484` n `213` status `ready` deltaP `-1.1129` edge `-0.2043` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-9.1373` n `176` status `ready` deltaP `-18.8447` edge `-0.1973` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
