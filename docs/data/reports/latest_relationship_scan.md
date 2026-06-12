# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T12:07:28.077376+00:00`
- Price records: `672`
- Market context records: `3684`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12897`

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

- `risk_on_high->crypto_major_24h` score `32.3744` n `32` status `ready` deltaP `36.1111` edge `2.4614` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `32.3744` n `32` status `ready` deltaP `36.1111` edge `2.4614` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.0314` n `32` status `ready` deltaP `38.3681` edge `1.9135` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.0314` n `32` status `ready` deltaP `38.3681` edge `1.9135` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `24.1142` n `32` status `ready` deltaP `35.2431` edge `1.7897` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `24.1142` n `32` status `ready` deltaP `35.2431` edge `1.7897` maxDD `-0.8779`
- `risk_on_high->index_24h` score `14.3068` n `32` status `ready` deltaP `38.1944` edge `0.9376` maxDD `0.0`
- `risk_on_and_context->index_24h` score `14.3068` n `32` status `ready` deltaP `38.1944` edge `0.9376` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.8771` n `32` status `ready` deltaP `19.2073` edge `0.8906` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.8771` n `32` status `ready` deltaP `19.2073` edge `0.8906` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `5.1976` n `32` status `ready` deltaP `23.7847` edge `0.3007` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `5.1976` n `32` status `ready` deltaP `23.7847` edge `0.3007` maxDD `-0.7574`
- `market_context_high->index_24h` score `3.9107` n `157` status `ready` deltaP `23.5447` edge `0.3405` maxDD `-11.3924`
- `risk_on_high->equity_4h` score `2.1927` n `32` status `ready` deltaP `9.0701` edge `0.3341` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.1927` n `32` status `ready` deltaP `9.0701` edge `0.3341` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `2.0197` n `32` status `ready` deltaP `-0.686` edge `0.3573` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.0197` n `32` status `ready` deltaP `-0.686` edge `0.3573` maxDD `-11.7537`
- `market_context_high->equity_24h` score `1.7435` n `157` status `ready` deltaP `15.4382` edge `0.6088` maxDD `-35.3144`
- `risk_on_high->crypto_major_1h` score `1.2051` n `32` status `ready` deltaP `2.5262` edge `0.2446` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.2051` n `32` status `ready` deltaP `2.5262` edge `0.2446` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
