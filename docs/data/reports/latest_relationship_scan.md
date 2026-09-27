# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T05:37:29.487218+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11760`

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

- `news_risk_high->unknown_24h` score `1955.0052` n `114` status `ready` deltaP `1.2153` edge `162.909` maxDD `0.0`
- `market_context_high->unknown_1h` score `109.1795` n `47` status `ready` deltaP `10.2974` edge `9.0343` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `52.3401` n `44` status `ready` deltaP `30.1926` edge `4.1955` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.4502` n `44` status `ready` deltaP `14.9148` edge `2.3094` maxDD `-2.7051`
- `market_context_high->equity_24h` score `27.952` n `44` status `ready` deltaP `36.0954` edge `2.1201` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8909` n `44` status `ready` deltaP `33.4912` edge `0.4431` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.8782` n `44` status `ready` deltaP `34.2171` edge `0.1189` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.2056` n `44` status `ready` deltaP `35.8508` edge `0.0352` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.8009` n `44` status `ready` deltaP `16.2971` edge `0.1624` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.135` n `44` status `ready` deltaP `8.398` edge `0.1012` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.0098` n `114` status `ready` deltaP `18.3479` edge `0.1266` maxDD `-6.8481`
- `market_context_high->equity_1h` score `0.9583` n `47` status `ready` deltaP `11.3167` edge `0.0447` maxDD `-1.5564`
- `market_context_high->crypto_major_4h` score `0.8658` n `44` status `ready` deltaP `6.9152` edge `0.1165` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.7388` n `47` status `ready` deltaP `7.6284` edge `0.0965` maxDD `-4.8632`
- `market_context_high->index_1h` score `0.7232` n `47` status `ready` deltaP `11.3167` edge `0.0085` maxDD `-0.2275`
- `news_risk_high->index_24h` score `0.6054` n `114` status `ready` deltaP `12.9569` edge `0.0336` maxDD `-2.2287`
- `market_context_high->crypto_alt_1h` score `0.4567` n `47` status `ready` deltaP `7.2111` edge `0.0789` maxDD `-5.7799`
- `market_context_high->fx_1h` score `0.3108` n `47` status `ready` deltaP `10.2592` edge `0.0071` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.0503` n `47` status `ready` deltaP `3.8763` edge `0.0102` maxDD `-0.215`
- `news_risk_high->index_1h` score `-0.1778` n `142` status `ready` deltaP `1.6973` edge `0.003` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
