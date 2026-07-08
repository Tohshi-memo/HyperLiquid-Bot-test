# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T21:52:43.989352+00:00`
- Price records: `672`
- Market context records: `6128`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `10.3343` n `30` status `ready` deltaP `38.6458` edge `0.6183` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.8404` n `30` status `ready` deltaP `69.4444` edge `0.1904` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3457` n `32` status `ready` deltaP `45.3506` edge `0.0644` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3919` n `32` status `ready` deltaP `28.7425` edge `0.0216` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.3049` n `32` status `ready` deltaP `13.9783` edge `0.1208` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7086` n `32` status `ready` deltaP `9.0756` edge `0.0765` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.5337` n `195` status `ready` deltaP `4.6646` edge `0.1051` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.0815` n `30` status `ready` deltaP `8.7152` edge `0.0186` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2754` n `195` status `ready` deltaP `1.4348` edge `-0.0003` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.5431` n `30` status `ready` deltaP `14.0973` edge `-0.1187` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.7012` n `195` status `ready` deltaP `2.9323` edge `0.0093` maxDD `-3.4996`
- `market_context_high->equity_1h` score `-0.7611` n `195` status `ready` deltaP `-0.1098` edge `0.0147` maxDD `-4.2573`
- `news_risk_high->metal_1h` score `-0.7769` n `32` status `ready` deltaP `-2.994` edge `-0.0299` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.7883` n `195` status `ready` deltaP `-2.4382` edge `-0.0048` maxDD `-0.5708`
- `market_context_high->metal_1h` score `-0.8296` n `195` status `ready` deltaP `2.3906` edge `-0.0052` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.8673` n `195` status `ready` deltaP `4.0596` edge `0.037` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.8931` n `195` status `ready` deltaP `4.7636` edge `0.0305` maxDD `-9.807`
- `news_risk_high->crypto_major_24h` score `-0.993` n `30` status `ready` deltaP `8.993` edge `-0.1093` maxDD `-4.2368`
- `market_context_high->index_4h` score `-1.0115` n `195` status `ready` deltaP `0.0219` edge `0.0166` maxDD `-1.381`
- `market_context_high->metal_24h` score `-1.1002` n `195` status `ready` deltaP `14.4738` edge `0.0193` maxDD `-11.8809`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
