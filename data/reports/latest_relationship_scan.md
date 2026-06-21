# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T16:18:59.450013+00:00`
- Price records: `672`
- Market context records: `4329`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10794`

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

- `risk_on_high->unknown_4h` score `130.8335` n `44` status `ready` deltaP `-0.984` edge `11.0912` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.8335` n `44` status `ready` deltaP `-0.984` edge `11.0912` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `31.5795` n `224` status `ready` deltaP `3.657` edge `2.7652` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `10.927` n `224` status `ready` deltaP `1.0453` edge `1.4466` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.7651` n `44` status `ready` deltaP `32.331` edge `0.0196` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.7651` n `44` status `ready` deltaP `32.331` edge `0.0196` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.4164` n `44` status `ready` deltaP `-20.2178` edge `0.506` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.4164` n `44` status `ready` deltaP `-20.2178` edge `0.506` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `2.2773` n `44` status `ready` deltaP `22.9167` edge `0.037` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.2773` n `44` status `ready` deltaP `22.9167` edge `0.037` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.7705` n `44` status `ready` deltaP `17.8493` edge `0.0951` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.7705` n `44` status `ready` deltaP `17.8493` edge `0.0951` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.4027` n `44` status `ready` deltaP `8.043` edge `0.0029` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.4027` n `44` status `ready` deltaP `8.043` edge `0.0029` maxDD `-0.1704`
- `risk_on_high->metal_4h` score `0.3421` n `44` status `ready` deltaP `5.4185` edge `0.0413` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.3421` n `44` status `ready` deltaP `5.4185` edge `0.0413` maxDD `-1.3516`
- `risk_on_high->index_24h` score `0.2656` n `44` status `ready` deltaP `19.4444` edge `-0.1075` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.2656` n `44` status `ready` deltaP `19.4444` edge `-0.1075` maxDD `0.0`
- `risk_on_high->crypto_major_1h` score `0.2517` n `44` status `ready` deltaP `8.3969` edge `0.0305` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2517` n `44` status `ready` deltaP `8.3969` edge `0.0305` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
