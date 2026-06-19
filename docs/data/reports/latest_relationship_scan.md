# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-19T16:22:31.022660+00:00`
- Price records: `672`
- Market context records: `4118`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10016`

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

- `risk_on_high->unknown_4h` score `145.5307` n `40` status `ready` deltaP `-8.6699` edge `12.3672` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.5307` n `40` status `ready` deltaP `-8.6699` edge `12.3672` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `39.744` n `198` status `ready` deltaP `1.2833` edge `3.4614` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `14.7146` n `198` status `ready` deltaP `-9.5876` edge `1.6935` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `11.5211` n `198` status `ready` deltaP `-2.0285` edge `1.5166` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.8441` n `40` status `ready` deltaP `36.8443` edge `-0.0039` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.8441` n `40` status `ready` deltaP `36.8443` edge `-0.0039` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `1.7281` n `40` status `ready` deltaP `18.6997` edge `0.0859` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.7281` n `40` status `ready` deltaP `18.6997` edge `0.0859` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.5434` n `40` status `ready` deltaP `11.6133` edge `0.0258` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.5434` n `40` status `ready` deltaP `11.6133` edge `0.0258` maxDD `-1.3516`
- `risk_on_high->metal_24h` score `0.2894` n `40` status `ready` deltaP `-19.348` edge `0.2275` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `0.2894` n `40` status `ready` deltaP `-19.348` edge `0.2275` maxDD `-1.9133`
- `risk_on_high->equity_1h` score `0.2747` n `40` status `ready` deltaP `11.0171` edge `-0.0116` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.2747` n `40` status `ready` deltaP `11.0171` edge `-0.0116` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `0.208` n `40` status `ready` deltaP `10.7526` edge `0.0092` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.208` n `40` status `ready` deltaP `10.7526` edge `0.0092` maxDD `-2.3372`
- `risk_on_high->equity_24h` score `0.1647` n `40` status `ready` deltaP `29.3592` edge `-0.182` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.1647` n `40` status `ready` deltaP `29.3592` edge `-0.182` maxDD `0.0`
- `risk_on_high->fx_4h` score `0.0875` n `40` status `ready` deltaP `10.108` edge `0.0029` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
