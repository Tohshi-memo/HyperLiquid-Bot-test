# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T08:52:33.116670+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8298`

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

- `market_context_high->unknown_4h` score `17.9563` n `128` status `ready` deltaP `-2.4009` edge `1.5459` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.6022` n `113` status `ready` deltaP `28.4445` edge `0.1546` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.1326` n `113` status `ready` deltaP `21.5293` edge `0.0307` maxDD `-1.2451`
- `market_context_high->fx_4h` score `0.1013` n `128` status `ready` deltaP `9.0129` edge `0.0082` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.0389` n `138` status `ready` deltaP `5.821` edge `0.002` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.2921` n `138` status `ready` deltaP `6.2158` edge `0.0003` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.3459` n `138` status `ready` deltaP `1.4016` edge `0.0119` maxDD `-1.0053`
- `market_context_high->index_24h` score `-0.5572` n `113` status `ready` deltaP `11.1296` edge `-0.0174` maxDD `-4.925`
- `market_context_high->commodity_4h` score `-0.6115` n `128` status `ready` deltaP `3.6204` edge `0.0478` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6484` n `138` status `ready` deltaP `-2.0004` edge `-0.0046` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.2924` n `128` status `ready` deltaP `3.2584` edge `-0.0164` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.3966` n `138` status `ready` deltaP `1.024` edge `-0.0278` maxDD `-9.3126`
- `market_context_high->index_4h` score `-2.3172` n `128` status `ready` deltaP `-10.9566` edge `-0.0366` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-3.8108` n `138` status `ready` deltaP `-2.0785` edge `-0.0751` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-3.8324` n `138` status `ready` deltaP `-2.8812` edge `-0.0517` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.7692` n `113` status `ready` deltaP `-2.0726` edge `-0.1119` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-6.0553` n `128` status `ready` deltaP `-8.1365` edge `-0.2181` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.5251` n `113` status `ready` deltaP `-18.9927` edge `-0.151` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.9017` n `113` status `ready` deltaP `-4.3803` edge `-0.2981` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-8.9144` n `128` status `ready` deltaP `-9.4512` edge `-0.3537` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
