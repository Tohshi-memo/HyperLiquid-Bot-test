# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T20:22:29.403222+00:00`
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

- `market_context_high->unknown_24h` score `1616.3604` n `134` status `ready` deltaP `-1.9227` edge `134.7525` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `62.703` n `134` status `ready` deltaP `5.7517` edge `5.2002` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.2591` n `134` status `ready` deltaP `27.6249` edge `0.0224` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.2777` n `134` status `ready` deltaP `9.5563` edge `0.0098` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.0918` n `134` status `ready` deltaP `13.2395` edge `0.0131` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.0769` n `134` status `ready` deltaP `11.8038` edge `0.0496` maxDD `-1.0837`
- `market_context_high->fx_1h` score `-0.1104` n `134` status `ready` deltaP `3.4297` edge `-0.0012` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3978` n `134` status `ready` deltaP `0.7463` edge `0.0133` maxDD `-0.4475`
- `market_context_high->crypto_major_1h` score `-0.4089` n `134` status `ready` deltaP `5.3691` edge `0.0329` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.4193` n `134` status `ready` deltaP `1.7875` edge `0.0407` maxDD `-2.3383`
- `market_context_high->fx_4h` score `-0.5029` n `134` status `ready` deltaP `-0.1683` edge `-0.0035` maxDD `-0.4545`
- `market_context_high->index_1h` score `-0.996` n `134` status `ready` deltaP `-3.7425` edge `-0.0022` maxDD `-1.1344`
- `market_context_high->fx_24h` score `-1.0632` n `134` status `ready` deltaP `4.8404` edge `0.0122` maxDD `-0.9792`
- `market_context_high->crypto_alt_1h` score `-1.1393` n `134` status `ready` deltaP `2.1003` edge `0.0264` maxDD `-8.251`
- `market_context_high->equity_4h` score `-1.5167` n `134` status `ready` deltaP `-2.7917` edge `-0.0174` maxDD `-6.008`
- `market_context_high->metal_24h` score `-1.6608` n `134` status `ready` deltaP `3.9257` edge `0.0256` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.4456` n `134` status `ready` deltaP `-7.1965` edge `-0.0238` maxDD `-3.5621`
- `market_context_high->equity_24h` score `-2.566` n `134` status `ready` deltaP `10.0617` edge `-0.0052` maxDD `-14.0571`
- `market_context_high->crypto_major_4h` score `-2.6978` n `134` status `ready` deltaP `4.6551` edge `-0.0474` maxDD `-19.0267`
- `market_context_high->commodity_24h` score `-4.4231` n `134` status `ready` deltaP `1.5988` edge `-0.0187` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
