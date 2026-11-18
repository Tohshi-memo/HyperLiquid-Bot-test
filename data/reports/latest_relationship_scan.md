# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T03:37:25.009556+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4173`

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

- `market_context_high->unknown_24h` score `1484.7186` n `98` status `ready` deltaP `3.4722` edge `123.7034` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.3174` n `98` status `ready` deltaP `45.4967` edge `1.9875` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.1437` n `98` status `ready` deltaP `30.8638` edge `1.8199` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.387` n `98` status `ready` deltaP `0.6813` edge `0.006` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.7597` n `98` status `ready` deltaP `-0.3422` edge `0.1859` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.8317` n `98` status `ready` deltaP `15.3557` edge `0.1508` maxDD `-15.7982`
- `market_context_high->index_1h` score `-1.0091` n `98` status `ready` deltaP `-4.4208` edge `-0.0012` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-1.0401` n `98` status `ready` deltaP `7.6562` edge `-0.007` maxDD `-6.1238`
- `market_context_high->crypto_alt_1h` score `-1.1767` n `98` status `ready` deltaP `-1.6589` edge `0.0105` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3185` n `98` status `ready` deltaP `-8.148` edge `-0.0009` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.494` n `98` status `ready` deltaP `-3.4501` edge `0.1897` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.2998` n `98` status `ready` deltaP `-2.1355` edge `0.0093` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.7626` n `98` status `ready` deltaP `-10.8263` edge `-0.0237` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9618` n `98` status `ready` deltaP `-16.1218` edge `-0.0346` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.3151` n `98` status `ready` deltaP `-0.3391` edge `-0.0554` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6084` n `98` status `ready` deltaP `-25.4542` edge `-0.0101` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7588` n `98` status `ready` deltaP `-18.8138` edge `-0.0069` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.6859` n `98` status `ready` deltaP `-26.3439` edge `-0.1188` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.3616` n `98` status `ready` deltaP `-9.1305` edge `-0.0937` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-13.3295` n `98` status `ready` deltaP `-17.7825` edge `-0.3068` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
