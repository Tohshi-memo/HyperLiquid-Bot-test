# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-19T23:52:29.462768+00:00`
- Price records: `672`
- Market context records: `4153`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9992`

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

- `risk_on_high->unknown_4h` score `144.7016` n `40` status `ready` deltaP `-10.1829` edge `12.3082` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `144.7016` n `40` status `ready` deltaP `-10.1829` edge `12.3082` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `36.2283` n `202` status `ready` deltaP `1.0909` edge `3.1697` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `10.7109` n `198` status `ready` deltaP `-13.2983` edge `1.3846` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `9.7025` n `202` status `ready` deltaP `-4.8116` edge `1.3836` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.348` n `40` status `ready` deltaP `34.5427` edge `-0.0299` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.348` n `40` status `ready` deltaP `34.5427` edge `-0.0299` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `1.027` n `40` status `ready` deltaP `16.25` edge `0.0438` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.027` n `40` status `ready` deltaP `16.25` edge `0.0438` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.7974` n `40` status `ready` deltaP `0.195` edge `0.2933` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.7974` n `40` status `ready` deltaP `0.195` edge `0.2933` maxDD `-12.9187`
- `risk_on_high->equity_1h` score `0.1872` n `40` status `ready` deltaP `10.4641` edge `-0.0152` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.1872` n `40` status `ready` deltaP `10.4641` edge `-0.0152` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `0.0932` n `40` status `ready` deltaP `9.9102` edge `0.0001` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0932` n `40` status `ready` deltaP `9.9102` edge `0.0001` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0921` n `40` status `ready` deltaP `10.0915` edge `0.0036` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0921` n `40` status `ready` deltaP `10.0915` edge `0.0036` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0326` n `40` status `ready` deltaP `3.9521` edge `0.0008` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0326` n `40` status `ready` deltaP `3.9521` edge `0.0008` maxDD `-0.1704`
- `risk_on_high->metal_4h` score `0.014` n `40` status `ready` deltaP `8.0488` edge `-0.0183` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
