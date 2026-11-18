# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T19:22:26.700649+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2298`

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

- `market_context_high->unknown_24h` score `1366.1478` n `98` status `ready` deltaP `3.4722` edge `113.8225` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.6026` n `98` status `ready` deltaP `39.594` edge `1.807` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.7213` n `98` status `ready` deltaP `24.6138` edge `1.551` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.306` n `98` status `ready` deltaP `1.8789` edge `0.0084` maxDD `-2.1461`
- `market_context_high->metal_24h` score `-0.4609` n `98` status `ready` deltaP `15.3557` edge `0.1817` maxDD `-15.7982`
- `market_context_high->crypto_alt_4h` score `-0.4967` n `98` status `ready` deltaP `1.6395` edge `0.2064` maxDD `-17.1476`
- `market_context_high->metal_4h` score `-0.5474` n `98` status `ready` deltaP `11.9245` edge `0.0056` maxDD `-6.1238`
- `market_context_high->crypto_major_4h` score `-0.8565` n `98` status `ready` deltaP `-1.316` edge `0.2572` maxDD `-22.3259`
- `market_context_high->index_1h` score `-0.869` n `98` status `ready` deltaP `-2.0256` edge `0.0008` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.1229` n `98` status `ready` deltaP `-1.5092` edge `0.0164` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3795` n `98` status `ready` deltaP `-8.8965` edge `-0.001` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-1.9234` n `98` status `ready` deltaP `0.11` edge `0.0257` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.4239` n `98` status `ready` deltaP `-7.7775` edge `-0.0158` maxDD `-4.7471`
- `market_context_high->equity_1h` score `-2.7941` n `98` status `ready` deltaP `1.9064` edge `-0.0278` maxDD `-11.0868`
- `market_context_high->commodity_1h` score `-2.8863` n `98` status `ready` deltaP `-15.523` edge `-0.0323` maxDD `-3.7125`
- `market_context_high->fx_4h` score `-4.4549` n `98` status `ready` deltaP `-23.6249` edge `-0.0095` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7564` n `98` status `ready` deltaP `-18.8138` edge `-0.0067` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.2748` n `98` status `ready` deltaP `-22.9902` edge `-0.1069` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.9761` n `98` status `ready` deltaP `-15.2069` edge `-0.1044` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-11.6633` n `98` status `ready` deltaP `-13.5142` edge `-0.1998` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
