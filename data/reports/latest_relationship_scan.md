# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T03:07:29.424784+00:00`
- Price records: `672`
- Market context records: `3953`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11267`

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

- `risk_on_high->unknown_4h` score `144.0452` n `41` status `ready` deltaP `2.5915` edge `12.1677` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `144.0452` n `41` status `ready` deltaP `2.5915` edge `12.1677` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `22.5968` n `154` status `ready` deltaP `-8.8992` edge `2.9382` maxDD `-69.331`
- `market_context_high->unknown_4h` score `19.5157` n `165` status `ready` deltaP `-0.7936` edge `2.1725` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.2171` n `41` status `ready` deltaP `42.0139` edge `0.488` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2171` n `41` status `ready` deltaP `42.0139` edge `0.488` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.3204` n `41` status `ready` deltaP `35.9757` edge `0.0416` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.3204` n `41` status `ready` deltaP `35.9757` edge `0.0416` maxDD `-0.0458`
- `market_context_high->index_24h` score `3.315` n `154` status `ready` deltaP `25.965` edge `0.2171` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.2945` n `154` status `ready` deltaP `17.3769` edge `0.3102` maxDD `-9.1203`
- `market_context_high->equity_24h` score `2.9832` n `154` status `ready` deltaP `19.2866` edge `0.423` maxDD `-14.5715`
- `risk_on_high->index_24h` score `2.8545` n `41` status `ready` deltaP `29.8611` edge `0.0388` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.8545` n `41` status `ready` deltaP `29.8611` edge `0.0388` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.1695` n `165` status `ready` deltaP `19.8384` edge `0.2052` maxDD `-7.8662`
- `market_context_high->equity_4h` score `2.0011` n `165` status `ready` deltaP `17.8234` edge `0.1782` maxDD `-7.0879`
- `risk_on_high->crypto_major_4h` score `1.8545` n `41` status `ready` deltaP `21.4939` edge `0.0778` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.8545` n `41` status `ready` deltaP `21.4939` edge `0.0778` maxDD `-2.6576`
- `market_context_high->metal_1h` score `0.8542` n `168` status `ready` deltaP `11.9154` edge `0.0553` maxDD `-2.751`
- `market_context_high->crypto_major_1h` score `0.8271` n `168` status `ready` deltaP `11.3024` edge `0.0859` maxDD `-4.7193`
- `risk_on_high->commodity_24h` score `0.6263` n `41` status `ready` deltaP `3.5569` edge `0.2694` maxDD `-13.9406`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
