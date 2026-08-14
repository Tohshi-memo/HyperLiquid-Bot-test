# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T18:37:33.215769+00:00`
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

- `market_context_high->unknown_24h` score `136.1185` n `128` status `ready` deltaP `-33.2466` edge `11.8561` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.756` n `32` status `ready` deltaP `-46.5278` edge `4.5847` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.756` n `32` status `ready` deltaP `-46.5278` edge `4.5847` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `10.2732` n `36` status `ready` deltaP `12.8472` edge `0.8084` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.5907` n `36` status `ready` deltaP `39.939` edge `0.3663` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.005` n `128` status `ready` deltaP `28.3854` edge `0.2336` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.5811` n `32` status `ready` deltaP `30.7292` edge `0.1769` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.5811` n `32` status `ready` deltaP `30.7292` edge `0.1769` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.697` n `32` status `ready` deltaP `18.6738` edge `0.1185` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.697` n `32` status `ready` deltaP `18.6738` edge `0.1185` maxDD `-0.1258`
- `risk_on_high->crypto_major_24h` score `2.5796` n `32` status `ready` deltaP `19.0972` edge `0.319` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.5796` n `32` status `ready` deltaP `19.0972` edge `0.319` maxDD `-6.2481`
- `news_risk_high->index_24h` score `2.3317` n `36` status `ready` deltaP `16.6667` edge `0.0832` maxDD `0.0`
- `news_risk_high->index_4h` score `1.8864` n `36` status `ready` deltaP `21.7479` edge `0.0254` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.7492` n `128` status `ready` deltaP `17.1113` edge `0.0788` maxDD `-0.7687`
- `news_risk_high->equity_1h` score `1.7142` n `36` status `ready` deltaP `8.4332` edge `0.1185` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2875` n `32` status `ready` deltaP `13.6602` edge `0.0395` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2875` n `32` status `ready` deltaP `13.6602` edge `0.0395` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.0995` n `32` status `ready` deltaP `13.1944` edge `0.0221` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.0995` n `32` status `ready` deltaP `13.1944` edge `0.0221` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
