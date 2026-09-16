# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T13:07:33.806122+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11471`

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

- `news_risk_high->unknown_4h` score `368.2714` n `83` status `ready` deltaP `-21.0531` edge `30.9191` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `23.7339` n `78` status `ready` deltaP `47.7698` edge `1.6984` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `21.0169` n `78` status `ready` deltaP `39.7303` edge `1.6336` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.9578` n `78` status `ready` deltaP `47.2489` edge `1.1089` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.6885` n `78` status `ready` deltaP `53.4321` edge `0.3021` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4585` n `78` status `ready` deltaP `37.0993` edge `0.3363` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.3056` n `52` status `ready` deltaP `33.6806` edge `0.2176` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.3056` n `52` status `ready` deltaP `33.6806` edge `0.2176` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.0065` n `149` status `ready` deltaP `26.9692` edge `0.2066` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3669` n `52` status `ready` deltaP `31.9311` edge `-0.0114` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3669` n `52` status `ready` deltaP `31.9311` edge `-0.0114` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.232` n `149` status `ready` deltaP `29.1562` edge `0.0132` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.1696` n `52` status `ready` deltaP `28.2716` edge `0.0273` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.1696` n `52` status `ready` deltaP `28.2716` edge `0.0273` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.0694` n `149` status `ready` deltaP `24.7739` edge `0.0491` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8521` n `149` status `ready` deltaP `13.8157` edge `0.0166` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5029` n `83` status `ready` deltaP `14.3274` edge `0.0318` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.4274` n `52` status `ready` deltaP `10.0024` edge `0.1496` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.4274` n `52` status `ready` deltaP `10.0024` edge `0.1496` maxDD `-6.2526`
- `risk_on_high->commodity_1h` score `0.2288` n `52` status `ready` deltaP `6.8978` edge `0.0083` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
