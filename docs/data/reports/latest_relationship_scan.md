# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T00:37:27.110137+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11566`

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

- `market_context_high->unknown_4h` score `94.2646` n `88` status `ready` deltaP `8.4396` edge `7.8439` maxDD `-0.9161`
- `market_context_high->unknown_24h` score `72.8172` n `88` status `ready` deltaP `4.9937` edge `6.0489` maxDD `-0.4609`
- `news_risk_high->equity_24h` score `47.9036` n `38` status `ready` deltaP `36.5052` edge `3.7486` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `26.433` n `38` status `ready` deltaP `48.6615` edge `2.0749` maxDD `-12.7247`
- `market_context_high->equity_24h` score `19.7578` n `88` status `ready` deltaP `19.4597` edge `1.7559` maxDD `-16.7984`
- `news_risk_high->crypto_alt_24h` score `11.7008` n `38` status `ready` deltaP `24.6767` edge `0.9854` maxDD `-10.9876`
- `news_risk_high->equity_4h` score `11.2123` n `53` status `ready` deltaP `33.9536` edge `0.8202` maxDD `-6.9762`
- `news_risk_high->index_24h` score `7.0422` n `38` status `ready` deltaP `33.218` edge `0.3654` maxDD `0.0`
- `news_risk_high->commodity_24h` score `6.9652` n `38` status `ready` deltaP `39.9654` edge `0.314` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.4433` n `88` status `ready` deltaP `34.9638` edge `1.1024` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.7683` n `88` status `ready` deltaP `34.315` edge `0.2239` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.2713` n `53` status `ready` deltaP `41.3657` edge `0.1178` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.744` n `53` status `ready` deltaP `20.4384` edge `0.3245` maxDD `-9.2335`
- `market_context_high->index_24h` score `3.7055` n `88` status `ready` deltaP `19.5816` edge `0.2245` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.6005` n `53` status `ready` deltaP `18.6137` edge `0.2472` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `2.6294` n `53` status `ready` deltaP `23.815` edge `0.0857` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.2044` n `53` status `ready` deltaP `20.8985` edge `0.088` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.0264` n `53` status `ready` deltaP `24.3927` edge `0.0317` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `2.0079` n `53` status `ready` deltaP `23.907` edge `0.2619` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3664` n `53` status `ready` deltaP `17.7748` edge `0.0255` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
