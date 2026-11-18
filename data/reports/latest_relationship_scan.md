# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T05:37:30.176148+00:00`
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

- `market_context_high->unknown_24h` score `1443.5526` n `98` status `ready` deltaP `3.4722` edge `120.2729` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.2591` n `98` status `ready` deltaP `44.9759` edge `1.9835` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.0158` n `98` status `ready` deltaP `30.8638` edge `1.8035` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.359` n `98` status `ready` deltaP `1.1304` edge `0.0066` maxDD `-2.1461`
- `market_context_high->metal_24h` score `-0.7537` n `98` status `ready` deltaP `15.3557` edge `0.1573` maxDD `-15.7982`
- `market_context_high->crypto_alt_4h` score `-0.7564` n `98` status `ready` deltaP `-0.1898` edge `0.1853` maxDD `-17.1476`
- `market_context_high->metal_4h` score `-0.8477` n `98` status `ready` deltaP `8.8757` edge `0.0009` maxDD `-6.1238`
- `market_context_high->index_1h` score `-0.9834` n `98` status `ready` deltaP `-3.9717` edge `-0.0009` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.1471` n `98` status `ready` deltaP `-1.5092` edge `0.0133` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3304` n `98` status `ready` deltaP `-8.2977` edge `-0.0009` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.458` n `98` status `ready` deltaP `-3.2977` edge `0.1933` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.2998` n `98` status `ready` deltaP `-2.1355` edge `0.0093` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.6472` n `98` status `ready` deltaP `-9.7592` edge `-0.0212` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9055` n `98` status `ready` deltaP `-15.523` edge `-0.0339` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.2564` n `98` status `ready` deltaP `-0.0397` edge `-0.0525` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.612` n `98` status `ready` deltaP `-25.4542` edge `-0.0104` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7744` n `98` status `ready` deltaP `-18.8138` edge `-0.0082` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.5878` n `98` status `ready` deltaP `-25.5817` edge `-0.1157` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.2657` n `98` status `ready` deltaP `-8.2625` edge `-0.0915` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.9475` n `98` status `ready` deltaP `-16.563` edge `-0.2831` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
