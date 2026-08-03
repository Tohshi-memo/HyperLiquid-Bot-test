# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T06:22:58.392798+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5903`

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

- `news_risk_high->unknown_24h` score `1150.7579` n `37` status `ready` deltaP `19.5711` edge `95.8081` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `13.2087` n `40` status `ready` deltaP `51.4583` edge `0.7974` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.0298` n `40` status `ready` deltaP `51.3194` edge `0.5898` maxDD `-0.6889`
- `news_risk_high->commodity_1h` score `0.9251` n `37` status `ready` deltaP `19.5137` edge `0.0097` maxDD `-0.6947`
- `news_risk_high->equity_4h` score `0.7688` n `37` status `ready` deltaP `-6.3407` edge `0.2172` maxDD `-3.4427`
- `news_risk_high->index_4h` score `0.3461` n `37` status `ready` deltaP `1.92` edge `0.0541` maxDD `-0.3783`
- `market_context_high->commodity_1h` score `0.3377` n `47` status `ready` deltaP `7.2652` edge `0.0323` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.3021` n `47` status `ready` deltaP `5.0338` edge `0.0898` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.0475` n `47` status `ready` deltaP `14.0277` edge `-0.0039` maxDD `-1.8531`
- `market_context_high->fx_1h` score `0.0328` n `47` status `ready` deltaP `7.7143` edge `-0.0083` maxDD `-0.7804`
- `news_risk_high->fx_24h` score `-0.1743` n `37` status `ready` deltaP `7.484` edge `0.0374` maxDD `-2.4786`
- `market_context_high->crypto_alt_4h` score `-0.2322` n `47` status `ready` deltaP `2.1439` edge `0.0465` maxDD `-4.9116`
- `news_risk_high->metal_1h` score `-0.233` n `37` status `ready` deltaP `0.1538` edge `0.0011` maxDD `-0.5599`
- `news_risk_high->crypto_alt_1h` score `-0.2873` n `37` status `ready` deltaP `5.2517` edge `-0.0078` maxDD `-3.1233`
- `news_risk_high->commodity_4h` score `-0.3075` n `37` status `ready` deltaP `7.449` edge `-0.0206` maxDD `-2.0418`
- `news_risk_high->fx_4h` score `-0.3807` n `37` status `ready` deltaP `0.2266` edge `0.0281` maxDD `-0.6071`
- `news_risk_high->fx_1h` score `-0.4769` n `37` status `ready` deltaP `-4.3616` edge `0.0002` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.6123` n `37` status `ready` deltaP `-2.9981` edge `-0.0029` maxDD `-0.5845`
- `market_context_high->fx_24h` score `-0.6803` n `40` status `ready` deltaP `0.6597` edge `0.0369` maxDD `-2.506`
- `news_risk_high->metal_4h` score `-0.7618` n `37` status `ready` deltaP `-1.9612` edge `-0.0153` maxDD `-0.8085`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
