# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T06:22:24.753950+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9142`

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

- `risk_on_high->commodity_24h` score `8.0884` n `54` status `ready` deltaP `43.2056` edge `0.386` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.0884` n `54` status `ready` deltaP `43.2056` edge `0.386` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.5582` n `122` status `ready` deltaP `19.6347` edge `0.5904` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `6.0394` n `122` status `ready` deltaP `21.9962` edge `0.4888` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.3645` n `54` status `ready` deltaP `22.3973` edge `0.3424` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.3645` n `54` status `ready` deltaP `22.3973` edge `0.3424` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.1358` n `54` status `ready` deltaP `35.4449` edge `0.3792` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.1358` n `54` status `ready` deltaP `35.4449` edge `0.3792` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.4727` n `123` status `ready` deltaP `13.4791` edge `0.1393` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.9538` n `123` status `ready` deltaP `6.397` edge `0.1174` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.2396` n `122` status `ready` deltaP `11.6853` edge `0.0466` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.341` n `123` status `ready` deltaP `7.894` edge `0.0059` maxDD `-0.9556`
- `market_context_high->fx_1h` score `-0.3426` n `123` status `ready` deltaP `0.1684` edge `-0.0019` maxDD `-0.4516`
- `risk_on_high->metal_1h` score `-0.3582` n `54` status `ready` deltaP `3.6483` edge `0.0029` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3582` n `54` status `ready` deltaP `3.6483` edge `0.0029` maxDD `-0.8513`
- `risk_on_high->crypto_major_1h` score `-0.4382` n `54` status `ready` deltaP `2.1513` edge `0.0017` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4382` n `54` status `ready` deltaP `2.1513` edge `0.0017` maxDD `-3.7781`
- `market_context_high->index_1h` score `-0.4711` n `123` status `ready` deltaP `2.472` edge `-0.0021` maxDD `-1.3154`
- `risk_on_high->index_1h` score `-0.4739` n `54` status `ready` deltaP `-2.9029` edge `-0.003` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.4739` n `54` status `ready` deltaP `-2.9029` edge `-0.003` maxDD `-0.7394`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
