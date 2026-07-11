# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T11:33:59.188588+00:00`
- Price records: `672`
- Market context records: `6386`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11072`

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

- `news_risk_high->crypto_alt_24h` score `14.109` n `32` status `ready` deltaP `37.5` edge `0.9405` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.4524` n `32` status `ready` deltaP `53.8194` edge `0.1789` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.3207` n `32` status `ready` deltaP `37.5` edge `0.1306` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `4.288` n `32` status `ready` deltaP `17.5347` edge `0.5108` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.9596` n `32` status `ready` deltaP `40.9299` edge `0.0617` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3967` n `32` status `ready` deltaP `28.8922` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4928` n `32` status `ready` deltaP `14.4274` edge `0.1419` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8551` n `32` status `ready` deltaP `10.7223` edge `0.0843` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.4853` n `216` status `ready` deltaP `15.0406` edge `0.0416` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.1469` n `216` status `ready` deltaP `8.7568` edge `0.0215` maxDD `-0.4108`
- `market_context_high->unknown_1h` score `0.0645` n `228` status `ready` deltaP `-6.4818` edge `0.1494` maxDD `-3.7317`
- `news_risk_high->unknown_1h` score `-0.1686` n `32` status `ready` deltaP `7.2792` edge `-0.0281` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.2312` n `146` status `ready` deltaP `19.6205` edge `0.0964` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.4501` n `228` status `ready` deltaP `2.5896` edge `0.0028` maxDD `-1.8877`
- `market_context_high->index_1h` score `-0.6559` n `228` status `ready` deltaP `-2.2245` edge `0.0027` maxDD `-0.7564`
- `news_risk_high->metal_1h` score `-0.6772` n `32` status `ready` deltaP `-1.7964` edge `-0.0251` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.6778` n `228` status `ready` deltaP `-2.5029` edge `-0.0019` maxDD `-2.1314`
- `market_context_high->fx_1h` score `-0.7344` n `228` status `ready` deltaP `-0.9324` edge `-0.0016` maxDD `-0.9376`
- `news_risk_high->index_24h` score `-0.737` n `32` status `ready` deltaP `0.5208` edge `-0.0108` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.8147` n `216` status `ready` deltaP `7.7687` edge `0.0502` maxDD `-8.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
