# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T15:22:30.349772+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10832`

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

- `risk_on_high->unknown_4h` score `20.3728` n `133` status `ready` deltaP `7.779` edge `1.7077` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.3728` n `133` status `ready` deltaP `7.779` edge `1.7077` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.4393` n `133` status `ready` deltaP `-1.353` edge `1.02` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.4393` n `133` status `ready` deltaP `-1.353` edge `1.02` maxDD `-1.95`
- `market_context_high->unknown_4h` score `9.5928` n `206` status `ready` deltaP `8.9762` edge `0.8091` maxDD `-2.563`
- `market_context_high->unknown_1h` score `9.2638` n `212` status `ready` deltaP `-0.7288` edge `0.8399` maxDD `-2.0446`
- `news_risk_high->crypto_alt_24h` score `2.0548` n `56` status `ready` deltaP `18.254` edge `0.0765` maxDD `-0.8236`
- `news_risk_high->commodity_4h` score `1.6189` n `56` status `ready` deltaP `13.3493` edge `0.066` maxDD `-0.2737`
- `news_risk_high->commodity_24h` score `1.1775` n `56` status `ready` deltaP `10.4415` edge `0.0458` maxDD `-0.0495`
- `news_risk_high->index_1h` score `0.3702` n `56` status `ready` deltaP `8.7682` edge `0.0049` maxDD `-0.2715`
- `news_risk_high->equity_1h` score `0.3188` n `56` status `ready` deltaP `6.9504` edge `0.039` maxDD `-1.2241`
- `risk_on_high->metal_1h` score `0.1257` n `133` status `ready` deltaP `12.5625` edge `0.0036` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1257` n `133` status `ready` deltaP `12.5625` edge `0.0036` maxDD `-1.699`
- `market_context_high->equity_24h` score `0.0767` n `167` status `ready` deltaP `12.9845` edge `0.3544` maxDD `-20.7654`
- `news_risk_high->commodity_1h` score `0.0744` n `56` status `ready` deltaP `7.2498` edge `0.0025` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1754` n `133` status `ready` deltaP `3.693` edge `-0.0026` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1754` n `133` status `ready` deltaP `3.693` edge `-0.0026` maxDD `-0.5605`
- `news_risk_high->equity_24h` score `-0.224` n `56` status `ready` deltaP `2.4306` edge `0.0684` maxDD `-5.0655`
- `news_risk_high->fx_4h` score `-0.2296` n `56` status `ready` deltaP `4.5514` edge `-0.0014` maxDD `-1.1796`
- `news_risk_high->metal_1h` score `-0.2595` n `56` status `ready` deltaP `2.2241` edge `-0.0058` maxDD `-1.3833`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
