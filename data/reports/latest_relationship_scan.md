# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T04:37:29.296034+00:00`
- Price records: `672`
- Market context records: `4587`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9937`

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

- `market_context_high->unknown_1h` score `71.7383` n `154` status `ready` deltaP `6.5013` edge `5.9849` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `3.7534` n `154` status `ready` deltaP `8.1941` edge `0.3792` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.5785` n `154` status `ready` deltaP `1.3939` edge `0.0221` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.67` n `154` status `ready` deltaP `3.2012` edge `0.001` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-0.8209` n `154` status `ready` deltaP `-1.4018` edge `-0.0036` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.8339` n `154` status `ready` deltaP `2.3044` edge `-0.01` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.8897` n `154` status `ready` deltaP `-2.5449` edge `0.0016` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.1319` n `154` status `ready` deltaP `4.5672` edge `0.0352` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.2913` n `154` status `ready` deltaP `1.271` edge `0.0029` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.5999` n `154` status `ready` deltaP `-3.1437` edge `-0.0115` maxDD `-2.7358`
- `market_context_high->unknown_24h` score `-2.5357` n `152` status `ready` deltaP `1.6539` edge `-0.13` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-2.8752` n `154` status `ready` deltaP `-3.099` edge `-0.0828` maxDD `-17.8795`
- `market_context_high->index_24h` score `-5.268` n `152` status `ready` deltaP `-6.9444` edge `-0.0916` maxDD `-29.3321`
- `market_context_high->commodity_24h` score `-5.3171` n `152` status `ready` deltaP `9.311` edge `0.0463` maxDD `-31.4504`
- `market_context_high->fx_24h` score `-5.324` n `152` status `ready` deltaP `-12.3355` edge `-0.0102` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.3572` n `154` status `ready` deltaP `-1.2462` edge `-0.1094` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.752` n `154` status `ready` deltaP `-6.1922` edge `-0.1461` maxDD `-27.356`
- `market_context_high->crypto_alt_4h` score `-9.0595` n `154` status `ready` deltaP `-3.6982` edge `-0.2711` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2105` n `154` status `ready` deltaP `-7.1548` edge `-0.3398` maxDD `-67.3902`
- `market_context_high->crypto_major_4h` score `-12.0216` n `154` status `ready` deltaP `-3.9694` edge `-0.4204` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
