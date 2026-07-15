# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T06:37:29.095365+00:00`
- Price records: `672`
- Market context records: `6791`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11670`

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

- `market_context_high->unknown_24h` score `0.8766` n `176` status `ready` deltaP `-1.1995` edge `0.4956` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.121` n `176` status `ready` deltaP `8.4912` edge `0.1403` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.2683` n `185` status `ready` deltaP `6.4986` edge `0.0203` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.3943` n `185` status `ready` deltaP `-0.3366` edge `0.0002` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4285` n `185` status `ready` deltaP `3.4965` edge `0.0174` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.6541` n `185` status `ready` deltaP `-1.8587` edge `0.0001` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.6785` n `185` status `ready` deltaP `-1.3764` edge `-0.0095` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.7109` n `185` status `ready` deltaP `-5.2929` edge `-0.003` maxDD `-1.2285`
- `market_context_high->equity_1h` score `-1.2726` n `185` status `ready` deltaP `2.2326` edge `-0.0165` maxDD `-4.0213`
- `market_context_high->fx_4h` score `-1.3315` n `176` status `ready` deltaP `5.7096` edge `-0.0024` maxDD `-2.1765`
- `market_context_high->index_4h` score `-1.3777` n `176` status `ready` deltaP `4.4623` edge `-0.0184` maxDD `-5.7046`
- `market_context_high->commodity_4h` score `-1.449` n `176` status `ready` deltaP `-2.3836` edge `-0.0209` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5839` n `185` status `ready` deltaP `-5.4426` edge `-0.0056` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.5281` n `176` status `ready` deltaP `-4.7949` edge `-0.0061` maxDD `-5.2172`
- `market_context_high->crypto_major_4h` score `-3.0249` n `176` status `ready` deltaP `1.372` edge `-0.0655` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-3.0268` n `176` status `ready` deltaP `0.8453` edge `-0.0535` maxDD `-19.2145`
- `market_context_high->unknown_4h` score `-3.3045` n `176` status `ready` deltaP `-14.3432` edge `0.0568` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.4237` n `176` status `ready` deltaP `1.3304` edge `-0.1491` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.4821` n `176` status `ready` deltaP `-9.6117` edge `-0.0058` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-9.1648` n `176` status `ready` deltaP `-18.3239` edge `-0.2043` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
