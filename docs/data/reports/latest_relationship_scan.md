# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T18:37:30.117263+00:00`
- Price records: `672`
- Market context records: `6946`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11728`

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

- `market_context_high->fx_1h` score `-0.2273` n `237` status `ready` deltaP `2.6333` edge `0.0018` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3685` n `237` status `ready` deltaP `2.5797` edge `0.022` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.727` n `237` status `ready` deltaP `-0.2388` edge `-0.0005` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7356` n `237` status `ready` deltaP `-2.3895` edge `-0.0016` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.8952` n `229` status `ready` deltaP `12.4501` edge `0.0086` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.1957` n `237` status `ready` deltaP `3.0288` edge `0.0154` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2454` n `237` status `ready` deltaP `-2.5247` edge `-0.0148` maxDD `-2.4388`
- `market_context_high->unknown_24h` score `-1.5156` n `222` status `ready` deltaP `-8.7155` edge `0.3091` maxDD `-17.9576`
- `market_context_high->unknown_1h` score `-1.5949` n `237` status `ready` deltaP `-1.9809` edge `-0.0296` maxDD `-3.2083`
- `market_context_high->index_4h` score `-1.6629` n `229` status `ready` deltaP `8.4867` edge `-0.0118` maxDD `-11.3047`
- `market_context_high->commodity_4h` score `-1.663` n `229` status `ready` deltaP `-4.5485` edge `-0.0339` maxDD `-5.5853`
- `market_context_high->equity_1h` score `-2.0131` n `237` status `ready` deltaP `2.2385` edge `-0.0176` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-2.0305` n `229` status `ready` deltaP `4.2896` edge `0.0094` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.8151` n `229` status `ready` deltaP `1.3553` edge `-0.0116` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.8712` n `229` status `ready` deltaP `-0.3422` edge `-0.0331` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.0745` n `229` status `ready` deltaP `-7.7771` edge `0.0322` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.6702` n `222` status `ready` deltaP `-5.809` edge `-0.0803` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.3597` n `222` status `ready` deltaP `-6.9122` edge `-0.0136` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.9369` n `229` status `ready` deltaP `5.0963` edge `-0.0853` maxDD `-60.0417`
- `market_context_high->metal_24h` score `-9.3215` n `222` status `ready` deltaP `-14.0483` edge `-0.1258` maxDD `-37.7157`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
