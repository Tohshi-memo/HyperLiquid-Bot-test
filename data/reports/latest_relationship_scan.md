# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T00:37:35.431495+00:00`
- Price records: `672`
- Market context records: `3943`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11355`

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

- `risk_on_high->unknown_4h` score `144.2911` n `41` status `ready` deltaP `3.5061` edge `12.1821` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `144.2911` n `41` status `ready` deltaP `3.5061` edge `12.1821` maxDD `-10.8303`
- `market_context_high->unknown_4h` score `16.5924` n `175` status `ready` deltaP `-3.0305` edge `1.9438` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.3227` n `41` status `ready` deltaP `42.0139` edge `0.4968` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.3227` n `41` status `ready` deltaP `42.0139` edge `0.4968` maxDD `0.0`
- `market_context_high->unknown_24h` score `9.2754` n `164` status `ready` deltaP `-10.2515` edge `2.2639` maxDD `-100.1416`
- `risk_on_high->equity_4h` score `3.6715` n `41` status `ready` deltaP `37.5` edge `0.0607` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.6715` n `41` status `ready` deltaP `37.5` edge `0.0607` maxDD `-0.0458`
- `market_context_high->equity_24h` score `3.5345` n `164` status `ready` deltaP `20.6724` edge `0.4597` maxDD `-14.5715`
- `market_context_high->index_24h` score `3.4167` n `164` status `ready` deltaP `25.7664` edge `0.2269` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.3198` n `164` status `ready` deltaP `17.0181` edge `0.3147` maxDD `-9.1203`
- `risk_on_high->index_24h` score `2.9176` n `41` status `ready` deltaP `30.0347` edge `0.0429` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.9176` n `41` status `ready` deltaP `30.0347` edge `0.0429` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `2.3352` n `41` status `ready` deltaP `23.0183` edge `0.1077` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.3352` n `41` status `ready` deltaP `23.0183` edge `0.1077` maxDD `-2.6576`
- `market_context_high->crypto_major_4h` score `1.4637` n `175` status `ready` deltaP `17.2762` edge `0.1733` maxDD `-8.653`
- `market_context_high->equity_4h` score `0.9904` n `175` status `ready` deltaP `14.9494` edge `0.147` maxDD `-8.1306`
- `risk_on_high->metal_24h` score `0.7433` n `41` status `ready` deltaP `-15.299` edge `0.2587` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `0.7433` n `41` status `ready` deltaP `-15.299` edge `0.2587` maxDD `-1.9133`
- `risk_on_high->commodity_24h` score `0.5927` n `41` status `ready` deltaP `3.5569` edge `0.2666` maxDD `-13.9406`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
