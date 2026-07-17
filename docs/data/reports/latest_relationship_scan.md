# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T19:52:33.727402+00:00`
- Price records: `672`
- Market context records: `7062`
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

- `market_context_high->fx_4h` score `0.6058` n `187` status `ready` deltaP `16.3778` edge `0.0113` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.2381` n `187` status `ready` deltaP `3.4759` edge `0.0021` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.3016` n `187` status `ready` deltaP `2.0646` edge `0.034` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.5685` n `187` status `ready` deltaP `4.2677` edge `0.0339` maxDD `-7.1523`
- `market_context_high->unknown_1h` score `-0.6099` n `187` status `ready` deltaP `-0.9951` edge `0.0253` maxDD `-1.8929`
- `market_context_high->metal_1h` score `-0.7841` n `187` status `ready` deltaP `-3.3062` edge `-0.0017` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.7851` n `187` status `ready` deltaP `-0.8462` edge `-0.0039` maxDD `-2.2895`
- `market_context_high->unknown_4h` score `-0.9647` n `187` status `ready` deltaP `-5.4071` edge `0.1191` maxDD `-4.742`
- `market_context_high->commodity_1h` score `-1.3562` n `187` status `ready` deltaP `-4.8873` edge `-0.0188` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.6337` n `187` status `ready` deltaP `-7.2772` edge `-0.0449` maxDD `-2.9494`
- `market_context_high->equity_1h` score `-1.8993` n `187` status `ready` deltaP `4.138` edge `-0.0288` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.3319` n `187` status `ready` deltaP `0.7125` edge `-0.0338` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.4401` n `187` status `ready` deltaP `-2.4538` edge `-0.0561` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.8539` n `187` status `ready` deltaP `1.0272` edge `0.0058` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.0` n `187` status `ready` deltaP `3.2461` edge `0.0222` maxDD `-24.6094`
- `market_context_high->metal_4h` score `-3.5464` n `187` status `ready` deltaP `0.763` edge `-0.0023` maxDD `-5.5324`
- `market_context_high->fx_24h` score `-3.5486` n `187` status `ready` deltaP `-0.2256` edge `-0.0115` maxDD `-3.9503`
- `market_context_high->unknown_24h` score `-3.8133` n `187` status `ready` deltaP `-14.9566` edge `0.1255` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-7.9041` n `187` status `ready` deltaP `4.2284` edge `-0.1545` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.4273` n `187` status `ready` deltaP `-20.0618` edge `-0.0925` maxDD `-44.4154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
