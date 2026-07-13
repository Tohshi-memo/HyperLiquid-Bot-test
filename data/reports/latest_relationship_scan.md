# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T03:37:28.904887+00:00`
- Price records: `672`
- Market context records: `6566`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9886`

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

- `market_context_high->unknown_24h` score `6.245` n `144` status `ready` deltaP `11.032` edge `0.7769` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.7163` n `210` status `ready` deltaP `-5.3512` edge `0.2688` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3905` n `144` status `ready` deltaP `13.3492` edge `0.2137` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3506` n `210` status `ready` deltaP `0.9268` edge `-0.0004` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.3713` n `210` status `ready` deltaP `7.4226` edge `0.0295` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.4355` n `210` status `ready` deltaP `6.8631` edge `0.0297` maxDD `-5.8368`
- `market_context_high->index_1h` score `-0.5429` n `210` status `ready` deltaP `-0.3075` edge `0.0044` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.5943` n `210` status `ready` deltaP `-0.4784` edge `-0.0047` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.8018` n `208` status `ready` deltaP `8.3718` edge `0.0094` maxDD `-4.7739`
- `market_context_high->equity_1h` score `-1.1189` n `210` status `ready` deltaP `2.1568` edge `0.0034` maxDD `-4.2147`
- `market_context_high->metal_1h` score `-1.2289` n `210` status `ready` deltaP `-3.2094` edge `-0.0003` maxDD `-2.1239`
- `market_context_high->crypto_major_4h` score `-1.2691` n `208` status `ready` deltaP `8.4273` edge `0.0645` maxDD `-13.6711`
- `market_context_high->unknown_4h` score `-1.3588` n `208` status `ready` deltaP `-15.7601` edge `0.2324` maxDD `-10.5788`
- `market_context_high->commodity_4h` score `-1.3807` n `208` status `ready` deltaP `-2.2855` edge `-0.0123` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.4298` n `208` status `ready` deltaP `5.7692` edge `0.0697` maxDD `-15.9845`
- `market_context_high->fx_4h` score `-1.7679` n `208` status `ready` deltaP `-0.2761` edge `-0.0036` maxDD `-3.3635`
- `market_context_high->metal_24h` score `-1.9429` n `144` status `ready` deltaP `6.0917` edge `0.0905` maxDD `-5.7746`
- `market_context_high->metal_4h` score `-1.9629` n `208` status `ready` deltaP `-1.0024` edge `0.0249` maxDD `-4.5893`
- `market_context_high->index_24h` score `-3.7581` n `144` status `ready` deltaP `1.4429` edge `-0.0007` maxDD `-10.7676`
- `market_context_high->fx_24h` score `-3.8336` n `144` status `ready` deltaP `-4.8143` edge `-0.0059` maxDD `-9.2795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
