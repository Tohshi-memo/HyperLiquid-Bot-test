# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T16:37:29.862697+00:00`
- Price records: `672`
- Market context records: `8214`
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

- `news_risk_high->unknown_24h` score `7983.4071` n `43` status `ready` deltaP `36.9792` edge `665.0374` maxDD `0.0`
- `market_context_high->equity_24h` score `21.3563` n `30` status `ready` deltaP `37.743` edge `1.6191` maxDD `-4.9489`
- `market_context_high->crypto_major_24h` score `18.2773` n `30` status `ready` deltaP `36.875` edge `1.3667` maxDD `-4.8208`
- `market_context_high->crypto_alt_24h` score `17.0137` n `30` status `ready` deltaP `37.3958` edge `1.2355` maxDD `-3.0264`
- `market_context_high->equity_4h` score `8.9185` n `30` status `ready` deltaP `47.4289` edge `0.4313` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.0349` n `30` status `ready` deltaP `45.4514` edge `0.3767` maxDD `-0.4771`
- `news_risk_high->equity_4h` score `7.3934` n `54` status `ready` deltaP `26.6881` edge `0.4979` maxDD `-3.4427`
- `market_context_high->crypto_major_4h` score `6.8595` n `30` status `ready` deltaP `30.0204` edge `0.3894` maxDD `-0.433`
- `market_context_high->index_24h` score `5.8451` n `30` status `ready` deltaP `37.743` edge `0.2748` maxDD `-0.8132`
- `market_context_high->crypto_alt_4h` score `5.0364` n `30` status `ready` deltaP `23.811` edge `0.2812` maxDD `-0.6195`
- `market_context_high->metal_4h` score `3.8807` n `30` status `ready` deltaP `37.8659` edge `0.084` maxDD `-0.0438`
- `market_context_high->index_4h` score `3.6157` n `30` status `ready` deltaP `36.4939` edge `0.0623` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.1696` n `54` status `ready` deltaP `22.8765` edge `0.1425` maxDD `-1.1366`
- `market_context_high->fx_24h` score `2.7328` n `30` status `ready` deltaP `45.3819` edge `0.0809` maxDD `-0.3134`
- `news_risk_high->index_4h` score `2.6761` n `54` status `ready` deltaP `22.4198` edge `0.0926` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.5257` n `54` status `ready` deltaP `12.613` edge `0.3091` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.8558` n `54` status `ready` deltaP `13.0018` edge `0.1077` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.7811` n `54` status `ready` deltaP `14.7039` edge `0.0938` maxDD `-1.1388`
- `market_context_high->equity_1h` score `1.7344` n `30` status `ready` deltaP `8.8024` edge `0.1005` maxDD `-0.1718`
- `market_context_high->crypto_major_1h` score `1.4266` n `30` status `ready` deltaP `13.7425` edge `0.0468` maxDD `-0.5626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
