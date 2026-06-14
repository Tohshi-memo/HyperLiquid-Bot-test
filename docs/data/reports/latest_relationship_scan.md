# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T15:52:29.198114+00:00`
- Price records: `672`
- Market context records: `3906`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11356`

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

- `risk_on_high->unknown_4h` score `46.9369` n `72` status `ready` deltaP `4.2174` edge `6.2036` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `46.9369` n `72` status `ready` deltaP `4.2174` edge `6.2036` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `24.7807` n `39` status `ready` deltaP `18.8969` edge `2.0538` maxDD `-6.5108`
- `risk_on_and_context->crypto_major_24h` score `24.7807` n `39` status `ready` deltaP `18.8969` edge `2.0538` maxDD `-6.5108`
- `risk_on_high->equity_24h` score `23.3171` n `39` status `ready` deltaP `42.0139` edge `1.663` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `23.3171` n `39` status `ready` deltaP `42.0139` edge `1.663` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `12.9743` n `39` status `ready` deltaP `16.8136` edge `1.1467` maxDD `-11.5415`
- `risk_on_and_context->crypto_alt_24h` score `12.9743` n `39` status `ready` deltaP `16.8136` edge `1.1467` maxDD `-11.5415`
- `risk_on_high->index_24h` score `9.6088` n `39` status `ready` deltaP `30.0347` edge `0.6005` maxDD `0.0`
- `risk_on_and_context->index_24h` score `9.6088` n `39` status `ready` deltaP `30.0347` edge `0.6005` maxDD `0.0`
- `market_context_high->unknown_4h` score `6.4141` n `209` status `ready` deltaP `-1.9628` edge `1.3763` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.402` n `165` status `ready` deltaP `20.8018` edge `0.6978` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.77` n `72` status `ready` deltaP `20.5284` edge `0.4562` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.77` n `72` status `ready` deltaP `20.5284` edge `0.4562` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.7448` n `165` status `ready` deltaP `25.7923` edge `0.3374` maxDD `-7.1159`
- `market_context_high->metal_24h` score `2.9453` n `165` status `ready` deltaP `19.7569` edge `0.2569` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.6971` n `209` status `ready` deltaP `16.6807` edge `0.29` maxDD `-9.4488`
- `risk_on_high->equity_4h` score `2.5893` n `72` status `ready` deltaP `24.9492` edge `0.1629` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5893` n `72` status `ready` deltaP `24.9492` edge `0.1629` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `1.5065` n `165` status `ready` deltaP `3.0461` edge `0.5516` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
