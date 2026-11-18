# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T12:22:27.018493+00:00`
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

- `market_context_high->unknown_24h` score `1365.9144` n `98` status `ready` deltaP `2.4306` edge `113.81` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `14.4698` n `98` status `ready` deltaP `40.462` edge `1.9124` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.9976` n `98` status `ready` deltaP `26.5235` edge `1.7019` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2383` n `98` status `ready` deltaP `2.9268` edge `0.0101` maxDD `-2.1461`
- `market_context_high->metal_4h` score `-0.4778` n `98` status `ready` deltaP `11.9245` edge `0.0114` maxDD `-6.1238`
- `market_context_high->metal_24h` score `-0.5701` n `98` status `ready` deltaP `15.3557` edge `0.1726` maxDD `-15.7982`
- `market_context_high->crypto_alt_4h` score `-0.863` n `98` status `ready` deltaP `-0.7996` edge `0.1757` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.9686` n `98` status `ready` deltaP `-3.6723` edge `-0.001` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2578` n `98` status `ready` deltaP `-2.7068` edge `0.0071` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3556` n `98` status `ready` deltaP `-8.5971` edge `-0.001` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.4771` n `98` status `ready` deltaP `-3.755` edge `0.1939` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.2063` n `98` status `ready` deltaP `-1.387` edge `0.0121` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.7394` n `98` status `ready` deltaP `-10.5214` edge `-0.0238` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9187` n `98` status `ready` deltaP `-15.8224` edge `-0.033` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.1737` n `98` status `ready` deltaP `0.4094` edge `-0.0486` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.5816` n `98` status `ready` deltaP `-25.1493` edge `-0.0099` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7876` n `98` status `ready` deltaP `-18.8138` edge `-0.0093` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.252` n `98` status `ready` deltaP `-22.9902` edge `-0.105` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.6402` n `98` status `ready` deltaP `-11.9083` edge `-0.0984` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.8737` n `98` status `ready` deltaP `-16.1057` edge `-0.28` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
