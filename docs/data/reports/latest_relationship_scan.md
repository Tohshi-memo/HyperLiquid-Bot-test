# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T06:22:26.781336+00:00`
- Price records: `672`
- Market context records: `6789`
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

- `market_context_high->unknown_24h` score `0.8797` n `176` status `ready` deltaP `-1.1995` edge `0.496` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.0987` n `176` status `ready` deltaP `8.3176` edge `0.1396` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.2432` n `185` status `ready` deltaP `6.6483` edge `0.0214` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.402` n `185` status `ready` deltaP `-0.4863` edge `0.0002` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4093` n `185` status `ready` deltaP `3.6462` edge `0.018` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.6541` n `185` status `ready` deltaP `-1.8587` edge `0.0001` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.6785` n `185` status `ready` deltaP `-1.3764` edge `-0.0095` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.7132` n `185` status `ready` deltaP `-5.2929` edge `-0.0033` maxDD `-1.2285`
- `market_context_high->equity_1h` score `-1.275` n `185` status `ready` deltaP `2.2326` edge `-0.0167` maxDD `-4.0213`
- `market_context_high->fx_4h` score `-1.3307` n `176` status `ready` deltaP `5.7096` edge `-0.0023` maxDD `-2.1765`
- `market_context_high->index_4h` score `-1.3666` n `176` status `ready` deltaP `4.6147` edge `-0.018` maxDD `-5.7046`
- `market_context_high->commodity_4h` score `-1.4601` n `176` status `ready` deltaP `-2.536` edge `-0.0213` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5994` n `185` status `ready` deltaP `-5.5923` edge `-0.0059` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.5391` n `176` status `ready` deltaP `-4.9474` edge `-0.0065` maxDD `-5.2172`
- `market_context_high->crypto_major_4h` score `-2.9982` n `176` status `ready` deltaP `1.5244` edge `-0.0631` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-3.0118` n `176` status `ready` deltaP `0.9977` edge `-0.0526` maxDD `-19.2145`
- `market_context_high->unknown_4h` score `-3.2863` n `176` status `ready` deltaP `-14.1907` edge `0.0573` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.4072` n `176` status `ready` deltaP `1.4828` edge `-0.148` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.4821` n `176` status `ready` deltaP `-9.6117` edge `-0.0058` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-9.141` n `176` status `ready` deltaP `-18.1503` edge `-0.2024` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
