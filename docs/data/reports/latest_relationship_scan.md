# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T22:07:18.169507+00:00`
- Price records: `672`
- Market context records: `1159`
- Flow alert records: `5239`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8750`

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

- `market_context_high->crypto_major_24h` score `20.5353` n `144` status `ready` deltaP `44.9653` edge `1.5247` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `10.0539` n `144` status `ready` deltaP `21.3542` edge `0.8971` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.7722` n `144` status `ready` deltaP `20.8334` edge `0.6018` maxDD `-6.4404`
- `market_context_high->index_24h` score `6.0102` n `144` status `ready` deltaP `19.4445` edge `0.427` maxDD `-3.4627`
- `market_context_high->metal_24h` score `5.564` n `144` status `ready` deltaP `-2.7778` edge `0.6489` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.4439` n `160` status `ready` deltaP `12.0579` edge `0.1896` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.1492` n `160` status `ready` deltaP `9.0701` edge `0.1036` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4564` n `160` status `ready` deltaP `7.2043` edge `0.0217` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3401` n `160` status `ready` deltaP `3.3308` edge `0.0439` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `0.1755` n `160` status `ready` deltaP `8.5823` edge `0.1574` maxDD `-8.3693`
- `market_context_high->fx_1h` score `0.1241` n `160` status `ready` deltaP `8.2822` edge `0.0007` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0303` n `160` status `ready` deltaP `7.253` edge `0.0321` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.3197` n `160` status `ready` deltaP `2.7358` edge `0.0394` maxDD `-3.4088`
- `market_context_high->metal_1h` score `-0.3812` n `160` status `ready` deltaP `5.8159` edge `-0.0095` maxDD `-2.2164`
- `market_context_high->unknown_24h` score `-0.779` n `144` status `ready` deltaP `3.4722` edge `0.1849` maxDD `-10.1706`
- `market_context_high->commodity_1h` score `-0.853` n `160` status `ready` deltaP `-3.4768` edge `-0.0054` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.9211` n `160` status `ready` deltaP `-2.3628` edge `-0.0027` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.0648` n `160` status `ready` deltaP `5.3963` edge `0.124` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-1.736` n `160` status `ready` deltaP `6.0671` edge `-0.0676` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-1.8021` n `160` status `ready` deltaP `7.2561` edge `-0.0769` maxDD `-6.7322`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
