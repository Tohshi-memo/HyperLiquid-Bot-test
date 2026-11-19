# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T03:07:25.009009+00:00`
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

- `market_context_high->unknown_24h` score `1365.8091` n `98` status `ready` deltaP `5.2083` edge `113.7827` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.3015` n `98` status `ready` deltaP `39.594` edge `1.7684` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.3137` n `98` status `ready` deltaP `24.4402` edge `1.4999` maxDD `-13.3222`
- `market_context_high->metal_24h` score `-0.2689` n `98` status `ready` deltaP `15.3557` edge `0.1977` maxDD `-15.7982`
- `market_context_high->metal_1h` score `-0.3551` n `98` status `ready` deltaP `0.9807` edge `0.0081` maxDD `-2.1461`
- `market_context_high->metal_4h` score `-0.6904` n `98` status `ready` deltaP `10.8574` edge `0.0008` maxDD `-6.1238`
- `market_context_high->index_1h` score `-0.9398` n `98` status `ready` deltaP `-3.2232` edge `-0.0003` maxDD `-1.2295`
- `market_context_high->crypto_alt_4h` score `-0.9408` n `98` status `ready` deltaP `-0.4947` edge `0.1637` maxDD `-17.1476`
- `market_context_high->crypto_major_4h` score `-1.1952` n `98` status `ready` deltaP `-3.2977` edge `0.227` maxDD `-22.3259`
- `market_context_high->crypto_alt_1h` score `-1.2297` n `98` status `ready` deltaP `-2.108` edge `0.0067` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.4179` n `98` status `ready` deltaP `-9.3456` edge `-0.0012` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-1.9678` n `98` status `ready` deltaP `0.2597` edge `0.021` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.6812` n `98` status `ready` deltaP `-10.0641` edge `-0.022` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9031` n `98` status `ready` deltaP `-15.523` edge `-0.0337` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.0974` n `98` status `ready` deltaP `0.2597` edge `-0.0421` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.6312` n `98` status `ready` deltaP `-25.4542` edge `-0.012` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7456` n `98` status `ready` deltaP `-18.8138` edge `-0.0058` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.5758` n `98` status `ready` deltaP `-25.5817` edge `-0.1147` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.0086` n `98` status `ready` deltaP `-15.5541` edge `-0.1048` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.6326` n `98` status `ready` deltaP `-16.1057` edge `-0.2633` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
