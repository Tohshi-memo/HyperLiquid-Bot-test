# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T02:07:41.335449+00:00`
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

- `market_context_high->unknown_24h` score `1659.9206` n `134` status `ready` deltaP `-2.7908` edge `138.3883` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `40.8863` n `134` status `ready` deltaP `5.142` edge `3.3862` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.7446` n `134` status `ready` deltaP `31.4443` edge `0.0374` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.305` n `134` status `ready` deltaP `9.8557` edge `0.0113` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.1621` n `134` status `ready` deltaP `12.7184` edge `0.0506` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.138` n `134` status `ready` deltaP `7.3152` edge `0.0655` maxDD `-5.2213`
- `market_context_high->metal_4h` score `0.105` n `134` status `ready` deltaP `13.2395` edge `0.0148` maxDD `-1.8344`
- `market_context_high->equity_1h` score `-0.0488` n `134` status `ready` deltaP `3.2845` edge `0.0616` maxDD `-2.3383`
- `market_context_high->equity_24h` score `-0.0542` n `134` status `ready` deltaP `14.0548` edge `0.1775` maxDD `-14.0571`
- `market_context_high->fx_1h` score `-0.1275` n `134` status `ready` deltaP `3.1303` edge `-0.0014` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3403` n `134` status `ready` deltaP `1.4948` edge `0.0131` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.5967` n `134` status `ready` deltaP `0.4095` edge `0.0792` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.5971` n `134` status `ready` deltaP `-1.8452` edge `-0.0044` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.6575` n `134` status `ready` deltaP `4.1961` edge `0.0742` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8762` n `134` status `ready` deltaP `-2.5449` edge `-0.0002` maxDD `-1.1344`
- `market_context_high->fx_24h` score `-1.4281` n `134` status `ready` deltaP `1.1946` edge `0.0061` maxDD `-0.9792`
- `market_context_high->metal_24h` score `-1.5103` n `134` status `ready` deltaP `3.9257` edge `0.0449` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-1.5601` n `134` status `ready` deltaP `8.0088` edge `0.0761` maxDD `-19.0267`
- `market_context_high->index_4h` score `-2.1313` n `134` status `ready` deltaP `-4.4526` edge `-0.0159` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-4.0182` n `134` status `ready` deltaP `5.2446` edge `0.0089` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
