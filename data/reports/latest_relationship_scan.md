# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T00:37:27.186923+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11474`

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

- `news_risk_high->unknown_24h` score `3502.3032` n `94` status `ready` deltaP `1.2153` edge `291.8505` maxDD `0.0`
- `market_context_high->unknown_1h` score `75.4611` n `44` status `ready` deltaP `10.1524` edge `6.2254` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `51.0286` n `44` status `ready` deltaP `26.894` edge `4.1082` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `27.7146` n `44` status `ready` deltaP `14.9148` edge `2.2481` maxDD `-2.7051`
- `market_context_high->equity_24h` score `27.6664` n `44` status `ready` deltaP `36.0954` edge `2.0963` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.6661` n `44` status `ready` deltaP `31.5815` edge `0.4371` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.647` n `44` status `ready` deltaP `31.613` edge `0.117` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.4553` n `44` status `ready` deltaP `38.7472` edge `0.0367` maxDD `-0.2323`
- `market_context_high->equity_4h` score `3.137` n `44` status `ready` deltaP `19.1934` edge `0.1711` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.5967` n `44` status `ready` deltaP `10.0749` edge `0.1285` maxDD `-3.3417`
- `news_risk_high->index_24h` score `1.313` n `94` status `ready` deltaP `17.8968` edge `0.0513` maxDD `-2.2287`
- `market_context_high->crypto_major_4h` score `1.2106` n `44` status `ready` deltaP `8.1347` edge `0.1371` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `1.2067` n `44` status `ready` deltaP `9.4175` edge `0.1112` maxDD `-4.5405`
- `news_risk_high->metal_24h` score `1.1085` n `94` status `ready` deltaP `25.6169` edge `0.1361` maxDD `-6.8481`
- `market_context_high->equity_1h` score `1.1031` n `44` status `ready` deltaP `12.1666` edge `0.0511` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.7793` n `44` status `ready` deltaP `11.8672` edge `0.0095` maxDD `-0.2275`
- `market_context_high->metal_1h` score `0.2599` n `44` status `ready` deltaP `6.3146` edge `0.0112` maxDD `-0.1976`
- `market_context_high->fx_1h` score `0.1469` n `44` status `ready` deltaP `7.2128` edge `0.0064` maxDD `-0.1854`
- `market_context_high->crypto_alt_1h` score `0.1327` n `44` status `ready` deltaP `4.1508` edge `0.0723` maxDD `-5.7799`
- `news_risk_high->index_1h` score `-0.1417` n `139` status `ready` deltaP `2.0732` edge `0.0035` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
