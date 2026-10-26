# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T14:36:22.202697+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8062`

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

- `market_context_high->unknown_4h` score `56.6339` n `149` status `ready` deltaP `0.3034` edge `4.751` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.5363` n `113` status `ready` deltaP `27.794` edge `0.1505` maxDD `-7.3625`
- `market_context_high->fx_4h` score `0.1305` n `149` status `ready` deltaP `9.3786` edge `0.0082` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.1155` n `151` status `ready` deltaP `6.5156` edge `0.002` maxDD `-0.1986`
- `market_context_high->fx_24h` score `-0.034` n `113` status `ready` deltaP `18.6561` edge `0.0285` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.2297` n `151` status `ready` deltaP `7.0264` edge `0.0029` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.3269` n `151` status `ready` deltaP `1.7739` edge `0.011` maxDD `-1.0053`
- `market_context_high->index_24h` score `-0.3994` n `113` status `ready` deltaP `11.5689` edge `-0.0001` maxDD `-4.925`
- `market_context_high->index_1h` score `-0.5604` n `151` status `ready` deltaP `-0.8335` edge `-0.0011` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.5962` n `149` status `ready` deltaP `5.0269` edge `0.0397` maxDD `-1.165`
- `market_context_high->metal_4h` score `-1.093` n `149` status `ready` deltaP `5.4274` edge `-0.0053` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.1408` n `151` status `ready` deltaP `2.4777` edge `-0.0047` maxDD `-9.3126`
- `market_context_high->index_4h` score `-1.806` n `149` status `ready` deltaP `-4.4109` edge `-0.0147` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.1847` n `151` status `ready` deltaP `-0.7919` edge `-0.0462` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.2687` n `151` status `ready` deltaP `-2.16` edge `-0.028` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.3432` n `113` status `ready` deltaP `-1.8159` edge `-0.059` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.928` n `149` status `ready` deltaP `-2.702` edge `-0.1098` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-5.9799` n `113` status `ready` deltaP `-2.0445` edge `-0.1955` maxDD `-36.6024`
- `market_context_high->commodity_24h` score `-6.4157` n `113` status `ready` deltaP `-18.2098` edge `-0.1422` maxDD `-24.0477`
- `market_context_high->equity_4h` score `-7.5718` n `149` status `ready` deltaP `-3.8368` edge `-0.219` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
