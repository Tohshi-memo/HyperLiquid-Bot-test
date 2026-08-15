# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T07:39:43.132435+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `137.0804` n `128` status `ready` deltaP `-27.9287` edge `11.9008` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.3812` n `32` status `ready` deltaP `-41.2099` edge `4.6294` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.3812` n `32` status `ready` deltaP `-41.2099` edge `4.6294` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `11.9691` n `36` status `ready` deltaP `21.4615` edge `0.8923` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.5186` n `36` status `ready` deltaP `38.8128` edge `0.3678` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.0585` n `128` status `ready` deltaP `28.6787` edge `0.2361` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.6346` n `32` status `ready` deltaP `31.0225` edge `0.1794` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.6346` n `32` status `ready` deltaP `31.0225` edge `0.1794` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.1229` n `32` status `ready` deltaP `27.5076` edge `0.4608` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.1229` n `32` status `ready` deltaP `27.5076` edge `0.4608` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.174` n `36` status `ready` deltaP `25.6499` edge `0.0935` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.8188` n `32` status `ready` deltaP `20.2863` edge `0.1179` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8188` n `32` status `ready` deltaP `20.2863` edge `0.1179` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `1.871` n `128` status `ready` deltaP `18.7238` edge `0.0782` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.7869` n `36` status `ready` deltaP `20.624` edge `0.0246` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6734` n `36` status `ready` deltaP `7.7728` edge `0.1195` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2558` n `32` status `ready` deltaP `13.2941` edge `0.0393` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2558` n `32` status `ready` deltaP `13.2941` edge `0.0393` maxDD `-0.1957`
- `market_context_high->commodity_1h` score `0.6192` n `128` status `ready` deltaP `8.6066` edge `0.0239` maxDD `-0.3742`
- `risk_on_high->fx_4h` score `0.5751` n `32` status `ready` deltaP `7.0253` edge `0.0152` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
