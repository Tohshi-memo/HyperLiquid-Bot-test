# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T05:52:31.022070+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9704`

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

- `market_context_high->unknown_4h` score `33.7407` n `119` status `ready` deltaP `-6.3781` edge `2.9248` maxDD `-2.3109`
- `market_context_high->crypto_major_24h` score `8.4623` n `54` status `ready` deltaP `15.5093` edge `1.2451` maxDD `-13.7531`
- `market_context_high->equity_24h` score `7.8212` n `54` status `ready` deltaP `23.4375` edge `0.5741` maxDD `-2.6198`
- `risk_on_high->crypto_major_4h` score `6.1143` n `49` status `ready` deltaP `34.529` edge `0.3646` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `6.1143` n `49` status `ready` deltaP `34.529` edge `0.3646` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `5.3642` n `49` status `ready` deltaP `22.0632` edge `0.3447` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.3642` n `49` status `ready` deltaP `22.0632` edge `0.3447` maxDD `-1.9151`
- `market_context_high->index_24h` score `5.1922` n `54` status `ready` deltaP `44.0393` edge `0.152` maxDD `-0.0329`
- `market_context_high->crypto_alt_24h` score `3.165` n `54` status `ready` deltaP `-6.1921` edge `0.9065` maxDD `-26.4229`
- `risk_on_high->metal_4h` score `2.0051` n `49` status `ready` deltaP `19.7518` edge `0.0707` maxDD `-0.4899`
- `risk_on_and_context->metal_4h` score `2.0051` n `49` status `ready` deltaP `19.7518` edge `0.0707` maxDD `-0.4899`
- `risk_on_high->crypto_alt_1h` score `1.6638` n `60` status `ready` deltaP `9.1417` edge `0.1374` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.6638` n `60` status `ready` deltaP `9.1417` edge `0.1374` maxDD `-2.4421`
- `risk_on_high->crypto_major_1h` score `1.3666` n `60` status `ready` deltaP `9.4012` edge `0.1165` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.3666` n `60` status `ready` deltaP `9.4012` edge `0.1165` maxDD `-3.2233`
- `market_context_high->crypto_major_4h` score `0.9763` n `119` status `ready` deltaP `11.7198` edge `0.2576` maxDD `-11.1784`
- `market_context_high->crypto_alt_1h` score `0.8387` n `130` status `ready` deltaP `7.3469` edge `0.116` maxDD `-4.9401`
- `market_context_high->crypto_alt_4h` score `0.7236` n `119` status `ready` deltaP `5.8567` edge `0.2771` maxDD `-13.8008`
- `market_context_high->crypto_major_1h` score `0.4544` n `130` status `ready` deltaP `4.0166` edge `0.0874` maxDD `-3.4384`
- `market_context_high->metal_4h` score `0.3802` n `119` status `ready` deltaP `11.3484` edge `0.0283` maxDD `-1.1153`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
