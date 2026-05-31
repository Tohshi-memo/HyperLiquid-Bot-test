# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T17:36:27.597929+00:00`
- Price records: `672`
- Market context records: `2479`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9248`

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

- `market_context_high->unknown_24h` score `5.2094` n `123` status `ready` deltaP `19.8213` edge `0.3348` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.246` n `136` status `ready` deltaP `21.3504` edge `0.4794` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.9891` n `136` status `ready` deltaP `18.6334` edge `0.3892` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `1.8581` n `123` status `ready` deltaP `10.5268` edge `0.5573` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.5553` n `136` status `ready` deltaP `9.9983` edge `0.165` maxDD `-3.4972`
- `market_context_high->crypto_major_1h` score `0.5369` n `142` status `ready` deltaP `7.7634` edge `0.1124` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.3975` n `142` status `ready` deltaP `6.0998` edge `0.1112` maxDD `-6.1656`
- `market_context_high->index_24h` score `-0.0018` n `123` status `ready` deltaP `4.1285` edge `0.0704` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1875` n `123` status `ready` deltaP `18.297` edge `0.0151` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.2134` n `136` status `ready` deltaP `5.4878` edge `0.0202` maxDD `-2.3986`
- `market_context_high->fx_1h` score `-0.3321` n `142` status `ready` deltaP `0.9594` edge `0.0045` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.3513` n `142` status `ready` deltaP `2.3678` edge `0.0269` maxDD `-3.0902`
- `market_context_high->crypto_alt_24h` score `-0.3679` n `123` status `ready` deltaP `0.4616` edge `0.6455` maxDD `-43.6595`
- `market_context_high->metal_1h` score `-0.4794` n `142` status `ready` deltaP `1.0922` edge `0.0072` maxDD `-3.0759`
- `market_context_high->fx_4h` score `-0.6294` n `136` status `ready` deltaP `-0.4842` edge `0.0085` maxDD `-0.8774`
- `market_context_high->commodity_1h` score `-0.6391` n `142` status `ready` deltaP `1.3199` edge `-0.0029` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.6416` n `142` status `ready` deltaP `-1.0141` edge `0.0027` maxDD `-1.2855`
- `market_context_high->fx_24h` score `-0.8911` n `123` status `ready` deltaP `3.0573` edge `0.0039` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-0.9088` n `136` status `ready` deltaP `3.5868` edge `0.0391` maxDD `-4.7664`
- `market_context_high->equity_1h` score `-0.9345` n `142` status `ready` deltaP `-1.0078` edge `0.0127` maxDD `-2.7085`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
