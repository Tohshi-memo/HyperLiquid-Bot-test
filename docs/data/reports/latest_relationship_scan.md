# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T10:07:29.010717+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11882`

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

- `news_risk_high->unknown_24h` score `3797.1213` n `94` status `ready` deltaP `-0.7166` edge `316.436` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `69.8421` n `47` status `ready` deltaP `8.4693` edge `5.7708` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.5531` n `47` status `ready` deltaP `22.6101` edge `3.8513` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.5058` n `47` status `ready` deltaP `20.0945` edge `2.2795` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.5015` n `47` status `ready` deltaP `33.3739` edge `1.9382` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.1012` n `47` status `ready` deltaP `29.5545` edge `0.4077` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.4077` n `47` status `ready` deltaP `28.982` edge `0.1146` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7533` n `47` status `ready` deltaP `17.6018` edge `0.1539` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5798` n `47` status `ready` deltaP `29.758` edge `0.032` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.4317` n `47` status `ready` deltaP `11.5172` edge `0.1093` maxDD `-3.3417`
- `news_risk_high->index_24h` score `1.3638` n `94` status `ready` deltaP `18.9162` edge `0.0529` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.118` n `94` status `ready` deltaP `25.7905` edge `0.1375` maxDD `-6.9545`
- `market_context_high->equity_1h` score `1.053` n `47` status `ready` deltaP `12.0652` edge `0.0476` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.7702` n `47` status `ready` deltaP `12.3646` edge `0.0096` maxDD `-0.2275`
- `market_context_high->crypto_major_4h` score `0.7517` n `47` status `ready` deltaP `6.8241` edge `0.1076` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.5572` n `47` status `ready` deltaP `11.1574` edge `0.0077` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.3866` n `47` status `ready` deltaP `5.5007` edge `0.0773` maxDD `-4.5405`
- `news_risk_high->index_1h` score `0.1395` n `137` status `ready` deltaP `5.5313` edge `0.0039` maxDD `-0.3322`
- `market_context_high->metal_1h` score `0.0204` n `47` status `ready` deltaP `3.5769` edge `0.0104` maxDD `-0.1976`
- `market_context_high->fx_4h` score `-0.0165` n `47` status `ready` deltaP `8.7117` edge `0.0073` maxDD `-0.6736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
