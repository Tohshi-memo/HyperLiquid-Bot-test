# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T10:22:31.498346+00:00`
- Price records: `672`
- Market context records: `7344`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14631`

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

- `risk_on_high->crypto_major_4h` score `7.3537` n `32` status `ready` deltaP `40.0152` edge `0.3653` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.3537` n `32` status `ready` deltaP `40.0152` edge `0.3653` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `6.0357` n `32` status `ready` deltaP `33.1555` edge `0.3063` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `6.0357` n `32` status `ready` deltaP `33.1555` edge `0.3063` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.4162` n `32` status `ready` deltaP `19.0549` edge `0.3673` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.4162` n `32` status `ready` deltaP `19.0549` edge `0.3673` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.2986` n `32` status `ready` deltaP `20.5277` edge `0.0541` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.2986` n `32` status `ready` deltaP `20.5277` edge `0.0541` maxDD `-0.957`
- `risk_on_high->equity_1h` score `0.2319` n `32` status `ready` deltaP `4.6547` edge `0.0364` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.2319` n `32` status `ready` deltaP `4.6547` edge `0.0364` maxDD `-1.3497`
- `risk_on_high->commodity_1h` score `0.2283` n `32` status `ready` deltaP `3.9977` edge `0.0203` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2283` n `32` status `ready` deltaP `3.9977` edge `0.0203` maxDD `-0.2339`
- `risk_on_high->crypto_alt_1h` score `0.1803` n `32` status `ready` deltaP `1.1976` edge `0.0522` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.1803` n `32` status `ready` deltaP `1.1976` edge `0.0522` maxDD `-0.9651`
- `risk_on_high->metal_4h` score `-0.0146` n `32` status `ready` deltaP `0.3049` edge `0.0791` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.0146` n `32` status `ready` deltaP `0.3049` edge `0.0791` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.1964` n `129` status `ready` deltaP `3.6386` edge `-0.0005` maxDD `-0.5821`
- `market_context_high->unknown_4h` score `-0.5223` n `129` status `ready` deltaP `6.9909` edge `0.1223` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.7276` n `129` status `ready` deltaP `-3.4151` edge `-0.0133` maxDD `-1.5775`
- `market_context_high->index_1h` score `-0.7796` n `129` status `ready` deltaP `-4.8606` edge `-0.0067` maxDD `-1.868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
