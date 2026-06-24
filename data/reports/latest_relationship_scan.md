# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T14:22:28.995499+00:00`
- Price records: `672`
- Market context records: `4629`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9851`

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

- `market_context_high->unknown_1h` score `70.026` n `146` status `ready` deltaP `8.3094` edge `5.826` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.4067` n `146` status `ready` deltaP `9.5807` edge `0.4244` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.3269` n `146` status `ready` deltaP `3.2483` edge `0.0307` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5574` n `146` status `ready` deltaP `-1.8005` edge `-0.004` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7531` n `146` status `ready` deltaP `1.7541` edge `0.0` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.8149` n `146` status `ready` deltaP `-1.7964` edge `0.0062` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.9054` n `146` status `ready` deltaP `1.5912` edge `-0.0144` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.0093` n `146` status `ready` deltaP `5.6485` edge `0.0437` maxDD `-9.1941`
- `market_context_high->unknown_24h` score `-1.4215` n `144` status `ready` deltaP `5.3819` edge `-0.062` maxDD `-4.7201`
- `market_context_high->equity_4h` score `-1.6862` n `146` status `ready` deltaP `-0.9982` edge `-0.0326` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.6999` n `146` status `ready` deltaP `-4.2142` edge `-0.0127` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.958` n `146` status `ready` deltaP `-4.3905` edge `-0.0848` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.6997` n `144` status `ready` deltaP `11.9791` edge `0.0534` maxDD `-29.3255`
- `market_context_high->fx_24h` score `-5.1156` n `144` status `ready` deltaP `-9.8958` edge `-0.0091` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.5404` n `146` status `ready` deltaP `-2.0958` edge `-0.119` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.7984` n `146` status `ready` deltaP `-5.9921` edge `-0.1513` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.1629` n `144` status `ready` deltaP `-8.3334` edge `-0.0872` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.172` n `146` status `ready` deltaP `-3.5061` edge `-0.2868` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.236` n `146` status `ready` deltaP `-6.843` edge `-0.3453` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.3297` n `146` status `ready` deltaP `-5.5588` edge `-0.4493` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
