# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T08:07:26.124109+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11908`

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

- `news_risk_high->unknown_24h` score `1534.794` n `121` status `ready` deltaP `1.2153` edge `127.8914` maxDD `0.0`
- `market_context_high->unknown_1h` score `120.4914` n `45` status `ready` deltaP `10.8018` edge `9.9736` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `54.632` n `41` status `ready` deltaP `30.0263` edge `4.3876` maxDD `-2.4756`
- `market_context_high->equity_24h` score `29.0367` n `41` status `ready` deltaP `35.9291` edge `2.2116` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `28.9745` n `41` status `ready` deltaP `14.7485` edge `2.3542` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.1212` n `41` status `ready` deltaP `33.3249` edge `0.4634` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.3833` n `41` status `ready` deltaP `39.8712` edge `0.1233` maxDD `-0.2401`
- `market_context_high->equity_4h` score `3.3854` n `42` status `ready` deltaP `20.8333` edge `0.1767` maxDD `-1.3444`
- `market_context_high->index_4h` score `3.1245` n `42` status `ready` deltaP `34.5674` edge `0.037` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `2.225` n `42` status `ready` deltaP `12.7177` edge `0.1549` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.3731` n `45` status `ready` deltaP `15.7219` edge `0.0499` maxDD `-1.5564`
- `market_context_high->crypto_major_1h` score `1.311` n `45` status `ready` deltaP `11.3007` edge `0.1197` maxDD `-4.8632`
- `market_context_high->crypto_major_4h` score `1.1981` n `42` status `ready` deltaP `7.063` edge `0.1432` maxDD `-5.2359`
- `market_context_high->crypto_alt_1h` score `1.1241` n `45` status `ready` deltaP `10.6787` edge `0.1114` maxDD `-5.7799`
- `market_context_high->index_1h` score `0.9287` n `45` status `ready` deltaP `13.2003` edge `0.0089` maxDD `-0.2275`
- `news_risk_high->index_24h` score `0.6162` n `121` status `ready` deltaP `14.2763` edge `0.0257` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.4314` n `121` status `ready` deltaP `14.7956` edge `0.1228` maxDD `-6.8392`
- `market_context_high->fx_1h` score `0.3659` n `45` status `ready` deltaP `11.2442` edge `0.0076` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.0369` n `45` status `ready` deltaP `3.6793` edge `0.0104` maxDD `-0.215`
- `news_risk_high->index_1h` score `-0.1618` n `139` status `ready` deltaP `1.8654` edge `0.0031` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
