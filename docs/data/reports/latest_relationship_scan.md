# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T23:37:32.054024+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4173`

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

- `market_context_high->unknown_24h` score `1490.853` n `98` status `ready` deltaP `3.4722` edge `124.2146` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.6077` n `98` status `ready` deltaP `47.0592` edge `2.0143` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.6558` n `98` status `ready` deltaP `33.1208` edge `1.8705` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.5194` n `98` status `ready` deltaP `-1.1151` edge `0.001` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.8204` n `98` status `ready` deltaP `-1.1044` edge `0.1832` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.9241` n `98` status `ready` deltaP `15.3557` edge `0.1431` maxDD `-15.7982`
- `market_context_high->index_1h` score `-1.0909` n `98` status `ready` deltaP `-5.6184` edge `-0.0037` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2749` n `98` status `ready` deltaP `-2.5571` edge `0.0039` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3568` n `98` status `ready` deltaP `-8.5971` edge `-0.0011` maxDD `-0.3721`
- `market_context_high->metal_4h` score `-1.3618` n `98` status `ready` deltaP `5.6745` edge `-0.0206` maxDD `-6.1238`
- `market_context_high->crypto_major_4h` score `-1.449` n `98` status `ready` deltaP `-3.755` edge `0.1975` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.3825` n `98` status `ready` deltaP `-2.7343` edge `0.0064` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.9227` n `98` status `ready` deltaP `-12.1982` edge `-0.0279` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-3.0145` n `98` status `ready` deltaP `-16.5709` edge `-0.036` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.6653` n `98` status `ready` deltaP `-1.8361` edge `-0.0746` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6144` n `98` status `ready` deltaP `-25.4542` edge `-0.0106` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7185` n `98` status `ready` deltaP `-18.6402` edge `-0.0047` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.8391` n `98` status `ready` deltaP `-27.8683` edge `-0.1214` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.6024` n `98` status `ready` deltaP `-10.8666` edge `-0.1022` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-13.6692` n `98` status `ready` deltaP `-18.8496` edge `-0.328` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
