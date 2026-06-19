# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-19T23:37:25.115617+00:00`
- Price records: `672`
- Market context records: `4152`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10040`

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

- `risk_on_high->unknown_4h` score `144.71` n `40` status `ready` deltaP `-10.1829` edge `12.3089` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `144.71` n `40` status `ready` deltaP `-10.1829` edge `12.3089` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `36.2331` n `202` status `ready` deltaP `1.0909` edge `3.1701` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `10.8437` n `198` status `ready` deltaP `-13.169` edge `1.3948` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `9.7109` n `202` status `ready` deltaP `-4.8116` edge `1.3843` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.3818` n `40` status `ready` deltaP `34.6951` edge `-0.0281` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.3818` n `40` status `ready` deltaP `34.6951` edge `-0.0281` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `1.0656` n `40` status `ready` deltaP `16.4024` edge `0.046` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.0656` n `40` status `ready` deltaP `16.4024` edge `0.046` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.7532` n `40` status `ready` deltaP `0.0779` edge `0.2904` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.7532` n `40` status `ready` deltaP `0.0779` edge `0.2904` maxDD `-12.9187`
- `risk_on_high->equity_1h` score `0.2088` n `40` status `ready` deltaP `10.6138` edge `-0.0144` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.2088` n `40` status `ready` deltaP `10.6138` edge `-0.0144` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `0.1065` n `40` status `ready` deltaP `9.9102` edge `0.0018` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.1065` n `40` status `ready` deltaP `9.9102` edge `0.0018` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0913` n `40` status `ready` deltaP `10.0915` edge `0.0035` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0913` n `40` status `ready` deltaP `10.0915` edge `0.0035` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0326` n `40` status `ready` deltaP `3.9521` edge `0.0008` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0326` n `40` status `ready` deltaP `3.9521` edge `0.0008` maxDD `-0.1704`
- `risk_on_high->metal_4h` score `0.0258` n `40` status `ready` deltaP `8.2012` edge `-0.0178` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
