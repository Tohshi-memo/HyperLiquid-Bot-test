# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T14:22:29.943778+00:00`
- Price records: `672`
- Market context records: `6716`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `1.4438` n `176` status `ready` deltaP `2.7935` edge `0.5417` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.0524` n `176` status `ready` deltaP `8.4003` edge `0.0367` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.0212` n `176` status `ready` deltaP `5.7975` edge `0.036` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3555` n `176` status `ready` deltaP `0.3334` edge `0.0007` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.4882` n `176` status `ready` deltaP `7.9704` edge `0.093` maxDD `-5.2791`
- `market_context_high->index_1h` score `-0.557` n `176` status `ready` deltaP `-0.2688` edge `0.0018` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6359` n `176` status `ready` deltaP `-0.3028` edge `-0.0112` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.6755` n `176` status `ready` deltaP `-4.6918` edge `-0.0028` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-0.924` n `176` status `ready` deltaP `4.0045` edge `-0.001` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.0686` n `176` status `ready` deltaP `8.4257` edge `-0.0052` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2225` n `176` status `ready` deltaP `7.3864` edge `0.0004` maxDD `-2.1765`
- `market_context_high->unknown_1h` score `-1.3694` n `176` status `ready` deltaP `-8.6724` edge `0.0338` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6796` n `176` status `ready` deltaP `-3.908` edge `-0.0403` maxDD `-5.5853`
- `market_context_high->crypto_major_4h` score `-1.9907` n `176` status `ready` deltaP `5.9451` edge `0.0366` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.1417` n `176` status `ready` deltaP `4.3514` edge `0.0366` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.4675` n `176` status `ready` deltaP `-5.0998` edge `0.0037` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.6282` n `176` status `ready` deltaP `6.8182` edge `-0.0837` maxDD `-27.1529`
- `market_context_high->unknown_4h` score `-4.0448` n `176` status `ready` deltaP `-18.0017` edge `0.0195` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.2688` n `176` status `ready` deltaP `-7.8756` edge `0.0004` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-7.1857` n `176` status `ready` deltaP `-7.0392` edge `-0.0258` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
