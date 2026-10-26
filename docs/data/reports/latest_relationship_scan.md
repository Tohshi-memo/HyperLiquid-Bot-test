# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T13:37:32.139195+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8396`

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

- `market_context_high->unknown_4h` score `15.8343` n `145` status `ready` deltaP `-0.0809` edge `1.3536` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.5623` n `113` status `ready` deltaP `28.0973` edge `0.1518` maxDD `-7.3625`
- `market_context_high->fx_4h` score `0.171` n `145` status `ready` deltaP `9.8402` edge `0.0085` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.1095` n `151` status `ready` deltaP `6.4411` edge `0.002` maxDD `-0.1986`
- `market_context_high->fx_24h` score `0.0012` n `113` status `ready` deltaP `19.2724` edge `0.0289` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.2449` n `151` status `ready` deltaP `6.8089` edge `0.0024` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.3247` n `151` status `ready` deltaP `1.846` edge `0.0107` maxDD `-1.0053`
- `market_context_high->index_24h` score `-0.4135` n `113` status `ready` deltaP `11.4768` edge `-0.0013` maxDD `-4.925`
- `market_context_high->commodity_4h` score `-0.483` n `145` status `ready` deltaP `6.0366` edge `0.0424` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.5658` n `151` status `ready` deltaP `-0.9071` edge `-0.0013` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.0402` n `145` status `ready` deltaP `6.2027` edge `-0.0037` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.1781` n `151` status `ready` deltaP `2.2544` edge `-0.008` maxDD `-9.3126`
- `market_context_high->index_4h` score `-1.8789` n `145` status `ready` deltaP `-5.3322` edge `-0.0179` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.2258` n `151` status `ready` deltaP `-1.0112` edge `-0.05` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.3119` n `151` status `ready` deltaP `-2.3764` edge `-0.0321` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.3862` n `113` status `ready` deltaP `-2.0726` edge `-0.0628` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.9437` n `145` status `ready` deltaP `-2.4936` edge `-0.1132` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-6.0985` n `113` status `ready` deltaP `-2.6441` edge `-0.2067` maxDD `-36.6024`
- `market_context_high->commodity_24h` score `-6.4708` n `113` status `ready` deltaP `-18.8191` edge `-0.1452` maxDD `-24.0477`
- `market_context_high->equity_4h` score `-7.6982` n `145` status `ready` deltaP `-4.2725` edge `-0.2323` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
