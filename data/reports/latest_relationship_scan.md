# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T23:07:26.142822+00:00`
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

- `market_context_high->unknown_24h` score `1490.9778` n `98` status `ready` deltaP `3.4722` edge `124.225` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.6248` n `98` status `ready` deltaP `47.0592` edge `2.0165` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.6909` n `98` status `ready` deltaP `33.1208` edge `1.875` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.5109` n `98` status `ready` deltaP `-0.9654` edge `0.0011` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.7931` n `98` status `ready` deltaP `-1.1044` edge `0.1867` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.8915` n `98` status `ready` deltaP `15.7029` edge `0.1435` maxDD `-15.7982`
- `market_context_high->index_1h` score `-1.0722` n `98` status `ready` deltaP `-5.319` edge `-0.0033` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2609` n `98` status `ready` deltaP `-2.5571` edge `0.0057` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3448` n `98` status `ready` deltaP `-8.4474` edge `-0.0011` maxDD `-0.3721`
- `market_context_high->metal_4h` score `-1.3702` n `98` status `ready` deltaP `5.6745` edge `-0.0213` maxDD `-6.1238`
- `market_context_high->crypto_major_4h` score `-1.4038` n `98` status `ready` deltaP `-3.755` edge `0.2033` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.319` n `98` status `ready` deltaP `-2.4349` edge `0.0097` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.9191` n `98` status `ready` deltaP `-12.1982` edge `-0.0276` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9882` n `98` status `ready` deltaP `-16.2715` edge `-0.0358` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.5946` n `98` status `ready` deltaP `-1.5367` edge `-0.0707` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6132` n `98` status `ready` deltaP `-25.4542` edge `-0.0105` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.6823` n `98` status `ready` deltaP `-18.293` edge `-0.004` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.8111` n `98` status `ready` deltaP `-27.5634` edge `-0.1211` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.6144` n `98` status `ready` deltaP `-10.8666` edge `-0.1032` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-13.6176` n `98` status `ready` deltaP `-18.8496` edge `-0.3237` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
