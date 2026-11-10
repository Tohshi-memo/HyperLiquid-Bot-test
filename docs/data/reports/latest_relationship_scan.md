# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T05:07:33.392946+00:00`
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

- `market_context_high->unknown_4h` score `37.9045` n `88` status `ready` deltaP `7.6774` edge `3.1523` maxDD `-0.9153`
- `market_context_high->equity_24h` score `33.8618` n `80` status `ready` deltaP `31.8566` edge `2.8499` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4193` n `80` status `ready` deltaP `25.5546` edge `0.3275` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `3.0356` n `80` status `ready` deltaP `19.5927` edge `0.768` maxDD `-33.4213`
- `market_context_high->metal_24h` score `-0.1365` n `80` status `ready` deltaP `15.6651` edge `-0.0605` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.4432` n `88` status `ready` deltaP `3.0485` edge `0.0104` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4938` n `88` status `ready` deltaP `0.592` edge `0.001` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.6386` n `88` status `ready` deltaP `0.6652` edge `0.0243` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.8264` n `88` status `ready` deltaP `0.3464` edge `-0.0105` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0843` n `88` status `ready` deltaP `-9.0024` edge `0.0041` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2431` n `88` status `ready` deltaP `-2.8825` edge `-0.0018` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3872` n `88` status `ready` deltaP `-15.4055` edge `-0.0067` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7928` n `88` status `ready` deltaP `-9.0024` edge `0.0148` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9654` n `88` status `ready` deltaP `0.4831` edge `-0.0573` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.2141` n `88` status `ready` deltaP `-8.1347` edge `-0.0115` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.9198` n `80` status `ready` deltaP `-7.4025` edge `-0.034` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.1931` n `88` status `ready` deltaP `-5.2599` edge `-0.112` maxDD `-15.9848`
- `market_context_high->commodity_24h` score `-5.1824` n `80` status `ready` deltaP `-21.8306` edge `-0.051` maxDD `-21.43`
- `market_context_high->equity_4h` score `-7.5015` n `88` status `ready` deltaP `-2.439` edge `-0.2277` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1558` n `88` status `ready` deltaP `1.9402` edge `-0.2641` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
