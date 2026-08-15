# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T12:37:25.293198+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `137.5022` n `128` status `ready` deltaP `-24.6358` edge `11.914` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.6554` n `32` status `ready` deltaP `-37.917` edge `4.6426` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.6554` n `32` status `ready` deltaP `-37.917` edge `4.6426` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.6713` n `36` status `ready` deltaP `24.9278` edge `0.9277` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.7161` n `36` status `ready` deltaP `40.3963` edge `0.3737` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.4057` n `128` status `ready` deltaP `31.2784` edge `0.2477` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.9818` n `32` status `ready` deltaP `33.6222` edge `0.191` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.9818` n `32` status `ready` deltaP `33.6222` edge `0.191` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.251` n `32` status `ready` deltaP `28.2008` edge `0.4726` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.251` n `32` status `ready` deltaP `28.2008` edge `0.4726` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.5269` n `36` status `ready` deltaP `29.1161` edge `0.0998` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9695` n `32` status `ready` deltaP `21.5701` edge `0.1219` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9695` n `32` status `ready` deltaP `21.5701` edge `0.1219` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.0217` n `128` status `ready` deltaP `20.0076` edge `0.0822` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.9376` n `36` status `ready` deltaP `22.3577` edge `0.0256` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7394` n `36` status `ready` deltaP `8.4332` edge `0.1206` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3078` n `32` status `ready` deltaP `13.9596` edge `0.0392` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3078` n `32` status `ready` deltaP `13.9596` edge `0.0392` maxDD `-0.1957`
- `market_context_high->commodity_1h` score `0.6712` n `128` status `ready` deltaP `9.2721` edge `0.0238` maxDD `-0.3742`
- `risk_on_high->equity_24h` score `0.5902` n `32` status `ready` deltaP `13.4695` edge `0.1638` maxDD `-11.2348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
