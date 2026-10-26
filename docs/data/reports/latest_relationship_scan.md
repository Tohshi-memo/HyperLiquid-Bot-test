# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T06:37:33.556064+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7158`

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

- `market_context_high->unknown_4h` score `22.1988` n `119` status `ready` deltaP `-2.8605` edge `1.9025` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.6068` n `113` status `ready` deltaP `28.4445` edge `0.1552` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.2224` n `113` status `ready` deltaP `23.0918` edge `0.0318` maxDD `-1.2451`
- `market_context_high->fx_1h` score `0.0621` n `130` status `ready` deltaP `5.8337` edge `0.0021` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.0061` n `119` status `ready` deltaP `7.6706` edge `0.0082` maxDD `-0.4545`
- `market_context_high->commodity_1h` score `-0.3364` n `130` status `ready` deltaP `-0.4284` edge `0.0098` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.3901` n `130` status `ready` deltaP `4.6614` edge `-0.0019` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.6186` n `119` status `ready` deltaP `0.1934` edge `0.0423` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6554` n `130` status `ready` deltaP `-2.029` edge `-0.0053` maxDD `-1.2155`
- `market_context_high->index_24h` score `-0.6991` n `113` status `ready` deltaP `9.9143` edge `-0.0275` maxDD `-4.925`
- `market_context_high->metal_4h` score `-1.216` n `119` status `ready` deltaP `4.6808` edge `-0.0161` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.3431` n `130` status `ready` deltaP `2.158` edge `-0.0285` maxDD `-9.3126`
- `market_context_high->index_4h` score `-2.1596` n `119` status `ready` deltaP `-8.0613` edge `-0.0357` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.3803` n `130` status `ready` deltaP `-0.2326` edge `-0.075` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.4631` n `130` status `ready` deltaP `-1.8333` edge `-0.0551` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-5.0749` n `113` status `ready` deltaP `-3.2879` edge `-0.143` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-6.4118` n `119` status `ready` deltaP `-11.1959` edge `-0.2434` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.575` n `113` status `ready` deltaP `-18.9927` edge `-0.1574` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-7.4424` n `113` status `ready` deltaP `-5.9428` edge `-0.357` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-9.0061` n `119` status `ready` deltaP `-8.6788` edge `-0.3706` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
