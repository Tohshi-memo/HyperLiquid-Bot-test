# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T20:07:39.076561+00:00`
- Price records: `672`
- Market context records: `4550`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10045`

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

- `market_context_high->unknown_1h` score `58.8234` n `165` status `ready` deltaP `6.615` edge `4.9079` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `5.2169` n `165` status `ready` deltaP `7.0704` edge `0.5442` maxDD `-7.5275`
- `market_context_high->fx_4h` score `-0.4765` n `165` status `ready` deltaP `6.6981` edge `0.0025` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.632` n `165` status `ready` deltaP `-0.8175` edge `0.0132` maxDD `-2.7684`
- `market_context_high->fx_1h` score `-0.6796` n `165` status `ready` deltaP `0.2595` edge `-0.0029` maxDD `-1.1038`
- `market_context_high->equity_4h` score `-0.709` n `165` status `ready` deltaP `2.5379` edge `0.0691` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.841` n `165` status `ready` deltaP `1.9429` edge `-0.0085` maxDD `-5.9823`
- `market_context_high->index_1h` score `-1.0019` n `165` status `ready` deltaP `-2.5485` edge `-0.0106` maxDD `-2.7358`
- `market_context_high->equity_1h` score `-1.0907` n `165` status `ready` deltaP `-2.3843` edge `0.0237` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.9433` n `165` status `ready` deltaP `2.9278` edge `0.0293` maxDD `-9.1941`
- `market_context_high->unknown_24h` score `-2.8249` n `163` status `ready` deltaP `2.5094` edge `-0.1598` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-4.5145` n `165` status `ready` deltaP `-4.7169` edge `-0.0796` maxDD `-17.8795`
- `market_context_high->fx_24h` score `-5.4827` n `163` status `ready` deltaP `-13.5843` edge `-0.0151` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.5272` n `165` status `ready` deltaP `-3.611` edge `-0.1078` maxDD `-22.2982`
- `market_context_high->index_24h` score `-5.713` n `163` status `ready` deltaP `-9.473` edge `-0.1318` maxDD `-29.3321`
- `market_context_high->crypto_major_1h` score `-6.4888` n `165` status `ready` deltaP `-5.137` edge `-0.1312` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-7.173` n `163` status `ready` deltaP `6.07` edge `0.0299` maxDD `-40.7825`
- `market_context_high->crypto_alt_4h` score `-8.7103` n `165` status `ready` deltaP `-2.1286` edge `-0.2368` maxDD `-63.9243`
- `market_context_high->equity_24h` score `-13.4017` n `163` status `ready` deltaP `-1.1269` edge `-0.2427` maxDD `-102.1031`
- `market_context_high->metal_4h` score `-15.5326` n `165` status `ready` deltaP `-7.5684` edge `-0.3222` maxDD `-67.4051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
