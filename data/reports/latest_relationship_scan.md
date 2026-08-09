# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T11:37:29.838547+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9825`

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

- `market_context_high->equity_24h` score `3.828` n `103` status `ready` deltaP `4.5729` edge `0.5945` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.5618` n `103` status `ready` deltaP `11.5174` edge `0.1943` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.0661` n `143` status `ready` deltaP `13.985` edge `0.0629` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7773` n `143` status `ready` deltaP `10.6916` edge `0.0278` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7388` n `103` status `ready` deltaP `21.4013` edge `0.0387` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.5406` n `103` status `ready` deltaP `8.753` edge `0.1641` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3205` n `143` status `ready` deltaP `3.9959` edge `-0.0038` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.3746` n `143` status `ready` deltaP `-0.6448` edge `-0.0048` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.4931` n `143` status `ready` deltaP `5.6755` edge `-0.0036` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6651` n `143` status `ready` deltaP `-4.4386` edge `-0.0061` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.7722` n `143` status `ready` deltaP `0.6087` edge `-0.0079` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.8582` n `143` status `ready` deltaP `0.4115` edge `0.0086` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-0.9734` n `143` status `ready` deltaP `-1.051` edge `-0.0169` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.8305` n `143` status `ready` deltaP `-9.5348` edge `-0.0248` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.3983` n `143` status `ready` deltaP `-0.1993` edge `-0.0648` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.1064` n `143` status `ready` deltaP `-10.388` edge `-0.0574` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-3.5039` n `143` status `ready` deltaP `-6.1424` edge `-0.0854` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-3.6524` n `103` status `ready` deltaP `3.7891` edge `-0.0802` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-5.6306` n `103` status `ready` deltaP `-15.5711` edge `-0.2211` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.761` n `143` status `ready` deltaP `-5.495` edge `-0.5654` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
