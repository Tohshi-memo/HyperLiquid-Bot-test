# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T04:07:25.458095+00:00`
- Price records: `672`
- Market context records: `7317`
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

- `risk_on_high->crypto_major_4h` score `7.8643` n `31` status `ready` deltaP `41.9551` edge `0.3836` maxDD `-0.3018`
- `risk_on_and_context->crypto_major_4h` score `7.8643` n `31` status `ready` deltaP `41.9551` edge `0.3836` maxDD `-0.3018`
- `risk_on_high->crypto_alt_4h` score `6.3845` n `31` status `ready` deltaP `34.363` edge `0.3202` maxDD `-0.3794`
- `risk_on_and_context->crypto_alt_4h` score `6.3845` n `31` status `ready` deltaP `34.363` edge `0.3202` maxDD `-0.3794`
- `risk_on_high->unknown_4h` score `5.5818` n `31` status `ready` deltaP `19.3695` edge `0.379` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.5818` n `31` status `ready` deltaP `19.3695` edge `0.379` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.2355` n `32` status `ready` deltaP `19.7792` edge `0.051` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.2355` n `32` status `ready` deltaP `19.7792` edge `0.051` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.2007` n `32` status `ready` deltaP `3.8476` edge `0.019` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2007` n `32` status `ready` deltaP `3.8476` edge `0.019` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.2006` n `32` status `ready` deltaP `4.0541` edge `0.0364` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.2006` n `32` status `ready` deltaP `4.0541` edge `0.0364` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.0682` n `32` status `ready` deltaP `-0.1497` edge `0.0468` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.0682` n `32` status `ready` deltaP `-0.1497` edge `0.0468` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.1925` n `129` status `ready` deltaP `3.6386` edge `0.0` maxDD `-0.5821`
- `risk_on_high->metal_4h` score `-0.2308` n `31` status `ready` deltaP `-1.7671` edge `0.0749` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.2308` n `31` status `ready` deltaP `-1.7671` edge `0.0749` maxDD `-0.5882`
- `market_context_high->unknown_4h` score `-0.5649` n `127` status `ready` deltaP `6.1869` edge `0.1222` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.7456` n `129` status `ready` deltaP `-3.5652` edge `-0.0146` maxDD `-1.5775`
- `market_context_high->index_1h` score `-0.7547` n `129` status `ready` deltaP `-4.4102` edge `-0.0065` maxDD `-1.868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
