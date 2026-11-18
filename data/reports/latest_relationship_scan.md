# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T19:52:32.423499+00:00`
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

- `market_context_high->unknown_24h` score `1367.0168` n `98` status `ready` deltaP `3.8194` edge `113.8926` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.5269` n `98` status `ready` deltaP `39.594` edge `1.7973` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.6195` n `98` status `ready` deltaP `24.4402` edge `1.5391` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.3045` n `98` status `ready` deltaP `1.8789` edge `0.0086` maxDD `-2.1461`
- `market_context_high->metal_24h` score `-0.4453` n `98` status `ready` deltaP `15.3557` edge `0.183` maxDD `-15.7982`
- `market_context_high->crypto_alt_4h` score `-0.5115` n `98` status `ready` deltaP `1.6395` edge `0.2045` maxDD `-17.1476`
- `market_context_high->metal_4h` score `-0.5486` n `98` status `ready` deltaP `11.9245` edge `0.0055` maxDD `-6.1238`
- `market_context_high->index_1h` score `-0.8518` n `98` status `ready` deltaP `-1.7262` edge `0.001` maxDD `-1.2295`
- `market_context_high->crypto_major_4h` score `-0.862` n `98` status `ready` deltaP `-1.316` edge `0.2565` maxDD `-22.3259`
- `market_context_high->crypto_alt_1h` score `-1.1284` n `98` status `ready` deltaP `-1.5092` edge `0.0157` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3556` n `98` status `ready` deltaP `-8.5971` edge `-0.001` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-1.915` n `98` status `ready` deltaP `0.11` edge `0.0264` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.4507` n `98` status `ready` deltaP `-8.0824` edge `-0.016` maxDD `-4.7471`
- `market_context_high->equity_1h` score `-2.7809` n `98` status `ready` deltaP `1.9064` edge `-0.0267` maxDD `-11.0868`
- `market_context_high->commodity_1h` score `-2.9055` n `98` status `ready` deltaP `-15.6727` edge `-0.0329` maxDD `-3.7125`
- `market_context_high->fx_4h` score `-4.4549` n `98` status `ready` deltaP `-23.6249` edge `-0.0095` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7552` n `98` status `ready` deltaP `-18.8138` edge `-0.0066` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.3112` n `98` status `ready` deltaP `-23.2951` edge `-0.1079` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.0122` n `98` status `ready` deltaP `-15.5541` edge `-0.1051` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-11.7091` n `98` status `ready` deltaP `-13.6666` edge `-0.2026` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
