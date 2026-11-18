# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T23:22:27.117040+00:00`
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

- `market_context_high->unknown_24h` score `1371.1371` n `98` status `ready` deltaP `5.2083` edge `114.2267` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.2804` n `98` status `ready` deltaP `39.594` edge `1.7657` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.3324` n `98` status `ready` deltaP `24.4402` edge `1.5023` maxDD `-13.3222`
- `market_context_high->metal_24h` score `-0.3313` n `98` status `ready` deltaP `15.3557` edge `0.1925` maxDD `-15.7982`
- `market_context_high->metal_1h` score `-0.3426` n `98` status `ready` deltaP `1.2801` edge `0.0077` maxDD `-2.1461`
- `market_context_high->metal_4h` score `-0.5764` n `98` status `ready` deltaP `11.7721` edge `0.0042` maxDD `-6.1238`
- `market_context_high->crypto_alt_4h` score `-0.725` n `98` status `ready` deltaP `1.0297` edge `0.1812` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.932` n `98` status `ready` deltaP `-3.0735` edge `-0.0003` maxDD `-1.2295`
- `market_context_high->crypto_major_4h` score `-1.0114` n `98` status `ready` deltaP `-1.7733` edge `0.2404` maxDD `-22.3259`
- `market_context_high->crypto_alt_1h` score `-1.172` n `98` status `ready` deltaP `-1.8086` edge `0.0121` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.4167` n `98` status `ready` deltaP `-9.3456` edge `-0.0011` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-1.939` n `98` status `ready` deltaP `0.2597` edge `0.0234` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.5634` n `98` status `ready` deltaP `-8.997` edge `-0.0193` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.8863` n `98` status `ready` deltaP `-15.3733` edge `-0.0333` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.0207` n `98` status `ready` deltaP `0.8585` edge `-0.0397` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.5754` n `98` status `ready` deltaP `-24.9969` edge `-0.0104` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.748` n `98` status `ready` deltaP `-18.8138` edge `-0.006` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.4858` n `98` status `ready` deltaP `-24.6671` edge `-0.1133` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.0918` n `98` status `ready` deltaP `-16.2486` edge `-0.1071` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.1951` n `98` status `ready` deltaP `-14.5813` edge `-0.237` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
