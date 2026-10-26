# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T07:22:27.225060+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9076`

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

- `market_context_high->unknown_4h` score `19.8093` n `122` status `ready` deltaP `-2.579` edge `1.7015` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.6076` n `113` status `ready` deltaP `28.4445` edge `0.1553` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.1922` n `113` status `ready` deltaP `22.571` edge `0.0314` maxDD `-1.2451`
- `market_context_high->fx_4h` score `0.0612` n `122` status `ready` deltaP `8.4816` edge `0.0084` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0056` n `132` status `ready` deltaP `4.9946` edge `0.0018` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.4161` n `132` status `ready` deltaP `4.1916` edge `-0.0021` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.435` n `132` status `ready` deltaP `0.4673` edge `0.0107` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.5508` n `122` status `ready` deltaP `1.3919` edge `0.043` maxDD `-1.165`
- `market_context_high->index_24h` score `-0.6416` n `113` status `ready` deltaP `10.4351` edge `-0.0236` maxDD `-4.925`
- `market_context_high->index_1h` score `-0.669` n `132` status `ready` deltaP `-2.2909` edge `-0.0053` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.247` n `122` status `ready` deltaP `4.1908` edge `-0.0168` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.3765` n `132` status `ready` deltaP `1.5152` edge `-0.0285` maxDD `-9.3126`
- `market_context_high->index_4h` score `-2.2123` n `122` status `ready` deltaP `-9.0739` edge `-0.0357` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.3978` n `132` status `ready` deltaP `-0.6442` edge `-0.0745` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-3.8308` n `132` status `ready` deltaP `-2.3363` edge `-0.0552` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.9699` n `113` status `ready` deltaP `-2.767` edge `-0.133` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-6.2691` n `122` status `ready` deltaP `-10.1034` edge `-0.2324` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.5594` n `113` status `ready` deltaP `-18.9927` edge `-0.1554` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-7.246` n `113` status `ready` deltaP `-5.4219` edge `-0.3353` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-8.9117` n `122` status `ready` deltaP `-8.2742` edge `-0.3612` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
