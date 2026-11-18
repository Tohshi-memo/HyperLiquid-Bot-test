# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T06:22:32.368202+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4215`

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

- `market_context_high->unknown_24h` score `1412.5691` n `98` status `ready` deltaP `3.2986` edge `117.6921` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.193` n `98` status `ready` deltaP `44.4551` edge `1.9785` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `13.8998` n `98` status `ready` deltaP `30.343` edge `1.7921` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.3457` n `98` status `ready` deltaP `1.2801` edge `0.0073` maxDD `-2.1461`
- `market_context_high->metal_24h` score `-0.7261` n `98` status `ready` deltaP `15.3557` edge `0.1596` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.7907` n `98` status `ready` deltaP `9.333` edge `0.0026` maxDD `-6.1238`
- `market_context_high->crypto_alt_4h` score `-0.8176` n `98` status `ready` deltaP `-0.6471` edge `0.1805` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.9834` n `98` status `ready` deltaP `-3.9717` edge `-0.0009` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.1908` n `98` status `ready` deltaP `-1.8086` edge `0.0097` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.37` n `98` status `ready` deltaP `-8.7468` edge `-0.0012` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.4926` n `98` status `ready` deltaP `-3.6025` edge `0.1909` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.3262` n `98` status `ready` deltaP `-2.2852` edge `0.0081` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.652` n `98` status `ready` deltaP `-9.7592` edge `-0.0216` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9331` n `98` status `ready` deltaP `-15.8224` edge `-0.0342` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.2648` n `98` status `ready` deltaP `-0.0397` edge `-0.0532` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6266` n `98` status `ready` deltaP `-25.6067` edge `-0.0106` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7828` n `98` status `ready` deltaP `-18.8138` edge `-0.0089` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.5672` n `98` status `ready` deltaP `-25.4293` edge `-0.115` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.2808` n `98` status `ready` deltaP `-8.4361` edge `-0.0916` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.9391` n `98` status `ready` deltaP `-16.563` edge `-0.2824` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
