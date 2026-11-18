# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T08:52:33.806352+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3939`

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

- `market_context_high->unknown_24h` score `1367.6491` n `98` status `ready` deltaP `2.6042` edge `113.9534` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `14.8906` n `98` status `ready` deltaP `42.719` edge `1.9513` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `13.5272` n `98` status `ready` deltaP `28.6069` edge `1.7559` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2725` n `98` status `ready` deltaP `2.328` edge `0.0097` maxDD `-2.1461`
- `market_context_high->metal_4h` score `-0.6076` n `98` status `ready` deltaP `10.8574` edge `0.0077` maxDD `-6.1238`
- `market_context_high->metal_24h` score `-0.6421` n `98` status `ready` deltaP `15.3557` edge `0.1666` maxDD `-15.7982`
- `market_context_high->crypto_alt_4h` score `-0.9368` n `98` status `ready` deltaP `-1.4093` edge `0.1703` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.9943` n `98` status `ready` deltaP `-4.1214` edge `-0.0013` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2741` n `98` status `ready` deltaP `-2.7068` edge `0.005` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.328` n `98` status `ready` deltaP `-8.2977` edge `-0.0007` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.5869` n `98` status `ready` deltaP `-4.5172` edge `0.1849` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.3406` n `98` status `ready` deltaP `-2.2852` edge `0.0069` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.7542` n `98` status `ready` deltaP `-10.8263` edge `-0.023` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.8983` n `98` status `ready` deltaP `-15.523` edge `-0.0333` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.3115` n `98` status `ready` deltaP `-0.4888` edge `-0.0541` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6388` n `98` status `ready` deltaP `-25.7591` edge `-0.0106` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7936` n `98` status `ready` deltaP `-18.8138` edge `-0.0098` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.3684` n `98` status `ready` deltaP `-23.9049` edge `-0.1086` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.4485` n `98` status `ready` deltaP `-10.1722` edge `-0.094` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.9583` n `98` status `ready` deltaP `-16.563` edge `-0.284` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
