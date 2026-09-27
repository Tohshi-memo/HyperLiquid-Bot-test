# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T02:07:29.362356+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11444`

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

- `news_risk_high->unknown_24h` score `2973.0828` n `100` status `ready` deltaP `1.2153` edge `247.7488` maxDD `0.0`
- `market_context_high->unknown_1h` score `74.9811` n `44` status `ready` deltaP `10.1524` edge `6.1854` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `51.3795` n `44` status `ready` deltaP `27.9356` edge `4.1305` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `27.8022` n `44` status `ready` deltaP `14.9148` edge `2.2554` maxDD `-2.7051`
- `market_context_high->equity_24h` score `27.7336` n `44` status `ready` deltaP `36.0954` edge `2.1019` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.6932` n `44` status `ready` deltaP `31.7551` edge `0.4382` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.6983` n `44` status `ready` deltaP `32.1338` edge `0.1178` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.3738` n `44` status `ready` deltaP `37.8325` edge `0.036` maxDD `-0.2323`
- `market_context_high->equity_4h` score `3.0062` n `44` status `ready` deltaP `18.2788` edge `0.1663` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.3402` n `44` status `ready` deltaP `9.3127` edge `0.1122` maxDD `-3.3417`
- `news_risk_high->index_24h` score `1.2443` n `100` status `ready` deltaP `18.0278` edge `0.0447` maxDD `-2.2287`
- `market_context_high->crypto_major_1h` score `1.106` n `44` status `ready` deltaP `8.9684` edge `0.1058` maxDD `-4.5405`
- `market_context_high->equity_1h` score `1.0923` n `44` status `ready` deltaP `12.1666` edge `0.0502` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `1.0489` n `100` status `ready` deltaP `24.8611` edge `0.1335` maxDD `-6.8481`
- `market_context_high->crypto_major_4h` score `0.9732` n `44` status `ready` deltaP `7.3725` edge `0.1224` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.802` n `44` status `ready` deltaP `12.1666` edge `0.0094` maxDD `-0.2275`
- `market_context_high->metal_1h` score `0.2468` n `44` status `ready` deltaP `6.1649` edge `0.0111` maxDD `-0.1976`
- `market_context_high->fx_1h` score `0.1469` n `44` status `ready` deltaP `7.2128` edge `0.0064` maxDD `-0.1854`
- `market_context_high->crypto_alt_1h` score `0.0727` n `44` status `ready` deltaP `4.1508` edge `0.0673` maxDD `-5.7799`
- `news_risk_high->index_1h` score `-0.119` n `139` status `ready` deltaP `2.3726` edge `0.0034` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
