# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T04:37:30.922042+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11562`

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

- `market_context_high->unknown_4h` score `37.8597` n `88` status `ready` deltaP `7.3725` edge `3.1506` maxDD `-0.9153`
- `market_context_high->equity_24h` score `33.6327` n `78` status `ready` deltaP `31.7224` edge `2.8317` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4247` n `78` status `ready` deltaP `25.5166` edge `0.3282` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `2.8299` n `78` status `ready` deltaP `19.0419` edge `0.7453` maxDD `-33.4213`
- `market_context_high->metal_24h` score `-0.0779` n `78` status `ready` deltaP `15.4668` edge `-0.0543` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.4144` n `88` status `ready` deltaP `3.3479` edge `0.0108` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5039` n `88` status `ready` deltaP `0.4423` edge `0.0007` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.6677` n `88` status `ready` deltaP `0.3603` edge `0.0226` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.8256` n `88` status `ready` deltaP `0.3464` edge `-0.0104` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0664` n `88` status `ready` deltaP `-8.703` edge `0.0044` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2297` n `88` status `ready` deltaP `-2.73` edge `-0.0011` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3794` n `88` status `ready` deltaP `-15.2558` edge `-0.0067` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7632` n `88` status `ready` deltaP `-8.703` edge `0.0166` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9717` n `88` status `ready` deltaP `0.4831` edge `-0.0581` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.2308` n `88` status `ready` deltaP `-8.4396` edge `-0.0116` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-3.0466` n `78` status `ready` deltaP `-8.7166` edge `-0.0358` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.1955` n `88` status `ready` deltaP `-5.2599` edge `-0.1123` maxDD `-15.9848`
- `market_context_high->commodity_24h` score `-4.8433` n `78` status `ready` deltaP `-21.2216` edge `-0.0393` maxDD `-19.879`
- `market_context_high->equity_4h` score `-7.4907` n `88` status `ready` deltaP `-2.439` edge `-0.2268` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1558` n `88` status `ready` deltaP `1.9402` edge `-0.2641` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
