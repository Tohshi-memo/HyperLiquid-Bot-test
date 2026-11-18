# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T15:52:32.496270+00:00`
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

- `market_context_high->unknown_24h` score `1365.1326` n `98` status `ready` deltaP `2.2569` edge `113.746` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `14.201` n `98` status `ready` deltaP `40.2884` edge `1.8791` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.544` n `98` status `ready` deltaP `26.3499` edge `1.6449` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2492` n `98` status `ready` deltaP `2.7771` edge `0.0097` maxDD `-2.1461`
- `market_context_high->metal_24h` score `-0.5197` n `98` status `ready` deltaP `15.3557` edge `0.1768` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.533` n `98` status `ready` deltaP `11.9245` edge `0.0068` maxDD `-6.1238`
- `market_context_high->crypto_alt_4h` score `-0.5812` n `98` status `ready` deltaP `1.3346` edge `0.1976` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.9328` n `98` status `ready` deltaP `-3.0735` edge `-0.0004` maxDD `-1.2295`
- `market_context_high->crypto_major_4h` score `-1.1161` n `98` status `ready` deltaP `-2.0782` edge `0.229` maxDD `-22.3259`
- `market_context_high->crypto_alt_1h` score `-1.1487` n `98` status `ready` deltaP `-1.5092` edge `0.0131` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.37` n `98` status `ready` deltaP `-8.7468` edge `-0.0012` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-2.0625` n `98` status `ready` deltaP `-0.4888` edge `0.0181` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.533` n `98` status `ready` deltaP `-8.6921` edge `-0.0188` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.8504` n `98` status `ready` deltaP `-15.2236` edge `-0.0313` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.0183` n `98` status `ready` deltaP `0.8585` edge `-0.0395` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.573` n `98` status `ready` deltaP `-24.9969` edge `-0.0102` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7792` n `98` status `ready` deltaP `-18.8138` edge `-0.0086` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.2143` n `98` status `ready` deltaP `-22.5329` edge `-0.1049` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.7499` n `98` status `ready` deltaP `-12.95` edge `-0.1006` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.0301` n `98` status `ready` deltaP `-14.1239` edge `-0.2263` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
