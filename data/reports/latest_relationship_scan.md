# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T09:37:30.402860+00:00`
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

- `news_risk_high->unknown_24h` score `3659.4495` n `96` status `ready` deltaP `-0.6945` edge `304.9632` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `69.9057` n `47` status `ready` deltaP `8.619` edge `5.7751` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.6378` n `47` status `ready` deltaP `22.7837` edge `3.8572` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.6932` n `47` status `ready` deltaP `20.4417` edge `2.2928` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.4775` n `47` status `ready` deltaP `33.3739` edge `1.9362` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.1314` n `47` status `ready` deltaP `29.9017` edge `0.4079` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.3939` n `47` status `ready` deltaP `28.8084` edge `0.1146` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7387` n `47` status `ready` deltaP `17.4494` edge `0.1537` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5676` n `47` status `ready` deltaP `29.6056` edge `0.032` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.4341` n `47` status `ready` deltaP `11.5172` edge `0.1095` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.1355` n `96` status `ready` deltaP `26.2153` edge `0.1369` maxDD `-6.9545`
- `news_risk_high->index_24h` score `1.1089` n `96` status `ready` deltaP `17.5347` edge `0.0492` maxDD `-2.2287`
- `market_context_high->equity_1h` score `1.0518` n `47` status `ready` deltaP `12.0652` edge `0.0475` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.7702` n `47` status `ready` deltaP `12.3646` edge `0.0096` maxDD `-0.2275`
- `market_context_high->crypto_major_4h` score `0.7034` n `47` status `ready` deltaP `6.5192` edge `0.1056` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.5584` n `47` status `ready` deltaP `11.1574` edge `0.0078` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.347` n `47` status `ready` deltaP `5.2013` edge `0.076` maxDD `-4.5405`
- `news_risk_high->index_1h` score `0.1371` n `137` status `ready` deltaP `5.5313` edge `0.0037` maxDD `-0.3322`
- `market_context_high->fx_4h` score `0.0091` n `47` status `ready` deltaP `9.0166` edge `0.0074` maxDD `-0.6736`
- `market_context_high->metal_1h` score `0.004` n `47` status `ready` deltaP `3.2775` edge `0.0103` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
