# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T11:07:33.037796+00:00`
- Price records: `672`
- Market context records: `4821`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7588`

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

- `market_context_high->unknown_1h` score `12.7285` n `113` status `ready` deltaP `11.9204` edge `1.023` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.9146` n `113` status `ready` deltaP `17.6545` edge `0.6629` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.7065` n `106` status `ready` deltaP `14.2099` edge `0.2062` maxDD `-3.3647`
- `market_context_high->equity_4h` score `0.6236` n `113` status `ready` deltaP `11.5192` edge `0.1413` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.4322` n `113` status `ready` deltaP `9.1989` edge `0.0344` maxDD `-1.7769`
- `market_context_high->commodity_4h` score `0.3064` n `113` status `ready` deltaP `14.564` edge `0.0594` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.0487` n `113` status `ready` deltaP `5.6687` edge `0.0216` maxDD `-1.7598`
- `market_context_high->equity_1h` score `-0.2048` n `113` status `ready` deltaP `2.9609` edge `0.0156` maxDD `-2.928`
- `market_context_high->fx_4h` score `-0.3995` n `113` status `ready` deltaP `3.7368` edge `0.0015` maxDD `-1.5439`
- `market_context_high->fx_1h` score `-1.006` n `113` status `ready` deltaP `-2.3224` edge `-0.0034` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.1755` n `113` status `ready` deltaP `-0.6054` edge `-0.0031` maxDD `-1.9327`
- `market_context_high->metal_1h` score `-2.2255` n `113` status `ready` deltaP `-0.8254` edge `-0.0695` maxDD `-13.4916`
- `market_context_high->crypto_alt_1h` score `-2.2304` n `113` status `ready` deltaP `3.7094` edge `-0.0224` maxDD `-12.7225`
- `market_context_high->crypto_major_1h` score `-2.3237` n `113` status `ready` deltaP `1.8295` edge `-0.0507` maxDD `-18.0858`
- `market_context_high->commodity_24h` score `-2.3243` n `106` status `ready` deltaP `18.7337` edge `0.088` maxDD `-27.5371`
- `market_context_high->fx_24h` score `-2.479` n `106` status `ready` deltaP `-11.9857` edge `-0.0193` maxDD `-2.9238`
- `market_context_high->crypto_alt_4h` score `-3.7449` n `113` status `ready` deltaP `8.2843` edge `0.0098` maxDD `-38.2779`
- `market_context_high->index_24h` score `-4.1332` n `106` status `ready` deltaP `-4.5827` edge `-0.1085` maxDD `-23.2678`
- `market_context_high->crypto_major_4h` score `-7.2882` n `113` status `ready` deltaP `5.2314` edge `-0.1461` maxDD `-60.5192`
- `market_context_high->metal_4h` score `-8.5729` n `113` status `ready` deltaP `5.7144` edge `-0.3267` maxDD `-60.1721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
