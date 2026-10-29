# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T19:52:31.697188+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6816`

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

- `market_context_high->unknown_24h` score `1617.4003` n `134` status `ready` deltaP `-1.7491` edge `134.838` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `63.188` n `134` status `ready` deltaP `5.9041` edge `5.2396` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.2145` n `134` status `ready` deltaP `27.2777` edge `0.021` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.2948` n `134` status `ready` deltaP `9.8557` edge `0.01` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.1013` n `134` status `ready` deltaP `13.3919` edge `0.0133` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.0975` n `134` status `ready` deltaP `11.9562` edge `0.0503` maxDD `-1.0837`
- `market_context_high->fx_1h` score `-0.094` n `134` status `ready` deltaP `3.7291` edge `-0.0011` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3691` n `134` status `ready` deltaP `1.0457` edge `0.0137` maxDD `-0.4475`
- `market_context_high->crypto_major_1h` score `-0.4317` n `134` status `ready` deltaP `5.3691` edge `0.031` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.4457` n `134` status `ready` deltaP `1.7875` edge `0.0385` maxDD `-2.3383`
- `market_context_high->fx_4h` score `-0.4942` n `134` status `ready` deltaP `-0.0159` edge `-0.0034` maxDD `-0.4545`
- `market_context_high->index_1h` score `-0.9984` n `134` status `ready` deltaP `-3.7425` edge `-0.0024` maxDD `-1.1344`
- `market_context_high->fx_24h` score `-1.0295` n `134` status `ready` deltaP `5.1876` edge `0.0127` maxDD `-0.9792`
- `market_context_high->crypto_alt_1h` score `-1.1581` n `134` status `ready` deltaP `2.1003` edge `0.024` maxDD `-8.251`
- `market_context_high->equity_4h` score `-1.5533` n `134` status `ready` deltaP `-2.7917` edge `-0.0221` maxDD `-6.008`
- `market_context_high->metal_24h` score `-1.6741` n `134` status `ready` deltaP `3.9257` edge `0.0239` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.448` n `134` status `ready` deltaP `-7.1965` edge `-0.024` maxDD `-3.5621`
- `market_context_high->crypto_major_4h` score `-2.7492` n `134` status `ready` deltaP `4.6551` edge `-0.054` maxDD `-19.0267`
- `market_context_high->equity_24h` score `-2.7546` n `134` status `ready` deltaP `9.7145` edge `-0.0186` maxDD `-14.0571`
- `market_context_high->commodity_24h` score `-4.4552` n `134` status `ready` deltaP `1.2516` edge `-0.0205` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
