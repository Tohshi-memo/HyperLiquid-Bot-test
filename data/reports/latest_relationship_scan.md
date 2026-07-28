# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T16:22:41.371883+00:00`
- Price records: `672`
- Market context records: `8213`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5920`

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

- `news_risk_high->unknown_24h` score `8008.9107` n `43` status `ready` deltaP `36.9792` edge `667.1627` maxDD `0.0`
- `market_context_high->equity_24h` score `21.2728` n `30` status `ready` deltaP `37.5694` edge `1.6133` maxDD `-4.9489`
- `market_context_high->crypto_major_24h` score `18.2581` n `30` status `ready` deltaP `36.875` edge `1.3651` maxDD `-4.8208`
- `market_context_high->crypto_alt_24h` score `16.9813` n `30` status `ready` deltaP `37.3958` edge `1.2328` maxDD `-3.0264`
- `market_context_high->equity_4h` score `8.8859` n `30` status `ready` deltaP `47.2765` edge `0.4296` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.0019` n `30` status `ready` deltaP `45.2778` edge `0.3751` maxDD `-0.4771`
- `news_risk_high->equity_4h` score `7.3609` n `54` status `ready` deltaP `26.5357` edge `0.4962` maxDD `-3.4427`
- `market_context_high->crypto_major_4h` score `6.9005` n `30` status `ready` deltaP `30.1728` edge `0.3918` maxDD `-0.433`
- `market_context_high->index_24h` score `5.8403` n `30` status `ready` deltaP `37.743` edge `0.2744` maxDD `-0.8132`
- `market_context_high->crypto_alt_4h` score `5.0593` n `30` status `ready` deltaP `23.9634` edge `0.2821` maxDD `-0.6195`
- `market_context_high->metal_4h` score `3.8843` n `30` status `ready` deltaP `37.8659` edge `0.0843` maxDD `-0.0438`
- `market_context_high->index_4h` score `3.6157` n `30` status `ready` deltaP `36.4939` edge `0.0623` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.1493` n `54` status `ready` deltaP `22.7268` edge `0.1418` maxDD `-1.1366`
- `market_context_high->fx_24h` score `2.7313` n `30` status `ready` deltaP `45.3819` edge `0.0807` maxDD `-0.3134`
- `news_risk_high->index_4h` score `2.6761` n `54` status `ready` deltaP `22.4198` edge `0.0926` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.5524` n `54` status `ready` deltaP `12.7654` edge `0.3115` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.8546` n `54` status `ready` deltaP `13.0018` edge `0.1076` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.7811` n `54` status `ready` deltaP `14.7039` edge `0.0938` maxDD `-1.1388`
- `market_context_high->equity_1h` score `1.714` n `30` status `ready` deltaP `8.6527` edge `0.0998` maxDD `-0.1718`
- `market_context_high->crypto_major_1h` score `1.4254` n `30` status `ready` deltaP `13.7425` edge `0.0467` maxDD `-0.5626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
