# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T05:52:30.189366+00:00`
- Price records: `672`
- Market context records: `3964`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10240`

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

- `risk_on_high->unknown_4h` score `148.185` n `40` status `ready` deltaP `1.5549` edge `12.5196` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `148.185` n `40` status `ready` deltaP `1.5549` edge `12.5196` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `36.6881` n `144` status `ready` deltaP `-7.2916` edge `3.6802` maxDD `-37.9399`
- `market_context_high->unknown_4h` score `22.02` n `158` status `ready` deltaP `1.6498` edge `2.3649` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `8.9363` n `40` status `ready` deltaP `42.0139` edge `0.4646` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.9363` n `40` status `ready` deltaP `42.0139` edge `0.4646` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4087` n `40` status `ready` deltaP `37.439` edge `0.0392` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.4087` n `40` status `ready` deltaP `37.439` edge `0.0392` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.0002` n `144` status `ready` deltaP `15.7986` edge `0.2962` maxDD `-9.1203`
- `market_context_high->index_24h` score `2.949` n `144` status `ready` deltaP `25.6944` edge `0.1884` maxDD `-7.1159`
- `risk_on_high->index_24h` score `2.6997` n `40` status `ready` deltaP `29.8611` edge `0.0259` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.6997` n `40` status `ready` deltaP `29.8611` edge `0.0259` maxDD `0.0`
- `market_context_high->equity_4h` score `2.3253` n `158` status `ready` deltaP `19.6858` edge `0.1928` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.3243` n `158` status `ready` deltaP `20.0178` edge `0.2169` maxDD `-7.8662`
- `market_context_high->equity_24h` score `1.8393` n `144` status `ready` deltaP `17.7083` edge `0.3382` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `1.6874` n `40` status `ready` deltaP `20.3659` edge `0.0714` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6874` n `40` status `ready` deltaP `20.3659` edge `0.0714` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.5933` n `166` status `ready` deltaP `12.3584` edge `0.1046` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.084` n `166` status `ready` deltaP `9.5322` edge `0.0832` maxDD `-2.1799`
- `market_context_high->metal_1h` score `1.0701` n `166` status `ready` deltaP `12.6398` edge `0.0643` maxDD `-2.751`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
