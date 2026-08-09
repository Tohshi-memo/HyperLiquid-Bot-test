# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T11:07:24.471562+00:00`
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

- `market_context_high->equity_24h` score `3.8112` n `103` status `ready` deltaP `4.5729` edge `0.5931` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.5944` n `103` status `ready` deltaP `11.8646` edge `0.1947` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.0965` n `143` status `ready` deltaP `14.2899` edge `0.0634` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7761` n `143` status `ready` deltaP `10.6916` edge `0.0277` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.745` n `103` status `ready` deltaP `21.4013` edge `0.0395` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.5414` n `103` status `ready` deltaP `8.753` edge `0.1642` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3085` n `143` status `ready` deltaP `4.1456` edge `-0.0038` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.391` n `143` status `ready` deltaP `-0.9442` edge `-0.0049` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.4797` n `143` status `ready` deltaP `5.8279` edge `-0.0035` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6651` n `143` status `ready` deltaP `-4.4386` edge `-0.0061` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.7978` n `143` status `ready` deltaP `0.3039` edge `-0.008` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.8725` n `143` status `ready` deltaP `0.2618` edge `0.0084` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-0.9734` n `143` status `ready` deltaP `-1.051` edge `-0.0169` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.8138` n `143` status `ready` deltaP `-9.3851` edge `-0.0244` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.4299` n `143` status `ready` deltaP `-0.5042` edge `-0.0654` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.092` n `143` status `ready` deltaP `-10.2383` edge `-0.0572` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-3.4881` n `143` status `ready` deltaP `-5.9899` edge `-0.0851` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-3.5826` n `103` status `ready` deltaP `4.1364` edge `-0.0767` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-5.5176` n `103` status `ready` deltaP `-15.2239` edge `-0.214` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.7741` n `143` status `ready` deltaP `-5.6447` edge `-0.5655` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
