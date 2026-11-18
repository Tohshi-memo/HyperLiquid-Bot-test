# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T22:22:36.989171+00:00`
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

- `market_context_high->unknown_24h` score `1370.3403` n `98` status `ready` deltaP `5.2083` edge `114.1603` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.2999` n `98` status `ready` deltaP `39.594` edge `1.7682` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.3441` n `98` status `ready` deltaP `24.4402` edge `1.5038` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.3481` n `98` status `ready` deltaP `1.1304` edge `0.008` maxDD `-2.1461`
- `market_context_high->metal_24h` score `-0.3673` n `98` status `ready` deltaP `15.3557` edge `0.1895` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.5898` n `98` status `ready` deltaP `11.6196` edge `0.0041` maxDD `-6.1238`
- `market_context_high->crypto_alt_4h` score `-0.6891` n `98` status `ready` deltaP `1.0297` edge `0.1858` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.911` n `98` status `ready` deltaP `-2.7741` edge `0.0004` maxDD `-1.2295`
- `market_context_high->crypto_major_4h` score `-0.9848` n `98` status `ready` deltaP `-1.7733` edge `0.2438` maxDD `-22.3259`
- `market_context_high->crypto_alt_1h` score `-1.1284` n `98` status `ready` deltaP `-1.5092` edge `0.0157` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3795` n `98` status `ready` deltaP `-8.8965` edge `-0.001` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-1.8586` n `98` status `ready` deltaP `0.5591` edge `0.0281` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.5306` n `98` status `ready` deltaP `-8.6921` edge `-0.0186` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.8875` n `98` status `ready` deltaP `-15.3733` edge `-0.0334` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-2.908` n `98` status `ready` deltaP `1.1579` edge `-0.0323` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.5486` n `98` status `ready` deltaP `-24.692` edge `-0.0102` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7516` n `98` status `ready` deltaP `-18.8138` edge `-0.0063` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.4518` n `98` status `ready` deltaP `-24.3622` edge `-0.1125` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.099` n `98` status `ready` deltaP `-16.2486` edge `-0.1077` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.0831` n `98` status `ready` deltaP `-14.2764` edge `-0.2297` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
