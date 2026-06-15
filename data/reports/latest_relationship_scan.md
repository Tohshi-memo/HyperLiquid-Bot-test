# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T05:35:57.790781+00:00`
- Price records: `672`
- Market context records: `3963`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11256`

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

- `risk_on_high->unknown_4h` score `148.2116` n `40` status `ready` deltaP `1.7073` edge `12.5208` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `148.2116` n `40` status `ready` deltaP `1.7073` edge `12.5208` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `36.8412` n `144` status `ready` deltaP `-7.118` edge `3.6918` maxDD `-37.9399`
- `market_context_high->unknown_4h` score `22.2866` n `157` status `ready` deltaP `1.5321` edge `2.3879` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `8.9063` n `40` status `ready` deltaP `42.0139` edge `0.4621` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.9063` n `40` status `ready` deltaP `42.0139` edge `0.4621` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.3942` n `40` status `ready` deltaP `37.439` edge `0.038` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.3942` n `40` status `ready` deltaP `37.439` edge `0.038` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.0026` n `144` status `ready` deltaP `15.7986` edge `0.2964` maxDD `-9.1203`
- `market_context_high->index_24h` score `2.937` n `144` status `ready` deltaP `25.6944` edge `0.1874` maxDD `-7.1159`
- `risk_on_high->index_24h` score `2.6877` n `40` status `ready` deltaP `29.8611` edge `0.0249` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.6877` n `40` status `ready` deltaP `29.8611` edge `0.0249` maxDD `0.0`
- `market_context_high->equity_4h` score `2.3186` n `157` status `ready` deltaP `19.5568` edge `0.1931` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.3017` n `157` status `ready` deltaP `19.8404` edge `0.2162` maxDD `-7.8662`
- `market_context_high->equity_24h` score `1.8093` n `144` status `ready` deltaP `17.7083` edge `0.3357` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `1.6718` n `40` status `ready` deltaP `20.3659` edge `0.0701` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6718` n `40` status `ready` deltaP `20.3659` edge `0.0701` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.5765` n `166` status `ready` deltaP `12.3584` edge `0.1032` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.0672` n `166` status `ready` deltaP `9.3825` edge `0.0828` maxDD `-2.1799`
- `market_context_high->metal_1h` score `1.0402` n `166` status `ready` deltaP `12.4901` edge `0.0628` maxDD `-2.751`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
