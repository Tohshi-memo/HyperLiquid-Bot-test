# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T12:13:42.604420+00:00`
- Price records: `672`
- Market context records: `4620`
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

- `market_context_high->unknown_1h` score `69.363` n `147` status `ready` deltaP `8.257` edge `5.7711` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.3946` n `147` status `ready` deltaP `9.8183` edge `0.4218` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.3838` n `147` status `ready` deltaP `2.9268` edge `0.0281` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5692` n `147` status `ready` deltaP `-2.0266` edge `-0.004` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7723` n `147` status `ready` deltaP `1.4892` edge `-0.0007` maxDD `-1.9927`
- `market_context_high->index_4h` score `-0.9276` n `147` status `ready` deltaP `1.2091` edge `-0.0147` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.9347` n `147` status `ready` deltaP `-2.7353` edge `-0.0029` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.0921` n `147` status `ready` deltaP `4.8065` edge `0.0387` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.7623` n `147` status `ready` deltaP `-4.8444` edge `-0.0137` maxDD `-2.7358`
- `market_context_high->equity_4h` score `-1.8088` n `147` status `ready` deltaP `-1.6758` edge `-0.0438` maxDD `-8.8203`
- `market_context_high->unknown_24h` score `-1.8838` n `145` status `ready` deltaP `3.9679` edge `-0.0911` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-2.9743` n `147` status `ready` deltaP `-4.4483` edge `-0.0865` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.7445` n `145` status `ready` deltaP `11.6295` edge `0.052` maxDD `-29.3255`
- `market_context_high->fx_24h` score `-5.2048` n `145` status `ready` deltaP `-10.9363` edge `-0.0096` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.7151` n `147` status `ready` deltaP `-3.0347` edge `-0.1273` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.9561` n `147` status `ready` deltaP `-6.7487` edge `-0.1594` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.2467` n `145` status `ready` deltaP `-8.3166` edge `-0.0943` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.2938` n `147` status `ready` deltaP `-4.3035` edge `-0.2971` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.3336` n `147` status `ready` deltaP `-7.1905` edge `-0.3555` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.4363` n `147` status `ready` deltaP `-6.333` edge `-0.4578` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
