# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T14:07:48.599199+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->unknown_24h` score `55.8639` n `161` status `ready` deltaP `-23.6898` edge `5.1045` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `22.5578` n `32` status `ready` deltaP `-42.1875` edge `3.2483` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `22.5578` n `32` status `ready` deltaP `-42.1875` edge `3.2483` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `8.4155` n `32` status `ready` deltaP `7.9861` edge `0.686` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.8036` n `36` status `ready` deltaP `36.2805` edge `0.3251` maxDD `0.0`
- `risk_on_high->commodity_24h` score `3.7687` n `32` status `ready` deltaP `27.0833` edge `0.1335` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `3.7687` n `32` status `ready` deltaP `27.0833` edge `0.1335` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.642` n `32` status `ready` deltaP `18.8262` edge `0.1129` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.642` n `32` status `ready` deltaP `18.8262` edge `0.1129` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.4356` n `32` status `ready` deltaP `15.625` edge `0.0988` maxDD `0.0`
- `risk_on_high->fx_24h` score `2.0024` n `32` status `ready` deltaP `22.3958` edge `0.036` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `2.0024` n `32` status `ready` deltaP `22.3958` edge `0.036` maxDD `-0.1418`
- `market_context_high->commodity_24h` score `1.7997` n `161` status `ready` deltaP `17.1454` edge `0.116` maxDD `-2.4263`
- `news_risk_high->index_4h` score `1.7791` n `36` status `ready` deltaP `20.376` edge `0.0256` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.4612` n `36` status `ready` deltaP `7.2356` edge `0.1054` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.4605` n `161` status `ready` deltaP `16.4776` edge `0.0757` maxDD `-2.1077`
- `risk_on_high->crypto_major_24h` score `1.2689` n `32` status `ready` deltaP `12.3264` edge `0.1961` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.2689` n `32` status `ready` deltaP `12.3264` edge `0.1961` maxDD `-6.2481`
- `risk_on_high->commodity_1h` score `1.2192` n `32` status `ready` deltaP `13.0614` edge `0.0378` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2192` n `32` status `ready` deltaP `13.0614` edge `0.0378` maxDD `-0.1957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
