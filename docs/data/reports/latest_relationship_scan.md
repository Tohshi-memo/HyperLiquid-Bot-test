# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T06:22:38.826455+00:00`
- Price records: `672`
- Market context records: `3966`
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

- `risk_on_high->unknown_4h` score `148.1523` n `40` status `ready` deltaP `1.25` edge `12.5189` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `148.1523` n `40` status `ready` deltaP `1.25` edge `12.5189` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `35.8924` n `145` status `ready` deltaP `-7.3228` edge `3.6141` maxDD `-37.9399`
- `market_context_high->unknown_4h` score `21.7037` n `159` status `ready` deltaP `1.6116` edge `2.3388` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.0047` n `40` status `ready` deltaP `42.0139` edge `0.4703` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0047` n `40` status `ready` deltaP `42.0139` edge `0.4703` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4411` n `40` status `ready` deltaP `37.439` edge `0.0419` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.4411` n `40` status `ready` deltaP `37.439` edge `0.0419` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.0929` n `145` status `ready` deltaP `15.9663` edge `0.3028` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.0161` n `145` status `ready` deltaP `25.7232` edge `0.1938` maxDD `-7.1159`
- `risk_on_high->index_24h` score `2.7213` n `40` status `ready` deltaP `29.8611` edge `0.0277` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7213` n `40` status `ready` deltaP `29.8611` edge `0.0277` maxDD `0.0`
- `market_context_high->equity_4h` score `2.3607` n `159` status `ready` deltaP `19.8132` edge `0.1949` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.3371` n `159` status `ready` deltaP `20.1929` edge `0.2168` maxDD `-7.8662`
- `market_context_high->equity_24h` score `2.0208` n `145` status `ready` deltaP `17.876` edge `0.3522` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `1.7066` n `40` status `ready` deltaP `20.3659` edge `0.073` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.7066` n `40` status `ready` deltaP `20.3659` edge `0.073` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.6173` n `166` status `ready` deltaP `12.5081` edge `0.1056` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.1163` n `166` status `ready` deltaP `9.8316` edge `0.0839` maxDD `-2.1799`
- `market_context_high->metal_1h` score `1.1037` n `166` status `ready` deltaP `12.7895` edge `0.0661` maxDD `-2.751`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
