# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T08:07:44.063080+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4227`

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

- `market_context_high->unknown_24h` score `1368.1233` n `98` status `ready` deltaP `2.9514` edge `113.9906` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `14.9855` n `98` status `ready` deltaP `43.2398` edge `1.96` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `13.6291` n `98` status `ready` deltaP `29.1277` edge `1.7655` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2943` n `98` status `ready` deltaP `2.0286` edge `0.0089` maxDD `-2.1461`
- `market_context_high->metal_4h` score `-0.6682` n `98` status `ready` deltaP `10.4001` edge `0.0057` maxDD `-6.1238`
- `market_context_high->metal_24h` score `-0.6709` n `98` status `ready` deltaP `15.3557` edge `0.1642` maxDD `-15.7982`
- `market_context_high->crypto_alt_4h` score `-0.9368` n `98` status `ready` deltaP `-1.4093` edge `0.1703` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.9842` n `98` status `ready` deltaP `-3.9717` edge `-0.001` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2796` n `98` status `ready` deltaP `-2.7068` edge `0.0043` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3676` n `98` status `ready` deltaP `-8.7468` edge `-0.001` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.5932` n `98` status `ready` deltaP `-4.5172` edge `0.1841` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.3682` n `98` status `ready` deltaP `-2.4349` edge `0.0056` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.725` n `98` status `ready` deltaP `-10.5214` edge `-0.0226` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.8827` n `98` status `ready` deltaP `-15.3733` edge `-0.033` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.2947` n `98` status `ready` deltaP `-0.3391` edge `-0.0537` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6558` n `98` status `ready` deltaP `-25.9115` edge `-0.011` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7948` n `98` status `ready` deltaP `-18.8138` edge `-0.0099` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.429` n `98` status `ready` deltaP `-24.3622` edge `-0.1106` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.3948` n `98` status `ready` deltaP `-9.6514` edge `-0.093` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.9631` n `98` status `ready` deltaP `-16.563` edge `-0.2844` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
