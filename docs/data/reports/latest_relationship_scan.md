# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T07:49:50.443282+00:00`
- Price records: `672`
- Market context records: `7333`
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

- `risk_on_high->crypto_major_4h` score `7.4563` n `32` status `ready` deltaP `40.4726` edge `0.3708` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.4563` n `32` status `ready` deltaP `40.4726` edge `0.3708` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `6.1974` n `32` status `ready` deltaP `33.9177` edge `0.3147` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `6.1974` n `32` status `ready` deltaP `33.9177` edge `0.3147` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.4282` n `32` status `ready` deltaP `19.0549` edge `0.3683` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.4282` n `32` status `ready` deltaP `19.0549` edge `0.3683` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.3251` n `32` status `ready` deltaP `20.6774` edge `0.0565` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.3251` n `32` status `ready` deltaP `20.6774` edge `0.0565` maxDD `-0.957`
- `risk_on_high->equity_1h` score `0.2092` n `32` status `ready` deltaP `4.2042` edge `0.0365` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.2092` n `32` status `ready` deltaP `4.2042` edge `0.0365` maxDD `-1.3497`
- `risk_on_high->commodity_1h` score `0.2031` n `32` status `ready` deltaP `3.8476` edge `0.0192` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2031` n `32` status `ready` deltaP `3.8476` edge `0.0192` maxDD `-0.2339`
- `risk_on_high->crypto_alt_1h` score `0.1991` n `32` status `ready` deltaP `1.1976` edge `0.0546` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.1991` n `32` status `ready` deltaP `1.1976` edge `0.0546` maxDD `-0.9651`
- `risk_on_high->metal_4h` score `0.0849` n `32` status `ready` deltaP `1.2195` edge `0.0813` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `0.0849` n `32` status `ready` deltaP `1.2195` edge `0.0813` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.1785` n `129` status `ready` deltaP `3.9389` edge `-0.0002` maxDD `-0.5821`
- `market_context_high->unknown_4h` score `-0.5145` n `129` status `ready` deltaP `6.9909` edge `0.1233` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.744` n `129` status `ready` deltaP `-3.5652` edge `-0.0144` maxDD `-1.5775`
- `market_context_high->crypto_major_1h` score `-0.7639` n `129` status `ready` deltaP `3.8412` edge `0.0175` maxDD `-7.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
