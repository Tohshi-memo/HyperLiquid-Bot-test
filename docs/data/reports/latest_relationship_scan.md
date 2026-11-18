# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T14:22:30.571288+00:00`
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

- `market_context_high->unknown_24h` score `1363.6696` n `98` status `ready` deltaP `1.9097` edge `113.6264` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `14.3567` n `98` status `ready` deltaP `40.462` edge `1.8979` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.794` n `98` status `ready` deltaP `26.5235` edge `1.6758` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.25` n `98` status `ready` deltaP `2.7771` edge `0.0096` maxDD `-2.1461`
- `market_context_high->metal_4h` score `-0.5114` n `98` status `ready` deltaP `11.9245` edge `0.0086` maxDD `-6.1238`
- `market_context_high->metal_24h` score `-0.5413` n `98` status `ready` deltaP `15.3557` edge `0.175` maxDD `-15.7982`
- `market_context_high->crypto_alt_4h` score `-0.7216` n `98` status `ready` deltaP `0.42` edge `0.1857` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.9429` n `98` status `ready` deltaP `-3.2232` edge `-0.0007` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2056` n `98` status `ready` deltaP `-1.9583` edge `0.0088` maxDD `-7.6911`
- `market_context_high->crypto_major_4h` score `-1.3166` n `98` status `ready` deltaP `-2.9928` edge `0.2094` maxDD `-22.3259`
- `market_context_high->fx_1h` score `-1.37` n `98` status `ready` deltaP `-8.7468` edge `-0.0012` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-2.156` n `98` status `ready` deltaP `-0.9379` edge `0.0133` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.6434` n `98` status `ready` deltaP `-9.6068` edge `-0.0219` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9115` n `98` status `ready` deltaP `-15.6727` edge `-0.0334` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.1101` n `98` status `ready` deltaP `0.7088` edge `-0.0453` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6108` n `98` status `ready` deltaP `-25.4542` edge `-0.0103` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7864` n `98` status `ready` deltaP `-18.8138` edge `-0.0092` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.2556` n `98` status `ready` deltaP `-22.9902` edge `-0.1053` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.6752` n `98` status `ready` deltaP `-12.2555` edge `-0.099` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.5556` n `98` status `ready` deltaP `-15.0386` edge `-0.2606` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
