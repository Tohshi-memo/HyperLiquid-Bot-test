# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T04:37:30.698747+00:00`
- Price records: `672`
- Market context records: `7319`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14831`

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

- `risk_on_high->crypto_major_4h` score `7.1647` n `32` status `ready` deltaP `39.1834` edge `0.3551` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.1647` n `32` status `ready` deltaP `39.1834` edge `0.3551` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `5.8001` n `32` status `ready` deltaP `32.1462` edge `0.2934` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.8001` n `32` status `ready` deltaP `32.1462` edge `0.2934` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.2773` n `32` status `ready` deltaP `17.8585` edge `0.3637` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.2773` n `32` status `ready` deltaP `17.8585` edge `0.3637` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.2495` n `32` status `ready` deltaP `19.9289` edge `0.0518` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.2495` n `32` status `ready` deltaP `19.9289` edge `0.0518` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.1995` n `32` status `ready` deltaP `3.8476` edge `0.0189` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.1995` n `32` status `ready` deltaP `3.8476` edge `0.0189` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.185` n `32` status `ready` deltaP `3.9039` edge `0.0354` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.185` n `32` status `ready` deltaP `3.9039` edge `0.0354` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.0978` n `32` status `ready` deltaP `0.1497` edge `0.0486` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.0978` n `32` status `ready` deltaP `0.1497` edge `0.0486` maxDD `-0.9651`
- `risk_on_high->metal_4h` score `-0.0796` n `32` status `ready` deltaP `0.0474` edge `0.0754` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.0796` n `32` status `ready` deltaP `0.0474` edge `0.0754` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.1847` n `129` status `ready` deltaP `3.7887` edge `0.0` maxDD `-0.5821`
- `market_context_high->unknown_4h` score `-0.6126` n `129` status `ready` deltaP `5.7945` edge `0.1187` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.7464` n `129` status `ready` deltaP `-3.5652` edge `-0.0147` maxDD `-1.5775`
- `market_context_high->index_1h` score `-0.764` n `129` status `ready` deltaP `-4.5603` edge `-0.0067` maxDD `-1.868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
