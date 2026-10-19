# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T22:22:27.128575+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8186`

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

- `market_context_high->commodity_24h` score `2.9008` n `76` status `ready` deltaP `23.3826` edge `0.171` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `1.0501` n `43` status `ready` deltaP `18.7621` edge `0.0422` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.0501` n `43` status `ready` deltaP `18.7621` edge `0.0422` maxDD `-1.7154`
- `risk_on_high->equity_1h` score `0.4589` n `43` status `ready` deltaP `13.1493` edge `0.0084` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.4589` n `43` status `ready` deltaP `13.1493` edge `0.0084` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.4316` n `43` status `ready` deltaP `10.0056` edge `-0.0004` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.4316` n `43` status `ready` deltaP `10.0056` edge `-0.0004` maxDD `-0.4273`
- `risk_on_high->fx_4h` score `-0.2238` n `43` status `ready` deltaP `0.2482` edge `0.0061` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2238` n `43` status `ready` deltaP `0.2482` edge `0.0061` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.2956` n `43` status `ready` deltaP `-0.3342` edge `-0.001` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2956` n `43` status `ready` deltaP `-0.3342` edge `-0.001` maxDD `-0.1065`
- `market_context_high->metal_1h` score `-0.388` n `95` status `ready` deltaP `-2.047` edge `0.0014` maxDD `-0.6669`
- `market_context_high->crypto_major_1h` score `-0.4308` n `95` status `ready` deltaP `0.2458` edge `0.0448` maxDD `-4.8007`
- `market_context_high->fx_4h` score `-0.5569` n `95` status `ready` deltaP `-1.4409` edge `0.0023` maxDD `-0.7936`
- `market_context_high->commodity_1h` score `-0.6603` n `95` status `ready` deltaP `-0.9896` edge `-0.0046` maxDD `-1.5434`
- `risk_on_high->index_4h` score `-0.7262` n `43` status `ready` deltaP `3.8677` edge `0.0004` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.7262` n `43` status `ready` deltaP `3.8677` edge `0.0004` maxDD `-0.9359`
- `market_context_high->fx_1h` score `-0.7533` n `95` status `ready` deltaP `-6.2338` edge `-0.0021` maxDD `-0.5667`
- `market_context_high->metal_4h` score `-0.7673` n `95` status `ready` deltaP `-0.7734` edge `0.0379` maxDD `-1.4893`
- `market_context_high->index_1h` score `-0.8225` n `95` status `ready` deltaP `0.5074` edge `-0.0048` maxDD `-1.0365`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
