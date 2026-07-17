# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T16:37:29.214520+00:00`
- Price records: `672`
- Market context records: `7047`
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

- `market_context_high->fx_4h` score `0.2806` n `200` status `ready` deltaP `14.2927` edge `0.0106` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.2999` n `200` status `ready` deltaP `2.7485` edge `0.0018` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.4989` n `200` status `ready` deltaP `1.7036` edge `0.0335` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.5779` n `200` status `ready` deltaP `3.9521` edge `0.0348` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.7483` n `200` status `ready` deltaP `-2.8952` edge `-0.015` maxDD `-1.9306`
- `market_context_high->index_1h` score `-0.7635` n `200` status `ready` deltaP `-0.6108` edge `-0.0027` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8316` n `200` status `ready` deltaP `-4.1138` edge `-0.0024` maxDD `-2.1427`
- `market_context_high->unknown_1h` score `-0.8726` n `200` status `ready` deltaP `-2.1048` edge `0.0147` maxDD `-2.204`
- `market_context_high->unknown_4h` score `-1.4491` n `200` status `ready` deltaP `-5.7195` edge `0.1004` maxDD `-6.3091`
- `market_context_high->equity_1h` score `-1.8705` n `200` status `ready` deltaP `3.7904` edge `-0.0228` maxDD `-14.716`
- `market_context_high->metal_4h` score `-2.0911` n `200` status `ready` deltaP `3.7256` edge `0.0054` maxDD `-5.5324`
- `market_context_high->index_4h` score `-2.1188` n `200` status `ready` deltaP `3.4451` edge `-0.0247` maxDD `-12.2591`
- `market_context_high->commodity_4h` score `-2.2064` n `200` status `ready` deltaP `-4.7744` edge `-0.036` maxDD `-2.9494`
- `market_context_high->commodity_24h` score `-2.215` n `199` status `ready` deltaP `-0.39` edge `-0.0511` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.5478` n `200` status `ready` deltaP `2.939` edge `0.0323` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-2.7612` n `200` status `ready` deltaP `4.5671` edge `0.044` maxDD `-24.6094`
- `market_context_high->unknown_24h` score `-2.8683` n `199` status `ready` deltaP `-11.7078` edge `0.2223` maxDD `-23.2919`
- `market_context_high->fx_24h` score `-3.559` n `199` status `ready` deltaP `-0.5802` edge `-0.01` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-7.5615` n `200` status `ready` deltaP `3.7073` edge `-0.1071` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.9572` n `199` status `ready` deltaP `-16.6771` edge `-0.0773` maxDD `-44.303`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
