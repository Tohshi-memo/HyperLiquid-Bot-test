# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T01:37:29.342093+00:00`
- Price records: `672`
- Market context records: `4574`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9991`

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

- `market_context_high->unknown_1h` score `69.9222` n `157` status `ready` deltaP `6.585` edge `5.833` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `3.1579` n `157` status `ready` deltaP `7.4549` edge `0.3345` maxDD `-4.6834`
- `market_context_high->fx_4h` score `-0.5491` n `157` status `ready` deltaP `5.3761` edge `0.002` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.632` n `157` status `ready` deltaP `1.0994` edge `0.0196` maxDD `-2.0345`
- `market_context_high->equity_1h` score `-0.712` n `157` status `ready` deltaP `-2.1883` edge `0.022` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-0.7162` n `157` status `ready` deltaP `2.1147` edge `0.071` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-0.737` n `157` status `ready` deltaP `-0.3976` edge `-0.0033` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.819` n `157` status `ready` deltaP `2.5011` edge `-0.0094` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.1813` n `157` status `ready` deltaP `3.6614` edge `0.0349` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.5792` n `157` status `ready` deltaP `-2.8252` edge `-0.0119` maxDD `-2.7358`
- `market_context_high->unknown_24h` score `-2.8878` n `155` status `ready` deltaP `1.5278` edge `-0.1585` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-2.9392` n `157` status `ready` deltaP `-4.4043` edge `-0.0823` maxDD `-17.8795`
- `market_context_high->fx_24h` score `-5.3976` n `155` status `ready` deltaP `-13.0309` edge `-0.0117` maxDD `-6.0982`
- `market_context_high->index_24h` score `-5.3993` n `155` status `ready` deltaP `-8.0601` edge `-0.101` maxDD `-29.3321`
- `market_context_high->crypto_alt_1h` score `-5.5207` n `157` status `ready` deltaP `-2.8252` edge `-0.1125` maxDD `-22.2982`
- `market_context_high->commodity_24h` score `-5.8449` n `155` status `ready` deltaP `8.3815` edge `0.0415` maxDD `-34.0892`
- `market_context_high->crypto_major_1h` score `-6.7555` n `157` status `ready` deltaP `-6.2359` edge `-0.1461` maxDD `-27.356`
- `market_context_high->crypto_alt_4h` score `-9.0498` n `157` status `ready` deltaP `-3.7974` edge `-0.2692` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2462` n `157` status `ready` deltaP `-8.2773` edge `-0.3367` maxDD `-67.4051`
- `market_context_high->crypto_major_4h` score `-11.8577` n `157` status `ready` deltaP `-2.8119` edge `-0.4071` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
