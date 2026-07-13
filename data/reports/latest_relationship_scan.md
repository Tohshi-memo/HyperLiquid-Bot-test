# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T09:07:30.706560+00:00`
- Price records: `672`
- Market context records: `6588`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9808`

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

- `market_context_high->unknown_24h` score `4.6031` n `156` status `ready` deltaP `6.6925` edge `0.669` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.9813` n `210` status `ready` deltaP `-5.7285` edge `0.2934` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.0179` n `156` status `ready` deltaP `11.8872` edge `0.1924` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3355` n `210` status `ready` deltaP `1.1577` edge `0.0` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.475` n `210` status `ready` deltaP `6.4485` edge `0.0227` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.523` n `210` status `ready` deltaP `0.489` edge `-0.002` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.581` n `210` status `ready` deltaP `-0.8298` edge `0.003` maxDD `-0.7564`
- `market_context_high->crypto_alt_1h` score `-0.649` n `210` status `ready` deltaP `4.5438` edge `0.0178` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.9128` n `210` status `ready` deltaP `9.142` edge `0.01` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.2184` n `210` status `ready` deltaP `1.6325` edge `-0.0014` maxDD `-4.2147`
- `market_context_high->commodity_4h` score `-1.2584` n `210` status `ready` deltaP `-0.6693` edge `-0.0074` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.4129` n `210` status `ready` deltaP `-4.9244` edge `-0.0042` maxDD `-2.1239`
- `market_context_high->fx_4h` score `-1.6934` n `210` status `ready` deltaP `0.9915` edge `-0.0025` maxDD `-3.3635`
- `market_context_high->unknown_4h` score `-1.7069` n `210` status `ready` deltaP `-17.0659` edge `0.2121` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.8587` n `210` status `ready` deltaP `6.8191` edge `0.0477` maxDD `-16.8495`
- `market_context_high->metal_4h` score `-2.1649` n `210` status `ready` deltaP `-1.5012` edge `0.0185` maxDD `-5.2172`
- `market_context_high->crypto_alt_4h` score `-2.1701` n `210` status `ready` deltaP `3.7137` edge `0.0372` maxDD `-19.2145`
- `market_context_high->metal_24h` score `-3.4153` n `156` status `ready` deltaP `2.8332` edge `0.0719` maxDD `-8.3653`
- `market_context_high->fx_24h` score `-3.7398` n `156` status `ready` deltaP `-3.7299` edge `-0.0011` maxDD `-9.2795`
- `market_context_high->equity_4h` score `-4.7519` n `210` status `ready` deltaP `7.3534` edge `-0.0181` maxDD `-27.1529`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
