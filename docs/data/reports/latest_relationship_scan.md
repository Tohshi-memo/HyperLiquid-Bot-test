# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T15:37:29.411977+00:00`
- Price records: `672`
- Market context records: `2154`
- Flow alert records: `8098`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `market_context_high->crypto_alt_4h` score `13.6474` n `147` status `ready` deltaP `38.0122` edge `0.9775` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.9417` n `147` status `ready` deltaP `41.93` edge `0.7686` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.2874` n `147` status `ready` deltaP `24.7003` edge `0.4342` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.6571` n `147` status `ready` deltaP `25.8058` edge `0.3255` maxDD `-5.0894`
- `news_risk_high->commodity_4h` score `4.1166` n `38` status `ready` deltaP `30.9291` edge `0.3887` maxDD `-3.0367`
- `market_context_high->index_24h` score `3.584` n `147` status `ready` deltaP `13.9208` edge `0.3287` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.4569` n `147` status `ready` deltaP `18.3134` edge `0.2137` maxDD `-1.817`
- `market_context_high->index_4h` score `3.294` n `147` status `ready` deltaP `24.1289` edge `0.182` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `3.2472` n `147` status `ready` deltaP `16.4355` edge `0.2474` maxDD `-4.9097`
- `market_context_high->metal_4h` score `2.8997` n `147` status `ready` deltaP `20.9235` edge `0.2409` maxDD `-4.7664`
- `market_context_high->equity_24h` score `2.8666` n `147` status `ready` deltaP `25.6838` edge `0.5575` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.8427` n `147` status `ready` deltaP `27.3349` edge `0.5867` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `2.516` n `38` status `ready` deltaP `31.6592` edge `0.017` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.1887` n `147` status `ready` deltaP `20.6987` edge `1.0012` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.6329` n `38` status `ready` deltaP `15.7494` edge `0.1034` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.0039` n `43` status `ready` deltaP `18.7195` edge `0.0058` maxDD `-1.7548`
- `news_risk_high->commodity_1h` score `0.8142` n `43` status `ready` deltaP `10.7645` edge `0.1006` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.7801` n `147` status `ready` deltaP `10.1613` edge `0.0761` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.6771` n `147` status `ready` deltaP `9.7825` edge `0.0582` maxDD `-2.3594`
- `news_risk_high->fx_1h` score `0.4885` n `43` status `ready` deltaP `8.4389` edge `0.0101` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
