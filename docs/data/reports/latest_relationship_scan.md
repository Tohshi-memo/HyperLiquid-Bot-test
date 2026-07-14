# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T12:07:27.317146+00:00`
- Price records: `672`
- Market context records: `6707`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->unknown_24h` score `1.3415` n `178` status `ready` deltaP `2.2062` edge `0.5325` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.1977` n `178` status `ready` deltaP `9.2899` edge `0.0494` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `0.1523` n `178` status `ready` deltaP `6.5566` edge `0.0454` maxDD `-3.7803`
- `market_context_high->commodity_24h` score `-0.3285` n `178` status `ready` deltaP `8.347` edge `0.1038` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3524` n `178` status `ready` deltaP `0.4087` edge `0.0006` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.5516` n `178` status `ready` deltaP `-0.3751` edge `0.0032` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.6139` n `178` status `ready` deltaP `-4.047` edge `0.0008` maxDD `-1.2017`
- `market_context_high->commodity_1h` score `-0.6672` n `178` status `ready` deltaP `-0.7838` edge `-0.012` maxDD `-2.1314`
- `market_context_high->equity_1h` score `-0.8733` n `178` status `ready` deltaP `4.2337` edge `0.0017` maxDD `-3.8827`
- `market_context_high->index_4h` score `-0.9818` n `178` status `ready` deltaP `9.5112` edge `-0.0013` maxDD `-5.7046`
- `market_context_high->unknown_1h` score `-1.0445` n `178` status `ready` deltaP `-7.7155` edge `0.0545` maxDD `-3.2083`
- `market_context_high->fx_4h` score `-1.2155` n `178` status `ready` deltaP `7.574` edge `0.0005` maxDD `-2.2132`
- `market_context_high->crypto_major_4h` score `-1.7229` n `178` status `ready` deltaP `6.7896` edge `0.0653` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.7642` n `178` status `ready` deltaP `-4.9654` edge `-0.0441` maxDD `-5.5853`
- `market_context_high->crypto_alt_4h` score `-1.9319` n `178` status `ready` deltaP `5.0562` edge `0.0588` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.3812` n `178` status `ready` deltaP `-4.3847` edge `0.01` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.5047` n `178` status `ready` deltaP `7.0944` edge `-0.0697` maxDD `-27.1529`
- `market_context_high->unknown_4h` score `-3.8456` n `178` status `ready` deltaP `-16.8317` edge `0.0283` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.342` n `178` status `ready` deltaP `-8.265` edge `0.0009` maxDD `-5.9438`
- `market_context_high->metal_24h` score `-7.0312` n `178` status `ready` deltaP `-5.9886` edge `-0.013` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
