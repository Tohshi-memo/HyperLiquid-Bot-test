# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T11:07:31.579416+00:00`
- Price records: `672`
- Market context records: `4615`
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

- `market_context_high->unknown_1h` score `69.3894` n `147` status `ready` deltaP `8.4067` edge `5.7723` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.38` n `147` status `ready` deltaP `9.6659` edge `0.4216` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.4018` n `147` status `ready` deltaP `2.7771` edge `0.0276` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5614` n `147` status `ready` deltaP `-1.8769` edge `-0.004` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7731` n `147` status `ready` deltaP `1.4892` edge `-0.0008` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.9214` n `147` status `ready` deltaP `-2.5856` edge `-0.0022` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.9363` n `147` status `ready` deltaP `1.0567` edge `-0.0148` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.0898` n `147` status `ready` deltaP `4.8065` edge `0.039` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.7491` n `147` status `ready` deltaP `-4.6947` edge `-0.0136` maxDD `-2.7358`
- `market_context_high->equity_4h` score `-1.7882` n `147` status `ready` deltaP `-1.3709` edge `-0.0432` maxDD `-8.8203`
- `market_context_high->unknown_24h` score `-2.0772` n `145` status `ready` deltaP `3.6207` edge `-0.1049` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-2.9945` n `147` status `ready` deltaP `-4.598` edge `-0.0881` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.6881` n `145` status `ready` deltaP `11.6295` edge `0.0567` maxDD `-29.3255`
- `market_context_high->fx_24h` score `-5.2676` n `145` status `ready` deltaP `-11.6307` edge `-0.0102` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.636` n `147` status `ready` deltaP `-2.7353` edge `-0.1227` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.8638` n `147` status `ready` deltaP `-6.2996` edge `-0.1547` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.3367` n `145` status `ready` deltaP `-8.3166` edge `-0.1018` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.2608` n `147` status `ready` deltaP `-3.9986` edge `-0.2949` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.372` n `147` status `ready` deltaP `-7.343` edge `-0.3594` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.3986` n `147` status `ready` deltaP `-6.0281` edge `-0.455` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
