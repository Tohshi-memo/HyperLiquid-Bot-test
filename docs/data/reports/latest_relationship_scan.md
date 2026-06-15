# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T12:22:29.438106+00:00`
- Price records: `672`
- Market context records: `3991`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10092`

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

- `risk_on_high->unknown_4h` score `147.0466` n `40` status `ready` deltaP `-1.9512` edge `12.4481` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `147.0466` n `40` status `ready` deltaP `-1.9512` edge `12.4481` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `38.1907` n `146` status `ready` deltaP `-5.6982` edge `3.6224` maxDD `-24.1486`
- `market_context_high->unknown_4h` score `22.3637` n `158` status `ready` deltaP `1.9412` edge `2.3916` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.3371` n `40` status `ready` deltaP `42.0139` edge `0.498` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.3371` n `40` status `ready` deltaP `42.0139` edge `0.498` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.9492` n `40` status `ready` deltaP `37.8963` edge `0.0812` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.9492` n `40` status `ready` deltaP `37.8963` edge `0.0812` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.3029` n `146` status `ready` deltaP `16.1316` edge `0.3192` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.1311` n `146` status `ready` deltaP `25.7515` edge `0.2032` maxDD `-7.1159`
- `risk_on_high->index_24h` score `2.8005` n `40` status `ready` deltaP `29.8611` edge `0.0343` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.8005` n `40` status `ready` deltaP `29.8611` edge `0.0343` maxDD `0.0`
- `market_context_high->equity_24h` score `2.4012` n `146` status `ready` deltaP `18.0413` edge `0.3828` maxDD `-14.5715`
- `market_context_high->equity_4h` score `2.2407` n `158` status `ready` deltaP `20.1431` edge `0.1827` maxDD `-7.0879`
- `risk_on_high->crypto_major_4h` score `1.9258` n `40` status `ready` deltaP `20.9756` edge `0.0872` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.9258` n `40` status `ready` deltaP `20.9756` edge `0.0872` maxDD `-2.6576`
- `market_context_high->crypto_major_4h` score `1.5681` n `158` status `ready` deltaP `18.0959` edge `0.1667` maxDD `-7.8662`
- `market_context_high->crypto_major_1h` score `1.3598` n `158` status `ready` deltaP `11.4947` edge `0.0909` maxDD `-2.3372`
- `market_context_high->equity_1h` score `0.9221` n `158` status `ready` deltaP `8.6031` edge `0.0759` maxDD `-2.1799`
- `risk_on_high->commodity_24h` score `0.9219` n `40` status `ready` deltaP `4.1667` edge `0.2772` maxDD `-12.9187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
