# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T03:37:32.237258+00:00`
- Price records: `672`
- Market context records: `3955`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11179`

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

- `risk_on_high->unknown_4h` score `144.05` n `41` status `ready` deltaP `2.5915` edge `12.1681` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `144.05` n `41` status `ready` deltaP `2.5915` edge `12.1681` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `25.4047` n `152` status `ready` deltaP `-8.58` edge `3.0806` maxDD `-62.8406`
- `market_context_high->unknown_4h` score `20.1987` n `163` status `ready` deltaP `-0.1169` edge `2.2249` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.1895` n `41` status `ready` deltaP `42.0139` edge `0.4857` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.1895` n `41` status `ready` deltaP `42.0139` edge `0.4857` maxDD `0.0`
- `market_context_high->index_24h` score `3.2857` n `152` status `ready` deltaP `25.9137` edge `0.215` maxDD `-7.1159`
- `risk_on_high->equity_4h` score `3.2444` n `41` status `ready` deltaP `35.6708` edge `0.0373` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.2444` n `41` status `ready` deltaP `35.6708` edge `0.0373` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.2358` n `152` status `ready` deltaP `17.0779` edge `0.3073` maxDD `-9.1203`
- `market_context_high->equity_24h` score `2.8453` n `152` status `ready` deltaP `18.9876` edge `0.4135` maxDD `-14.5715`
- `risk_on_high->index_24h` score `2.8401` n `41` status `ready` deltaP `29.8611` edge `0.0376` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.8401` n `41` status `ready` deltaP `29.8611` edge `0.0376` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.2933` n `163` status `ready` deltaP `20.4109` edge `0.2117` maxDD `-7.8662`
- `market_context_high->equity_4h` score `2.1446` n `163` status `ready` deltaP `18.4629` edge `0.1859` maxDD `-7.0879`
- `risk_on_high->crypto_major_4h` score `1.7965` n `41` status `ready` deltaP `21.189` edge `0.075` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.7965` n `41` status `ready` deltaP `21.189` edge `0.075` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.2362` n `168` status `ready` deltaP `11.3024` edge `0.0925` maxDD `-3.1864`
- `market_context_high->metal_1h` score `0.7409` n `168` status `ready` deltaP `11.0244` edge `0.0518` maxDD `-2.751`
- `market_context_high->crypto_alt_4h` score `0.6906` n `163` status `ready` deltaP `12.7666` edge `0.1029` maxDD `-7.1038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
