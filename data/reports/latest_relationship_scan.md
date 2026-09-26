# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T12:52:33.398867+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11822`

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

- `news_risk_high->unknown_24h` score `4478.2159` n `85` status `ready` deltaP `0.1736` edge `373.1835` maxDD `0.0`
- `market_context_high->unknown_1h` score `69.295` n `47` status `ready` deltaP `8.0201` edge `5.7282` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.202` n `47` status `ready` deltaP `22.4364` edge `3.8232` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `27.3834` n `47` status `ready` deltaP `18.1848` edge `2.1987` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.6383` n `47` status `ready` deltaP `33.3739` edge `1.9496` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.0209` n `47` status `ready` deltaP `28.6864` edge `0.4068` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.4209` n `47` status `ready` deltaP `28.982` edge `0.1157` maxDD `-0.2401`
- `news_risk_high->crypto_alt_24h` score `3.1444` n `85` status `ready` deltaP `12.0772` edge `0.5767` maxDD `-29.2814`
- `market_context_high->equity_4h` score `2.7521` n `47` status `ready` deltaP `17.6018` edge `0.1538` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.7053` n `47` status `ready` deltaP `31.2824` edge `0.0323` maxDD `-0.2323`
- `news_risk_high->index_24h` score `2.3156` n `85` status `ready` deltaP `26.8341` edge `0.0711` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.5275` n `85` status `ready` deltaP `32.161` edge `0.1462` maxDD `-6.8481`
- `market_context_high->crypto_alt_4h` score `1.3001` n `47` status `ready` deltaP `10.9075` edge `0.1024` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0374` n `47` status `ready` deltaP `11.9155` edge `0.0473` maxDD `-1.5564`
- `market_context_high->crypto_major_4h` score `0.8555` n `47` status `ready` deltaP `7.2814` edge `0.1132` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.8074` n `47` status `ready` deltaP `12.8137` edge `0.0097` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.4817` n `47` status `ready` deltaP `10.2592` edge `0.0074` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.4022` n `47` status `ready` deltaP `5.6504` edge `0.0776` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.0289` n `47` status `ready` deltaP `3.7266` edge `0.0105` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0711` n `139` status `ready` deltaP `2.9714` edge `0.0034` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
