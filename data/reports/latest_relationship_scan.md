# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T11:52:26.283136+00:00`
- Price records: `672`
- Market context records: `6388`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11074`

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

- `news_risk_high->crypto_alt_24h` score `14.0807` n `32` status `ready` deltaP `37.3264` edge `0.9393` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.4686` n `32` status `ready` deltaP `53.9931` edge `0.1791` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.343` n `32` status `ready` deltaP `37.6736` edge `0.1313` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `4.2856` n `32` status `ready` deltaP `17.5347` edge `0.5105` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.973` n `32` status `ready` deltaP `41.0823` edge `0.0618` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3979` n `32` status `ready` deltaP `28.8922` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4803` n `32` status `ready` deltaP `14.2777` edge `0.1413` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8411` n `32` status `ready` deltaP `10.5726` edge `0.0835` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.4853` n `216` status `ready` deltaP `15.0406` edge `0.0416` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.1718` n `216` status `ready` deltaP `9.0673` edge `0.0215` maxDD `-0.4108`
- `market_context_high->unknown_1h` score `0.0681` n `228` status `ready` deltaP `-6.4818` edge `0.1497` maxDD `-3.7317`
- `news_risk_high->unknown_1h` score `-0.1698` n `32` status `ready` deltaP `7.2792` edge `-0.0282` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.2304` n `146` status `ready` deltaP `19.6205` edge `0.0965` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.4666` n `228` status `ready` deltaP `2.3007` edge `0.0026` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.6694` n `32` status `ready` deltaP `-1.6467` edge `-0.0251` maxDD `-1.6464`
- `market_context_high->index_1h` score `-0.6709` n `228` status `ready` deltaP `-2.5134` edge `0.0027` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.6786` n `228` status `ready` deltaP `-2.5029` edge `-0.002` maxDD `-2.1314`
- `market_context_high->fx_1h` score `-0.7332` n `228` status `ready` deltaP `-0.9324` edge `-0.0015` maxDD `-0.9376`
- `news_risk_high->index_24h` score `-0.7385` n `32` status `ready` deltaP `0.5208` edge `-0.011` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.7875` n `216` status `ready` deltaP `8.0793` edge `0.0504` maxDD `-8.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
