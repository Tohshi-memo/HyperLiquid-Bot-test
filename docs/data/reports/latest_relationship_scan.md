# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T06:37:35.775592+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7085`

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

- `market_context_high->unknown_24h` score `1727.0546` n `134` status `ready` deltaP `-2.7908` edge `143.9828` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `35.1143` n `134` status `ready` deltaP `4.2273` edge `2.9113` maxDD `-0.3966`
- `market_context_high->index_24h` score `3.0246` n `134` status `ready` deltaP `33.3541` edge `0.048` maxDD `-0.1315`
- `market_context_high->equity_24h` score `1.252` n `134` status `ready` deltaP `16.3117` edge `0.2713` maxDD `-14.0571`
- `market_context_high->metal_1h` score `0.312` n `134` status `ready` deltaP `9.8557` edge `0.0122` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.2109` n `134` status `ready` deltaP `13.3281` edge `0.0506` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.1963` n `134` status `ready` deltaP `14.1541` edge `0.0204` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.0483` n `134` status `ready` deltaP `3.8833` edge `0.0657` maxDD `-2.3383`
- `market_context_high->fx_1h` score `-0.0621` n `134` status `ready` deltaP `4.3279` edge `-0.001` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.0923` n `134` status `ready` deltaP `6.5667` edge `0.0513` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.3068` n `134` status `ready` deltaP `1.7942` edge `0.0139` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.3877` n `134` status `ready` deltaP `1.3242` edge `0.0999` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.5702` n `134` status `ready` deltaP `-1.3878` edge `-0.004` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.7924` n `134` status `ready` deltaP `3.5973` edge `0.0609` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8486` n `134` status `ready` deltaP `-2.2455` edge `0.0001` maxDD `-1.1344`
- `market_context_high->metal_24h` score `-1.387` n `134` status `ready` deltaP `3.9257` edge `0.0607` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-1.7315` n `134` status `ready` deltaP `8.1612` edge `0.0531` maxDD `-19.0267`
- `market_context_high->fx_24h` score `-1.7513` n `134` status `ready` deltaP `-1.9304` edge `0.0` maxDD `-0.9792`
- `market_context_high->index_4h` score `-2.027` n `134` status `ready` deltaP `-3.538` edge `-0.0133` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-3.8043` n `134` status `ready` deltaP `8.0224` edge `0.0178` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
