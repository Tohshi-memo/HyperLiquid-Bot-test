# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T17:52:33.281452+00:00`
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

- `market_context_high->unknown_24h` score `1621.8092` n `134` status `ready` deltaP `-0.5338` edge `135.1973` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `66.069` n `134` status `ready` deltaP `6.6663` edge `5.4746` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.0614` n `134` status `ready` deltaP `25.8888` edge `0.0175` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.3306` n `134` status `ready` deltaP `10.4545` edge `0.0106` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.2029` n `134` status `ready` deltaP `12.7184` edge `0.054` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.0831` n `134` status `ready` deltaP `13.087` edge `0.013` maxDD `-1.8344`
- `market_context_high->fx_1h` score `-0.0769` n `134` status `ready` deltaP `4.0285` edge `-0.0009` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3415` n `134` status `ready` deltaP `1.3451` edge `0.014` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4317` n `134` status `ready` deltaP `1.0512` edge `-0.0025` maxDD `-0.4545`
- `market_context_high->equity_1h` score `-0.5033` n `134` status `ready` deltaP `1.4881` edge `0.0357` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.5324` n `134` status `ready` deltaP `4.7703` edge `0.0266` maxDD `-5.2213`
- `market_context_high->fx_24h` score `-0.9118` n `134` status `ready` deltaP `6.4029` edge `0.0144` maxDD `-0.9792`
- `market_context_high->index_1h` score `-0.9864` n `134` status `ready` deltaP `-3.5928` edge `-0.0024` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-1.2267` n `134` status `ready` deltaP `1.6512` edge `0.0182` maxDD `-8.251`
- `market_context_high->equity_4h` score `-1.6316` n `134` status `ready` deltaP `-3.0966` edge `-0.0301` maxDD `-6.008`
- `market_context_high->metal_24h` score `-1.7154` n `134` status `ready` deltaP `3.9257` edge `0.0186` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.4784` n `134` status `ready` deltaP `-7.5014` edge `-0.0245` maxDD `-3.5621`
- `market_context_high->crypto_major_4h` score `-2.7955` n `134` status `ready` deltaP `4.3502` edge `-0.0579` maxDD `-19.0267`
- `market_context_high->equity_24h` score `-3.3709` n `134` status `ready` deltaP `8.3256` edge `-0.0607` maxDD `-14.0571`
- `market_context_high->commodity_24h` score `-4.6132` n `134` status `ready` deltaP `-0.1373` edge `-0.0315` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
