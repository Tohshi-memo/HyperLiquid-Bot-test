# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T12:52:28.797105+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5108`

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

- `market_context_high->unknown_4h` score `38.2335` n `113` status `ready` deltaP `-0.2914` edge `3.2216` maxDD `-1.016`
- `market_context_high->commodity_24h` score `0.4823` n `57` status `ready` deltaP `13.1762` edge `0.0649` maxDD `-3.6055`
- `market_context_high->fx_4h` score `0.0475` n `113` status `ready` deltaP `8.221` edge `0.009` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0895` n `113` status `ready` deltaP `3.1106` edge `0.0027` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.5182` n `113` status `ready` deltaP `-0.3325` edge `0.0091` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6623` n `113` status `ready` deltaP `4.3347` edge `-0.0049` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6628` n `113` status `ready` deltaP `-2.0362` edge `-0.0062` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.9162` n `113` status `ready` deltaP `-3.61` edge `0.0295` maxDD `-1.165`
- `market_context_high->crypto_major_24h` score `-0.9294` n `57` status `ready` deltaP `-2.0559` edge `-0.0029` maxDD `-4.5369`
- `market_context_high->crypto_major_1h` score `-1.4228` n `113` status `ready` deltaP `1.75` edge `-0.036` maxDD `-9.3126`
- `market_context_high->unknown_1h` score `-1.6259` n `113` status `ready` deltaP `4.1704` edge `-0.1144` maxDD `-1.5781`
- `market_context_high->fx_24h` score `-1.804` n `57` status `ready` deltaP `-0.2101` edge `0.0083` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-1.8856` n `113` status `ready` deltaP `4.7661` edge `-0.0179` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1862` n `113` status `ready` deltaP `-8.3774` edge `-0.037` maxDD `-4.3282`
- `market_context_high->index_24h` score `-2.4252` n `57` status `ready` deltaP `-5.8936` edge `-0.1434` maxDD `-4.925`
- `market_context_high->crypto_alt_1h` score `-3.2133` n `113` status `ready` deltaP `-2.4588` edge `-0.064` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.7728` n `57` status `ready` deltaP `-11.3121` edge `0.0104` maxDD `-7.2843`
- `market_context_high->equity_1h` score `-3.8859` n `113` status `ready` deltaP `-0.5392` edge `-0.0929` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-5.5808` n `57` status `ready` deltaP `0.8589` edge `-0.1706` maxDD `-36.3828`
- `market_context_high->crypto_major_4h` score `-10.0304` n `113` status `ready` deltaP `-12.7428` edge `-0.2511` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
