# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T13:36:09.593917+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `market_context_high->unknown_24h` score `102.6125` n `143` status `ready` deltaP `-33.4523` edge `9.0653` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.94` n `32` status `ready` deltaP `-44.4444` edge `4.5944` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.94` n `32` status `ready` deltaP `-44.4444` edge `4.5944` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.5228` n `36` status `ready` deltaP `9.7222` edge `0.7667` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.1418` n `36` status `ready` deltaP `37.9573` edge `0.3421` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.8486` n `32` status `ready` deltaP `32.8125` edge `0.1853` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.8486` n `32` status `ready` deltaP `32.8125` edge `0.1853` maxDD `0.0`
- `market_context_high->commodity_24h` score `2.9951` n `143` status `ready` deltaP `22.323` edge `0.1811` maxDD `-2.4263`
- `risk_on_high->commodity_4h` score `2.9176` n `32` status `ready` deltaP `20.3506` edge `0.1257` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9176` n `32` status `ready` deltaP `20.3506` edge `0.1257` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.0754` n `36` status `ready` deltaP `14.0625` edge `0.0792` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `1.9269` n `32` status `ready` deltaP `16.1458` edge `0.255` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.9269` n `32` status `ready` deltaP `16.1458` edge `0.255` maxDD `-6.2481`
- `news_risk_high->index_4h` score `1.6665` n `36` status `ready` deltaP `19.6138` edge `0.0213` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6626` n `36` status `ready` deltaP `8.4332` edge `0.1142` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.2864` n `143` status `ready` deltaP `15.6522` edge `0.0667` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.2827` n `32` status `ready` deltaP `13.5105` edge `0.0401` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2827` n `32` status `ready` deltaP `13.5105` edge `0.0401` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.2485` n `32` status `ready` deltaP `14.7569` edge `0.0241` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.2485` n `32` status `ready` deltaP `14.7569` edge `0.0241` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
