# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T20:52:23.704930+00:00`
- Price records: `672`
- Market context records: `7067`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11502`

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

- `market_context_high->fx_4h` score `0.709` n `183` status `ready` deltaP `17.5929` edge `0.0118` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1398` n `183` status `ready` deltaP `4.6448` edge `0.0025` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.2768` n `183` status `ready` deltaP `2.302` edge `0.0356` maxDD `-4.5815`
- `market_context_high->unknown_1h` score `-0.3052` n `183` status `ready` deltaP `-0.1162` edge `0.0312` maxDD `-1.4688`
- `market_context_high->crypto_major_1h` score `-0.545` n `183` status `ready` deltaP `4.5401` edge `0.0351` maxDD `-7.1523`
- `market_context_high->index_1h` score `-0.797` n `183` status `ready` deltaP `-1.0896` edge `-0.0038` maxDD `-2.2895`
- `market_context_high->unknown_4h` score `-0.8207` n `183` status `ready` deltaP `-5.0929` edge `0.129` maxDD `-4.742`
- `market_context_high->metal_1h` score `-0.8467` n `183` status `ready` deltaP `-4.316` edge `-0.003` maxDD `-2.1427`
- `market_context_high->commodity_1h` score `-0.8623` n `183` status `ready` deltaP `-4.4575` edge `-0.0192` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.6108` n `183` status `ready` deltaP `-6.7764` edge `-0.0453` maxDD `-2.9494`
- `market_context_high->equity_1h` score `-1.8254` n `183` status `ready` deltaP `5.2133` edge `-0.0265` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.3044` n `183` status `ready` deltaP `1.3003` edge `-0.0342` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.4104` n `183` status `ready` deltaP `-2.0833` edge `-0.0561` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.9315` n `183` status `ready` deltaP `0.5264` edge `-0.0008` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.072` n `183` status `ready` deltaP `2.6114` edge `0.0172` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.5538` n `183` status `ready` deltaP `-0.1707` edge `-0.0123` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-3.6462` n `183` status `ready` deltaP `-0.2291` edge `-0.004` maxDD `-5.5324`
- `market_context_high->unknown_24h` score `-4.1097` n `183` status `ready` deltaP `-15.8869` edge `0.0937` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-7.9032` n `183` status `ready` deltaP `4.5157` edge `-0.1563` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.618` n `183` status `ready` deltaP `-21.5164` edge `-0.0987` maxDD `-44.4154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
