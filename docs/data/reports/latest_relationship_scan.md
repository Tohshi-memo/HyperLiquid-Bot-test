# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T12:07:29.615916+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2572`

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

- `market_context_high->unknown_1h` score `11994.691` n `108` status `ready` deltaP `0.8373` edge `999.5718` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `7441.6824` n `108` status `ready` deltaP `0.0621` edge `620.1682` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `14.4503` n `94` status `ready` deltaP `42.2429` edge `1.7326` maxDD `-10.9297`
- `market_context_high->crypto_alt_24h` score `11.1966` n `94` status `ready` deltaP `22.8354` edge `1.4412` maxDD `-8.9716`
- `market_context_high->crypto_major_4h` score `0.6278` n `108` status `ready` deltaP `2.1115` edge `0.3483` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `0.2331` n `108` status `ready` deltaP `2.5688` edge `0.2245` maxDD `-12.9396`
- `market_context_high->metal_24h` score `0.0304` n `94` status `ready` deltaP `16.615` edge `0.2006` maxDD `-14.7068`
- `market_context_high->metal_4h` score `-0.0195` n `108` status `ready` deltaP `15.4302` edge `0.0245` maxDD `-5.9858`
- `market_context_high->metal_1h` score `-0.2467` n `108` status `ready` deltaP `3.2934` edge `0.0129` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.7012` n `108` status `ready` deltaP `2.5449` edge `0.0668` maxDD `-9.2267`
- `market_context_high->index_1h` score `-0.7077` n `108` status `ready` deltaP `-1.1588` edge `0.0032` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.0352` n `108` status `ready` deltaP `-2.8332` edge `0.0272` maxDD `-6.9489`
- `market_context_high->index_4h` score `-1.2086` n `108` status `ready` deltaP `-2.9415` edge `-0.001` maxDD `-4.7471`
- `market_context_high->fx_1h` score `-1.5578` n `108` status `ready` deltaP `-11.0723` edge `-0.0011` maxDD `-0.392`
- `market_context_high->fx_4h` score `-2.4439` n `108` status `ready` deltaP `-15.7125` edge `-0.0045` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-2.5265` n `108` status `ready` deltaP `-11.1943` edge `-0.0281` maxDD `-3.9584`
- `market_context_high->equity_1h` score `-2.5344` n `108` status `ready` deltaP `1.4693` edge `-0.0173` maxDD `-10.9626`
- `market_context_high->fx_24h` score `-6.8462` n `94` status `ready` deltaP `-20.246` edge `-0.0064` maxDD `-5.6645`
- `market_context_high->commodity_4h` score `-7.742` n `108` status `ready` deltaP `-26.1574` edge `-0.1089` maxDD `-14.9509`
- `market_context_high->index_24h` score `-9.4114` n `94` status `ready` deltaP `-17.9632` edge `-0.1223` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
