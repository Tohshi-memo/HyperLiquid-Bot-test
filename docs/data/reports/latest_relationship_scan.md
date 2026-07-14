# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T15:37:33.074832+00:00`
- Price records: `672`
- Market context records: `6721`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->unknown_24h` score `1.4024` n `176` status `ready` deltaP `2.7935` edge `0.5364` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.0688` n `176` status `ready` deltaP `8.55` edge `0.0378` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.0021` n `176` status `ready` deltaP `5.9472` edge `0.0366` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3563` n `176` status `ready` deltaP `0.3334` edge `0.0006` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.4498` n `176` status `ready` deltaP `7.9704` edge `0.0962` maxDD `-5.2791`
- `market_context_high->index_1h` score `-0.5477` n `176` status `ready` deltaP `-0.1191` edge `0.002` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6499` n `176` status `ready` deltaP `-0.4525` edge `-0.012` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.6607` n `176` status `ready` deltaP `-4.5421` edge `-0.0019` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-0.9169` n `176` status `ready` deltaP `4.1542` edge `-0.0014` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.134` n `176` status `ready` deltaP `7.6635` edge `-0.0085` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2146` n `176` status `ready` deltaP `7.5388` edge `0.0004` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.6064` n `176` status `ready` deltaP `-3.1458` edge `-0.036` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-2.0091` n `176` status `ready` deltaP `-8.373` edge `-0.0215` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.0937` n `176` status `ready` deltaP `5.9451` edge `0.0234` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.2746` n `176` status `ready` deltaP `3.8941` edge `0.0226` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.5326` n `176` status `ready` deltaP `-5.5571` edge `-0.0016` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.7934` n `176` status `ready` deltaP `6.056` edge `-0.0998` maxDD `-27.1529`
- `market_context_high->unknown_4h` score `-4.0308` n `176` status `ready` deltaP `-18.3066` edge `0.0227` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.3201` n `176` status `ready` deltaP `-8.3965` edge `-0.0004` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-7.3666` n `176` status `ready` deltaP `-7.9072` edge `-0.0432` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
