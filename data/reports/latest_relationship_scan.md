# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T17:07:32.274169+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8530`

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

- `market_context_high->unknown_24h` score `1296.9996` n `144` status `ready` deltaP `-2.6042` edge `108.1934` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `22.026` n `149` status `ready` deltaP `4.385` edge `1.8215` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.5218` n `144` status `ready` deltaP `24.8264` edge `0.0301` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1745` n `149` status `ready` deltaP `7.269` edge `0.0019` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.0822` n `149` status `ready` deltaP `7.2291` edge `0.0048` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.091` n `149` status `ready` deltaP `8.327` edge `0.0075` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.2752` n `149` status `ready` deltaP `7.5785` edge `0.0425` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.4112` n `149` status `ready` deltaP `7.2015` edge `0.0396` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.4861` n `144` status `ready` deltaP `13.368` edge `0.0276` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.6788` n `149` status `ready` deltaP `-0.64` edge `0.0061` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7266` n `149` status `ready` deltaP `-3.3246` edge `-0.0027` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7411` n `149` status `ready` deltaP `9.0563` edge `-0.0013` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.3945` n `149` status `ready` deltaP `1.0891` edge `0.0052` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.4995` n `149` status `ready` deltaP `3.4943` edge `0.0208` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.6728` n `144` status `ready` deltaP `6.9444` edge `0.0274` maxDD `-15.7143`
- `market_context_high->index_4h` score `-3.0322` n `149` status `ready` deltaP `-9.1791` edge `-0.0293` maxDD `-5.6417`
- `market_context_high->metal_24h` score `-3.1163` n `144` status `ready` deltaP `1.2153` edge `0.0248` maxDD `-9.4075`
- `market_context_high->crypto_major_24h` score `-3.1387` n `144` status `ready` deltaP `1.5625` edge `0.0729` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.353` n `149` status `ready` deltaP `4.119` edge `-0.0254` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.3102` n `149` status `ready` deltaP `-2.8677` edge `-0.1383` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
