# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T11:22:29.991175+00:00`
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

- `market_context_high->commodity_24h` score `1.7465` n `76` status `ready` deltaP `16.6933` edge `0.1194` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.684` n `43` status `ready` deltaP `14.6729` edge `0.017` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.684` n `43` status `ready` deltaP `14.6729` edge `0.017` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.5022` n `43` status `ready` deltaP `10.769` edge `0.0004` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.5022` n `43` status `ready` deltaP `10.769` edge `0.0004` maxDD `-0.4273`
- `risk_on_high->equity_24h` score `0.4564` n `43` status `ready` deltaP `-20.5016` edge `0.6856` maxDD `-28.5375`
- `risk_on_and_context->equity_24h` score `0.4564` n `43` status `ready` deltaP `-20.5016` edge `0.6856` maxDD `-28.5375`
- `market_context_high->crypto_major_24h` score `0.4346` n `76` status `ready` deltaP `1.0508` edge `0.6584` maxDD `-35.1086`
- `market_context_high->crypto_major_1h` score `0.2422` n `77` status `ready` deltaP `3.5987` edge `0.0952` maxDD `-3.7178`
- `market_context_high->crypto_major_4h` score `0.2124` n `77` status `ready` deltaP `3.3873` edge `0.3451` maxDD `-15.2359`
- `risk_on_high->fx_4h` score `0.0811` n `43` status `ready` deltaP `3.8346` edge `0.0076` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0811` n `43` status `ready` deltaP `3.8346` edge `0.0076` maxDD `-0.1126`
- `risk_on_high->commodity_24h` score `-0.1043` n `43` status `ready` deltaP `12.0728` edge `-0.0094` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.1043` n `43` status `ready` deltaP `12.0728` edge `-0.0094` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `-0.2622` n `43` status `ready` deltaP `0.2619` edge `-0.0007` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2622` n `43` status `ready` deltaP `0.2619` edge `-0.0007` maxDD `-0.1065`
- `risk_on_high->equity_4h` score `-0.2624` n `43` status `ready` deltaP `4.9849` edge `0.0802` maxDD `-4.824`
- `risk_on_and_context->equity_4h` score `-0.2624` n `43` status `ready` deltaP `4.9849` edge `0.0802` maxDD `-4.824`
- `market_context_high->metal_1h` score `-0.3493` n `77` status `ready` deltaP `-0.2528` edge `0.0076` maxDD `-0.4687`
- `market_context_high->equity_24h` score `-0.3879` n `76` status `ready` deltaP `-1.1625` edge `0.8943` maxDD `-55.843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
