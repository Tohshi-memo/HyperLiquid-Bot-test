# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T16:37:29.717698+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11441`

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

- `news_risk_high->unknown_4h` score `367.7242` n `83` status `ready` deltaP `-21.0531` edge `30.8735` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `23.1423` n `78` status `ready` deltaP `47.7698` edge `1.6491` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `20.5117` n `78` status `ready` deltaP `39.7303` edge `1.5915` maxDD `-9.098`
- `news_risk_high->equity_24h` score `13.978` n `78` status `ready` deltaP `44.992` edge `1.0423` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.3453` n `78` status `ready` deltaP `51.0016` edge `0.2897` maxDD `-0.075`
- `news_risk_high->metal_24h` score `5.8837` n `78` status `ready` deltaP `34.6688` edge `0.3046` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.6914` n `52` status `ready` deltaP `35.9375` edge `0.2347` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.6914` n `52` status `ready` deltaP `35.9375` edge `0.2347` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.3923` n `149` status `ready` deltaP `29.2261` edge `0.2237` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3777` n `52` status `ready` deltaP `31.9311` edge `-0.0105` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3777` n `52` status `ready` deltaP `31.9311` edge `-0.0105` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2428` n `149` status `ready` deltaP `29.1562` edge `0.0141` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.2312` n `52` status `ready` deltaP `28.5764` edge `0.0304` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.2312` n `52` status `ready` deltaP `28.5764` edge `0.0304` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.1309` n `149` status `ready` deltaP `25.0787` edge `0.0522` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9204` n `149` status `ready` deltaP `14.2648` edge `0.0193` maxDD `-0.3491`
- `risk_on_high->crypto_alt_4h` score `0.4382` n `52` status `ready` deltaP `9.8499` edge `0.152` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.4382` n `52` status `ready` deltaP `9.8499` edge `0.152` maxDD `-6.2526`
- `news_risk_high->index_4h` score `0.3907` n `83` status `ready` deltaP `12.4982` edge `0.0296` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2971` n `52` status `ready` deltaP `7.3469` edge `0.011` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
