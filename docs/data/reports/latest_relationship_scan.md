# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-19T18:52:28.821762+00:00`
- Price records: `672`
- Market context records: `4129`
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

- `risk_on_high->unknown_4h` score `145.0571` n `40` status `ready` deltaP `-9.5197` edge `12.3334` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.0571` n `40` status `ready` deltaP `-9.5197` edge `12.3334` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `38.0618` n `202` status `ready` deltaP `1.3903` edge `3.3205` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `13.4342` n `198` status `ready` deltaP `-10.7871` edge `1.5948` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `11.0476` n `198` status `ready` deltaP `-2.8783` edge `1.4828` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.7084` n `40` status `ready` deltaP `36.0779` edge `-0.0101` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.7084` n `40` status `ready` deltaP `36.0779` edge `-0.0101` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `1.5238` n `40` status `ready` deltaP `17.8858` edge `0.0743` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.5238` n `40` status `ready` deltaP `17.8858` edge `0.0743` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.43` n `40` status `ready` deltaP `10.7678` edge `0.0169` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.43` n `40` status `ready` deltaP `10.7678` edge `0.0169` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.2855` n `40` status `ready` deltaP `11.0629` edge `-0.011` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.2855` n `40` status `ready` deltaP `11.0629` edge `-0.011` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `0.2132` n `40` status `ready` deltaP `10.9581` edge `0.0085` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2132` n `40` status `ready` deltaP `10.9581` edge `0.0085` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0447` n `40` status `ready` deltaP `9.3911` edge `0.0022` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0447` n `40` status `ready` deltaP `9.3911` edge `0.0022` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `-0.0001` n `40` status `ready` deltaP `3.3533` edge `0.0006` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `-0.0001` n `40` status `ready` deltaP `3.3533` edge `0.0006` maxDD `-0.1704`
- `risk_on_high->metal_24h` score `-0.0385` n `40` status `ready` deltaP `-20.2837` edge `0.1917` maxDD `-1.9133`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
