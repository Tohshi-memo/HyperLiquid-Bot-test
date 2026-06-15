# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T09:37:34.491723+00:00`
- Price records: `672`
- Market context records: `3979`
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

- `risk_on_high->unknown_4h` score `147.7207` n `40` status `ready` deltaP `-0.2744` edge `12.4931` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `147.7207` n `40` status `ready` deltaP `-0.2744` edge `12.4931` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `29.379` n `153` status `ready` deltaP `-7.1998` edge `3.0705` maxDD `-37.9399`
- `market_context_high->unknown_4h` score `19.2672` n `166` status `ready` deltaP `0.6593` edge `2.1421` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.2255` n `40` status `ready` deltaP `42.0139` edge `0.4887` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2255` n `40` status `ready` deltaP `42.0139` edge `0.4887` maxDD `0.0`
- `market_context_high->metal_24h` score `3.717` n `153` status `ready` deltaP `17.2284` edge `0.3464` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `3.6846` n `40` status `ready` deltaP `37.439` edge `0.0622` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.6846` n `40` status `ready` deltaP `37.439` edge `0.0622` maxDD `-0.0458`
- `market_context_high->index_24h` score `3.4354` n `153` status `ready` deltaP `25.9395` edge `0.2273` maxDD `-7.1159`
- `market_context_high->equity_24h` score `3.1225` n `153` status `ready` deltaP `19.1381` edge `0.4356` maxDD `-14.5715`
- `risk_on_high->index_24h` score `2.7849` n `40` status `ready` deltaP `29.8611` edge `0.033` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7849` n `40` status `ready` deltaP `29.8611` edge `0.033` maxDD `0.0`
- `market_context_high->equity_4h` score `2.5618` n `166` status `ready` deltaP `20.6619` edge `0.206` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.2733` n `166` status `ready` deltaP `19.5599` edge `0.2157` maxDD `-7.8662`
- `risk_on_high->crypto_major_4h` score `1.8898` n `40` status `ready` deltaP `20.9756` edge `0.0842` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.8898` n `40` status `ready` deltaP `20.9756` edge `0.0842` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.6245` n `166` status `ready` deltaP `12.5081` edge `0.1062` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.1512` n `166` status `ready` deltaP `9.6819` edge `0.0878` maxDD `-2.1799`
- `market_context_high->crypto_alt_4h` score `1.0218` n `166` status `ready` deltaP `13.6369` edge `0.1247` maxDD `-7.1038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
