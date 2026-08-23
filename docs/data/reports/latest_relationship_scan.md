# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T02:22:23.043281+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `news_risk_high->unknown_4h` score `11.5034` n `31` status `ready` deltaP `30.1829` edge `0.7574` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.6665` n `31` status `ready` deltaP `47.2561` edge `0.2405` maxDD `0.0`
- `news_risk_high->unknown_1h` score `4.8812` n `43` status `ready` deltaP `28.2726` edge `0.2301` maxDD `-0.2787`
- `news_risk_high->fx_4h` score `3.1197` n `31` status `ready` deltaP `36.5116` edge `0.03` maxDD `-0.0746`
- `news_risk_high->metal_4h` score `1.9839` n `31` status `ready` deltaP `25.4869` edge `0.0038` maxDD `-0.0045`
- `market_context_high->unknown_1h` score `1.6197` n `135` status `ready` deltaP `6.4638` edge `0.1146` maxDD `-0.4843`
- `news_risk_high->fx_1h` score `1.3566` n `43` status `ready` deltaP `18.5002` edge `0.0067` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.3164` n `43` status `ready` deltaP `25.477` edge `0.0271` maxDD `-0.9204`
- `market_context_high->unknown_4h` score `1.177` n `135` status `ready` deltaP `20.5533` edge `-0.0176` maxDD `-0.3736`
- `news_risk_high->index_4h` score `0.3648` n `31` status `ready` deltaP `7.1253` edge `0.0215` maxDD `-0.0884`
- `news_risk_high->commodity_1h` score `0.3306` n `43` status `ready` deltaP `12.4217` edge `-0.0096` maxDD `-0.4666`
- `news_risk_high->commodity_4h` score `0.2303` n `31` status `ready` deltaP `12.1508` edge `-0.0178` maxDD `-1.0273`
- `news_risk_high->metal_1h` score `0.1277` n `43` status `ready` deltaP `6.7922` edge `-0.0066` maxDD `-0.1184`
- `news_risk_high->crypto_major_4h` score `0.1154` n `31` status `ready` deltaP `-5.655` edge `0.184` maxDD `-6.9344`
- `market_context_high->fx_4h` score `0.1134` n `135` status `ready` deltaP `8.4112` edge `0.0087` maxDD `-0.3527`
- `market_context_high->index_1h` score `-0.0626` n `135` status `ready` deltaP `6.1466` edge `0.0041` maxDD `-0.9144`
- `news_risk_high->index_1h` score `-0.0839` n `43` status `ready` deltaP `3.3387` edge `0.0023` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.1428` n `135` status `ready` deltaP `1.9628` edge `0.0045` maxDD `-0.2043`
- `news_risk_high->crypto_major_1h` score `-0.2143` n `43` status `ready` deltaP `9.6575` edge `-0.0041` maxDD `-5.0209`
- `market_context_high->equity_1h` score `-0.361` n `135` status `ready` deltaP `4.185` edge `0.0328` maxDD `-5.2257`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
