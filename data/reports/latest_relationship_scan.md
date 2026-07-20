# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T07:22:25.734577+00:00`
- Price records: `672`
- Market context records: `7331`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14728`

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

- `risk_on_high->crypto_major_4h` score `7.4177` n `32` status `ready` deltaP `40.3201` edge `0.3686` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.4177` n `32` status `ready` deltaP `40.3201` edge `0.3686` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `6.1502` n `32` status `ready` deltaP `33.6128` edge `0.3128` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `6.1502` n `32` status `ready` deltaP `33.6128` edge `0.3128` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.4162` n `32` status `ready` deltaP `19.0549` edge `0.3673` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.4162` n `32` status `ready` deltaP `19.0549` edge `0.3673` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.329` n `32` status `ready` deltaP `20.6774` edge `0.057` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.329` n `32` status `ready` deltaP `20.6774` edge `0.057` maxDD `-0.957`
- `risk_on_high->equity_1h` score `0.2123` n `32` status `ready` deltaP `4.2042` edge `0.0369` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.2123` n `32` status `ready` deltaP `4.2042` edge `0.0369` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.2076` n `32` status `ready` deltaP `1.1976` edge `0.0557` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.2076` n `32` status `ready` deltaP `1.1976` edge `0.0557` maxDD `-0.9651`
- `risk_on_high->commodity_1h` score `0.1947` n `32` status `ready` deltaP `3.8476` edge `0.0185` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.1947` n `32` status `ready` deltaP `3.8476` edge `0.0185` maxDD `-0.2339`
- `risk_on_high->metal_4h` score `0.0813` n `32` status `ready` deltaP `1.2195` edge `0.081` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `0.0813` n `32` status `ready` deltaP `1.2195` edge `0.081` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.1691` n `129` status `ready` deltaP `4.089` edge `0.0` maxDD `-0.5821`
- `market_context_high->unknown_4h` score `-0.5223` n `129` status `ready` deltaP `6.9909` edge `0.1223` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.7495` n `129` status `ready` deltaP `-3.5652` edge `-0.0151` maxDD `-1.5775`
- `market_context_high->crypto_major_1h` score `-0.76` n `129` status `ready` deltaP `3.8412` edge `0.018` maxDD `-7.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
