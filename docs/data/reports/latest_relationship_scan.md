# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T06:52:27.186754+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9576`

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

- `market_context_high->unknown_4h` score `33.7504` n `119` status `ready` deltaP `-5.6902` edge `2.9151` maxDD `-1.8373`
- `market_context_high->crypto_major_24h` score `9.7108` n `54` status `ready` deltaP `20.544` edge `1.3716` maxDD `-13.7531`
- `risk_on_high->crypto_major_4h` score `5.9115` n `51` status `ready` deltaP `35.2492` edge `0.3429` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.9115` n `51` status `ready` deltaP `35.2492` edge `0.3429` maxDD `-4.1548`
- `market_context_high->crypto_alt_24h` score `5.8714` n `54` status `ready` deltaP `0.5208` edge `1.1457` maxDD `-22.7138`
- `risk_on_high->crypto_alt_4h` score `5.1202` n `51` status `ready` deltaP `22.9436` edge `0.3185` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.1202` n `51` status `ready` deltaP `22.9436` edge `0.3185` maxDD `-1.9151`
- `market_context_high->equity_24h` score `4.2902` n `54` status `ready` deltaP `18.4028` edge `0.5329` maxDD `-4.7777`
- `market_context_high->index_24h` score `4.289` n `54` status `ready` deltaP `37.3264` edge `0.141` maxDD `-0.2608`
- `risk_on_high->crypto_alt_1h` score `1.9501` n `58` status `ready` deltaP `11.3256` edge `0.1467` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.9501` n `58` status `ready` deltaP `11.3256` edge `0.1467` maxDD `-2.4421`
- `risk_on_high->crypto_major_1h` score `1.6233` n `58` status `ready` deltaP `11.3205` edge `0.1251` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.6233` n `58` status `ready` deltaP `11.3205` edge `0.1251` maxDD `-3.2233`
- `market_context_high->crypto_alt_1h` score `1.1882` n `126` status `ready` deltaP `9.3005` edge `0.1321` maxDD `-4.9401`
- `risk_on_high->metal_4h` score `0.9535` n `51` status `ready` deltaP `13.6388` edge `0.0476` maxDD `-1.0586`
- `risk_on_and_context->metal_4h` score `0.9535` n `51` status `ready` deltaP `13.6388` edge `0.0476` maxDD `-1.0586`
- `market_context_high->crypto_major_4h` score `0.8858` n `119` status `ready` deltaP `11.7198` edge `0.246` maxDD `-11.1784`
- `market_context_high->crypto_major_1h` score `0.7239` n `126` status `ready` deltaP `5.6007` edge `0.0993` maxDD `-3.4384`
- `market_context_high->crypto_alt_4h` score `0.3495` n `119` status `ready` deltaP `5.8567` edge `0.2616` maxDD `-13.8008`
- `market_context_high->unknown_1h` score `0.1054` n `126` status `ready` deltaP `-4.693` edge `0.0737` maxDD `-1.024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
