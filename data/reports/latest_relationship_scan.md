# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T03:37:27.928604+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6696`

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

- `market_context_high->unknown_24h` score `1682.0378` n `134` status `ready` deltaP `-2.7908` edge `140.2314` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `36.2455` n `134` status `ready` deltaP `4.8371` edge `3.0015` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.8736` n `134` status `ready` deltaP `32.486` edge `0.0412` maxDD `-0.1315`
- `market_context_high->equity_24h` score `0.4683` n `134` status `ready` deltaP `15.0964` edge `0.2141` maxDD `-14.0571`
- `market_context_high->metal_1h` score `0.3081` n `134` status `ready` deltaP `9.8557` edge `0.0117` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.1522` n `134` status `ready` deltaP `13.6968` edge `0.0178` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.1331` n `134` status `ready` deltaP `12.566` edge `0.0492` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.0373` n `134` status `ready` deltaP `7.0158` edge `0.0591` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.0548` n `134` status `ready` deltaP `3.2845` edge `0.0611` maxDD `-2.3383`
- `market_context_high->fx_1h` score `-0.1259` n `134` status `ready` deltaP `3.1303` edge `-0.0012` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3631` n `134` status `ready` deltaP `1.1954` edge `0.0132` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.4111` n `134` status `ready` deltaP `1.3242` edge `0.0969` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.5717` n `134` status `ready` deltaP `-1.3878` edge `-0.0042` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.691` n `134` status `ready` deltaP `4.0464` edge `0.0709` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8726` n `134` status `ready` deltaP `-2.5449` edge `0.0001` maxDD `-1.1344`
- `market_context_high->crypto_major_4h` score `-1.4237` n `134` status `ready` deltaP `8.771` edge `0.0885` maxDD `-19.0267`
- `market_context_high->metal_24h` score `-1.4658` n `134` status `ready` deltaP `3.9257` edge `0.0506` maxDD `-10.5088`
- `market_context_high->fx_24h` score `-1.539` n `134` status `ready` deltaP `0.1529` edge `0.0038` maxDD `-0.9792`
- `market_context_high->index_4h` score `-2.0246` n `134` status `ready` deltaP `-3.538` edge `-0.0131` maxDD `-3.5621`
- `market_context_high->crypto_alt_4h` score `-3.8209` n `134` status `ready` deltaP `1.2514` edge `0.0893` maxDD `-37.0003`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
