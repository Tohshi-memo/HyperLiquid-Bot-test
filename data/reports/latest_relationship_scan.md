# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T03:07:37.092715+00:00`
- Price records: `672`
- Market context records: `8156`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11842`

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

- `market_context_high->equity_24h` score `21.4555` n `74` status `ready` deltaP `44.3975` edge `1.583` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.9252` n `75` status `ready` deltaP `37.5406` edge `0.6003` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.6452` n `74` status `ready` deltaP `39.4097` edge `0.4577` maxDD `0.0`
- `news_risk_high->equity_4h` score `8.5591` n `43` status `ready` deltaP `32.5794` edge `0.5166` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `5.2348` n `43` status `ready` deltaP `19.2712` edge `0.3683` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.9656` n `75` status `ready` deltaP `35.9777` edge `0.0949` maxDD `-0.0092`
- `market_context_high->equity_1h` score `3.8794` n `75` status `ready` deltaP `20.6248` edge `0.2061` maxDD `-0.6254`
- `news_risk_high->equity_1h` score `3.8518` n `43` status `ready` deltaP `29.679` edge `0.154` maxDD `-1.1366`
- `market_context_high->index_24h` score `3.6167` n `74` status `ready` deltaP `23.5829` edge `0.2112` maxDD `-1.3621`
- `news_risk_high->index_4h` score `2.7195` n `43` status `ready` deltaP `22.7063` edge `0.0943` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.4702` n `75` status `ready` deltaP `23.7887` edge `0.1095` maxDD `-0.979`
- `market_context_high->crypto_alt_4h` score `2.1297` n `75` status `ready` deltaP `9.6585` edge `0.2248` maxDD `-3.9374`
- `market_context_high->fx_24h` score `2.0621` n `74` status `ready` deltaP `27.6887` edge `0.0576` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `2.0191` n `75` status `ready` deltaP `11.8293` edge `0.2612` maxDD `-6.7444`
- `market_context_high->index_1h` score `1.7311` n `75` status `ready` deltaP `20.3673` edge `0.0281` maxDD `-0.2368`
- `market_context_high->commodity_24h` score `1.6407` n `74` status `ready` deltaP `31.9022` edge `0.2862` maxDD `-15.7497`
- `news_risk_high->metal_4h` score `1.5489` n `43` status `ready` deltaP `14.8894` edge `0.0766` maxDD `-0.7433`
- `market_context_high->crypto_major_1h` score `1.4361` n `75` status `ready` deltaP `14.0279` edge `0.0672` maxDD `-1.6171`
- `news_risk_high->crypto_major_1h` score `1.3247` n `43` status `ready` deltaP `6.183` edge `0.1089` maxDD `-1.1783`
- `market_context_high->metal_1h` score `1.1076` n `75` status `ready` deltaP `14.7206` edge `0.032` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
