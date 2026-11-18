# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T05:22:27.499796+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4191`

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

- `market_context_high->unknown_24h` score `1453.8078` n `98` status `ready` deltaP `3.4722` edge `121.1275` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.2806` n `98` status `ready` deltaP `45.1495` edge `1.9851` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.0392` n `98` status `ready` deltaP `30.8638` edge `1.8065` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.3582` n `98` status `ready` deltaP `1.1304` edge `0.0067` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.736` n `98` status `ready` deltaP `-0.0374` edge `0.1869` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.7645` n `98` status `ready` deltaP `15.3557` edge `0.1564` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.8695` n `98` status `ready` deltaP `8.7233` edge `0.0001` maxDD `-6.1238`
- `market_context_high->index_1h` score `-0.9834` n `98` status `ready` deltaP `-3.9717` edge `-0.0009` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.1347` n `98` status `ready` deltaP `-1.3595` edge `0.0139` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3304` n `98` status `ready` deltaP `-8.2977` edge `-0.0009` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.4407` n `98` status `ready` deltaP `-3.1452` edge `0.1945` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.2782` n `98` status `ready` deltaP `-1.9858` edge `0.0101` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.6472` n `98` status `ready` deltaP `-9.7592` edge `-0.0212` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9055` n `98` status `ready` deltaP `-15.523` edge `-0.0339` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.2552` n `98` status `ready` deltaP `-0.0397` edge `-0.0524` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6108` n `98` status `ready` deltaP `-25.4542` edge `-0.0103` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.772` n `98` status `ready` deltaP `-18.8138` edge `-0.008` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.6024` n `98` status `ready` deltaP `-25.7342` edge `-0.1159` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.2669` n `98` status `ready` deltaP `-8.2625` edge `-0.0916` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.9693` n `98` status `ready` deltaP `-16.7154` edge `-0.2839` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
