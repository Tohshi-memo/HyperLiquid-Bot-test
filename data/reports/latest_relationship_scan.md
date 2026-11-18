# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T13:22:35.005321+00:00`
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

- `market_context_high->unknown_24h` score `1365.4091` n `98` status `ready` deltaP `2.0833` edge `113.7702` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `14.4316` n `98` status `ready` deltaP `40.462` edge `1.9075` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.9243` n `98` status `ready` deltaP `26.5235` edge `1.6925` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2367` n `98` status `ready` deltaP `2.9268` edge `0.0103` maxDD `-2.1461`
- `market_context_high->metal_4h` score `-0.4934` n `98` status `ready` deltaP `11.9245` edge `0.0101` maxDD `-6.1238`
- `market_context_high->metal_24h` score `-0.5473` n `98` status `ready` deltaP `15.3557` edge `0.1745` maxDD `-15.7982`
- `market_context_high->crypto_alt_4h` score `-0.7993` n `98` status `ready` deltaP `-0.1898` edge `0.1798` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.9344` n `98` status `ready` deltaP `-3.0735` edge `-0.0006` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2126` n `98` status `ready` deltaP `-2.108` edge `0.0089` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3568` n `98` status `ready` deltaP `-8.5971` edge `-0.0011` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.4271` n `98` status `ready` deltaP `-3.6025` edge `0.1993` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.1991` n `98` status `ready` deltaP `-1.387` edge `0.0127` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.7078` n `98` status `ready` deltaP `-10.2165` edge `-0.0232` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9235` n `98` status `ready` deltaP `-15.8224` edge `-0.0334` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.0909` n `98` status `ready` deltaP `0.8585` edge `-0.0447` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.623` n `98` status `ready` deltaP `-25.6067` edge `-0.0103` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7864` n `98` status `ready` deltaP `-18.8138` edge `-0.0092` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.252` n `98` status `ready` deltaP `-22.9902` edge `-0.105` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.6402` n `98` status `ready` deltaP `-11.9083` edge `-0.0984` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.7591` n `98` status `ready` deltaP `-15.6483` edge `-0.2735` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
