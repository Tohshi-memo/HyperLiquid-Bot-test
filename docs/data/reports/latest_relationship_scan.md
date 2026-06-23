# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T04:52:31.659838+00:00`
- Price records: `672`
- Market context records: `4483`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11089`

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

- `risk_on_high->unknown_4h` score `124.121` n `49` status `ready` deltaP `3.4159` edge `10.5037` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.121` n `49` status `ready` deltaP `3.4159` edge `10.5037` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `33.8054` n `224` status `ready` deltaP `3.5046` edge `2.9443` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `15.5394` n `224` status `ready` deltaP `3.2884` edge `1.8195` maxDD `-36.0512`
- `risk_on_high->equity_4h` score `4.3323` n `49` status `ready` deltaP `39.6341` edge `0.0968` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `4.3323` n `49` status `ready` deltaP `39.6341` edge `0.0968` maxDD `0.0`
- `risk_on_high->metal_24h` score `3.0181` n `46` status `ready` deltaP `-13.9116` edge `0.5411` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `3.0181` n `46` status `ready` deltaP `-13.9116` edge `0.5411` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `2.6515` n `49` status `ready` deltaP `21.2419` edge `0.1459` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.6515` n `49` status `ready` deltaP `21.2419` edge `0.1459` maxDD `-2.6576`
- `risk_on_high->unknown_24h` score `2.3569` n `46` status `ready` deltaP `13.7001` edge `0.1854` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `2.3569` n `46` status `ready` deltaP `13.7001` edge `0.1854` maxDD `-5.0928`
- `risk_on_high->index_24h` score `1.6487` n `46` status `ready` deltaP `22.2147` edge `0.007` maxDD `-0.75`
- `risk_on_and_context->index_24h` score `1.6487` n `46` status `ready` deltaP `22.2147` edge `0.007` maxDD `-0.75`
- `risk_on_high->metal_4h` score `1.6388` n `49` status `ready` deltaP `13.3244` edge `0.0813` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.6388` n `49` status `ready` deltaP `13.3244` edge `0.0813` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.1948` n `49` status `ready` deltaP `15.2909` edge `0.0319` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.1948` n `49` status `ready` deltaP `15.2909` edge `0.0319` maxDD `-0.7415`
- `risk_on_high->fx_4h` score `0.6315` n `49` status `ready` deltaP `15.7043` edge `0.007` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.6315` n `49` status `ready` deltaP `15.7043` edge `0.007` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
