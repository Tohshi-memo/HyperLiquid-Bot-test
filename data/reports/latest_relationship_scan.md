# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T17:22:30.816147+00:00`
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

- `market_context_high->unknown_24h` score `1622.2233` n `134` status `ready` deltaP `-0.1866` edge `135.2295` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `66.1306` n `134` status `ready` deltaP `6.9712` edge `5.4777` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.0415` n `134` status `ready` deltaP `25.7152` edge `0.017` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.3384` n `134` status `ready` deltaP `10.6042` edge `0.0106` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.2283` n `134` status `ready` deltaP `12.8708` edge `0.0551` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.0941` n `134` status `ready` deltaP `13.2395` edge `0.0134` maxDD `-1.8344`
- `market_context_high->fx_1h` score `-0.0769` n `134` status `ready` deltaP `4.0285` edge `-0.0009` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3247` n `134` status `ready` deltaP `1.4948` edge `0.0144` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4111` n `134` status `ready` deltaP `1.3561` edge `-0.0019` maxDD `-0.4545`
- `market_context_high->equity_1h` score `-0.5129` n `134` status `ready` deltaP `1.4881` edge `0.0349` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.554` n `134` status `ready` deltaP `4.7703` edge `0.0248` maxDD `-5.2213`
- `market_context_high->fx_24h` score `-0.8769` n `134` status `ready` deltaP `6.7501` edge `0.015` maxDD `-0.9792`
- `market_context_high->index_1h` score `-0.9876` n `134` status `ready` deltaP `-3.5928` edge `-0.0025` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-1.2399` n `134` status `ready` deltaP `1.6512` edge `0.0165` maxDD `-8.251`
- `market_context_high->equity_4h` score `-1.612` n `134` status `ready` deltaP `-2.9441` edge `-0.0286` maxDD `-6.008`
- `market_context_high->metal_24h` score `-1.7216` n `134` status `ready` deltaP `3.9257` edge `0.0178` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.4492` n `134` status `ready` deltaP `-7.1965` edge `-0.0241` maxDD `-3.5621`
- `market_context_high->crypto_major_4h` score `-2.7791` n `134` status `ready` deltaP `4.3502` edge `-0.0558` maxDD `-19.0267`
- `market_context_high->equity_24h` score `-3.4887` n `134` status `ready` deltaP `7.9784` edge `-0.0682` maxDD `-14.0571`
- `market_context_high->commodity_24h` score `-4.6554` n `134` status `ready` deltaP `-0.4845` edge `-0.0346` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
