# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T16:22:33.968941+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6784`

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

- `market_context_high->unknown_24h` score `1624.6597` n `134` status `ready` deltaP `0.5078` edge `135.4279` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `67.0894` n `134` status `ready` deltaP `6.9712` edge `5.5576` maxDD `-0.3966`
- `market_context_high->index_24h` score `1.9842` n `134` status `ready` deltaP `25.1943` edge `0.0157` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.3283` n `134` status `ready` deltaP `10.4545` edge `0.0103` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.2149` n `134` status `ready` deltaP `12.7184` edge `0.055` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.1059` n `134` status `ready` deltaP `13.3919` edge `0.0139` maxDD `-1.8344`
- `market_context_high->fx_1h` score `-0.0925` n `134` status `ready` deltaP `3.7291` edge `-0.0009` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3283` n `134` status `ready` deltaP `1.4948` edge `0.0141` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.3724` n `134` status `ready` deltaP `1.9658` edge `-0.001` maxDD `-0.4545`
- `market_context_high->equity_1h` score `-0.5141` n `134` status `ready` deltaP `1.4881` edge `0.0348` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.5576` n `134` status `ready` deltaP `4.7703` edge `0.0245` maxDD `-5.2213`
- `market_context_high->fx_24h` score `-0.8129` n `134` status `ready` deltaP `7.4446` edge `0.0157` maxDD `-0.9792`
- `market_context_high->index_1h` score `-0.9996` n `134` status `ready` deltaP `-3.7425` edge `-0.0025` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-1.2688` n `134` status `ready` deltaP `1.5015` edge `0.0138` maxDD `-8.251`
- `market_context_high->equity_4h` score `-1.5264` n `134` status `ready` deltaP `-2.3344` edge `-0.0217` maxDD `-6.008`
- `market_context_high->metal_24h` score `-1.7396` n `134` status `ready` deltaP `3.9257` edge `0.0155` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.4212` n `134` status `ready` deltaP `-6.8916` edge `-0.0238` maxDD `-3.5621`
- `market_context_high->crypto_major_4h` score `-2.672` n `134` status `ready` deltaP `4.6551` edge `-0.0441` maxDD `-19.0267`
- `market_context_high->equity_24h` score `-3.6883` n `134` status `ready` deltaP `7.2839` edge `-0.0802` maxDD `-14.0571`
- `market_context_high->commodity_24h` score `-4.7547` n `134` status `ready` deltaP `-1.179` edge `-0.0427` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
