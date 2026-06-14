# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T14:52:33.899126+00:00`
- Price records: `672`
- Market context records: `3902`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11358`

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

- `risk_on_high->unknown_4h` score `47.0988` n `72` status `ready` deltaP `4.8272` edge `6.2203` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `47.0988` n `72` status `ready` deltaP `4.8272` edge `6.2203` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `30.2902` n `35` status `ready` deltaP `27.2867` edge `2.3926` maxDD `-2.6927`
- `risk_on_and_context->crypto_major_24h` score `30.2902` n `35` status `ready` deltaP `27.2867` edge `2.3926` maxDD `-2.6927`
- `risk_on_high->equity_24h` score `25.2899` n `35` status `ready` deltaP `42.0139` edge `1.8274` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `25.2899` n `35` status `ready` deltaP `42.0139` edge `1.8274` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `19.1353` n `35` status `ready` deltaP `25.2033` edge `1.5031` maxDD `-4.7878`
- `risk_on_and_context->crypto_alt_24h` score `19.1353` n `35` status `ready` deltaP `25.2033` edge `1.5031` maxDD `-4.7878`
- `risk_on_high->index_24h` score `10.474` n `35` status `ready` deltaP `30.0347` edge `0.6726` maxDD `0.0`
- `risk_on_and_context->index_24h` score `10.474` n `35` status `ready` deltaP `30.0347` edge `0.6726` maxDD `0.0`
- `market_context_high->equity_24h` score `6.4666` n `162` status `ready` deltaP `20.409` edge `0.7058` maxDD `-14.5715`
- `market_context_high->unknown_4h` score `6.4451` n `209` status `ready` deltaP `-1.8315` edge `1.3794` maxDD `-35.6052`
- `risk_on_high->crypto_major_4h` score `5.729` n `72` status `ready` deltaP `20.376` edge `0.4538` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.729` n `72` status `ready` deltaP `20.376` edge `0.4538` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.8189` n `162` status `ready` deltaP `25.7137` edge `0.3441` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.1579` n `162` status `ready` deltaP `21.3349` edge `0.2641` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.6261` n `209` status `ready` deltaP `16.5283` edge `0.2851` maxDD `-9.4488`
- `risk_on_high->equity_4h` score `2.5977` n `72` status `ready` deltaP `24.9492` edge `0.1636` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5977` n `72` status `ready` deltaP `24.9492` edge `0.1636` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `1.921` n `162` status `ready` deltaP `4.1474` edge `0.5788` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
