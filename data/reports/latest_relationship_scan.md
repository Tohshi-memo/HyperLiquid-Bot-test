# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T15:07:29.445329+00:00`
- Price records: `672`
- Market context records: `2152`
- Flow alert records: `8092`
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

- `market_context_high->crypto_alt_4h` score `13.622` n `149` status `ready` deltaP `38.0699` edge `0.975` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.9406` n `149` status `ready` deltaP `42.067` edge `0.7676` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.381` n `149` status `ready` deltaP `25.0747` edge `0.4395` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.7552` n `149` status `ready` deltaP `25.9975` edge `0.3324` maxDD `-5.0894`
- `news_risk_high->commodity_4h` score `4.1121` n `36` status `ready` deltaP `29.9119` edge `0.3949` maxDD `-3.0367`
- `market_context_high->index_24h` score `3.6809` n `149` status `ready` deltaP `14.2769` edge `0.3344` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.5011` n `149` status `ready` deltaP `18.6111` edge `0.2154` maxDD `-1.817`
- `market_context_high->index_4h` score `3.3249` n `149` status `ready` deltaP `24.3206` edge `0.1833` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `3.2729` n `149` status `ready` deltaP `16.7424` edge `0.2475` maxDD `-4.9097`
- `market_context_high->metal_4h` score `3.0577` n `149` status `ready` deltaP `21.3527` edge `0.2512` maxDD `-4.7664`
- `market_context_high->equity_24h` score `3.0201` n `149` status `ready` deltaP `26.0125` edge `0.5681` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.8428` n `149` status `ready` deltaP `27.2616` edge `0.5872` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `2.4507` n `36` status `ready` deltaP `31.2331` edge `0.0144` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.1902` n `149` status `ready` deltaP `20.9359` edge `0.9998` maxDD `-62.3533`
- `news_risk_high->unknown_1h` score `1.0519` n `43` status `ready` deltaP `19.0189` edge `0.0078` maxDD `-1.7548`
- `news_risk_high->unknown_4h` score `0.8949` n `36` status `ready` deltaP `13.7026` edge `0.0957` maxDD `-2.7857`
- `market_context_high->equity_1h` score `0.8499` n `149` status `ready` deltaP `10.5996` edge `0.079` maxDD `-2.6402`
- `news_risk_high->commodity_1h` score `0.8111` n `43` status `ready` deltaP `10.7645` edge `0.1002` maxDD `-2.1052`
- `market_context_high->metal_1h` score `0.6792` n `149` status `ready` deltaP `9.8089` edge `0.0582` maxDD `-2.3594`
- `news_risk_high->fx_1h` score `0.4885` n `43` status `ready` deltaP `8.4389` edge `0.0101` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
