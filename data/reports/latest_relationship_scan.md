# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T02:37:35.888186+00:00`
- Price records: `672`
- Market context records: `3951`
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

- `risk_on_high->unknown_4h` score `144.0404` n `41` status `ready` deltaP `2.5915` edge `12.1673` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `144.0404` n `41` status `ready` deltaP `2.5915` edge `12.1673` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `19.857` n `156` status `ready` deltaP `-9.2014` edge `2.7976` maxDD `-75.5205`
- `market_context_high->unknown_4h` score `18.8605` n `167` status `ready` deltaP `-1.4541` edge `2.1223` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.2483` n `41` status `ready` deltaP `42.0139` edge `0.4906` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2483` n `41` status `ready` deltaP `42.0139` edge `0.4906` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.3988` n `41` status `ready` deltaP `36.2805` edge `0.0461` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.3988` n `41` status `ready` deltaP `36.2805` edge `0.0461` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.3514` n `156` status `ready` deltaP `17.6683` edge `0.313` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.3406` n `156` status `ready` deltaP `26.0149` edge `0.2189` maxDD `-7.1159`
- `market_context_high->equity_24h` score `3.0893` n `156` status `ready` deltaP `19.578` edge `0.4299` maxDD `-14.5715`
- `risk_on_high->index_24h` score `2.8677` n `41` status `ready` deltaP `29.8611` edge `0.0399` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.8677` n `41` status `ready` deltaP `29.8611` edge `0.0399` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.069` n `167` status `ready` deltaP `19.2867` edge `0.2005` maxDD `-7.8662`
- `risk_on_high->crypto_major_4h` score `1.9125` n `41` status `ready` deltaP `21.7987` edge `0.0806` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.9125` n `41` status `ready` deltaP `21.7987` edge `0.0806` maxDD `-2.6576`
- `market_context_high->equity_4h` score `1.8197` n `167` status `ready` deltaP `17.2064` edge `0.1672` maxDD `-7.0879`
- `market_context_high->metal_1h` score `0.7616` n `169` status `ready` deltaP `11.1177` edge `0.0529` maxDD `-2.751`
- `market_context_high->crypto_major_1h` score `0.715` n `169` status `ready` deltaP `11.0823` edge `0.0845` maxDD `-4.904`
- `risk_on_high->commodity_24h` score `0.6191` n `41` status `ready` deltaP `3.5569` edge `0.2688` maxDD `-13.9406`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
