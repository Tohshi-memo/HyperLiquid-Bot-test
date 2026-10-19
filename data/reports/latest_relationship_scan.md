# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T09:37:26.448392+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->commodity_24h` score `1.7321` n `76` status `ready` deltaP `16.6933` edge `0.1182` maxDD `-1.8119`
- `risk_on_high->equity_24h` score `1.3062` n `43` status `ready` deltaP `-19.2842` edge `0.7483` maxDD `-28.5375`
- `risk_on_and_context->equity_24h` score `1.3062` n `43` status `ready` deltaP `-19.2842` edge `0.7483` maxDD `-28.5375`
- `risk_on_high->equity_1h` score `0.7584` n `43` status `ready` deltaP `15.2735` edge `0.0192` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.7584` n `43` status `ready` deltaP `15.2735` edge `0.0192` maxDD `-1.9591`
- `market_context_high->crypto_major_24h` score `0.7426` n `76` status `ready` deltaP `1.9188` edge `0.6921` maxDD `-35.1086`
- `risk_on_high->index_1h` score `0.5527` n `43` status `ready` deltaP `11.3696` edge `0.0006` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.5527` n `43` status `ready` deltaP `11.3696` edge `0.0006` maxDD `-0.4273`
- `market_context_high->equity_24h` score `0.4619` n `76` status `ready` deltaP `0.0549` edge `0.957` maxDD `-55.843`
- `market_context_high->crypto_major_4h` score `0.2851` n `77` status `ready` deltaP `3.5397` edge `0.3534` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.2227` n `77` status `ready` deltaP `3.5987` edge `0.0927` maxDD `-3.7178`
- `risk_on_high->fx_4h` score `0.0508` n `43` status `ready` deltaP `3.4564` edge `0.0076` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0508` n `43` status `ready` deltaP `3.4564` edge `0.0076` maxDD `-0.1126`
- `risk_on_high->equity_4h` score `-0.0918` n `43` status `ready` deltaP `5.2272` edge `0.0928` maxDD `-4.824`
- `risk_on_and_context->equity_4h` score `-0.0918` n `43` status `ready` deltaP `5.2272` edge `0.0928` maxDD `-4.824`
- `risk_on_high->commodity_24h` score `-0.1187` n `43` status `ready` deltaP `12.0728` edge `-0.0106` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.1187` n `43` status `ready` deltaP `12.0728` edge `-0.0106` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `-0.238` n `43` status `ready` deltaP `0.7123` edge `-0.0006` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.238` n `43` status `ready` deltaP `0.7123` edge `-0.0006` maxDD `-0.1065`
- `market_context_high->metal_1h` score `-0.323` n `77` status `ready` deltaP `0.0466` edge `0.0078` maxDD `-0.4687`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
