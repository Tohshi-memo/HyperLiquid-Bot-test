# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T23:07:29.745840+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2262`

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

- `market_context_high->unknown_24h` score `1370.2275` n `98` status `ready` deltaP `5.2083` edge `114.1509` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.2859` n `98` status `ready` deltaP `39.594` edge `1.7664` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.3363` n `98` status `ready` deltaP `24.4402` edge `1.5028` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.3325` n `98` status `ready` deltaP `1.4298` edge `0.008` maxDD `-2.1461`
- `market_context_high->metal_24h` score `-0.3397` n `98` status `ready` deltaP `15.3557` edge `0.1918` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.574` n `98` status `ready` deltaP `11.7721` edge `0.0044` maxDD `-6.1238`
- `market_context_high->crypto_alt_4h` score `-0.7133` n `98` status `ready` deltaP `1.0297` edge `0.1827` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.9219` n `98` status `ready` deltaP `-2.9238` edge `0.0` maxDD `-1.2295`
- `market_context_high->crypto_major_4h` score `-1.0012` n `98` status `ready` deltaP `-1.7733` edge `0.2417` maxDD `-22.3259`
- `market_context_high->crypto_alt_1h` score `-1.1448` n `98` status `ready` deltaP `-1.6589` edge `0.0146` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.4047` n `98` status `ready` deltaP `-9.1959` edge `-0.0011` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-1.897` n `98` status `ready` deltaP `0.4094` edge `0.0259` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.5488` n `98` status `ready` deltaP `-8.8446` edge `-0.0191` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.8732` n `98` status `ready` deltaP `-15.2236` edge `-0.0332` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-2.9692` n `98` status `ready` deltaP `1.0082` edge `-0.0364` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.562` n `98` status `ready` deltaP `-24.8445` edge `-0.0103` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.748` n `98` status `ready` deltaP `-18.8138` edge `-0.006` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.4846` n `98` status `ready` deltaP `-24.6671` edge `-0.1132` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.093` n `98` status `ready` deltaP `-16.2486` edge `-0.1072` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.1565` n `98` status `ready` deltaP `-14.4288` edge `-0.2348` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
