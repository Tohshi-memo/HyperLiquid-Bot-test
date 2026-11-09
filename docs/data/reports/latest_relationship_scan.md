# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T22:22:33.135327+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `9918`

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

- `market_context_high->unknown_4h` score `29.3657` n `88` status `ready` deltaP `7.0676` edge `2.4448` maxDD `-0.9153`
- `market_context_high->equity_24h` score `15.4222` n `53` status `ready` deltaP `24.3844` edge `2.0551` maxDD `-16.9034`
- `market_context_high->index_24h` score `2.7143` n `53` status `ready` deltaP `20.1661` edge `0.2598` maxDD `-2.3671`
- `market_context_high->metal_24h` score `-0.3666` n `53` status `ready` deltaP `9.519` edge `-0.0387` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.4156` n `88` status `ready` deltaP `3.1982` edge `0.0117` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5662` n `88` status `ready` deltaP `-0.4559` edge `-0.0013` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.8477` n `88` status `ready` deltaP `0.0416` edge `-0.0112` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.9295` n `88` status `ready` deltaP `-2.9933` edge `0.0114` maxDD `-4.182`
- `market_context_high->crypto_alt_24h` score `-0.945` n `53` status `ready` deltaP `5.3824` edge `0.3524` maxDD `-33.4213`
- `market_context_high->metal_4h` score `-1.0891` n `88` status `ready` deltaP `-1.5105` edge `0.0088` maxDD `-4.0688`
- `market_context_high->index_1h` score `-1.1046` n `88` status `ready` deltaP `-9.3018` edge `0.0035` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.3023` n `88` status `ready` deltaP `-13.9085` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->commodity_24h` score `-1.3821` n `53` status `ready` deltaP `-13.0244` edge `0.078` maxDD `-6.4688`
- `market_context_high->equity_1h` score `-1.7726` n `88` status `ready` deltaP `-8.4036` edge `0.0134` maxDD `-8.1039`
- `market_context_high->fx_24h` score `-1.9244` n `53` status `ready` deltaP `-11.2357` edge `-0.0492` maxDD `-2.8088`
- `market_context_high->crypto_alt_1h` score `-1.9537` n `88` status `ready` deltaP `0.4831` edge `-0.0558` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.0885` n `88` status `ready` deltaP `-6.153` edge `-0.0086` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.2025` n `88` status `ready` deltaP `-5.2599` edge `-0.1132` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.4033` n `88` status `ready` deltaP `-2.5915` edge `-0.2185` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.14` n `88` status `ready` deltaP `2.0926` edge `-0.2638` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
