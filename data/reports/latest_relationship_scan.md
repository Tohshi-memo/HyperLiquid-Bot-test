# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T19:52:33.881639+00:00`
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

- `market_context_high->commodity_24h` score `2.5279` n `76` status `ready` deltaP `21.6465` edge `0.1515` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `0.6772` n `43` status `ready` deltaP `17.026` edge `0.0227` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.6772` n `43` status `ready` deltaP `17.026` edge `0.0227` maxDD `-1.7154`
- `risk_on_high->equity_1h` score `0.5308` n `43` status `ready` deltaP `13.8978` edge `0.0094` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.5308` n `43` status `ready` deltaP `13.8978` edge `0.0094` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.4447` n `43` status `ready` deltaP `10.1553` edge `-0.0003` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.4447` n `43` status `ready` deltaP `10.1553` edge `-0.0003` maxDD `-0.4273`
- `risk_on_high->fx_4h` score `-0.2408` n `43` status `ready` deltaP `0.0957` edge `0.0057` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2408` n `43` status `ready` deltaP `0.0957` edge `0.0057` maxDD `-0.1126`
- `market_context_high->crypto_major_1h` score `-0.2789` n `95` status `ready` deltaP `1.5931` edge `0.0553` maxDD `-4.8007`
- `risk_on_high->fx_1h` score `-0.28` n `43` status `ready` deltaP `-0.0348` edge `-0.001` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.28` n `43` status `ready` deltaP `-0.0348` edge `-0.001` maxDD `-0.1065`
- `market_context_high->metal_1h` score `-0.4301` n `95` status `ready` deltaP `-2.7955` edge `0.001` maxDD `-0.6669`
- `risk_on_high->index_4h` score `-0.6438` n `43` status `ready` deltaP `4.4774` edge `0.0032` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.6438` n `43` status `ready` deltaP `4.4774` edge `0.0032` maxDD `-0.9359`
- `market_context_high->fx_4h` score `-0.6536` n `92` status `ready` deltaP `-3.241` edge `0.0019` maxDD `-0.7936`
- `risk_on_high->equity_4h` score `-0.6779` n `43` status `ready` deltaP `3.6762` edge `0.0543` maxDD `-4.824`
- `risk_on_and_context->equity_4h` score `-0.6779` n `43` status `ready` deltaP `3.6762` edge `0.0543` maxDD `-4.824`
- `market_context_high->commodity_1h` score `-0.7133` n `95` status `ready` deltaP `-1.8878` edge `-0.0054` maxDD `-1.5434`
- `market_context_high->metal_4h` score `-0.7276` n `92` status `ready` deltaP `-0.3844` edge `0.0404` maxDD `-1.4893`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
