# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T12:52:38.230645+00:00`
- Price records: `672`
- Market context records: `3993`
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

- `risk_on_high->unknown_4h` score `147.0538` n `40` status `ready` deltaP `-1.9512` edge `12.4487` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `147.0538` n `40` status `ready` deltaP `-1.9512` edge `12.4487` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `39.959` n `144` status `ready` deltaP `-5.2083` edge `3.7665` maxDD `-24.1486`
- `market_context_high->unknown_4h` score `22.9277` n `156` status `ready` deltaP `1.4462` edge `2.4419` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.3251` n `40` status `ready` deltaP `42.0139` edge `0.497` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.3251` n `40` status `ready` deltaP `42.0139` edge `0.497` maxDD `0.0`
- `risk_on_high->equity_4h` score `4.0132` n `40` status `ready` deltaP `38.2012` edge `0.0845` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `4.0132` n `40` status `ready` deltaP `38.2012` edge `0.0845` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.209` n `144` status `ready` deltaP `15.7986` edge `0.3136` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.0786` n `144` status `ready` deltaP `25.6944` edge `0.1992` maxDD `-7.1159`
- `risk_on_high->index_24h` score `2.7885` n `40` status `ready` deltaP `29.8611` edge `0.0333` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7885` n `40` status `ready` deltaP `29.8611` edge `0.0333` maxDD `0.0`
- `market_context_high->equity_24h` score `2.2497` n `144` status `ready` deltaP `17.7083` edge `0.3724` maxDD `-14.5715`
- `market_context_high->equity_4h` score `2.1999` n `156` status `ready` deltaP `20.1884` edge `0.179` maxDD `-7.0879`
- `risk_on_high->crypto_major_4h` score `1.9006` n `40` status `ready` deltaP `20.9756` edge `0.0851` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.9006` n `40` status `ready` deltaP `20.9756` edge `0.0851` maxDD `-2.6576`
- `market_context_high->crypto_major_4h` score `1.3474` n `156` status `ready` deltaP `17.7064` edge `0.1509` maxDD `-7.8662`
- `market_context_high->crypto_major_1h` score `1.2285` n `156` status `ready` deltaP `11.0241` edge `0.0831` maxDD `-2.3372`
- `market_context_high->equity_1h` score `0.9724` n `156` status `ready` deltaP `8.9475` edge `0.0778` maxDD `-2.1799`
- `risk_on_high->commodity_24h` score `0.9591` n `40` status `ready` deltaP `4.1667` edge `0.2803` maxDD `-12.9187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
