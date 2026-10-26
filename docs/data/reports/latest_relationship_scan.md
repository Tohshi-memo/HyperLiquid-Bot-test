# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T03:07:23.503347+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5104`

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

- `market_context_high->unknown_4h` score `27.5323` n `113` status `ready` deltaP `-1.8158` edge `2.34` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.0833` n `99` status `ready` deltaP `21.8118` edge `0.1323` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.0539` n `99` status `ready` deltaP `20.3915` edge `0.0282` maxDD `-1.2451`
- `market_context_high->fx_4h` score `-0.0645` n `113` status `ready` deltaP `7.0014` edge `0.0078` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.1684` n `117` status `ready` deltaP `1.9244` edge `0.0014` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.522` n `117` status `ready` deltaP `-0.6205` edge `0.0107` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.5952` n `113` status `ready` deltaP `0.6583` edge `0.0422` maxDD `-1.165`
- `market_context_high->metal_1h` score `-0.6096` n `117` status `ready` deltaP `4.9184` edge `-0.0044` maxDD `-1.6682`
- `market_context_high->index_24h` score `-0.7642` n `99` status `ready` deltaP `10.7639` edge `-0.0415` maxDD `-4.925`
- `market_context_high->index_1h` score `-1.1108` n `117` status `ready` deltaP `-3.1604` edge `-0.0063` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-2.0194` n `113` status `ready` deltaP `3.3941` edge `-0.0199` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1498` n `113` status `ready` deltaP `-7.7676` edge `-0.0364` maxDD `-4.3282`
- `market_context_high->crypto_major_1h` score `-2.1869` n `117` status `ready` deltaP `2.33` edge `-0.0397` maxDD `-9.3126`
- `market_context_high->crypto_major_24h` score `-3.3369` n `99` status `ready` deltaP `0.7892` edge `-0.0432` maxDD `-14.2108`
- `market_context_high->crypto_alt_1h` score `-3.5827` n `117` status `ready` deltaP `-1.8758` edge `-0.07` maxDD `-12.2845`
- `market_context_high->equity_1h` score `-3.9529` n `117` status `ready` deltaP `-1.364` edge `-0.0921` maxDD `-12.2572`
- `market_context_high->commodity_24h` score `-4.6459` n `99` status `ready` deltaP `-14.3624` edge `-0.1054` maxDD `-15.558`
- `market_context_high->equity_24h` score `-7.3976` n `99` status `ready` deltaP `-2.2412` edge `-0.4051` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.0676` n `113` status `ready` deltaP `-12.7428` edge `-0.2542` maxDD `-32.9851`
- `market_context_high->crypto_alt_24h` score `-10.3771` n `99` status `ready` deltaP `-10.0537` edge `-0.3948` maxDD `-60.1528`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
