# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T19:37:30.370027+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8344`

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

- `market_context_high->commodity_24h` score `2.4936` n `76` status `ready` deltaP `21.4729` edge `0.1498` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `0.6429` n `43` status `ready` deltaP `16.8524` edge `0.021` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.6429` n `43` status `ready` deltaP `16.8524` edge `0.021` maxDD `-1.7154`
- `risk_on_high->equity_1h` score `0.532` n `43` status `ready` deltaP `13.8978` edge `0.0095` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.532` n `43` status `ready` deltaP `13.8978` edge `0.0095` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.4447` n `43` status `ready` deltaP `10.1553` edge `-0.0003` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.4447` n `43` status `ready` deltaP `10.1553` edge `-0.0003` maxDD `-0.4273`
- `risk_on_high->fx_4h` score `-0.2408` n `43` status `ready` deltaP `0.0957` edge `0.0057` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2408` n `43` status `ready` deltaP `0.0957` edge `0.0057` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.2722` n `43` status `ready` deltaP `0.1149` edge `-0.001` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2722` n `43` status `ready` deltaP `0.1149` edge `-0.001` maxDD `-0.1065`
- `market_context_high->crypto_major_1h` score `-0.2914` n `95` status `ready` deltaP `1.4434` edge `0.0547` maxDD `-4.8007`
- `market_context_high->metal_1h` score `-0.4394` n `95` status `ready` deltaP `-2.9452` edge `0.0008` maxDD `-0.6669`
- `risk_on_high->index_4h` score `-0.6462` n `43` status `ready` deltaP `4.4774` edge `0.003` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.6462` n `43` status `ready` deltaP `4.4774` edge `0.003` maxDD `-0.9359`
- `market_context_high->fx_4h` score `-0.6826` n `91` status `ready` deltaP `-3.8144` edge `0.002` maxDD `-0.7936`
- `risk_on_high->equity_4h` score `-0.6863` n `43` status `ready` deltaP `3.6762` edge `0.0536` maxDD `-4.824`
- `risk_on_and_context->equity_4h` score `-0.6863` n `43` status `ready` deltaP `3.6762` edge `0.0536` maxDD `-4.824`
- `market_context_high->commodity_1h` score `-0.7031` n `95` status `ready` deltaP `-1.7381` edge `-0.0051` maxDD `-1.5434`
- `market_context_high->metal_4h` score `-0.7055` n `91` status `ready` deltaP `-0.0352` edge `0.0409` maxDD `-1.4893`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
