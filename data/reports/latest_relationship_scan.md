# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T10:37:29.790831+00:00`
- Price records: `672`
- Market context records: `4613`
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

- `market_context_high->unknown_1h` score `69.3618` n `147` status `ready` deltaP `8.1073` edge `5.772` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.3328` n `147` status `ready` deltaP `9.361` edge `0.4197` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.4378` n `147` status `ready` deltaP `2.4777` edge `0.0266` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5614` n `147` status `ready` deltaP `-1.8769` edge `-0.004` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7739` n `147` status `ready` deltaP `1.4892` edge `-0.0009` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.9199` n `147` status `ready` deltaP `-2.5856` edge `-0.002` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.9355` n `147` status `ready` deltaP `1.0567` edge `-0.0147` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.0993` n `147` status `ready` deltaP `4.6541` edge `0.0388` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.7228` n `147` status `ready` deltaP `-4.3953` edge `-0.0134` maxDD `-2.7358`
- `market_context_high->equity_4h` score `-1.789` n `147` status `ready` deltaP `-1.3709` edge `-0.0433` maxDD `-8.8203`
- `market_context_high->unknown_24h` score `-2.1625` n `145` status `ready` deltaP `3.2735` edge `-0.1097` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-2.9984` n `147` status `ready` deltaP `-4.598` edge `-0.0886` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.6641` n `145` status `ready` deltaP `11.6295` edge `0.0587` maxDD `-29.3255`
- `market_context_high->fx_24h` score `-5.2978` n `145` status `ready` deltaP `-11.978` edge `-0.0104` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.6504` n `147` status `ready` deltaP `-2.7353` edge `-0.1239` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.8889` n `147` status `ready` deltaP `-6.4493` edge `-0.1558` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.3691` n `145` status `ready` deltaP `-8.3166` edge `-0.1045` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.2693` n `147` status `ready` deltaP `-3.9986` edge `-0.296` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.3837` n `147` status `ready` deltaP `-7.343` edge `-0.3609` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.4056` n `147` status `ready` deltaP `-6.0281` edge `-0.4559` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
