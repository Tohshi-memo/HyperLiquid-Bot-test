# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T06:37:14.080273+00:00`
- Price records: `672`
- Market context records: `1194`
- Flow alert records: `5344`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `18.5131` n `136` status `ready` deltaP `44.3321` edge `1.3604` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.596` n `136` status `ready` deltaP `22.0997` edge `0.6873` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `4.9969` n `136` status `ready` deltaP `4.1338` edge `0.5105` maxDD `-6.7322`
- `market_context_high->metal_24h` score `4.1802` n `136` status `ready` deltaP `-4.085` edge `0.5423` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.8263` n `136` status `ready` deltaP `15.0377` edge `0.2016` maxDD `-3.6396`
- `market_context_high->commodity_24h` score `2.2463` n `136` status `ready` deltaP `-3.4314` edge `0.5614` maxDD `-23.1066`
- `market_context_high->index_24h` score `2.0168` n `136` status `ready` deltaP `16.0948` edge `0.1694` maxDD `-5.3574`
- `market_context_high->equity_24h` score `1.4998` n `136` status `ready` deltaP `16.3603` edge `0.3159` maxDD `-14.2815`
- `market_context_high->index_4h` score `0.9574` n `136` status `ready` deltaP `10.5272` edge `0.0779` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.525` n `136` status `ready` deltaP `8.5857` edge `0.0182` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4198` n `136` status `ready` deltaP `4.1475` edge `0.0451` maxDD `-1.3546`
- `market_context_high->fx_24h` score `0.2271` n `136` status `ready` deltaP `8.5376` edge `0.0513` maxDD `-3.8101`
- `market_context_high->crypto_major_4h` score `-0.0545` n `136` status `ready` deltaP `7.1288` edge `0.1376` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.204` n `136` status `ready` deltaP `4.3457` edge `-0.0004` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.2594` n `136` status `ready` deltaP `7.8329` edge `-0.0128` maxDD `-2.2164`
- `market_context_high->crypto_major_1h` score `-0.2991` n `136` status `ready` deltaP `3.9495` edge `0.0119` maxDD `-4.1256`
- `market_context_high->unknown_24h` score `-0.3058` n `136` status `ready` deltaP `2.0527` edge `0.2338` maxDD `-10.1706`
- `market_context_high->crypto_alt_1h` score `-0.3938` n `136` status `ready` deltaP `0.4932` edge `0.0305` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.8494` n `136` status `ready` deltaP `-2.8047` edge `0.0094` maxDD `-2.252`
- `market_context_high->metal_4h` score `-1.0471` n `136` status `ready` deltaP `7.613` edge `-0.0419` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
