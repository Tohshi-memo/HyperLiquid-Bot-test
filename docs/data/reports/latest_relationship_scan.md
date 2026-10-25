# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T07:22:28.822397+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7926`

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

- `market_context_high->unknown_4h` score `46.1395` n `101` status `ready` deltaP `1.0037` edge `3.8718` maxDD `-1.016`
- `market_context_high->unknown_1h` score `13.4353` n `113` status `ready` deltaP `4.3201` edge `1.1397` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `9.6101` n `37` status `ready` deltaP `27.4118` edge `0.6789` maxDD `-4.1975`
- `market_context_high->crypto_major_24h` score `2.5029` n `37` status `ready` deltaP `16.2772` edge `0.206` maxDD `-5.8084`
- `market_context_high->commodity_24h` score `0.6844` n `37` status `ready` deltaP `13.476` edge `0.0888` maxDD `-3.6055`
- `market_context_high->fx_1h` score `-0.0639` n `113` status `ready` deltaP `3.5729` edge `0.0029` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.1013` n `101` status `ready` deltaP `5.7534` edge `0.0085` maxDD `-0.4545`
- `market_context_high->fx_24h` score `-0.2033` n `37` status `ready` deltaP `7.6295` edge `0.0061` maxDD `-0.9753`
- `market_context_high->commodity_1h` score `-0.5889` n `113` status `ready` deltaP `-1.081` edge `0.0082` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6335` n `113` status `ready` deltaP `4.6341` edge `-0.0045` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6628` n `113` status `ready` deltaP `-2.1727` edge `-0.0053` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.8706` n `101` status `ready` deltaP `-3.3175` edge `0.0334` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.4453` n `113` status `ready` deltaP `0.8518` edge `-0.0329` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.8811` n `101` status `ready` deltaP `5.3022` edge `-0.0211` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.0289` n `101` status `ready` deltaP `-5.2161` edge `-0.0379` maxDD `-4.3282`
- `market_context_high->metal_24h` score `-2.4915` n `37` status `ready` deltaP `-3.8992` edge `-0.032` maxDD `-6.3036`
- `market_context_high->crypto_alt_1h` score `-3.0721` n `113` status `ready` deltaP `-2.023` edge `-0.0593` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.7576` n `113` status `ready` deltaP `0.2093` edge `-0.0872` maxDD `-12.1865`
- `market_context_high->index_24h` score `-6.4268` n `37` status `ready` deltaP `-31.5034` edge `-0.1954` maxDD `-5.078`
- `market_context_high->crypto_major_4h` score `-9.0599` n `101` status `ready` deltaP `-9.4044` edge `-0.1926` maxDD `-33.3092`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
