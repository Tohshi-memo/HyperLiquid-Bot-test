# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T01:22:26.288088+00:00`
- Price records: `672`
- Market context records: `8044`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11848`

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

- `market_context_high->equity_24h` score `18.7065` n `78` status `ready` deltaP `31.7558` edge `1.4382` maxDD `-4.9489`
- `market_context_high->metal_24h` score `8.2052` n `78` status `ready` deltaP `35.8752` edge `0.4446` maxDD `0.0`
- `market_context_high->equity_4h` score `7.4425` n `91` status `ready` deltaP `30.1377` edge `0.4972` maxDD `-4.233`
- `market_context_high->commodity_24h` score `4.8644` n `78` status `ready` deltaP `32.5534` edge `0.3038` maxDD `-6.2367`
- `market_context_high->index_4h` score `2.733` n `91` status `ready` deltaP `28.3403` edge `0.0748` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.3763` n `91` status `ready` deltaP `21.8038` edge `0.1149` maxDD `-0.979`
- `market_context_high->index_24h` score `2.1591` n `78` status `ready` deltaP `11.9028` edge `0.1676` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.6616` n `91` status `ready` deltaP `14.6888` edge `0.1223` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.3009` n `78` status `ready` deltaP `28.334` edge `0.0491` maxDD `-0.6971`
- `market_context_high->index_1h` score `0.7914` n `91` status `ready` deltaP `13.5389` edge `0.0187` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.7653` n `91` status `ready` deltaP `10.892` edge `0.029` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.3707` n `91` status `ready` deltaP `9.3407` edge `0.0263` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.2268` n `91` status `ready` deltaP `6.7811` edge `0.1455` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.1413` n `91` status `ready` deltaP `3.1795` edge `0.1023` maxDD `-3.9374`
- `market_context_high->fx_4h` score `-0.054` n `91` status `ready` deltaP `6.5197` edge `0.0051` maxDD `-0.5788`
- `market_context_high->crypto_alt_1h` score `-0.1578` n `91` status `ready` deltaP `0.4984` edge `0.0197` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.4449` n `91` status `ready` deltaP `1.0019` edge `-0.0014` maxDD `-1.9855`
- `market_context_high->fx_1h` score `-0.7691` n `91` status `ready` deltaP `-3.9992` edge `-0.0008` maxDD `-0.2637`
- `market_context_high->commodity_4h` score `-0.9012` n `91` status `ready` deltaP `4.4308` edge `0.0051` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-2.0296` n `91` status `ready` deltaP `6.3911` edge `-0.1694` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
