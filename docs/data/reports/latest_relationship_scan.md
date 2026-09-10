# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T00:52:31.807631+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9978`

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

- `risk_on_high->crypto_alt_24h` score `13.8733` n `115` status `ready` deltaP `27.9439` edge `0.9928` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.8733` n `115` status `ready` deltaP `27.9439` edge `0.9928` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `8.7909` n `237` status `ready` deltaP `20.4774` edge `0.6788` maxDD `-3.9523`
- `risk_on_high->crypto_major_24h` score `7.4215` n `115` status `ready` deltaP `23.214` edge `1.2035` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.4215` n `115` status `ready` deltaP `23.214` edge `1.2035` maxDD `-24.5429`
- `risk_on_high->crypto_alt_4h` score `7.0127` n `115` status `ready` deltaP `36.3534` edge `0.3792` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.0127` n `115` status `ready` deltaP `36.3534` edge `0.3792` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.8903` n `115` status `ready` deltaP `26.2341` edge `0.3185` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8903` n `115` status `ready` deltaP `26.2341` edge `0.3185` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.8356` n `115` status `ready` deltaP `28.2941` edge `0.0519` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.8356` n `115` status `ready` deltaP `28.2941` edge `0.0519` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.172` n `237` status `ready` deltaP `11.8056` edge `0.1023` maxDD `0.0`
- `market_context_high->index_24h` score `2.1112` n `237` status `ready` deltaP `23.3079` edge `0.0599` maxDD `-0.1483`
- `risk_on_high->equity_24h` score `1.4568` n `115` status `ready` deltaP `11.8056` edge `0.0427` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.4568` n `115` status `ready` deltaP `11.8056` edge `0.0427` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.1413` n `115` status `ready` deltaP `4.4611` edge `0.1006` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.1413` n `115` status `ready` deltaP `4.4611` edge `0.1006` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.7148` n `115` status `ready` deltaP `19.218` edge `0.0791` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.7148` n `115` status `ready` deltaP `19.218` edge `0.0791` maxDD `-0.9131`
- `risk_on_high->equity_1h` score `0.4619` n `115` status `ready` deltaP `14.5106` edge `-0.0051` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
