# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T14:07:31.964380+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8406`

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

- `market_context_high->unknown_4h` score `14.9856` n `147` status `ready` deltaP `0.1255` edge `1.2815` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.5591` n `113` status `ready` deltaP `28.0973` edge `0.1514` maxDD `-7.3625`
- `market_context_high->fx_1h` score `0.1215` n `151` status `ready` deltaP `6.5908` edge `0.002` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1036` n `147` status `ready` deltaP `9.0426` edge `0.0082` maxDD `-0.4545`
- `market_context_high->fx_24h` score `-0.0184` n `113` status `ready` deltaP `18.9251` edge `0.0287` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.2246` n `151` status `ready` deltaP `7.1083` edge `0.003` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.3391` n `151` status `ready` deltaP `1.6963` edge `0.0105` maxDD `-1.0053`
- `market_context_high->index_24h` score `-0.3967` n `113` status `ready` deltaP `11.6504` edge `-0.0003` maxDD `-4.925`
- `market_context_high->commodity_4h` score `-0.5133` n `147` status `ready` deltaP `5.748` edge `0.0418` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.5565` n `151` status `ready` deltaP `-0.7574` edge `-0.0011` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.0733` n `147` status `ready` deltaP `5.8507` edge `-0.0056` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.14` n `151` status `ready` deltaP `2.5538` edge `-0.0051` maxDD `-9.3126`
- `market_context_high->index_4h` score `-1.8585` n `147` status `ready` deltaP `-5.0906` edge `-0.0169` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.1899` n `151` status `ready` deltaP `-0.7118` edge `-0.0474` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.269` n `151` status `ready` deltaP `-2.077` edge `-0.0286` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.3393` n `113` status `ready` deltaP `-1.7254` edge `-0.0591` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.9626` n `147` status `ready` deltaP `-2.8269` edge `-0.1134` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-6.0204` n `113` status `ready` deltaP `-2.2969` edge `-0.199` maxDD `-36.6024`
- `market_context_high->commodity_24h` score `-6.4434` n `113` status `ready` deltaP `-18.4719` edge `-0.144` maxDD `-24.0477`
- `market_context_high->equity_4h` score `-7.6755` n `147` status `ready` deltaP `-4.54` edge `-0.2276` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
