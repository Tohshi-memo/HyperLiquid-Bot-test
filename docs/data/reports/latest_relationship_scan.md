# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T01:37:35.146557+00:00`
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

- `market_context_high->unknown_24h` score `1367.7375` n `98` status `ready` deltaP `5.2083` edge `113.9434` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.3101` n `98` status `ready` deltaP `39.594` edge `1.7695` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.3394` n `98` status `ready` deltaP `24.4402` edge `1.5032` maxDD `-13.3222`
- `market_context_high->metal_24h` score `-0.2857` n `98` status `ready` deltaP `15.3557` edge `0.1963` maxDD `-15.7982`
- `market_context_high->metal_1h` score `-0.3816` n `98` status `ready` deltaP `0.6813` edge `0.0067` maxDD `-2.1461`
- `market_context_high->metal_4h` score `-0.6284` n `98` status `ready` deltaP `11.4672` edge `0.0019` maxDD `-6.1238`
- `market_context_high->crypto_alt_4h` score `-0.8246` n `98` status `ready` deltaP `0.42` edge `0.1725` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.9694` n `98` status `ready` deltaP `-3.6723` edge `-0.0011` maxDD `-1.2295`
- `market_context_high->crypto_major_4h` score `-1.1064` n `98` status `ready` deltaP `-2.5355` edge `0.2333` maxDD `-22.3259`
- `market_context_high->crypto_alt_1h` score `-1.2461` n `98` status `ready` deltaP `-2.2577` edge `0.0056` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.4418` n `98` status `ready` deltaP `-9.645` edge `-0.0012` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-2.023` n `98` status `ready` deltaP `-0.0397` edge `0.0184` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.607` n `98` status `ready` deltaP `-9.3019` edge `-0.0209` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9307` n `98` status `ready` deltaP `-15.8224` edge `-0.034` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.2138` n `98` status `ready` deltaP `-0.1894` edge `-0.0488` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.624` n `98` status `ready` deltaP `-25.4542` edge `-0.0114` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7456` n `98` status `ready` deltaP `-18.8138` edge `-0.0058` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.4834` n `98` status `ready` deltaP `-24.6671` edge `-0.1131` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.0158` n `98` status `ready` deltaP `-15.5541` edge `-0.1054` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.4059` n `98` status `ready` deltaP `-15.191` edge `-0.2505` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
