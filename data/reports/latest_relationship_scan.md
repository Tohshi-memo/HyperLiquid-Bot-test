# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T22:52:26.297946+00:00`
- Price records: `672`
- Market context records: `4666`
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

- `market_context_high->unknown_1h` score `70.2923` n `146` status `ready` deltaP `9.0579` edge `5.8432` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.3109` n `146` status `ready` deltaP `9.7331` edge `0.4154` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.5346` n `146` status `ready` deltaP `9.1681` edge `0.1591` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.4612` n `146` status `ready` deltaP `2.4998` edge `0.0245` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5388` n `146` status `ready` deltaP `-1.5011` edge `-0.0036` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.6957` n `146` status `ready` deltaP `4.1827` edge `-0.0048` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.735` n `146` status `ready` deltaP `1.9066` edge `0.0013` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.7736` n `146` status `ready` deltaP `-1.0479` edge `0.0065` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-1.107` n `146` status `ready` deltaP `2.3555` edge `0.0193` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.2668` n `146` status `ready` deltaP `4.5815` edge `0.0178` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.6939` n `146` status `ready` deltaP `-4.2142` edge `-0.0122` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.8052` n `146` status `ready` deltaP `-3.642` edge `-0.0702` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.5922` n `146` status `ready` deltaP `14.0625` edge `0.074` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-5.1732` n `146` status `ready` deltaP `-10.4214` edge `-0.0104` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.2285` n `146` status `ready` deltaP `-1.1976` edge `-0.099` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.4482` n `146` status `ready` deltaP `-4.7945` edge `-0.1301` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.3526` n `146` status `ready` deltaP `-6.3951` edge `-0.0326` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-7.9413` n `146` status `ready` deltaP `0.0` edge `-0.1524` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.4744` n `146` status `ready` deltaP `-2.7272` edge `-0.2751` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-11.1187` n `146` status `ready` deltaP `-2.2052` edge `-0.3164` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
