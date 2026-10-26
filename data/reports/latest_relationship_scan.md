# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T23:37:25.650020+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7985`

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

- `market_context_high->unknown_4h` score `90.4479` n `153` status `ready` deltaP `1.0172` edge `7.5641` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `20.9268` n `153` status `ready` deltaP `1.6242` edge `1.782` maxDD `-1.5807`
- `market_context_high->fx_1h` score `0.277` n `153` status `ready` deltaP `8.4145` edge `0.0028` maxDD `-0.1986`
- `market_context_high->metal_24h` score `0.2311` n `112` status `ready` deltaP `23.5887` edge `0.135` maxDD `-7.0108`
- `market_context_high->fx_4h` score `0.1798` n `153` status `ready` deltaP `9.9344` edge `0.0086` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.0355` n `112` status `ready` deltaP `16.3051` edge `0.0106` maxDD `-4.5747`
- `market_context_high->metal_1h` score `-0.1416` n `153` status `ready` deltaP `8.1807` edge `0.0065` maxDD `-1.6682`
- `market_context_high->fx_24h` score `-0.1477` n `112` status `ready` deltaP `16.7987` edge `0.0263` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.239` n `153` status `ready` deltaP `2.452` edge `0.0138` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.4093` n `153` status `ready` deltaP `6.0587` edge `0.0484` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.5992` n `153` status `ready` deltaP `-0.2867` edge `-0.0012` maxDD `-1.8971`
- `market_context_high->crypto_major_1h` score `-0.8358` n `153` status `ready` deltaP `4.8325` edge `0.0187` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.921` n `153` status `ready` deltaP `7.9697` edge `-0.0002` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.8237` n `153` status `ready` deltaP `1.0058` edge `-0.0129` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.9422` n `153` status `ready` deltaP `0.0235` edge `-0.0007` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.3789` n `153` status `ready` deltaP `-6.0796` edge `-0.0234` maxDD `-6.7447`
- `market_context_high->crypto_major_4h` score `-4.5064` n `153` status `ready` deltaP `0.4563` edge `-0.0768` maxDD `-32.9851`
- `market_context_high->crypto_major_24h` score `-4.5281` n `112` status `ready` deltaP `-2.7915` edge `-0.0762` maxDD `-29.1905`
- `market_context_high->commodity_24h` score `-5.9792` n `112` status `ready` deltaP `-13.2644` edge `-0.1192` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.8212` n `112` status `ready` deltaP `-7.2032` edge `-0.2832` maxDD `-35.4638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
