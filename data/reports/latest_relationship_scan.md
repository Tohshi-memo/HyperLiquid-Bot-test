# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T08:07:34.376360+00:00`
- Price records: `672`
- Market context records: `4705`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9638`

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

- `market_context_high->unknown_1h` score `76.916` n `144` status `ready` deltaP `13.7143` edge `6.36` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.2873` n `136` status `ready` deltaP `11.7827` edge `0.4831` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.632` n `135` status `ready` deltaP `13.75` edge `0.22` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3311` n `144` status `ready` deltaP `2.1083` edge `0.0231` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.7559` n `136` status `ready` deltaP `3.9545` edge `-0.011` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.8967` n `136` status `ready` deltaP `-0.7533` edge `-0.0017` maxDD `-1.9927`
- `market_context_high->commodity_4h` score `-1.1735` n `136` status `ready` deltaP `6.1065` edge `0.0196` maxDD `-9.1941`
- `market_context_high->equity_1h` score `-1.2097` n `144` status `ready` deltaP `-1.892` edge `0.0105` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-1.2936` n `144` status `ready` deltaP `-5.1356` edge `-0.0056` maxDD `-1.1038`
- `market_context_high->equity_4h` score `-1.3117` n `136` status `ready` deltaP `0.8339` edge `0.0032` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.672` n `144` status `ready` deltaP `-4.2332` edge `-0.0107` maxDD `-2.6999`
- `market_context_high->crypto_alt_1h` score `-3.2891` n `144` status `ready` deltaP `-1.5386` edge `-0.0827` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-3.847` n `144` status `ready` deltaP `-2.3287` edge `-0.1024` maxDD `-27.356`
- `market_context_high->metal_1h` score `-4.4413` n `144` status `ready` deltaP `-5.4766` edge `-0.0768` maxDD `-17.2107`
- `market_context_high->commodity_24h` score `-4.5029` n `135` status `ready` deltaP `16.0648` edge `0.0681` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-4.7901` n `135` status `ready` deltaP `-13.044` edge `-0.0162` maxDD `-5.3476`
- `market_context_high->index_24h` score `-8.4011` n `135` status `ready` deltaP `-10.6366` edge `-0.0917` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.4282` n `136` status `ready` deltaP `-2.7619` edge `-0.1964` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-8.9854` n `136` status `ready` deltaP `0.6546` edge `-0.271` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.3561` n `136` status `ready` deltaP `-3.1923` edge `-0.3446` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
