# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T19:22:43.835127+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10206`

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

- `market_context_high->equity_24h` score `8.5713` n `41` status `ready` deltaP `16.1009` edge `1.232` maxDD `-16.9034`
- `market_context_high->index_24h` score `1.5714` n `41` status `ready` deltaP `13.7126` edge `0.1563` maxDD `-2.3671`
- `market_context_high->commodity_24h` score `0.5828` n `41` status `ready` deltaP `-4.6117` edge `0.1642` maxDD `-1.6995`
- `market_context_high->metal_1h` score `-0.3173` n `88` status `ready` deltaP `4.0964` edge `0.0139` maxDD `-1.4122`
- `market_context_high->fx_24h` score `-0.5807` n `41` status `ready` deltaP `0.4903` edge `-0.0254` maxDD `-1.1849`
- `market_context_high->commodity_1h` score `-0.602` n `88` status `ready` deltaP `-0.905` edge `-0.0029` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.7763` n `88` status `ready` deltaP `1.0395` edge `-0.0087` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-1.006` n `88` status `ready` deltaP `-3.8207` edge `0.0071` maxDD `-4.182`
- `market_context_high->metal_4h` score `-1.0224` n `88` status `ready` deltaP `-0.8267` edge `0.0128` maxDD `-4.0688`
- `market_context_high->index_1h` score `-1.0384` n `88` status `ready` deltaP `-8.2539` edge `0.005` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.3265` n `88` status `ready` deltaP `-14.3576` edge `-0.0059` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.6619` n `88` status `ready` deltaP `-7.6551` edge `0.0226` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-2.0083` n `88` status `ready` deltaP `-0.1157` edge `-0.0588` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1065` n `88` status `ready` deltaP `-6.5293` edge `-0.0084` maxDD `-2.4506`
- `market_context_high->metal_24h` score `-2.2448` n `41` status `ready` deltaP `2.2108` edge `-0.1465` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-3.2064` n `88` status `ready` deltaP `-5.2599` edge `-0.1137` maxDD `-15.9848`
- `market_context_high->unknown_4h` score `-3.2646` n `88` status `ready` deltaP `6.7386` edge `-0.2722` maxDD `-0.9153`
- `market_context_high->crypto_alt_24h` score `-7.2726` n `41` status `ready` deltaP `-9.5279` edge `-0.0331` maxDD `-33.4213`
- `market_context_high->equity_4h` score `-7.2875` n `88` status `ready` deltaP `-2.3592` edge `-0.2104` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.3982` n `88` status `ready` deltaP `0.6348` edge `-0.2756` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
