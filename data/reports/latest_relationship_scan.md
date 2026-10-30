# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T06:07:29.289024+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6612`

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

- `market_context_high->unknown_24h` score `1719.5162` n `134` status `ready` deltaP `-2.7908` edge `143.3546` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `35.1721` n `134` status `ready` deltaP `4.3798` edge `2.9151` maxDD `-0.3966`
- `market_context_high->index_24h` score `3.0126` n `134` status `ready` deltaP `33.3541` edge `0.047` maxDD `-0.1315`
- `market_context_high->equity_24h` score `1.1656` n `134` status `ready` deltaP `16.3117` edge `0.2641` maxDD `-14.0571`
- `market_context_high->metal_1h` score `0.3104` n `134` status `ready` deltaP `9.8557` edge `0.012` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.1939` n `134` status `ready` deltaP `14.1541` edge `0.0201` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.1781` n `134` status `ready` deltaP `13.0233` edge `0.0499` maxDD `-1.0837`
- `market_context_high->equity_1h` score `0.0255` n `134` status `ready` deltaP `3.7336` edge `0.0648` maxDD `-2.3383`
- `market_context_high->fx_1h` score `-0.0699` n `134` status `ready` deltaP `4.1782` edge `-0.001` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.0791` n `134` status `ready` deltaP `6.7164` edge `0.0514` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.2948` n `134` status `ready` deltaP `1.9439` edge `0.0139` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.3642` n `134` status `ready` deltaP `1.4766` edge `0.1019` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.5702` n `134` status `ready` deltaP `-1.3878` edge `-0.004` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.7932` n `134` status `ready` deltaP `3.5973` edge `0.0608` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8474` n `134` status `ready` deltaP `-2.2455` edge `0.0002` maxDD `-1.1344`
- `market_context_high->metal_24h` score `-1.3979` n `134` status `ready` deltaP `3.9257` edge `0.0593` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-1.6768` n `134` status `ready` deltaP `8.3137` edge `0.0591` maxDD `-19.0267`
- `market_context_high->fx_24h` score `-1.7151` n `134` status `ready` deltaP `-1.5832` edge `0.0007` maxDD `-0.9792`
- `market_context_high->index_4h` score `-1.9966` n `134` status `ready` deltaP `-3.2331` edge `-0.0128` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-3.8317` n `134` status `ready` deltaP `7.6752` edge `0.0166` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
