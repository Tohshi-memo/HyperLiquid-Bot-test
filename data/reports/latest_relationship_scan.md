# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T18:22:26.008234+00:00`
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

- `market_context_high->commodity_24h` score `2.339` n `76` status `ready` deltaP `20.6049` edge `0.1427` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.5308` n `43` status `ready` deltaP `13.8978` edge `0.0094` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.5308` n `43` status `ready` deltaP `13.8978` edge `0.0094` maxDD `-1.9591`
- `risk_on_high->commodity_24h` score `0.4882` n `43` status `ready` deltaP `15.9844` edge `0.0139` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.4882` n `43` status `ready` deltaP `15.9844` edge `0.0139` maxDD `-1.7154`
- `risk_on_high->index_1h` score `0.4447` n `43` status `ready` deltaP `10.1553` edge `-0.0003` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.4447` n `43` status `ready` deltaP `10.1553` edge `-0.0003` maxDD `-0.4273`
- `risk_on_high->fx_4h` score `-0.2043` n `43` status `ready` deltaP `0.553` edge `0.0057` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2043` n `43` status `ready` deltaP `0.553` edge `0.0057` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.2644` n `43` status `ready` deltaP `0.2646` edge `-0.001` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2644` n `43` status `ready` deltaP `0.2646` edge `-0.001` maxDD `-0.1065`
- `market_context_high->crypto_major_1h` score `-0.3272` n `95` status `ready` deltaP `1.144` edge `0.0521` maxDD `-4.8007`
- `market_context_high->metal_1h` score `-0.4558` n `95` status `ready` deltaP `-3.2446` edge `0.0007` maxDD `-0.6669`
- `risk_on_high->index_4h` score `-0.69` n `43` status `ready` deltaP `4.0201` edge `0.0024` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.69` n `43` status `ready` deltaP `4.0201` edge `0.0024` maxDD `-0.9359`
- `market_context_high->fx_4h` score `-0.6935` n `86` status `ready` deltaP `-4.0982` edge `0.0025` maxDD `-0.7936`
- `market_context_high->commodity_1h` score `-0.7078` n `95` status `ready` deltaP `-1.7381` edge `-0.0057` maxDD `-1.5434`
- `market_context_high->crypto_major_24h` score `-0.709` n `76` status `ready` deltaP `-3.8103` edge `0.5442` maxDD `-35.1086`
- `market_context_high->fx_1h` score `-0.7222` n `95` status `ready` deltaP `-5.635` edge `-0.0021` maxDD `-0.5667`
- `risk_on_high->equity_4h` score `-0.7781` n `43` status `ready` deltaP `3.2189` edge `0.049` maxDD `-4.824`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
