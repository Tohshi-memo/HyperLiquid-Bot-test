# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T17:37:30.737734+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8306`

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

- `market_context_high->commodity_24h` score `2.2764` n `76` status `ready` deltaP `20.2576` edge `0.1398` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.5164` n `43` status `ready` deltaP `13.8978` edge `0.0082` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.5164` n `43` status `ready` deltaP `13.8978` edge `0.0082` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.4447` n `43` status `ready` deltaP `10.1553` edge `-0.0003` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.4447` n `43` status `ready` deltaP `10.1553` edge `-0.0003` maxDD `-0.4273`
- `risk_on_high->commodity_24h` score `0.4257` n `43` status `ready` deltaP `15.6371` edge `0.011` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.4257` n `43` status `ready` deltaP `15.6371` edge `0.011` maxDD `-1.7154`
- `risk_on_high->fx_4h` score `-0.1787` n `43` status `ready` deltaP `0.8579` edge `0.0058` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1787` n `43` status `ready` deltaP `0.8579` edge `0.0058` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.2559` n `43` status `ready` deltaP `0.4143` edge `-0.0009` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2559` n `43` status `ready` deltaP `0.4143` edge `-0.0009` maxDD `-0.1065`
- `market_context_high->crypto_major_1h` score `-0.3311` n `95` status `ready` deltaP `1.144` edge `0.0516` maxDD `-4.8007`
- `market_context_high->metal_1h` score `-0.4293` n `95` status `ready` deltaP `-2.7955` edge `0.0011` maxDD `-0.6669`
- `market_context_high->crypto_major_24h` score `-0.6093` n `76` status `ready` deltaP `-3.2895` edge `0.5535` maxDD `-35.1086`
- `risk_on_high->index_4h` score `-0.6912` n `43` status `ready` deltaP `4.0201` edge `0.0023` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.6912` n `43` status `ready` deltaP `4.0201` edge `0.0023` maxDD `-0.9359`
- `market_context_high->commodity_1h` score `-0.707` n `95` status `ready` deltaP `-1.7381` edge `-0.0056` maxDD `-1.5434`
- `market_context_high->fx_1h` score `-0.7136` n `95` status `ready` deltaP `-5.4853` edge `-0.002` maxDD `-0.5667`
- `market_context_high->fx_4h` score `-0.7147` n `83` status `ready` deltaP `-4.5218` edge `0.0026` maxDD `-0.7936`
- `market_context_high->index_1h` score `-0.8093` n `95` status `ready` deltaP `0.6571` edge `-0.0047` maxDD `-1.0365`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
