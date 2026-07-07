# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T10:22:32.743887+00:00`
- Price records: `672`
- Market context records: `5971`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11220`

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

- `news_risk_high->fx_24h` score `7.1803` n `30` status `ready` deltaP `65.7986` edge `0.1597` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.0081` n `30` status `ready` deltaP `36.4931` edge `0.1946` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.9002` n `30` status `ready` deltaP `40.4573` edge `0.0599` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1615` n `30` status `ready` deltaP `26.0279` edge `0.0205` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4223` n `235` status `ready` deltaP `8.9199` edge `0.1685` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8333` n `30` status `ready` deltaP `10.1896` edge `0.0856` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1943` n `30` status `ready` deltaP `5.3194` edge `0.0356` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.0564` n `30` status `ready` deltaP `8.1944` edge `0.0253` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.3798` n `30` status `ready` deltaP `1.986` edge `-0.0253` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4459` n `242` status `ready` deltaP `3.432` edge `0.0328` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.4895` n `242` status `ready` deltaP `2.3717` edge `0.0013` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.4938` n `242` status `ready` deltaP `-1.3176` edge `0.0012` maxDD `-1.4578`
- `market_context_high->fx_1h` score `-0.6707` n `242` status `ready` deltaP `-0.6112` edge `-0.0007` maxDD `-0.756`
- `market_context_high->index_1h` score `-0.7031` n `242` status `ready` deltaP `-0.4491` edge `0.0042` maxDD `-1.3078`
- `market_context_high->equity_24h` score `-0.9362` n `213` status `ready` deltaP `20.9948` edge `0.3063` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.1085` n `30` status `ready` deltaP `-10.4491` edge `-0.021` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.1124` n `235` status `ready` deltaP `0.962` edge `0.0197` maxDD `-3.165`
- `market_context_high->crypto_major_1h` score `-1.1306` n `242` status `ready` deltaP `1.815` edge `0.0197` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.1634` n `242` status `ready` deltaP `1.5453` edge `0.0158` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.4307` n `235` status `ready` deltaP `-1.2286` edge `-0.0039` maxDD `-6.3734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
