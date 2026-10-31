# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T10:22:23.139469+00:00`
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

- `market_context_high->unknown_24h` score `1957.0753` n `122` status `ready` deltaP `-6.1219` edge `163.1734` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `102.273` n `98` status `ready` deltaP `-5.6427` edge `8.589` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `41.1463` n `122` status `ready` deltaP `1.7318` edge `3.4306` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `18.559` n `35` status `ready` deltaP `48.879` edge `1.2255` maxDD `-0.049`
- `market_context_high->equity_24h` score `9.6771` n `122` status `ready` deltaP `24.0209` edge `0.922` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.1925` n `98` status `ready` deltaP `18.638` edge `0.4471` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.4562` n `122` status `ready` deltaP `41.3792` edge `0.1138` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `0.9272` n `98` status `ready` deltaP `8.2457` edge `0.1052` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.9032` n `122` status `ready` deltaP `13.2718` edge `0.0158` maxDD `-0.3209`
- `market_context_high->metal_4h` score `0.4093` n `122` status `ready` deltaP `16.1435` edge `0.0324` maxDD `-1.671`
- `market_context_high->equity_1h` score `0.3806` n `122` status `ready` deltaP `5.2174` edge `0.0845` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.3437` n `122` status `ready` deltaP `8.8667` edge `0.0723` maxDD `-5.2213`
- `market_context_high->commodity_4h` score `0.0992` n `122` status `ready` deltaP `12.255` edge `0.0529` maxDD `-1.0837`
- `market_context_high->equity_4h` score `-0.0604` n `122` status `ready` deltaP `1.3344` edge `0.1418` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.1023` n `122` status `ready` deltaP `3.5707` edge `-0.0011` maxDD `-0.1986`
- `market_context_high->metal_24h` score `-0.2008` n `122` status `ready` deltaP `8.2565` edge `0.1839` maxDD `-10.5088`
- `market_context_high->commodity_1h` score `-0.25` n `122` status `ready` deltaP `2.1743` edge `0.0161` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4247` n `122` status `ready` deltaP `1.087` edge `-0.0025` maxDD `-0.4027`
- `market_context_high->index_1h` score `-0.5108` n `122` status `ready` deltaP `1.7817` edge `0.0014` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.8568` n `122` status `ready` deltaP `2.324` edge `0.0522` maxDD `-7.536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
