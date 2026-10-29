# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T19:22:33.322508+00:00`
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

- `market_context_high->unknown_24h` score `1617.8762` n `134` status `ready` deltaP `-1.5755` edge `134.8765` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `63.3692` n `134` status `ready` deltaP `5.9041` edge `5.2547` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.1771` n `134` status `ready` deltaP `26.9304` edge `0.0202` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.3127` n `134` status `ready` deltaP `10.1551` edge `0.0103` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.1193` n `134` status `ready` deltaP `12.1086` edge `0.0511` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.0926` n `134` status `ready` deltaP `13.2395` edge `0.0132` maxDD `-1.8344`
- `market_context_high->fx_1h` score `-0.0855` n `134` status `ready` deltaP `3.8788` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3547` n `134` status `ready` deltaP `1.1954` edge `0.0139` maxDD `-0.4475`
- `market_context_high->crypto_major_1h` score `-0.4257` n `134` status `ready` deltaP `5.3691` edge `0.0315` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.4397` n `134` status `ready` deltaP `1.7875` edge `0.039` maxDD `-2.3383`
- `market_context_high->fx_4h` score `-0.4855` n `134` status `ready` deltaP `0.1365` edge `-0.0033` maxDD `-0.4545`
- `market_context_high->fx_24h` score `-0.9969` n `134` status `ready` deltaP `5.5348` edge `0.0131` maxDD `-0.9792`
- `market_context_high->index_1h` score `-0.9972` n `134` status `ready` deltaP `-3.7425` edge `-0.0023` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-1.1417` n `134` status `ready` deltaP `2.25` edge `0.0251` maxDD `-8.251`
- `market_context_high->equity_4h` score `-1.5666` n `134` status `ready` deltaP `-2.7917` edge `-0.0238` maxDD `-6.008`
- `market_context_high->metal_24h` score `-1.6858` n `134` status `ready` deltaP `3.9257` edge `0.0224` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.4492` n `134` status `ready` deltaP `-7.1965` edge `-0.0241` maxDD `-3.5621`
- `market_context_high->crypto_major_4h` score `-2.768` n `134` status `ready` deltaP `4.6551` edge `-0.0564` maxDD `-19.0267`
- `market_context_high->equity_24h` score `-2.906` n `134` status `ready` deltaP `9.3673` edge `-0.0289` maxDD `-14.0571`
- `market_context_high->commodity_24h` score `-4.4943` n `134` status `ready` deltaP `0.9043` edge `-0.0232` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
