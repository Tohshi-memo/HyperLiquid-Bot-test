# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T18:37:25.037249+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7639`

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

- `market_context_high->unknown_24h` score `2854.8333` n `100` status `ready` deltaP `-9.1875` edge `238.007` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `82.7183` n `100` status `ready` deltaP `0.9268` edge `6.9003` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `77.4533` n `108` status `ready` deltaP `-5.4945` edge `6.5197` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `19.0793` n `68` status `ready` deltaP `45.6699` edge `1.2906` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.9699` n `100` status `ready` deltaP `26.2153` edge `1.0151` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.1107` n `108` status `ready` deltaP `19.0549` edge `0.4375` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.8859` n `100` status `ready` deltaP `43.5556` edge `0.1351` maxDD `-0.1315`
- `market_context_high->metal_4h` score `1.6863` n `100` status `ready` deltaP `20.8963` edge `0.0437` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.876` n `100` status `ready` deltaP `12.497` edge `0.0187` maxDD `-0.3209`
- `market_context_high->equity_4h` score `0.7515` n `100` status `ready` deltaP `6.2378` edge `0.1941` maxDD `-4.48`
- `news_risk_high->crypto_alt_1h` score `0.7449` n `108` status `ready` deltaP `8.4276` edge `0.1013` maxDD `-3.9659`
- `market_context_high->crypto_major_1h` score `0.5593` n `100` status `ready` deltaP `9.4012` edge `0.0867` maxDD `-5.2213`
- `market_context_high->equity_1h` score `0.506` n `100` status `ready` deltaP `7.7006` edge `0.1011` maxDD `-2.3383`
- `market_context_high->fx_1h` score `0.2341` n `100` status `ready` deltaP `8.6048` edge `-0.0006` maxDD `-0.1407`
- `market_context_high->fx_4h` score `0.2094` n `100` status `ready` deltaP `8.4085` edge `0.0005` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.1702` n `100` status `ready` deltaP `12.7927` edge `0.0571` maxDD `-0.978`
- `market_context_high->metal_24h` score `0.0442` n `100` status `ready` deltaP `13.2847` edge `0.1818` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-0.1017` n `100` status `ready` deltaP `16.6463` edge `0.15` maxDD `-14.5879`
- `market_context_high->index_1h` score `-0.2799` n `100` status `ready` deltaP `4.503` edge `0.0025` maxDD `-1.1344`
- `market_context_high->commodity_1h` score `-0.3698` n `100` status `ready` deltaP `-1.4072` edge `0.0134` maxDD `-0.4475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
