# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T03:52:27.742794+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6624`

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

- `market_context_high->unknown_24h` score `1685.759` n `134` status `ready` deltaP `-2.7908` edge `140.5415` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `36.2153` n `134` status `ready` deltaP `4.6846` edge `3.0` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.8934` n `134` status `ready` deltaP `32.6596` edge `0.0417` maxDD `-0.1315`
- `market_context_high->equity_24h` score `0.5434` n `134` status `ready` deltaP `15.27` edge `0.2192` maxDD `-14.0571`
- `market_context_high->metal_1h` score `0.3065` n `134` status `ready` deltaP `9.8557` edge `0.0115` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.1553` n `134` status `ready` deltaP `13.6968` edge `0.0182` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.1319` n `134` status `ready` deltaP `12.566` edge `0.0491` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.0023` n `134` status `ready` deltaP `6.8661` edge `0.0568` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.0608` n `134` status `ready` deltaP `3.2845` edge `0.0606` maxDD `-2.3383`
- `market_context_high->fx_1h` score `-0.1259` n `134` status `ready` deltaP `3.1303` edge `-0.0012` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3631` n `134` status `ready` deltaP `1.1954` edge `0.0132` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.3963` n `134` status `ready` deltaP `1.3242` edge `0.0988` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.571` n `134` status `ready` deltaP `-1.3878` edge `-0.0041` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.716` n `134` status `ready` deltaP `3.8967` edge `0.0687` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8726` n `134` status `ready` deltaP `-2.5449` edge `0.0001` maxDD `-1.1344`
- `market_context_high->crypto_major_4h` score `-1.4331` n `134` status `ready` deltaP `8.771` edge `0.0873` maxDD `-19.0267`
- `market_context_high->metal_24h` score `-1.4596` n `134` status `ready` deltaP `3.9257` edge `0.0514` maxDD `-10.5088`
- `market_context_high->fx_24h` score `-1.5565` n `134` status `ready` deltaP `-0.0207` edge `0.0035` maxDD `-0.9792`
- `market_context_high->index_4h` score `-2.0088` n `134` status `ready` deltaP `-3.3855` edge `-0.0128` maxDD `-3.5621`
- `market_context_high->crypto_alt_4h` score `-3.8052` n `134` status `ready` deltaP `1.4038` edge `0.0903` maxDD `-37.0003`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
