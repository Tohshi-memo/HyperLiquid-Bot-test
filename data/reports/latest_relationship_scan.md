# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T23:07:26.393977+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11717`

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

- `market_context_high->unknown_24h` score `127.8524` n `108` status `ready` deltaP `-27.2113` edge `16.8411` maxDD `-7.8016`
- `risk_on_high->unknown_24h` score `33.7307` n `32` status `ready` deltaP `-37.7437` edge `4.6511` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.7307` n `32` status `ready` deltaP `-37.7437` edge `4.6511` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.9755` n `36` status `ready` deltaP `26.6609` edge `0.9415` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6859` n `36` status `ready` deltaP `39.3293` edge `0.3783` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.7018` n `108` status `ready` deltaP `37.4895` edge `0.3143` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `5.6013` n `32` status `ready` deltaP `39.3414` edge `0.2045` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.6013` n `32` status `ready` deltaP `39.3414` edge `0.2045` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.0306` n `32` status `ready` deltaP `27.6809` edge `0.4478` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.0306` n `32` status `ready` deltaP `27.6809` edge `0.4478` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.8089` n `36` status `ready` deltaP `32.2357` edge `0.1025` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9523` n `32` status `ready` deltaP `21.2652` edge `0.1225` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9523` n `32` status `ready` deltaP `21.2652` edge `0.1225` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.2709` n `108` status `ready` deltaP `20.918` edge `0.0969` maxDD `-0.7687`
- `news_risk_high->index_4h` score `2.0412` n `36` status `ready` deltaP `23.5772` edge `0.0261` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.8113` n `36` status `ready` deltaP `9.032` edge `0.1226` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.424` n `32` status `ready` deltaP `15.3069` edge `0.0399` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.424` n `32` status `ready` deltaP `15.3069` edge `0.0399` maxDD `-0.1957`
- `risk_on_high->equity_24h` score `0.7879` n `32` status `ready` deltaP `15.2026` edge `0.1776` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `0.7879` n `32` status `ready` deltaP `15.2026` edge `0.1776` maxDD `-11.2348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
