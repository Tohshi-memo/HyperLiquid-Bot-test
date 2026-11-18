# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T09:07:31.074090+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3867`

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

- `market_context_high->unknown_24h` score `1367.5056` n `98` status `ready` deltaP `2.4306` edge `113.9426` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `14.8543` n `98` status `ready` deltaP `42.5454` edge `1.9478` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `13.4869` n `98` status `ready` deltaP `28.4333` edge `1.7519` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2725` n `98` status `ready` deltaP `2.328` edge `0.0097` maxDD `-2.1461`
- `market_context_high->metal_4h` score `-0.5894` n `98` status `ready` deltaP `11.0099` edge `0.0082` maxDD `-6.1238`
- `market_context_high->metal_24h` score `-0.6361` n `98` status `ready` deltaP `15.3557` edge `0.1671` maxDD `-15.7982`
- `market_context_high->crypto_alt_4h` score `-0.9446` n `98` status `ready` deltaP `-1.4093` edge `0.1693` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.9943` n `98` status `ready` deltaP `-4.1214` edge `-0.0013` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2632` n `98` status `ready` deltaP `-2.5571` edge `0.0054` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.328` n `98` status `ready` deltaP `-8.2977` edge `-0.0007` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.5901` n `98` status `ready` deltaP `-4.5172` edge `0.1845` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.3226` n `98` status `ready` deltaP `-2.1355` edge `0.0074` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.7566` n `98` status `ready` deltaP `-10.8263` edge `-0.0232` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.8851` n `98` status `ready` deltaP `-15.3733` edge `-0.0332` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.3079` n `98` status `ready` deltaP `-0.4888` edge `-0.0538` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6388` n `98` status `ready` deltaP `-25.7591` edge `-0.0106` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7936` n `98` status `ready` deltaP `-18.8138` edge `-0.0098` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.3502` n `98` status `ready` deltaP `-23.7524` edge `-0.1081` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.4684` n `98` status `ready` deltaP `-10.3458` edge `-0.0945` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.9631` n `98` status `ready` deltaP `-16.563` edge `-0.2844` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
