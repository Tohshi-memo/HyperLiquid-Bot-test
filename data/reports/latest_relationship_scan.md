# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T02:07:25.491452+00:00`
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

- `market_context_high->unknown_24h` score `101.3868` n `88` status `ready` deltaP `4.9937` edge `8.4297` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `92.932` n `88` status `ready` deltaP `7.9823` edge `7.7359` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `42.1122` n `44` status `ready` deltaP `35.4671` edge `3.2729` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `24.0845` n `44` status `ready` deltaP `43.8896` edge `1.911` maxDD `-12.7247`
- `market_context_high->equity_24h` score `18.4604` n `88` status `ready` deltaP `18.4216` edge `1.6547` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.2807` n `53` status `ready` deltaP `33.9536` edge `0.8259` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.6256` n `44` status `ready` deltaP `39.9654` edge `0.2857` maxDD `0.0`
- `news_risk_high->index_24h` score `6.358` n `44` status `ready` deltaP `32.1799` edge `0.3153` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.1484` n `88` status `ready` deltaP `34.9638` edge `1.0646` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.8525` n `88` status `ready` deltaP `35.0071` edge `0.2263` maxDD `-1.4245`
- `news_risk_high->crypto_alt_24h` score `4.6564` n `44` status `ready` deltaP `16.782` edge `0.7296` maxDD `-15.5602`
- `news_risk_high->metal_4h` score `4.3377` n `53` status `ready` deltaP `41.6705` edge `0.1213` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.8932` n `53` status `ready` deltaP `20.7433` edge `0.3349` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.4866` n `53` status `ready` deltaP `18.1646` edge `0.2407` maxDD `-3.6997`
- `market_context_high->index_24h` score `3.4556` n `88` status `ready` deltaP `18.5435` edge `0.2106` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.6054` n `53` status `ready` deltaP `23.815` edge `0.0837` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.196` n `53` status `ready` deltaP `20.8985` edge `0.0873` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.1771` n `53` status `ready` deltaP `24.8216` edge `0.2775` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `2.0612` n `53` status `ready` deltaP `24.6921` edge `0.0326` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3161` n `53` status `ready` deltaP `17.3257` edge `0.0243` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
