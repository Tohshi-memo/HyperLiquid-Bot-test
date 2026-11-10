# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T05:52:28.080277+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11538`

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

- `market_context_high->unknown_4h` score `37.9381` n `88` status `ready` deltaP `7.6774` edge `3.1551` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.442` n `83` status `ready` deltaP `32.0144` edge `2.8972` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4619` n `83` status `ready` deltaP `25.5769` edge `0.3309` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `3.4333` n `83` status `ready` deltaP `20.6845` edge `0.8117` maxDD `-33.4213`
- `market_context_high->metal_24h` score `-0.1862` n `83` status `ready` deltaP `15.9132` edge `-0.0663` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.4851` n `88` status `ready` deltaP `2.5994` edge `0.0099` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4868` n `88` status `ready` deltaP `0.7417` edge `0.0009` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.6174` n `88` status `ready` deltaP `0.8176` edge `0.026` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.8279` n `88` status `ready` deltaP `0.3464` edge `-0.0107` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.103` n `88` status `ready` deltaP `-9.3018` edge `0.0037` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2604` n `88` status `ready` deltaP `-3.0349` edge `-0.003` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3607` n `88` status `ready` deltaP `-14.9564` edge `-0.0063` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.8396` n `88` status `ready` deltaP `-9.4515` edge `0.0118` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.995` n `88` status `ready` deltaP `0.1837` edge `-0.0591` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1857` n `88` status `ready` deltaP `-7.6774` edge `-0.0109` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.9223` n `83` status `ready` deltaP `-7.6131` edge `-0.0328` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.2298` n `88` status `ready` deltaP `-5.5593` edge `-0.1147` maxDD `-15.9848`
- `market_context_high->commodity_24h` score `-5.5467` n `83` status `ready` deltaP `-22.689` edge `-0.0599` maxDD `-22.9966`
- `market_context_high->equity_4h` score `-7.5585` n `88` status `ready` deltaP `-2.8963` edge `-0.2294` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.2416` n `88` status `ready` deltaP `1.4828` edge `-0.2682` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
