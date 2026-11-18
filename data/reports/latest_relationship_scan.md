# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T18:37:27.891008+00:00`
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

- `market_context_high->unknown_24h` score `1365.94` n `98` status `ready` deltaP `3.125` edge `113.8075` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.7559` n `98` status `ready` deltaP `39.7676` edge `1.8255` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.934` n `98` status `ready` deltaP `25.1347` edge `1.5748` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2943` n `98` status `ready` deltaP `2.0286` edge `0.0089` maxDD `-2.1461`
- `market_context_high->metal_24h` score `-0.4753` n `98` status `ready` deltaP `15.3557` edge `0.1805` maxDD `-15.7982`
- `market_context_high->crypto_alt_4h` score `-0.4757` n `98` status `ready` deltaP `1.6395` edge `0.2091` maxDD `-17.1476`
- `market_context_high->metal_4h` score `-0.5402` n `98` status `ready` deltaP `11.9245` edge `0.0062` maxDD `-6.1238`
- `market_context_high->crypto_major_4h` score `-0.8565` n `98` status `ready` deltaP `-1.316` edge `0.2572` maxDD `-22.3259`
- `market_context_high->index_1h` score `-0.8697` n `98` status `ready` deltaP `-2.0256` edge `0.0007` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.0777` n `98` status `ready` deltaP `-1.0601` edge `0.0192` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3688` n `98` status `ready` deltaP `-8.7468` edge `-0.0011` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-1.9174` n `98` status `ready` deltaP `0.11` edge `0.0262` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.4081` n `98` status `ready` deltaP `-7.6251` edge `-0.0155` maxDD `-4.7471`
- `market_context_high->equity_1h` score `-2.7977` n `98` status `ready` deltaP `1.9064` edge `-0.0281` maxDD `-11.0868`
- `market_context_high->commodity_1h` score `-2.836` n `98` status `ready` deltaP `-15.0739` edge `-0.0311` maxDD `-3.7125`
- `market_context_high->fx_4h` score `-4.4805` n `98` status `ready` deltaP `-23.9298` edge `-0.0096` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.76` n `98` status `ready` deltaP `-18.8138` edge `-0.007` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.2251` n `98` status `ready` deltaP `-22.5329` edge `-0.1058` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.9212` n `98` status `ready` deltaP `-14.6861` edge `-0.1033` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-11.6151` n `98` status `ready` deltaP `-13.3618` edge `-0.1968` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
