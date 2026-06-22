# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T05:22:31.593379+00:00`
- Price records: `672`
- Market context records: `4386`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11239`

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

- `risk_on_high->unknown_4h` score `132.7405` n `44` status `ready` deltaP `-0.8315` edge `11.2491` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `132.7405` n `44` status `ready` deltaP `-0.8315` edge `11.2491` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `34.8803` n `217` status `ready` deltaP `2.5519` edge `3.0393` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `11.3376` n `213` status `ready` deltaP `4.0021` edge `1.4611` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.309` n `44` status `ready` deltaP `35.3797` edge `0.0446` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.309` n `44` status `ready` deltaP `35.3797` edge `0.0446` maxDD `-0.044`
- `risk_on_high->metal_24h` score `3.0129` n `44` status `ready` deltaP `-15.183` edge `0.5489` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `3.0129` n `44` status `ready` deltaP `-15.183` edge `0.5489` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `1.8173` n `44` status `ready` deltaP `17.8493` edge `0.099` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.8173` n `44` status `ready` deltaP `17.8493` edge `0.099` maxDD `-2.6576`
- `risk_on_high->equity_24h` score `1.769` n `44` status `ready` deltaP `20.3125` edge `0.012` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.769` n `44` status `ready` deltaP `20.3125` edge `0.012` maxDD `0.0`
- `risk_on_high->index_24h` score `1.2044` n `44` status `ready` deltaP `22.5694` edge `-0.0501` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.2044` n `44` status `ready` deltaP `22.5694` edge `-0.0501` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.4493` n `45` status `ready` deltaP `9.9302` edge `0.0102` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.4493` n `45` status `ready` deltaP `9.9302` edge `0.0102` maxDD `-0.7834`
- `risk_on_high->metal_4h` score `0.418` n `44` status `ready` deltaP `6.638` edge `0.0429` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.418` n `44` status `ready` deltaP `6.638` edge `0.0429` maxDD `-1.3516`
- `risk_on_high->fx_1h` score `0.4078` n `45` status `ready` deltaP `8.0772` edge `0.0031` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.4078` n `45` status `ready` deltaP `8.0772` edge `0.0031` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
