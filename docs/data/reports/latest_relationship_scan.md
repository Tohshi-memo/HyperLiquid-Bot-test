# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T21:22:28.050653+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `market_context_high->unknown_1h` score `1.5921` n `145` status `ready` deltaP `6.4496` edge `0.1124` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.8189` n `145` status `ready` deltaP `18.9088` edge `-0.0139` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1081` n `145` status `ready` deltaP `8.2507` edge `0.0091` maxDD `-0.3527`
- `market_context_high->index_1h` score `0.0053` n `145` status `ready` deltaP `7.3911` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1815` n `145` status `ready` deltaP `1.2482` edge `0.0043` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2975` n `145` status `ready` deltaP `8.0551` edge `-0.0169` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.3328` n `145` status `ready` deltaP `4.7873` edge `0.0324` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.374` n `145` status `ready` deltaP `-0.1631` edge `-0.005` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.5515` n `145` status `ready` deltaP `3.2485` edge `0.0112` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.8834` n `145` status `ready` deltaP `-4.2641` edge `0.0002` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.0908` n `145` status `ready` deltaP `-7.867` edge `-0.0024` maxDD `-1.1328`
- `market_context_high->fx_24h` score `-1.1548` n `129` status `ready` deltaP `0.4603` edge `0.0098` maxDD `-2.2066`
- `market_context_high->crypto_alt_1h` score `-1.662` n `145` status `ready` deltaP `-3.2696` edge `-0.0418` maxDD `-7.9582`
- `market_context_high->equity_4h` score `-1.6924` n `145` status `ready` deltaP `-0.5625` edge `0.0684` maxDD `-16.1967`
- `market_context_high->commodity_24h` score `-2.1289` n `129` status `ready` deltaP `-5.3819` edge `0.0418` maxDD `-4.666`
- `market_context_high->crypto_alt_4h` score `-2.3928` n `145` status `ready` deltaP `3.4967` edge `-0.0759` maxDD `-7.0785`
- `market_context_high->crypto_major_1h` score `-2.4486` n `145` status `ready` deltaP `-6.8408` edge `-0.1206` maxDD `-7.8171`
- `market_context_high->index_24h` score `-4.4045` n `129` status `ready` deltaP `-6.7143` edge `-0.0392` maxDD `-21.1244`
- `market_context_high->metal_24h` score `-5.3976` n `129` status `ready` deltaP `-23.6716` edge `-0.2034` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.7692` n `145` status `ready` deltaP `-0.1914` edge `-0.3465` maxDD `-5.6395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
