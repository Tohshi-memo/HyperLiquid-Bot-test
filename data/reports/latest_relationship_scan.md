# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T14:37:30.492588+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10926`

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

- `risk_on_high->unknown_4h` score `20.3488` n `133` status `ready` deltaP `7.779` edge `1.7057` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.3488` n `133` status `ready` deltaP `7.779` edge `1.7057` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.3025` n `133` status `ready` deltaP `-1.353` edge `1.0086` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.3025` n `133` status `ready` deltaP `-1.353` edge `1.0086` maxDD `-1.95`
- `market_context_high->unknown_4h` score `10.0344` n `203` status `ready` deltaP `8.6605` edge `0.848` maxDD `-2.563`
- `market_context_high->unknown_1h` score `9.127` n `212` status `ready` deltaP `-0.7288` edge `0.8285` maxDD `-2.0446`
- `news_risk_high->commodity_4h` score `1.4355` n `59` status `ready` deltaP `11.7171` edge `0.0616` maxDD `-0.2737`
- `news_risk_high->commodity_24h` score `1.0321` n `59` status `ready` deltaP `10.8286` edge `0.0311` maxDD `-0.0495`
- `market_context_high->equity_24h` score `0.2996` n `167` status `ready` deltaP `13.5053` edge `0.3695` maxDD `-20.7654`
- `risk_on_high->metal_1h` score `0.1576` n `133` status `ready` deltaP `12.8619` edge `0.0057` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1576` n `133` status `ready` deltaP `12.8619` edge `0.0057` maxDD `-1.699`
- `news_risk_high->index_1h` score `0.0219` n `59` status `ready` deltaP `5.681` edge `-0.004` maxDD `-0.8185`
- `news_risk_high->crypto_alt_24h` score `-0.16` n `59` status `ready` deltaP `14.0772` edge `-0.0348` maxDD `-4.4573`
- `news_risk_high->commodity_1h` score `-0.1667` n `59` status `ready` deltaP `4.4301` edge `0.0012` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1699` n `133` status `ready` deltaP `3.693` edge `-0.0019` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1699` n `133` status `ready` deltaP `3.693` edge `-0.0019` maxDD `-0.5605`
- `risk_on_high->crypto_alt_1h` score `-0.264` n `133` status `ready` deltaP `3.7031` edge `0.055` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.264` n `133` status `ready` deltaP `3.7031` edge `0.055` maxDD `-5.4685`
- `risk_on_high->commodity_1h` score `-0.3877` n `133` status `ready` deltaP `0.5561` edge `0.0011` maxDD `-1.0281`
- `risk_on_and_context->commodity_1h` score `-0.3877` n `133` status `ready` deltaP `0.5561` edge `0.0011` maxDD `-1.0281`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
