# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T12:37:24.392058+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8494`

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

- `market_context_high->commodity_24h` score `1.8086` n `76` status `ready` deltaP `17.2151` edge `0.1211` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.6468` n `43` status `ready` deltaP `14.5227` edge `0.0149` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.6468` n `43` status `ready` deltaP `14.5227` edge `0.0149` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.5022` n `43` status `ready` deltaP `10.769` edge `0.0004` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.5022` n `43` status `ready` deltaP `10.769` edge `0.0004` maxDD `-0.4273`
- `market_context_high->crypto_major_24h` score `0.2054` n `76` status `ready` deltaP `0.1827` edge `0.6348` maxDD `-35.1086`
- `market_context_high->crypto_major_4h` score `0.1773` n `77` status `ready` deltaP `3.3873` edge `0.3406` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.1744` n `77` status `ready` deltaP `3.1496` edge `0.0895` maxDD `-3.7178`
- `risk_on_high->fx_4h` score `0.0152` n `43` status `ready` deltaP `3.0712` edge `0.0072` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0152` n `43` status `ready` deltaP `3.0712` edge `0.0072` maxDD `-0.1126`
- `risk_on_high->commodity_24h` score `-0.0421` n `43` status `ready` deltaP `12.5946` edge `-0.0077` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.0421` n `43` status `ready` deltaP `12.5946` edge `-0.0077` maxDD `-1.7154`
- `risk_on_high->equity_24h` score `-0.2215` n `43` status `ready` deltaP `-21.3711` edge `0.6349` maxDD `-28.5375`
- `risk_on_and_context->equity_24h` score `-0.2215` n `43` status `ready` deltaP `-21.3711` edge `0.6349` maxDD `-28.5375`
- `risk_on_high->fx_1h` score `-0.2466` n `43` status `ready` deltaP `0.5622` edge `-0.0007` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2466` n `43` status `ready` deltaP `0.5622` edge `-0.0007` maxDD `-0.1065`
- `market_context_high->metal_1h` score `-0.3745` n `77` status `ready` deltaP `-0.5522` edge `0.0075` maxDD `-0.4687`
- `market_context_high->fx_4h` score `-0.4608` n `77` status `ready` deltaP `-0.0397` edge `0.0049` maxDD `-0.7635`
- `risk_on_high->equity_4h` score `-0.4781` n `43` status `ready` deltaP `4.3742` edge `0.0663` maxDD `-4.824`
- `risk_on_and_context->equity_4h` score `-0.4781` n `43` status `ready` deltaP `4.3742` edge `0.0663` maxDD `-4.824`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
