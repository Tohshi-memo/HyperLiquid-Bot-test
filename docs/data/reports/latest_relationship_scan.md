# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T15:37:34.573419+00:00`
- Price records: `672`
- Market context records: `7578`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14512`

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

- `market_context_high->commodity_4h` score `0.2571` n `163` status `ready` deltaP `9.8451` edge `0.0318` maxDD `-2.4139`
- `market_context_high->index_1h` score `0.0099` n `163` status `ready` deltaP `5.9268` edge `0.0106` maxDD `-0.9072`
- `market_context_high->commodity_24h` score `-0.0994` n `155` status `ready` deltaP `12.7144` edge `0.0653` maxDD `-7.0012`
- `market_context_high->commodity_1h` score `-0.1696` n `163` status `ready` deltaP `5.7425` edge `0.0048` maxDD `-1.5775`
- `market_context_high->index_4h` score `-0.4489` n `163` status `ready` deltaP `11.6518` edge `0.0374` maxDD `-3.4775`
- `market_context_high->fx_1h` score `-0.5117` n `163` status `ready` deltaP `1.169` edge `-0.0005` maxDD `-0.6615`
- `market_context_high->crypto_alt_1h` score `-0.6919` n `163` status `ready` deltaP `-0.0073` edge `0.0031` maxDD `-5.0068`
- `market_context_high->metal_1h` score `-0.7105` n `163` status `ready` deltaP `0.2333` edge `0.0119` maxDD `-1.0307`
- `market_context_high->unknown_24h` score `-0.764` n `156` status `ready` deltaP `7.8526` edge `0.0968` maxDD `-9.4349`
- `market_context_high->crypto_major_1h` score `-0.812` n `163` status `ready` deltaP `4.9153` edge `0.0015` maxDD `-7.403`
- `market_context_high->equity_1h` score `-0.8296` n `163` status `ready` deltaP `4.3866` edge `0.039` maxDD `-9.3015`
- `market_context_high->unknown_1h` score `-0.9369` n `163` status `ready` deltaP `0.5915` edge `-0.0617` maxDD `-1.3217`
- `market_context_high->fx_24h` score `-1.0528` n `155` status `ready` deltaP `6.3437` edge `0.014` maxDD `-3.8554`
- `market_context_high->crypto_alt_4h` score `-1.462` n `163` status `ready` deltaP `0.764` edge `0.0396` maxDD `-11.9038`
- `market_context_high->metal_4h` score `-1.4736` n `163` status `ready` deltaP `0.9091` edge `0.0532` maxDD `-4.8549`
- `market_context_high->equity_4h` score `-1.5071` n `163` status `ready` deltaP `3.6744` edge `0.219` maxDD `-21.9375`
- `market_context_high->unknown_4h` score `-2.0688` n `163` status `ready` deltaP `10.234` edge `-0.0978` maxDD `-6.1862`
- `market_context_high->fx_4h` score `-2.1376` n `163` status `ready` deltaP `-1.4052` edge `-0.0003` maxDD `-2.1439`
- `market_context_high->crypto_major_4h` score `-2.2135` n `163` status `ready` deltaP `4.9023` edge `0.0402` maxDD `-20.8664`
- `market_context_high->metal_24h` score `-3.5218` n `156` status `ready` deltaP `-5.0748` edge `0.0769` maxDD `-15.2332`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
