# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T02:07:23.487040+00:00`
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

- `news_risk_high->unknown_4h` score `10.9612` n `30` status `ready` deltaP `30.3354` edge `0.7112` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.6473` n `30` status `ready` deltaP `47.2561` edge `0.2389` maxDD `0.0`
- `news_risk_high->unknown_1h` score `4.0739` n `42` status `ready` deltaP `28.0511` edge `0.1643` maxDD `-0.2787`
- `news_risk_high->fx_4h` score `3.0953` n `30` status `ready` deltaP `36.3415` edge `0.0291` maxDD `-0.0746`
- `news_risk_high->metal_4h` score `1.9493` n `30` status `ready` deltaP `24.9492` edge `0.0045` maxDD `-0.0045`
- `market_context_high->unknown_1h` score `1.6821` n `135` status `ready` deltaP `6.4638` edge `0.1198` maxDD `-0.4843`
- `news_risk_high->fx_1h` score `1.301` n `42` status `ready` deltaP `17.8358` edge `0.0065` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.2866` n `42` status `ready` deltaP `24.9786` edge `0.0266` maxDD `-0.9204`
- `market_context_high->unknown_4h` score `1.236` n `135` status `ready` deltaP `20.7058` edge `-0.0137` maxDD `-0.3736`
- `news_risk_high->crypto_major_4h` score `0.5725` n `30` status `ready` deltaP `-3.872` edge `0.2102` maxDD `-6.9344`
- `news_risk_high->commodity_4h` score `0.3969` n `30` status `ready` deltaP `14.624` edge `-0.0171` maxDD `-1.0273`
- `news_risk_high->commodity_1h` score `0.2944` n `42` status `ready` deltaP `11.7408` edge `-0.0097` maxDD `-0.4666`
- `news_risk_high->index_4h` score `0.2347` n `30` status `ready` deltaP `5.6199` edge `0.0207` maxDD `-0.0884`
- `news_risk_high->metal_1h` score `0.1926` n `42` status `ready` deltaP `8.0268` edge `-0.0065` maxDD `-0.1184`
- `market_context_high->fx_4h` score `0.1213` n `135` status `ready` deltaP `8.5637` edge `0.0087` maxDD `-0.3527`
- `news_risk_high->crypto_major_1h` score `0.1008` n `42` status `ready` deltaP `11.1135` edge `0.0266` maxDD `-5.0209`
- `market_context_high->index_1h` score `-0.0626` n `135` status `ready` deltaP `6.1466` edge `0.0041` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1428` n `135` status `ready` deltaP `1.9628` edge `0.0045` maxDD `-0.2043`
- `news_risk_high->index_1h` score `-0.143` n `42` status `ready` deltaP `2.2313` edge `0.0021` maxDD `-0.1583`
- `market_context_high->equity_1h` score `-0.3618` n `135` status `ready` deltaP `4.185` edge `0.0327` maxDD `-5.2257`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
