# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T00:52:29.081784+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `4996.3952` n `59` status `ready` deltaP `23.6022` edge `416.251` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `14.7773` n `40` status `ready` deltaP `51.8056` edge `0.9258` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.2218` n `40` status `ready` deltaP `51.3194` edge `0.6058` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.316` n `59` status `ready` deltaP `13.2054` edge `0.348` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.6171` n `59` status `ready` deltaP `15.5281` edge `0.0693` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `0.9564` n `41` status `ready` deltaP `12.6525` edge `0.1229` maxDD `-2.7703`
- `market_context_high->crypto_alt_4h` score `0.7001` n `41` status `ready` deltaP `7.6219` edge `0.1295` maxDD `-4.9116`
- `market_context_high->fx_4h` score `0.6107` n `41` status `ready` deltaP `19.6647` edge `0.0268` maxDD `-1.3685`
- `news_risk_high->equity_1h` score `0.5019` n `59` status `ready` deltaP `8.0712` edge `0.0703` maxDD `-2.916`
- `market_context_high->commodity_1h` score `0.3557` n `47` status `ready` deltaP `7.4149` edge `0.0336` maxDD `-1.3282`
- `news_risk_high->metal_4h` score `0.0076` n `59` status `ready` deltaP `4.1029` edge `0.0129` maxDD `-0.8085`
- `news_risk_high->index_1h` score `-0.015` n `59` status `ready` deltaP `3.537` edge `0.0068` maxDD `-0.5845`
- `market_context_high->fx_1h` score `-0.0233` n `47` status `ready` deltaP `6.8161` edge `-0.0095` maxDD `-0.7804`
- `news_risk_high->crypto_alt_1h` score `-0.0676` n `59` status `ready` deltaP `6.3813` edge `0.017` maxDD `-3.1233`
- `news_risk_high->fx_4h` score `-0.0933` n `59` status `ready` deltaP `9.3298` edge `0.0216` maxDD `-0.6604`
- `news_risk_high->fx_1h` score `-0.0954` n `59` status `ready` deltaP `2.3445` edge `0.0044` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.2314` n `59` status `ready` deltaP `1.3448` edge `0.0017` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.3993` n `59` status `ready` deltaP `1.8954` edge `0.0082` maxDD `-3.762`
- `news_risk_high->commodity_1h` score `-0.4061` n `59` status `ready` deltaP `4.6382` edge `-0.0152` maxDD `-2.0891`
- `market_context_high->fx_24h` score `-0.7463` n `40` status `ready` deltaP `0.6597` edge `0.0314` maxDD `-2.506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
