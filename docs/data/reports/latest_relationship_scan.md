# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T13:07:35.900116+00:00`
- Price records: `672`
- Market context records: `3994`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10098`

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

- `risk_on_high->unknown_4h` score `147.0514` n `40` status `ready` deltaP `-1.9512` edge `12.4485` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `147.0514` n `40` status `ready` deltaP `-1.9512` edge `12.4485` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `40.8721` n `143` status `ready` deltaP `-4.9546` edge `3.8409` maxDD `-24.1486`
- `market_context_high->unknown_4h` score `23.2351` n `155` status `ready` deltaP `1.194` edge `2.4692` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.3155` n `40` status `ready` deltaP `42.0139` edge `0.4962` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.3155` n `40` status `ready` deltaP `42.0139` edge `0.4962` maxDD `0.0`
- `risk_on_high->equity_4h` score `4.0422` n `40` status `ready` deltaP `38.3537` edge `0.0859` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `4.0422` n `40` status `ready` deltaP `38.3537` edge `0.0859` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.1559` n `143` status `ready` deltaP `15.6287` edge `0.3103` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.057` n `143` status `ready` deltaP `25.6653` edge `0.1976` maxDD `-7.1159`
- `risk_on_high->index_24h` score `2.7813` n `40` status `ready` deltaP `29.8611` edge `0.0327` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7813` n `40` status `ready` deltaP `29.8611` edge `0.0327` maxDD `0.0`
- `market_context_high->equity_4h` score `2.1823` n `155` status `ready` deltaP `20.2085` edge `0.1774` maxDD `-7.0879`
- `market_context_high->equity_24h` score `2.1785` n `143` status `ready` deltaP `17.5384` edge `0.3676` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `1.8658` n `40` status `ready` deltaP `20.9756` edge `0.0822` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.8658` n `40` status `ready` deltaP `20.9756` edge `0.0822` maxDD `-2.6576`
- `market_context_high->crypto_major_4h` score `1.2799` n `155` status `ready` deltaP `17.5079` edge `0.1466` maxDD `-7.8662`
- `market_context_high->crypto_major_1h` score `1.1854` n `155` status `ready` deltaP `10.7842` edge `0.0811` maxDD `-2.3372`
- `market_context_high->metal_1h` score `1.0316` n `155` status `ready` deltaP `11.8428` edge `0.0571` maxDD `-2.0066`
- `market_context_high->equity_1h` score `1.0218` n `155` status `ready` deltaP `9.3694` edge `0.0791` maxDD `-2.1799`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
