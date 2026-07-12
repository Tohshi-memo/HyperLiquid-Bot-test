# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T17:22:31.074836+00:00`
- Price records: `672`
- Market context records: `6521`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7848`

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

- `news_risk_high->crypto_alt_24h` score `13.2487` n `32` status `ready` deltaP `36.211` edge `0.8774` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.5212` n `32` status `ready` deltaP `53.8995` edge `0.1841` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.4922` n `140` status `ready` deltaP `10.822` edge `0.7989` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.8956` n `32` status `ready` deltaP `20.911` edge `0.5662` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.6865` n `38` status `ready` deltaP `39.0164` edge `0.0517` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.5739` n `183` status `ready` deltaP `-5.7001` edge `0.3426` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.2027` n `32` status `ready` deltaP `23.3698` edge `0.0483` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.7784` n `38` status `ready` deltaP `22.3133` edge `0.0175` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.6469` n `140` status `ready` deltaP `14.7091` edge `0.226` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.6312` n `172` status `ready` deltaP `13.6698` edge `0.0291` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.5839` n `38` status `ready` deltaP `5.2001` edge `0.0939` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.3655` n `172` status `ready` deltaP `10.295` edge `0.1172` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.0929` n `38` status `ready` deltaP `1.7334` edge `0.0513` maxDD `-2.0756`
- `market_context_high->unknown_4h` score `-0.2188` n `172` status `ready` deltaP `-20.1396` edge `0.3566` maxDD `-10.5788`
- `news_risk_high->index_24h` score `-0.3179` n `32` status `ready` deltaP `6.51` edge `0.003` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.3523` n `172` status `ready` deltaP `10.0078` edge `0.058` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.4181` n `183` status `ready` deltaP `-0.2062` edge `-0.0015` maxDD `-0.7249`
- `market_context_high->crypto_major_4h` score `-0.4948` n `172` status `ready` deltaP `11.9718` edge `0.0858` maxDD `-12.6576`
- `market_context_high->commodity_1h` score `-0.4968` n `183` status `ready` deltaP `1.007` edge `-0.0021` maxDD `-2.1314`
- `market_context_high->crypto_major_1h` score `-0.5187` n `183` status `ready` deltaP `6.8682` edge `0.0143` maxDD `-6.7936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
