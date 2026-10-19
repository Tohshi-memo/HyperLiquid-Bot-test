# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T11:37:34.538258+00:00`
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

- `market_context_high->commodity_24h` score `1.7489` n `76` status `ready` deltaP `16.6933` edge `0.1196` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.696` n `43` status `ready` deltaP `14.823` edge `0.017` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.696` n `43` status `ready` deltaP `14.823` edge `0.017` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.5142` n `43` status `ready` deltaP `10.9191` edge `0.0004` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.5142` n `43` status `ready` deltaP `10.9191` edge `0.0004` maxDD `-0.4273`
- `market_context_high->crypto_major_24h` score `0.3959` n `76` status `ready` deltaP `0.8772` edge `0.6546` maxDD `-35.1086`
- `risk_on_high->equity_24h` score `0.3297` n `43` status `ready` deltaP `-20.6755` edge `0.6762` maxDD `-28.5375`
- `risk_on_and_context->equity_24h` score `0.3297` n `43` status `ready` deltaP `-20.6755` edge `0.6762` maxDD `-28.5375`
- `market_context_high->crypto_major_1h` score `0.2399` n `77` status `ready` deltaP `3.5987` edge `0.0949` maxDD `-3.7178`
- `market_context_high->crypto_major_4h` score `0.2101` n `77` status `ready` deltaP `3.3873` edge `0.3448` maxDD `-15.2359`
- `risk_on_high->fx_4h` score `0.0689` n `43` status `ready` deltaP `3.6819` edge `0.0076` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0689` n `43` status `ready` deltaP `3.6819` edge `0.0076` maxDD `-0.1126`
- `risk_on_high->commodity_24h` score `-0.1019` n `43` status `ready` deltaP `12.0728` edge `-0.0092` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.1019` n `43` status `ready` deltaP `12.0728` edge `-0.0092` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `-0.2544` n `43` status `ready` deltaP `0.412` edge `-0.0007` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2544` n `43` status `ready` deltaP `0.412` edge `-0.0007` maxDD `-0.1065`
- `risk_on_high->equity_4h` score `-0.2888` n `43` status `ready` deltaP `4.9849` edge `0.078` maxDD `-4.824`
- `risk_on_and_context->equity_4h` score `-0.2888` n `43` status `ready` deltaP `4.9849` edge `0.078` maxDD `-4.824`
- `market_context_high->metal_1h` score `-0.3625` n `77` status `ready` deltaP `-0.4025` edge `0.0075` maxDD `-0.4687`
- `market_context_high->fx_4h` score `-0.4259` n `77` status `ready` deltaP `0.571` edge `0.0053` maxDD `-0.7635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
