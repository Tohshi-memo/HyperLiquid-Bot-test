# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T07:07:31.262163+00:00`
- Price records: `672`
- Market context records: `3969`
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

- `risk_on_high->unknown_4h` score `147.6515` n `40` status `ready` deltaP `0.9451` edge `12.4788` maxDD `-10.7978`
- `risk_on_and_context->unknown_4h` score `147.6515` n `40` status `ready` deltaP `0.9451` edge `12.4788` maxDD `-10.7978`
- `market_context_high->unknown_24h` score `33.4932` n `148` status `ready` deltaP `-6.4002` edge `3.4063` maxDD `-37.8025`
- `market_context_high->unknown_4h` score `20.6876` n `162` status `ready` deltaP `1.4698` edge `2.2537` maxDD `-35.496`
- `risk_on_high->equity_24h` score `9.0983` n `40` status `ready` deltaP `42.0139` edge `0.4781` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0983` n `40` status `ready` deltaP `42.0139` edge `0.4781` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4843` n `40` status `ready` deltaP `37.439` edge `0.0455` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.4843` n `40` status `ready` deltaP `37.439` edge `0.0455` maxDD `-0.0458`
- `market_context_high->index_24h` score `3.1704` n `148` status `ready` deltaP `25.807` edge `0.2061` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.1527` n `148` status `ready` deltaP `16.9576` edge `0.2888` maxDD `-8.1303`
- `risk_on_high->index_24h` score `2.7513` n `40` status `ready` deltaP `29.8611` edge `0.0302` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7513` n `40` status `ready` deltaP `29.8611` edge `0.0302` maxDD `0.0`
- `market_context_high->equity_24h` score `2.4571` n `148` status `ready` deltaP `18.3653` edge `0.3853` maxDD `-14.5715`
- `market_context_high->equity_4h` score `2.3905` n `162` status `ready` deltaP `20.1859` edge `0.1949` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.2783` n `162` status `ready` deltaP `20.0881` edge `0.2126` maxDD `-7.8662`
- `risk_on_high->crypto_major_4h` score `1.703` n `40` status `ready` deltaP `20.3659` edge `0.0727` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.703` n `40` status `ready` deltaP `20.3659` edge `0.0727` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.6568` n `166` status `ready` deltaP `12.8075` edge `0.1069` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.1607` n `166` status `ready` deltaP `9.9813` edge `0.0866` maxDD `-2.1799`
- `market_context_high->metal_1h` score `1.0002` n `166` status `ready` deltaP `13.9907` edge `0.0634` maxDD `-2.8655`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
