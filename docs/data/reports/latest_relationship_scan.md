# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T16:07:28.049766+00:00`
- Price records: `672`
- Market context records: `6724`
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

- `market_context_high->unknown_24h` score `1.3915` n `176` status `ready` deltaP `2.7935` edge `0.535` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.0298` n `176` status `ready` deltaP `8.2506` edge `0.0348` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.0548` n `176` status `ready` deltaP `5.6478` edge `0.0342` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3477` n `176` status `ready` deltaP `0.4831` edge `0.0007` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.4318` n `176` status `ready` deltaP `7.9704` edge `0.0977` maxDD `-5.2791`
- `market_context_high->index_1h` score `-0.5562` n `176` status `ready` deltaP `-0.2688` edge `0.0019` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.656` n `176` status `ready` deltaP `-4.5421` edge `-0.0013` maxDD `-1.2017`
- `market_context_high->commodity_1h` score `-0.6616` n `176` status `ready` deltaP `-0.6022` edge `-0.0125` maxDD `-2.1314`
- `market_context_high->equity_1h` score `-0.9444` n `176` status `ready` deltaP `4.0045` edge `-0.0027` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.1577` n `176` status `ready` deltaP `7.3586` edge `-0.0095` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2146` n `176` status `ready` deltaP `7.5388` edge `0.0004` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.5853` n `176` status `ready` deltaP `-2.9933` edge `-0.0343` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.9863` n `176` status `ready` deltaP `-8.2233` edge `-0.0206` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.1522` n `176` status `ready` deltaP `5.9451` edge `0.0159` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.3396` n `176` status `ready` deltaP `3.5892` edge `0.0163` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.5649` n `176` status `ready` deltaP `-5.862` edge `-0.0037` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.8553` n `176` status `ready` deltaP `5.7511` edge `-0.1057` maxDD `-27.1529`
- `market_context_high->unknown_4h` score `-4.0718` n `176` status `ready` deltaP `-18.459` edge `0.0203` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.3376` n `176` status `ready` deltaP `-8.5701` edge `-0.0007` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-7.4345` n `176` status `ready` deltaP `-8.2545` edge `-0.0496` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
