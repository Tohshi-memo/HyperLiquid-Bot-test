# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T06:37:36.228572+00:00`
- Price records: `672`
- Market context records: `3967`
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

- `risk_on_high->unknown_4h` score `148.1317` n `40` status `ready` deltaP `1.0976` edge `12.5182` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `148.1317` n `40` status `ready` deltaP `1.0976` edge `12.5182` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `35.0946` n `146` status `ready` deltaP `-7.1847` edge `3.5467` maxDD `-37.9399`
- `market_context_high->unknown_4h` score `21.3934` n `160` status `ready` deltaP `1.7226` edge `2.3122` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.0407` n `40` status `ready` deltaP `42.0139` edge `0.4733` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0407` n `40` status `ready` deltaP `42.0139` edge `0.4733` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4543` n `40` status `ready` deltaP `37.439` edge `0.043` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.4543` n `40` status `ready` deltaP `37.439` edge `0.043` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.1877` n `146` status `ready` deltaP `16.1316` edge `0.3096` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.0603` n `146` status `ready` deltaP `25.7515` edge `0.1973` maxDD `-7.1159`
- `risk_on_high->index_24h` score `2.7357` n `40` status `ready` deltaP `29.8611` edge `0.0289` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7357` n `40` status `ready` deltaP `29.8611` edge `0.0289` maxDD `0.0`
- `market_context_high->equity_4h` score `2.3671` n `160` status `ready` deltaP `19.939` edge `0.1946` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.2831` n `160` status `ready` deltaP `19.8933` edge `0.2143` maxDD `-7.8662`
- `market_context_high->equity_24h` score `2.1684` n `146` status `ready` deltaP `18.0413` edge `0.3634` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `1.7212` n `40` status `ready` deltaP `20.5183` edge `0.0732` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.7212` n `40` status `ready` deltaP `20.5183` edge `0.0732` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.634` n `166` status `ready` deltaP `12.6578` edge `0.106` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.1391` n `166` status `ready` deltaP `9.9813` edge `0.0848` maxDD `-2.1799`
- `market_context_high->metal_1h` score `1.1217` n `166` status `ready` deltaP `12.9392` edge `0.0666` maxDD `-2.751`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
