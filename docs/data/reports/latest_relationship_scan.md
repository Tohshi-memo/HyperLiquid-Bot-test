# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T11:37:30.953662+00:00`
- Price records: `672`
- Market context records: `8298`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5892`

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

- `news_risk_high->unknown_24h` score `5951.2051` n `54` status `ready` deltaP `35.3009` edge `495.7405` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.7987` n `54` status `ready` deltaP `25.1637` edge `0.4585` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9431` n `54` status `ready` deltaP `21.2298` edge `0.1346` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5478` n `54` status `ready` deltaP `21.5052` edge `0.088` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9888` n `54` status `ready` deltaP `9.4117` edge `0.2616` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.9106` n `54` status `ready` deltaP `15.0033` edge `0.1026` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.5874` n `54` status `ready` deltaP `10.7563` edge `0.1003` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.5752` n `54` status `ready` deltaP `17.6886` edge `0.2232` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.1388` n `54` status `ready` deltaP `10.3489` edge `0.0727` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.3573` n `54` status `ready` deltaP `5.855` edge `0.0196` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.144` n `54` status `ready` deltaP `6.548` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0521` n `54` status `ready` deltaP `3.554` edge `0.0123` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4967` n `54` status `ready` deltaP `3.8505` edge `0.0064` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1468` n `54` status `ready` deltaP `-8.8102` edge `-0.0416` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0428` n `54` status `ready` deltaP `-20.544` edge `-0.0489` maxDD `-5.4165`
- `news_risk_high->metal_24h` score `-5.8043` n `54` status `ready` deltaP `-21.8172` edge `-0.0612` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.7942` n `54` status `ready` deltaP `-30.8096` edge `-0.1967` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-10.871` n `54` status `ready` deltaP `-5.9606` edge `-0.2722` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-11.9361` n `54` status `ready` deltaP `-23.206` edge `-0.2897` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-32.1314` n `54` status `ready` deltaP `-12.5579` edge `-1.1414` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
