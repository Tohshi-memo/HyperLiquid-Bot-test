# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T02:52:33.652667+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6708`

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

- `market_context_high->unknown_24h` score `1670.8862` n `134` status `ready` deltaP `-2.7908` edge `139.3021` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `36.3659` n `134` status `ready` deltaP `5.142` edge `3.0095` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.8103` n `134` status `ready` deltaP `31.9652` edge `0.0394` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.3065` n `134` status `ready` deltaP `9.8557` edge `0.0115` maxDD `-0.3659`
- `market_context_high->equity_24h` score `0.2167` n `134` status `ready` deltaP `14.5756` edge `0.1966` maxDD `-14.0571`
- `market_context_high->metal_4h` score `0.1429` n `134` status `ready` deltaP `13.6968` edge `0.0166` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.1403` n `134` status `ready` deltaP `12.566` edge `0.0498` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.0876` n `134` status `ready` deltaP `7.1655` edge `0.0623` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.0584` n `134` status `ready` deltaP `3.2845` edge `0.0608` maxDD `-2.3383`
- `market_context_high->fx_1h` score `-0.1267` n `134` status `ready` deltaP `3.1303` edge `-0.0013` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3667` n `134` status `ready` deltaP `1.1954` edge `0.0129` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.4973` n `134` status `ready` deltaP `0.8668` edge `0.0889` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.5892` n `134` status `ready` deltaP `-1.6927` edge `-0.0044` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.6762` n `134` status `ready` deltaP `4.0464` edge `0.0728` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.875` n `134` status `ready` deltaP `-2.5449` edge `-0.0001` maxDD `-1.1344`
- `market_context_high->crypto_major_4h` score `-1.4692` n `134` status `ready` deltaP `8.4661` edge `0.0847` maxDD `-19.0267`
- `market_context_high->fx_24h` score `-1.4842` n `134` status `ready` deltaP `0.6737` edge `0.0049` maxDD `-0.9792`
- `market_context_high->metal_24h` score `-1.4861` n `134` status `ready` deltaP `3.9257` edge `0.048` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.0767` n `134` status `ready` deltaP `-3.9953` edge `-0.0144` maxDD `-3.5621`
- `market_context_high->crypto_alt_4h` score `-3.9133` n `134` status `ready` deltaP `0.7941` edge `0.0805` maxDD `-37.0003`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
