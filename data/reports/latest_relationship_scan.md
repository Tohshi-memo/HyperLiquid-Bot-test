# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T15:22:34.003720+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7962`

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

- `market_context_high->unknown_4h` score `120.0227` n `151` status `ready` deltaP `0.499` edge `10.0321` maxDD `-1.016`
- `market_context_high->unknown_1h` score `28.216` n `153` status `ready` deltaP `1.6242` edge `2.3894` maxDD `-1.5781`
- `market_context_high->metal_24h` score `0.4929` n `113` status `ready` deltaP `27.2741` edge `0.1484` maxDD `-7.3625`
- `market_context_high->fx_4h` score `0.177` n `151` status `ready` deltaP `9.9297` edge `0.0084` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.1732` n `153` status `ready` deltaP `7.1621` edge `0.0025` maxDD `-0.1986`
- `market_context_high->fx_24h` score `-0.0634` n `113` status `ready` deltaP `18.1362` edge `0.0282` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.1875` n `153` status `ready` deltaP `7.4322` edge `0.0056` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.3513` n `153` status `ready` deltaP `1.499` edge `0.0108` maxDD `-1.0053`
- `market_context_high->index_24h` score `-0.397` n `113` status `ready` deltaP `11.5689` edge `0.0002` maxDD `-4.925`
- `market_context_high->index_1h` score `-0.5003` n `153` status `ready` deltaP `-0.0822` edge `0.0016` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.5917` n `151` status `ready` deltaP `5.1125` edge `0.0395` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.0229` n `153` status `ready` deltaP `3.1858` edge `0.0057` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.0417` n `151` status `ready` deltaP `6.1296` edge `-0.0034` maxDD `-5.3474`
- `market_context_high->index_4h` score `-1.7357` n `151` status `ready` deltaP `-3.6731` edge `-0.0106` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.0056` n `153` status `ready` deltaP `-0.002` edge `-0.0285` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.1254` n `153` status `ready` deltaP `-1.3238` edge `-0.0152` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.3432` n `113` status `ready` deltaP `-1.8159` edge `-0.059` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.8216` n `151` status `ready` deltaP `-1.9908` edge `-0.1009` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-5.9636` n `113` status `ready` deltaP `-2.0445` edge `-0.1934` maxDD `-36.6024`
- `market_context_high->commodity_24h` score `-6.3746` n `113` status `ready` deltaP `-17.6899` edge `-0.1404` maxDD `-24.0477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
