# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T21:22:30.584470+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `9954`

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

- `market_context_high->unknown_4h` score `14.0421` n `88` status `ready` deltaP `7.043` edge `1.168` maxDD `-0.9153`
- `market_context_high->equity_24h` score `13.1547` n `49` status `ready` deltaP `22.0741` edge `1.7798` maxDD `-16.9034`
- `market_context_high->index_24h` score `2.3522` n `49` status `ready` deltaP `18.3178` edge `0.2257` maxDD `-2.3671`
- `market_context_high->metal_1h` score `-0.4156` n `88` status `ready` deltaP `3.1982` edge `0.0117` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5942` n `88` status `ready` deltaP `-0.905` edge `-0.0019` maxDD `-1.7935`
- `market_context_high->commodity_24h` score `-0.7564` n `49` status `ready` deltaP `-10.7912` edge `0.1038` maxDD `-4.6399`
- `market_context_high->index_4h` score `-0.8425` n `88` status `ready` deltaP `0.1262` edge `-0.0111` maxDD `-2.4871`
- `market_context_high->metal_24h` score `-0.9238` n `49` status `ready` deltaP `7.5938` edge `-0.0723` maxDD `-1.4245`
- `market_context_high->commodity_4h` score `-0.9612` n `88` status `ready` deltaP `-3.3641` edge `0.0098` maxDD `-4.182`
- `market_context_high->metal_4h` score `-1.0853` n `88` status `ready` deltaP `-1.5878` edge `0.0098` maxDD `-4.0688`
- `market_context_high->index_1h` score `-1.1046` n `88` status `ready` deltaP `-9.3018` edge `0.0035` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.3023` n `88` status `ready` deltaP `-13.9085` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->fx_24h` score `-1.5549` n `49` status `ready` deltaP `-8.0784` edge `-0.0449` maxDD `-2.3801`
- `market_context_high->equity_1h` score `-1.7734` n `88` status `ready` deltaP `-8.4036` edge `0.0133` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-2.0013` n `88` status `ready` deltaP `0.034` edge `-0.0589` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.074` n `88` status `ready` deltaP `-5.9205` edge `-0.0083` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.2407` n `88` status `ready` deltaP `-5.709` edge `-0.1151` maxDD `-15.9848`
- `market_context_high->crypto_alt_24h` score `-3.8517` n `49` status `ready` deltaP `1.2238` edge `0.1803` maxDD `-33.4213`
- `market_context_high->equity_4h` score `-7.4029` n `88` status `ready` deltaP `-2.5114` edge `-0.219` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.2232` n `88` status `ready` deltaP `1.548` edge `-0.2671` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
