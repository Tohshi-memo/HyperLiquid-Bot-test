# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T18:37:28.659064+00:00`
- Price records: `672`
- Market context records: `3918`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11427`

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

- `risk_on_high->unknown_4h` score `57.8054` n `62` status `ready` deltaP `7.022` edge `7.5783` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `57.8054` n `62` status `ready` deltaP `7.022` edge `7.5783` maxDD `-13.467`
- `risk_on_high->equity_24h` score `18.0719` n `39` status `ready` deltaP `42.0139` edge `1.2259` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `18.0719` n `39` status `ready` deltaP `42.0139` edge `1.2259` maxDD `0.0`
- `market_context_high->unknown_4h` score `12.4086` n `198` status `ready` deltaP `-1.238` edge `1.5832` maxDD `-35.6052`
- `risk_on_high->crypto_major_4h` score `9.0218` n `62` status `ready` deltaP `30.3403` edge `0.6161` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `9.0218` n `62` status `ready` deltaP `30.3403` edge `0.6161` maxDD `-2.6576`
- `risk_on_high->crypto_major_24h` score `7.646` n `39` status `ready` deltaP `-4.8344` edge `1.227` maxDD `-11.1608`
- `risk_on_and_context->crypto_major_24h` score `7.646` n `39` status `ready` deltaP `-4.8344` edge `1.227` maxDD `-11.1608`
- `risk_on_high->index_24h` score `7.2364` n `39` status `ready` deltaP `30.0347` edge `0.4028` maxDD `0.0`
- `risk_on_and_context->index_24h` score `7.2364` n `39` status `ready` deltaP `30.0347` edge `0.4028` maxDD `0.0`
- `risk_on_high->equity_4h` score `6.4185` n `62` status `ready` deltaP `38.2376` edge `0.2847` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `6.4185` n `62` status `ready` deltaP `38.2376` edge `0.2847` maxDD `-0.0458`
- `market_context_high->equity_24h` score `5.3148` n `165` status `ready` deltaP `20.8018` edge `0.6072` maxDD `-14.5715`
- `market_context_high->index_24h` score `4.26` n `165` status `ready` deltaP `25.7923` edge `0.297` maxDD `-7.1159`
- `market_context_high->crypto_major_4h` score `3.5232` n `198` status `ready` deltaP `19.8971` edge `0.3374` maxDD `-9.4488`
- `risk_on_high->crypto_alt_4h` score `2.6201` n `62` status `ready` deltaP `2.7931` edge `0.2816` maxDD `-3.8835`
- `risk_on_and_context->crypto_alt_4h` score `2.6201` n `62` status `ready` deltaP `2.7931` edge `0.2816` maxDD `-3.8835`
- `market_context_high->metal_24h` score `2.5967` n `165` status `ready` deltaP `17.5947` edge `0.2506` maxDD `-9.1203`
- `risk_on_high->crypto_major_1h` score `1.9643` n `62` status `ready` deltaP `11.44` edge `0.1528` maxDD `-3.23`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
