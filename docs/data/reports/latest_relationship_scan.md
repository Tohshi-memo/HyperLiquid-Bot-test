# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T03:22:29.515290+00:00`
- Price records: `672`
- Market context records: `3954`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11267`

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

- `risk_on_high->unknown_4h` score `144.0452` n `41` status `ready` deltaP `2.5915` edge `12.1677` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `144.0452` n `41` status `ready` deltaP `2.5915` edge `12.1677` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `23.9813` n `153` status `ready` deltaP `-8.7418` edge `3.0085` maxDD `-66.1424`
- `market_context_high->unknown_4h` score `19.8498` n `164` status `ready` deltaP `-0.4573` edge `2.1981` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.2015` n `41` status `ready` deltaP `42.0139` edge `0.4867` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2015` n `41` status `ready` deltaP `42.0139` edge `0.4867` maxDD `0.0`
- `market_context_high->index_24h` score `3.3022` n `153` status `ready` deltaP `25.9395` edge `0.2162` maxDD `-7.1159`
- `risk_on_high->equity_4h` score `3.2782` n `41` status `ready` deltaP `35.8232` edge `0.0391` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.2782` n `41` status `ready` deltaP `35.8232` edge `0.0391` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.2598` n `153` status `ready` deltaP `17.2284` edge `0.3083` maxDD `-9.1203`
- `market_context_high->equity_24h` score `2.9185` n `153` status `ready` deltaP `19.1381` edge `0.4186` maxDD `-14.5715`
- `risk_on_high->index_24h` score `2.8485` n `41` status `ready` deltaP `29.8611` edge `0.0383` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.8485` n `41` status `ready` deltaP `29.8611` edge `0.0383` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.2318` n `164` status `ready` deltaP `20.1219` edge `0.2085` maxDD `-7.8662`
- `market_context_high->equity_4h` score `2.0864` n `164` status `ready` deltaP `18.1402` edge `0.1832` maxDD `-7.0879`
- `risk_on_high->crypto_major_4h` score `1.8231` n `41` status `ready` deltaP `21.3414` edge `0.0762` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.8231` n `41` status `ready` deltaP `21.3414` edge `0.0762` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `0.9763` n `168` status `ready` deltaP `11.3024` edge `0.088` maxDD `-4.226`
- `market_context_high->metal_1h` score `0.8017` n `168` status `ready` deltaP `11.4699` edge `0.0539` maxDD `-2.751`
- `market_context_high->crypto_alt_4h` score `0.6512` n `164` status `ready` deltaP `12.5` edge `0.1014` maxDD `-7.1038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
