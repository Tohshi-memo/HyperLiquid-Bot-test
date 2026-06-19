# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-19T18:07:28.052103+00:00`
- Price records: `672`
- Market context records: `4126`
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

- `risk_on_high->unknown_4h` score `145.2157` n `40` status `ready` deltaP `-9.2169` edge `12.3446` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.2157` n `40` status `ready` deltaP `-9.2169` edge `12.3446` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `38.4708` n `201` status `ready` deltaP `1.6572` edge `3.3528` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `13.8353` n `198` status `ready` deltaP `-10.4235` edge `1.6258` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `11.2062` n `198` status `ready` deltaP `-2.5755` edge `1.494` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.7582` n `40` status `ready` deltaP `36.3554` edge `-0.0078` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.7582` n `40` status `ready` deltaP `36.3554` edge `-0.0078` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `1.6024` n `40` status `ready` deltaP `18.1325` edge `0.0792` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6024` n `40` status `ready` deltaP `18.1325` edge `0.0792` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.4729` n `40` status `ready` deltaP `11.0241` edge `0.0207` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.4729` n `40` status `ready` deltaP `11.0241` edge `0.0207` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.3167` n `40` status `ready` deltaP `11.2126` edge `-0.0094` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.3167` n `40` status `ready` deltaP `11.2126` edge `-0.0094` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `0.2468` n `40` status `ready` deltaP `11.2575` edge `0.0108` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2468` n `40` status `ready` deltaP `11.2575` edge `0.0108` maxDD `-2.3372`
- `risk_on_high->metal_24h` score `0.0729` n `40` status `ready` deltaP `-20.0` edge `0.2041` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `0.0729` n `40` status `ready` deltaP `-20.0` edge `0.2041` maxDD `-1.9133`
- `risk_on_high->fx_4h` score `0.0584` n `40` status `ready` deltaP `9.6084` edge `0.0025` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0584` n `40` status `ready` deltaP `9.6084` edge `0.0025` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0085` n `40` status `ready` deltaP `3.503` edge `0.0007` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
