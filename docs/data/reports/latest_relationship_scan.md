# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T15:22:31.243894+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11964`

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

- `news_risk_high->unknown_24h` score `750.3468` n `136` status `ready` deltaP `1.2153` edge `62.5208` maxDD `0.0`
- `market_context_high->unknown_1h` score `164.7357` n `39` status `ready` deltaP `10.1605` edge `13.6649` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `58.1857` n `35` status `ready` deltaP `30.3026` edge `4.6819` maxDD `-2.4756`
- `market_context_high->equity_24h` score `31.0997` n `35` status `ready` deltaP `35.511` edge `2.3863` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `29.5102` n `35` status `ready` deltaP `15.0248` edge `2.397` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.6562` n `35` status `ready` deltaP `33.4276` edge `0.5073` maxDD `-0.3705`
- `market_context_high->crypto_alt_4h` score `4.9832` n `39` status `ready` deltaP `20.2861` edge `0.3343` maxDD `-3.3417`
- `market_context_high->metal_24h` score `4.4476` n `35` status `ready` deltaP `39.8958` edge `0.1285` maxDD `-0.2401`
- `market_context_high->equity_4h` score `4.0975` n `39` status `ready` deltaP `25.5941` edge `0.2043` maxDD `-1.3444`
- `market_context_high->index_4h` score `3.292` n `39` status `ready` deltaP `36.0303` edge `0.0412` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `2.5936` n `39` status `ready` deltaP `10.5418` edge `0.2363` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.7768` n `39` status `ready` deltaP `19.7183` edge `0.0569` maxDD `-1.5564`
- `market_context_high->crypto_alt_1h` score `1.4384` n `39` status `ready` deltaP `11.2775` edge `0.1336` maxDD `-5.7799`
- `market_context_high->crypto_major_1h` score `1.3819` n `39` status `ready` deltaP `11.5577` edge `0.1239` maxDD `-4.8632`
- `market_context_high->index_1h` score `1.0507` n `39` status `ready` deltaP `14.5901` edge `0.0098` maxDD `-0.2275`
- `news_risk_high->index_24h` score `0.9879` n `136` status `ready` deltaP `17.1671` edge `0.0374` maxDD `-2.2287`
- `market_context_high->fx_1h` score `0.8496` n `39` status `ready` deltaP `14.8127` edge `0.0077` maxDD `-0.1854`
- `market_context_high->metal_4h` score `0.5462` n `39` status `ready` deltaP `9.1816` edge `0.0222` maxDD `-0.3647`
- `news_risk_high->metal_24h` score `0.5064` n `136` status `ready` deltaP `15.7782` edge `0.1225` maxDD `-6.8392`
- `news_risk_high->index_1h` score `-0.0755` n `139` status `ready` deltaP `2.9133` edge `0.0033` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
