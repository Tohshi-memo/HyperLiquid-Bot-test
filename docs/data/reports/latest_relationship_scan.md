# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T05:22:28.673314+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9684`

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

- `market_context_high->unknown_4h` score `33.6197` n `119` status `ready` deltaP `-7.066` edge `2.9193` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.2619` n `54` status `ready` deltaP `26.794` edge `0.5859` maxDD `-2.4161`
- `market_context_high->crypto_major_24h` score `7.64` n `54` status `ready` deltaP `12.1528` edge `1.1711` maxDD `-14.4769`
- `risk_on_high->crypto_major_4h` score `5.8082` n `47` status `ready` deltaP `33.7474` edge `0.3443` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.8082` n `47` status `ready` deltaP `33.7474` edge `0.3443` maxDD `-4.1548`
- `market_context_high->index_24h` score `5.6047` n `54` status `ready` deltaP `47.3958` edge `0.1554` maxDD `-0.012`
- `risk_on_high->crypto_alt_4h` score `4.8954` n `47` status `ready` deltaP `21.1079` edge `0.312` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.8954` n `47` status `ready` deltaP `21.1079` edge `0.312` maxDD `-1.9151`
- `risk_on_high->metal_4h` score `2.4222` n `47` status `ready` deltaP `22.4864` edge `0.0768` maxDD `-0.3218`
- `risk_on_and_context->metal_4h` score `2.4222` n `47` status `ready` deltaP `22.4864` edge `0.0768` maxDD `-0.3218`
- `risk_on_high->crypto_alt_1h` score `1.8181` n `59` status `ready` deltaP `10.2152` edge `0.1431` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.8181` n `59` status `ready` deltaP `10.2152` edge `0.1431` maxDD `-2.4421`
- `market_context_high->crypto_alt_24h` score `1.6061` n `54` status `ready` deltaP `-9.5486` edge `0.766` maxDD `-28.7141`
- `risk_on_high->crypto_major_1h` score `1.4924` n `59` status `ready` deltaP `10.4181` edge `0.1202` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.4924` n `59` status `ready` deltaP `10.4181` edge `0.1202` maxDD `-3.2233`
- `market_context_high->crypto_major_4h` score `0.9217` n `119` status `ready` deltaP `11.7198` edge `0.2506` maxDD `-11.1784`
- `market_context_high->crypto_alt_1h` score `0.734` n `131` status `ready` deltaP `6.8771` edge `0.1104` maxDD `-4.9401`
- `market_context_high->crypto_alt_4h` score `0.5976` n `119` status `ready` deltaP `5.8567` edge `0.2666` maxDD `-13.8008`
- `market_context_high->metal_4h` score `0.5262` n `119` status `ready` deltaP `12.7242` edge `0.0313` maxDD `-1.1153`
- `market_context_high->crypto_major_1h` score `0.2292` n `131` status `ready` deltaP `3.5997` edge `0.0817` maxDD `-3.4384`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
