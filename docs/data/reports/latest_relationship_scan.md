# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T19:22:28.249773+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9806`

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

- `news_risk_high->crypto_major_24h` score `23.7555` n `98` status `ready` deltaP `11.2281` edge `2.5906` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.3842` n `98` status `ready` deltaP `15.2671` edge `2.085` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `12.8893` n `41` status `ready` deltaP `-0.9147` edge `1.0952` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.117` n `101` status `ready` deltaP `21.9678` edge `0.4009` maxDD `-7.675`
- `market_context_high->commodity_4h` score `4.2343` n `41` status `ready` deltaP `37.3476` edge `0.1172` maxDD `-0.0659`
- `news_risk_high->crypto_major_4h` score `4.0065` n `101` status `ready` deltaP `21.0532` edge `0.3193` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.9309` n `101` status `ready` deltaP `16.8302` edge `0.1786` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1923` n `101` status `ready` deltaP `18.6266` edge `0.1108` maxDD `-2.8494`
- `market_context_high->fx_4h` score `1.8501` n `41` status `ready` deltaP `25.1524` edge `0.0122` maxDD `-0.0569`
- `news_risk_high->commodity_24h` score `1.0448` n `98` status `ready` deltaP `22.775` edge `0.1127` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.9236` n `53` status `ready` deltaP `13.2838` edge `0.0062` maxDD `-0.0897`
- `market_context_high->commodity_1h` score `0.6977` n `53` status `ready` deltaP `12.5042` edge `0.0336` maxDD `-0.2012`
- `news_risk_high->metal_4h` score `0.63` n `101` status `ready` deltaP `17.2512` edge `0.0429` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6293` n `101` status `ready` deltaP `14.598` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->equity_24h` score `0.5398` n `98` status `ready` deltaP `16.3974` edge `0.0766` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.2793` n `53` status `ready` deltaP `7.7421` edge `0.0065` maxDD `-0.4538`
- `news_risk_high->equity_1h` score `0.2292` n `101` status `ready` deltaP `5.364` edge `0.0239` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `0.1469` n `101` status `ready` deltaP `8.0309` edge `0.0223` maxDD `-0.421`
- `news_risk_high->metal_24h` score `0.141` n `98` status `ready` deltaP `14.9837` edge `0.0026` maxDD `-2.4203`
- `news_risk_high->fx_1h` score `-0.3166` n `101` status `ready` deltaP `1.7949` edge `0.006` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
