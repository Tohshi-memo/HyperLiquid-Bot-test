# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T00:07:27.088117+00:00`
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

- `news_risk_high->unknown_24h` score `3694.0032` n `92` status `ready` deltaP `1.2153` edge `307.8255` maxDD `0.0`
- `market_context_high->unknown_1h` score `75.6831` n `44` status `ready` deltaP `10.1524` edge `6.2439` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `50.9144` n `44` status `ready` deltaP `26.5467` edge `4.101` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `27.663` n `44` status `ready` deltaP `14.9148` edge `2.2438` maxDD `-2.7051`
- `market_context_high->equity_24h` score `27.6484` n `44` status `ready` deltaP `36.0954` edge `2.0948` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.6475` n `44` status `ready` deltaP `31.4079` edge `0.4367` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.647` n `44` status `ready` deltaP `31.613` edge `0.117` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.4821` n `44` status `ready` deltaP `39.0521` edge `0.0369` maxDD `-0.2323`
- `market_context_high->equity_4h` score `3.1794` n `44` status `ready` deltaP `19.4983` edge `0.1726` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.6883` n `44` status `ready` deltaP `10.3797` edge `0.1341` maxDD `-3.3417`
- `news_risk_high->index_24h` score `1.4396` n `92` status `ready` deltaP `18.4632` edge `0.0539` maxDD `-2.2287`
- `market_context_high->crypto_major_4h` score `1.2998` n `44` status `ready` deltaP `8.4396` edge `0.1425` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `1.2127` n `44` status `ready` deltaP `9.4175` edge `0.1117` maxDD `-4.5405`
- `news_risk_high->metal_24h` score `1.1419` n `92` status `ready` deltaP `26.0794` edge `0.1373` maxDD `-6.8481`
- `market_context_high->equity_1h` score `1.1162` n `44` status `ready` deltaP `12.3163` edge `0.0512` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.7912` n `44` status `ready` deltaP `12.0169` edge `0.0095` maxDD `-0.2275`
- `market_context_high->metal_1h` score `0.248` n `44` status `ready` deltaP `6.1649` edge `0.0112` maxDD `-0.1976`
- `market_context_high->fx_1h` score `0.1469` n `44` status `ready` deltaP `7.2128` edge `0.0064` maxDD `-0.1854`
- `market_context_high->crypto_alt_1h` score `0.1399` n `44` status `ready` deltaP `4.1508` edge `0.0729` maxDD `-5.7799`
- `news_risk_high->equity_4h` score `-0.1055` n `139` status `ready` deltaP `16.3263` edge `0.0433` maxDD `-9.2079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
