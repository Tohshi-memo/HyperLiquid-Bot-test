# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T08:37:27.700644+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7653`

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

- `market_context_high->unknown_24h` score `1762.4972` n `128` status `ready` deltaP `-5.4687` edge `146.9542` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `101.2135` n `98` status `ready` deltaP `-5.9422` edge `8.5027` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `31.965` n `128` status `ready` deltaP `2.0007` edge `2.6637` maxDD `-0.3966`
- `market_context_high->equity_24h` score `8.9131` n `128` status `ready` deltaP `21.7014` edge `0.8738` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.4171` n `97` status `ready` deltaP `19.3849` edge `0.4529` maxDD `-7.1234`
- `market_context_high->index_24h` score `4.3071` n `128` status `ready` deltaP `40.625` edge `0.1064` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `0.926` n `98` status `ready` deltaP `8.2457` edge `0.1051` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.9033` n `128` status `ready` deltaP `13.3327` edge `0.0154` maxDD `-0.3209`
- `market_context_high->metal_4h` score `0.4334` n `128` status `ready` deltaP `16.5777` edge `0.0326` maxDD `-1.671`
- `market_context_high->equity_1h` score `0.4091` n `128` status `ready` deltaP `5.9179` edge `0.0822` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.352` n `128` status `ready` deltaP `9.375` edge `0.0696` maxDD `-5.2213`
- `market_context_high->commodity_4h` score `0.2925` n `128` status `ready` deltaP `13.6433` edge `0.0553` maxDD `-1.0837`
- `market_context_high->equity_4h` score `0.0083` n `128` status `ready` deltaP `2.5342` edge `0.1426` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.0227` n `128` status `ready` deltaP `5.0851` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2132` n `128` status `ready` deltaP `2.6946` edge `0.0157` maxDD `-0.4475`
- `market_context_high->metal_24h` score `-0.3718` n `128` status `ready` deltaP `5.9896` edge `0.1771` maxDD `-10.5088`
- `market_context_high->fx_4h` score `-0.5115` n `128` status `ready` deltaP `-0.4573` edge `-0.0028` maxDD `-0.4445`
- `market_context_high->index_1h` score `-0.5892` n `128` status `ready` deltaP `0.8468` edge `0.0011` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.7524` n `128` status `ready` deltaP `3.9249` edge `0.0549` maxDD `-7.536`
- `news_risk_high->index_1h` score `-0.8814` n `98` status `ready` deltaP `1.5642` edge `-0.0039` maxDD `-1.3981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
