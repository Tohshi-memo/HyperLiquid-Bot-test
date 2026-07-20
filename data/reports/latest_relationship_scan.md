# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T06:22:31.064259+00:00`
- Price records: `672`
- Market context records: `7327`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14722`

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

- `risk_on_high->crypto_major_4h` score `7.2959` n `32` status `ready` deltaP `39.8628` edge `0.3615` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.2959` n `32` status `ready` deltaP `39.8628` edge `0.3615` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `6.0127` n `32` status `ready` deltaP `33.003` edge `0.3054` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `6.0127` n `32` status `ready` deltaP `33.003` edge `0.3054` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.3374` n `32` status `ready` deltaP `18.4451` edge `0.3648` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.3374` n `32` status `ready` deltaP `18.4451` edge `0.3648` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.3127` n `32` status `ready` deltaP `20.5277` edge `0.0559` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.3127` n `32` status `ready` deltaP `20.5277` edge `0.0559` maxDD `-0.957`
- `risk_on_high->equity_1h` score `0.2155` n `32` status `ready` deltaP `4.2042` edge `0.0373` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.2155` n `32` status `ready` deltaP `4.2042` edge `0.0373` maxDD `-1.3497`
- `risk_on_high->commodity_1h` score `0.2139` n `32` status `ready` deltaP `3.9977` edge `0.0191` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2139` n `32` status `ready` deltaP `3.9977` edge `0.0191` maxDD `-0.2339`
- `risk_on_high->crypto_alt_1h` score `0.1983` n `32` status `ready` deltaP `1.0479` edge `0.0555` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.1983` n `32` status `ready` deltaP `1.0479` edge `0.0555` maxDD `-0.9651`
- `risk_on_high->metal_4h` score `0.0014` n `32` status `ready` deltaP `0.6098` edge `0.0784` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `0.0014` n `32` status `ready` deltaP `0.6098` edge `0.0784` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.152` n `129` status `ready` deltaP `4.3893` edge `0.0002` maxDD `-0.5821`
- `market_context_high->unknown_4h` score `-0.5735` n `129` status `ready` deltaP `6.3811` edge `0.1198` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.737` n `129` status `ready` deltaP `-3.4151` edge `-0.0145` maxDD `-1.5775`
- `market_context_high->crypto_major_1h` score `-0.7764` n `129` status `ready` deltaP `3.6915` edge `0.0169` maxDD `-7.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
