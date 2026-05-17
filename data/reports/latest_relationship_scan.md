# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T22:22:19.271505+00:00`
- Price records: `672`
- Market context records: `1056`
- Flow alert records: `4946`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8668`

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

- `market_context_high->crypto_major_24h` score `14.6934` n `179` status `ready` deltaP `33.6759` edge `1.0463` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.6741` n `179` status `ready` deltaP `11.7163` edge `0.4348` maxDD `-9.5387`
- `market_context_high->equity_24h` score `3.2122` n `179` status `ready` deltaP `10.7123` edge `0.2626` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.5368` n `179` status `ready` deltaP `9.99` edge `0.2131` maxDD `-2.1308`
- `market_context_high->metal_24h` score `1.4146` n `179` status `ready` deltaP `-7.1757` edge `0.3759` maxDD `-9.8145`
- `market_context_high->fx_1h` score `-0.0845` n `181` status `ready` deltaP `5.1667` edge `0.0003` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.4706` n `181` status `ready` deltaP `3.941` edge `0.0125` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.5649` n `181` status `ready` deltaP `-0.0191` edge `0.0258` maxDD `-4.1532`
- `market_context_high->crypto_major_1h` score `-0.6169` n `181` status `ready` deltaP `6.4214` edge `0.0094` maxDD `-6.2897`
- `market_context_high->commodity_1h` score `-0.6603` n `181` status `ready` deltaP `1.014` edge `0.019` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.7281` n `180` status `ready` deltaP `0.6437` edge `0.002` maxDD `-1.6381`
- `market_context_high->crypto_alt_1h` score `-1.2117` n `181` status `ready` deltaP `0.7221` edge `0.0028` maxDD `-5.3538`
- `market_context_high->index_4h` score `-1.2364` n `180` status `ready` deltaP `-0.0983` edge `0.039` maxDD `-5.9771`
- `market_context_high->equity_4h` score `-1.3942` n `180` status `ready` deltaP `1.5143` edge `0.069` maxDD `-9.9557`
- `market_context_high->metal_1h` score `-1.6564` n `181` status `ready` deltaP `3.2777` edge `-0.0339` maxDD `-6.7453`
- `market_context_high->crypto_alt_4h` score `-2.751` n `180` status `ready` deltaP `1.5312` edge `0.036` maxDD `-15.0367`
- `market_context_high->crypto_major_4h` score `-2.9223` n `180` status `ready` deltaP `6.7446` edge `0.052` maxDD `-20.2388`
- `market_context_high->fx_24h` score `-3.1727` n `179` status `ready` deltaP `3.3117` edge `-0.0212` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.5762` n `180` status `ready` deltaP `-5.0034` edge `0.0521` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.6218` n `180` status `ready` deltaP `-0.5082` edge `-0.1581` maxDD `-17.8947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
