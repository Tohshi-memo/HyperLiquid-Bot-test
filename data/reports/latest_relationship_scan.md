# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-19T23:07:28.114036+00:00`
- Price records: `672`
- Market context records: `4149`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10032`

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

- `risk_on_high->unknown_4h` score `144.7148` n `40` status `ready` deltaP `-10.1829` edge `12.3093` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `144.7148` n `40` status `ready` deltaP `-10.1829` edge `12.3093` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `36.2367` n `202` status `ready` deltaP `1.0909` edge `3.1704` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `11.1127` n `198` status `ready` deltaP `-12.9117` edge `1.4155` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `9.7157` n `202` status `ready` deltaP `-4.8116` edge `1.3847` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.459` n `40` status `ready` deltaP `35.0` edge `-0.0237` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.459` n `40` status `ready` deltaP `35.0` edge `-0.0237` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `1.133` n `40` status `ready` deltaP `16.5549` edge `0.0506` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.133` n `40` status `ready` deltaP `16.5549` edge `0.0506` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.659` n `40` status `ready` deltaP `-0.1553` edge `0.2841` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.659` n `40` status `ready` deltaP `-0.1553` edge `0.2841` maxDD `-12.9187`
- `risk_on_high->equity_1h` score `0.2591` n `40` status `ready` deltaP `10.9132` edge `-0.0122` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.2591` n `40` status `ready` deltaP `10.9132` edge `-0.0122` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `0.1299` n `40` status `ready` deltaP `10.0599` edge `0.0038` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.1299` n `40` status `ready` deltaP `10.0599` edge `0.0038` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.081` n `40` status `ready` deltaP `9.939` edge `0.0032` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.081` n `40` status `ready` deltaP `9.939` edge `0.0032` maxDD `-0.3925`
- `risk_on_high->metal_4h` score `0.0635` n `40` status `ready` deltaP `8.5061` edge `-0.015` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.0635` n `40` status `ready` deltaP `8.5061` edge `-0.015` maxDD `-1.3516`
- `risk_on_high->fx_1h` score `0.0233` n `40` status `ready` deltaP `3.8024` edge `0.0006` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
