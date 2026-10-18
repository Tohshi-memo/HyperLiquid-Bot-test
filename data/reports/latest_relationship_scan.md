# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T01:22:27.333368+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9622`

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

- `risk_on_high->commodity_24h` score `7.0966` n `54` status `ready` deltaP `39.3728` edge `0.3289` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0966` n `54` status `ready` deltaP `39.3728` edge `0.3289` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `1.1806` n `171` status `ready` deltaP `13.5349` edge `0.3486` maxDD `-15.2359`
- `risk_on_high->crypto_major_4h` score `0.3869` n `91` status `ready` deltaP `14.9809` edge `0.1978` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.3869` n `91` status `ready` deltaP `14.9809` edge `0.1978` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.3163` n `171` status `ready` deltaP `3.3521` edge `0.0929` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.0008` n `91` status `ready` deltaP `4.8559` edge `0.0061` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0008` n `91` status `ready` deltaP `4.8559` edge `0.0061` maxDD `-0.7394`
- `market_context_high->crypto_alt_1h` score `-0.0418` n `171` status `ready` deltaP `6.7812` edge `0.1013` maxDD `-7.3329`
- `market_context_high->index_1h` score `-0.1844` n `171` status `ready` deltaP `6.8674` edge `0.0054` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2968` n `91` status `ready` deltaP `0.4472` edge `-0.003` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2968` n `91` status `ready` deltaP `0.4472` edge `-0.003` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.335` n `171` status `ready` deltaP `5.3542` edge `0.0083` maxDD `-0.9556`
- `risk_on_high->equity_1h` score `-0.4128` n `91` status `ready` deltaP `9.5585` edge `0.0315` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4128` n `91` status `ready` deltaP `9.5585` edge `0.0315` maxDD `-5.3696`
- `market_context_high->metal_4h` score `-0.4415` n `171` status `ready` deltaP `8.2219` edge `0.0421` maxDD `-1.6961`
- `risk_on_high->metal_1h` score `-0.4782` n `91` status `ready` deltaP `1.1449` edge `0.0042` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4782` n `91` status `ready` deltaP `1.1449` edge `0.0042` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.5287` n `171` status `ready` deltaP `-2.0784` edge `-0.0018` maxDD `-0.503`
- `market_context_high->equity_1h` score `-0.6054` n `171` status `ready` deltaP `9.3014` edge `0.0415` maxDD `-7.3168`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
