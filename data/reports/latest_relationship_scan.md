# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T06:52:34.362086+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4221`

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

- `market_context_high->unknown_24h` score `1391.9944` n `98` status `ready` deltaP `3.125` edge `115.9787` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.1399` n `98` status `ready` deltaP `44.1079` edge `1.974` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `13.8178` n `98` status `ready` deltaP `29.9958` edge `1.7839` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.3255` n `98` status `ready` deltaP `1.5795` edge `0.0079` maxDD `-2.1461`
- `market_context_high->metal_24h` score `-0.7093` n `98` status `ready` deltaP `15.3557` edge `0.161` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.7555` n `98` status `ready` deltaP `9.6379` edge `0.0035` maxDD `-6.1238`
- `market_context_high->crypto_alt_4h` score `-0.8624` n `98` status `ready` deltaP `-0.952` edge `0.1768` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.9756` n `98` status `ready` deltaP `-3.822` edge `-0.0009` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2141` n `98` status `ready` deltaP `-2.108` edge `0.0087` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3819` n `98` status `ready` deltaP `-8.8965` edge `-0.0012` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.5209` n `98` status `ready` deltaP `-3.9074` edge `0.1893` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.2878` n `98` status `ready` deltaP `-1.9858` edge `0.0093` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.6544` n `98` status `ready` deltaP `-9.7592` edge `-0.0218` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9007` n `98` status `ready` deltaP `-15.523` edge `-0.0335` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.2396` n `98` status `ready` deltaP `0.11` edge `-0.0521` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6546` n `98` status `ready` deltaP `-25.9115` edge `-0.0109` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7876` n `98` status `ready` deltaP `-18.8138` edge `-0.0093` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.532` n `98` status `ready` deltaP `-25.1244` edge `-0.1141` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.3122` n `98` status `ready` deltaP `-8.7833` edge `-0.0919` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.9391` n `98` status `ready` deltaP `-16.563` edge `-0.2824` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
