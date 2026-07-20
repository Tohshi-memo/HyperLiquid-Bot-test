# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T03:52:29.006182+00:00`
- Price records: `672`
- Market context records: `7316`
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

- `risk_on_high->crypto_major_4h` score `8.423` n `30` status `ready` deltaP `45.0734` edge `0.4072` maxDD `-0.1288`
- `risk_on_and_context->crypto_major_4h` score `8.423` n `30` status `ready` deltaP `45.0734` edge `0.4072` maxDD `-0.1288`
- `risk_on_high->crypto_alt_4h` score `6.7974` n `30` status `ready` deltaP `36.8993` edge `0.3377` maxDD `-0.3794`
- `risk_on_and_context->crypto_alt_4h` score `6.7974` n `30` status `ready` deltaP `36.8993` edge `0.3377` maxDD `-0.3794`
- `risk_on_high->unknown_4h` score `5.3237` n `30` status `ready` deltaP `18.1235` edge `0.3658` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.3237` n `30` status `ready` deltaP `18.1235` edge `0.3658` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.2386` n `32` status `ready` deltaP `19.7792` edge `0.0514` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.2386` n `32` status `ready` deltaP `19.7792` edge `0.0514` maxDD `-0.957`
- `risk_on_high->equity_1h` score `0.2139` n `32` status `ready` deltaP `4.2042` edge `0.0371` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.2139` n `32` status `ready` deltaP `4.2042` edge `0.0371` maxDD `-1.3497`
- `risk_on_high->commodity_1h` score `0.2139` n `32` status `ready` deltaP `3.9977` edge `0.0191` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2139` n `32` status `ready` deltaP `3.9977` edge `0.0191` maxDD `-0.2339`
- `risk_on_high->crypto_alt_1h` score `0.0697` n `32` status `ready` deltaP `-0.1497` edge `0.047` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.0697` n `32` status `ready` deltaP `-0.1497` edge `0.047` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.2004` n `129` status `ready` deltaP `3.4884` edge `0.0` maxDD `-0.5821`
- `risk_on_high->metal_4h` score `-0.4432` n `30` status `ready` deltaP `-3.7026` edge `0.0701` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.4432` n `30` status `ready` deltaP `-3.7026` edge `0.0701` maxDD `-0.5882`
- `market_context_high->unknown_4h` score `-0.6125` n `126` status `ready` deltaP `5.9012` edge `0.118` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.737` n `129` status `ready` deltaP `-3.4151` edge `-0.0145` maxDD `-1.5775`
- `market_context_high->index_1h` score `-0.7461` n `129` status `ready` deltaP `-4.26` edge `-0.0064` maxDD `-1.868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
