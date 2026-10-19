# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T21:22:31.551051+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8212`

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

- `market_context_high->commodity_24h` score `2.7613` n `76` status `ready` deltaP `22.6882` edge `0.164` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `0.9105` n `43` status `ready` deltaP `18.0677` edge `0.0352` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.9105` n `43` status `ready` deltaP `18.0677` edge `0.0352` maxDD `-1.7154`
- `risk_on_high->equity_1h` score `0.5212` n `43` status `ready` deltaP `13.7481` edge `0.0096` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.5212` n `43` status `ready` deltaP `13.7481` edge `0.0096` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.4459` n `43` status `ready` deltaP `10.1553` edge `-0.0002` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.4459` n `43` status `ready` deltaP `10.1553` edge `-0.0002` maxDD `-0.4273`
- `risk_on_high->fx_4h` score `-0.2652` n `43` status `ready` deltaP `-0.2092` edge `0.0057` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2652` n `43` status `ready` deltaP `-0.2092` edge `0.0057` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.2963` n `43` status `ready` deltaP `-0.3342` edge `-0.0011` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2963` n `43` status `ready` deltaP `-0.3342` edge `-0.0011` maxDD `-0.1065`
- `market_context_high->crypto_major_1h` score `-0.3537` n `95` status `ready` deltaP `0.8446` edge `0.0507` maxDD `-4.8007`
- `market_context_high->metal_1h` score `-0.3873` n `95` status `ready` deltaP `-2.047` edge `0.0015` maxDD `-0.6669`
- `market_context_high->fx_4h` score `-0.5838` n `95` status `ready` deltaP `-1.8983` edge `0.0019` maxDD `-0.7936`
- `risk_on_high->index_4h` score `-0.6546` n `43` status `ready` deltaP `4.4774` edge `0.0023` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.6546` n `43` status `ready` deltaP `4.4774` edge `0.0023` maxDD `-0.9359`
- `market_context_high->commodity_1h` score `-0.6961` n `95` status `ready` deltaP `-1.5884` edge `-0.0052` maxDD `-1.5434`
- `risk_on_high->equity_4h` score `-0.7511` n `43` status `ready` deltaP `3.6762` edge `0.0482` maxDD `-4.824`
- `risk_on_and_context->equity_4h` score `-0.7511` n `43` status `ready` deltaP `3.6762` edge `0.0482` maxDD `-4.824`
- `market_context_high->fx_1h` score `-0.7541` n `95` status `ready` deltaP `-6.2338` edge `-0.0022` maxDD `-0.5667`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
