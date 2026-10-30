# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T02:37:28.322376+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6714`

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

- `market_context_high->unknown_24h` score `1667.2034` n `134` status `ready` deltaP `-2.7908` edge `138.9952` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `36.5351` n `134` status `ready` deltaP `5.142` edge `3.0236` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.788` n `134` status `ready` deltaP `31.7916` edge `0.0387` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.3065` n `134` status `ready` deltaP `9.8557` edge `0.0115` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.1427` n `134` status `ready` deltaP `12.566` edge `0.05` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.1303` n `134` status `ready` deltaP `13.5444` edge `0.016` maxDD `-1.8344`
- `market_context_high->equity_24h` score `0.1296` n `134` status `ready` deltaP `14.402` edge `0.1905` maxDD `-14.0571`
- `market_context_high->crypto_major_1h` score `0.1212` n `134` status `ready` deltaP `7.3152` edge `0.0641` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.05` n `134` status `ready` deltaP `3.2845` edge `0.0615` maxDD `-2.3383`
- `market_context_high->fx_1h` score `-0.1189` n `134` status `ready` deltaP `3.28` edge `-0.0013` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3715` n `134` status `ready` deltaP `1.1954` edge `0.0125` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.5263` n `134` status `ready` deltaP `0.7144` edge `0.0862` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.5892` n `134` status `ready` deltaP `-1.6927` edge `-0.0044` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.6591` n `134` status `ready` deltaP `4.1961` edge `0.074` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.875` n `134` status `ready` deltaP `-2.5449` edge `-0.0001` maxDD `-1.1344`
- `market_context_high->fx_24h` score `-1.4643` n `134` status `ready` deltaP `0.8473` edge `0.0054` maxDD `-0.9792`
- `market_context_high->crypto_major_4h` score `-1.4927` n `134` status `ready` deltaP `8.3137` edge `0.0827` maxDD `-19.0267`
- `market_context_high->metal_24h` score `-1.4939` n `134` status `ready` deltaP `3.9257` edge `0.047` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.0937` n `134` status `ready` deltaP `-4.1477` edge `-0.0148` maxDD `-3.5621`
- `market_context_high->crypto_alt_4h` score `-3.9517` n `134` status `ready` deltaP `0.6416` edge `0.0766` maxDD `-37.0003`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
