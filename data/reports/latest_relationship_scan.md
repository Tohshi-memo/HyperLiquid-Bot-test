# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T13:52:32.191412+00:00`
- Price records: `672`
- Market context records: `7034`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `market_context_high->fx_1h` score `-0.2362` n `211` status `ready` deltaP `2.1831` edge `0.0015` maxDD `-0.3733`
- `market_context_high->fx_4h` score `-0.2951` n `211` status `ready` deltaP `12.7673` edge `0.0093` maxDD `-1.2468`
- `market_context_high->crypto_alt_1h` score `-0.3082` n `211` status `ready` deltaP `2.0575` edge `0.0332` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.669` n `211` status `ready` deltaP `0.7123` edge `0.0006` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.6895` n `211` status `ready` deltaP `-1.9064` edge `0.0011` maxDD `-2.1427`
- `market_context_high->crypto_major_1h` score `-0.9398` n `211` status `ready` deltaP `3.9036` edge `0.0309` maxDD `-7.1523`
- `market_context_high->unknown_1h` score `-1.0739` n `211` status `ready` deltaP `-2.4562` edge `0.0058` maxDD `-2.6467`
- `market_context_high->commodity_1h` score `-1.2368` n `211` status `ready` deltaP `-3.6049` edge `-0.0174` maxDD `-1.9306`
- `market_context_high->unknown_24h` score `-1.4039` n `200` status `ready` deltaP `-8.2708` edge `0.3397` maxDD `-19.4976`
- `market_context_high->unknown_4h` score `-1.8992` n `211` status `ready` deltaP `-6.0513` edge `0.0869` maxDD `-7.7194`
- `market_context_high->index_4h` score `-1.9283` n `211` status `ready` deltaP `5.8772` edge `-0.0165` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-2.018` n `211` status `ready` deltaP `4.6497` edge `0.0086` maxDD `-5.5324`
- `market_context_high->commodity_4h` score `-2.0616` n `211` status `ready` deltaP `-3.6101` edge `-0.0317` maxDD `-2.9494`
- `market_context_high->commodity_24h` score `-2.3956` n `200` status `ready` deltaP `-1.2083` edge `-0.0607` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.6034` n `211` status `ready` deltaP `2.0496` edge `0.0311` maxDD `-22.2831`
- `market_context_high->equity_1h` score `-2.715` n `211` status `ready` deltaP `4.0547` edge `-0.011` maxDD `-14.716`
- `market_context_high->crypto_major_4h` score `-2.9134` n `211` status `ready` deltaP `3.1998` edge `0.0336` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.7181` n `200` status `ready` deltaP `-2.6111` edge `-0.0119` maxDD `-3.7759`
- `market_context_high->equity_4h` score `-7.2243` n `211` status `ready` deltaP `5.0319` edge `-0.0727` maxDD `-63.963`
- `market_context_high->metal_24h` score `-13.9405` n `200` status `ready` deltaP `-13.1597` edge `-0.0616` maxDD `-40.6567`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
