# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T11:07:28.046210+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8658`

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

- `news_risk_high->unknown_4h` score `384.6678` n `83` status `ready` deltaP `-21.358` edge `32.2875` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `13.1799` n `83` status `ready` deltaP `32.7958` edge `1.0176` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `12.4794` n `83` status `ready` deltaP `24.8619` edge `1.0737` maxDD `-13.2931`
- `risk_on_high->commodity_24h` score `9.052` n `52` status `ready` deltaP `48.7847` edge `0.4291` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.052` n `52` status `ready` deltaP `48.7847` edge `0.4291` maxDD `0.0`
- `news_risk_high->equity_24h` score `9.0083` n `83` status `ready` deltaP `34.0948` edge `0.7008` maxDD `-6.5262`
- `market_context_high->commodity_24h` score `7.7528` n `149` status `ready` deltaP `42.0733` edge `0.4181` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.8163` n `83` status `ready` deltaP `39.5248` edge `0.2388` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.0138` n `83` status `ready` deltaP `31.4696` edge `0.1701` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.5965` n `52` status `ready` deltaP `30.863` edge `0.0456` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.5965` n `52` status `ready` deltaP `30.863` edge `0.0456` maxDD `-0.1313`
- `risk_on_high->fx_24h` score `2.4968` n `52` status `ready` deltaP `32.6255` edge `-0.0052` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4968` n `52` status `ready` deltaP `32.6255` edge `-0.0052` maxDD `-0.0054`
- `market_context_high->commodity_4h` score `2.4963` n `149` status `ready` deltaP `27.3653` edge `0.0674` maxDD `-0.345`
- `market_context_high->fx_24h` score `2.362` n `149` status `ready` deltaP `29.8506` edge `0.0194` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.0426` n `149` status `ready` deltaP `15.6121` edge `0.0205` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.4193` n `52` status `ready` deltaP `8.6942` edge `0.0122` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4193` n `52` status `ready` deltaP `8.6942` edge `0.0122` maxDD `-0.1507`
- `news_risk_high->index_4h` score `0.2121` n `83` status `ready` deltaP `9.7543` edge `0.025` maxDD `-0.6935`
- `market_context_high->fx_1h` score `0.054` n `149` status `ready` deltaP `4.6518` edge `0.0017` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
