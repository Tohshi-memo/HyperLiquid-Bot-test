# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T08:22:34.625450+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2632`

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

- `market_context_high->unknown_1h` score `11995.5152` n `108` status `ready` deltaP `1.1367` edge `999.6385` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7446.6881` n `108` status `ready` deltaP `0.5194` edge `620.5823` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `13.4529` n `102` status `ready` deltaP `30.77` edge `1.3419` maxDD `-29.4102`
- `market_context_high->crypto_alt_24h` score `7.5308` n `102` status `ready` deltaP `16.8812` edge `1.119` maxDD `-43.6516`
- `market_context_high->crypto_major_4h` score `1.6655` n `108` status `ready` deltaP `5.0079` edge `0.3873` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.568` n `108` status `ready` deltaP `6.5322` edge `0.2947` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.6608` n `108` status `ready` deltaP `18.479` edge `0.0663` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.1159` n `108` status `ready` deltaP `5.6886` edge `0.0189` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2499` n `108` status `ready` deltaP `3.5651` edge `0.0054` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.2952` n `108` status `ready` deltaP `4.6962` edge `0.0705` maxDD `-6.5061`
- `market_context_high->crypto_alt_1h` score `-0.6405` n `108` status `ready` deltaP `-1.1865` edge `0.048` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.0955` n `108` status `ready` deltaP `6.792` edge `0.0413` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.557` n `108` status `ready` deltaP `-10.8006` edge `-0.0018` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.7468` n `108` status `ready` deltaP `-1.3098` edge `-0.0025` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.3468` n `108` status `ready` deltaP `-9.0708` edge `-0.0269` maxDD `-3.9892`
- `market_context_high->fx_4h` score `-2.3731` n `108` status `ready` deltaP `-14.7979` edge `-0.004` maxDD `-1.794`
- `market_context_high->metal_24h` score `-4.8959` n `102` status `ready` deltaP `14.5425` edge `0.0914` maxDD `-37.7071`
- `market_context_high->fx_24h` score `-6.5558` n `102` status `ready` deltaP `-16.8913` edge `-0.0064` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.996` n `108` status `ready` deltaP `-28.0431` edge `-0.1101` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.0905` n `108` status `ready` deltaP `-5.8322` edge `-0.0365` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
