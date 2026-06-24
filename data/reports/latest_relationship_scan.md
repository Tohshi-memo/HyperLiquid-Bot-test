# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T17:52:33.745263+00:00`
- Price records: `672`
- Market context records: `4644`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9996`

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

- `market_context_high->unknown_1h` score `70.1279` n `146` status `ready` deltaP `8.9082` edge `5.8305` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.9739` n `146` status `ready` deltaP `10.1905` edge `0.4676` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `-0.039` n `146` status `ready` deltaP `6.0431` edge `0.0488` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3533` n `146` status `ready` deltaP `2.9489` edge `0.0305` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5816` n `146` status `ready` deltaP `-2.2496` edge `-0.0041` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7081` n `146` status `ready` deltaP `2.3639` edge `0.0017` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.7097` n `146` status `ready` deltaP `-0.8982` edge `0.0137` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.7785` n `146` status `ready` deltaP `3.1156` edge `-0.0083` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.1321` n `146` status `ready` deltaP `5.3437` edge `0.03` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.1735` n `146` status `ready` deltaP `1.136` edge `0.0189` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.6915` n `146` status `ready` deltaP `-4.2142` edge `-0.012` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.9112` n `146` status `ready` deltaP `-3.9414` edge `-0.0818` maxDD `-17.8795`
- `market_context_high->fx_24h` score `-4.9917` n `146` status `ready` deltaP `-8.5117` edge `-0.008` maxDD `-6.0982`
- `market_context_high->commodity_24h` score `-5.1745` n `146` status `ready` deltaP `11.2847` edge `0.044` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.1949` n `146` status `ready` deltaP `-1.1976` edge `-0.0962` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.435` n `146` status `ready` deltaP `-4.6448` edge `-0.13` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.6427` n `146` status `ready` deltaP `-6.9159` edge `-0.0533` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.2459` n `146` status `ready` deltaP `-1.372` edge `-0.1823` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.8434` n `146` status `ready` deltaP `-4.7089` edge `-0.3092` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-11.3677` n `146` status `ready` deltaP `-3.4247` edge `-0.3402` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
