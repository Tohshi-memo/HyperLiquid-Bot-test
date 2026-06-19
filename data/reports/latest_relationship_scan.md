# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-19T16:37:32.574765+00:00`
- Price records: `672`
- Market context records: `4119`
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

- `risk_on_high->unknown_4h` score `145.4975` n `40` status `ready` deltaP `-8.6194` edge `12.3641` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.4975` n `40` status `ready` deltaP `-8.6194` edge `12.3641` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `39.6946` n `198` status `ready` deltaP `1.3403` edge `3.4569` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `14.5911` n `198` status `ready` deltaP `-9.706` edge `1.684` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `11.488` n `198` status `ready` deltaP `-1.978` edge `1.5135` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.8297` n `40` status `ready` deltaP `36.7537` edge `-0.0045` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.8297` n `40` status `ready` deltaP `36.7537` edge `-0.0045` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `1.7133` n `40` status `ready` deltaP `18.6194` edge `0.0852` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.7133` n `40` status `ready` deltaP `18.6194` edge `0.0852` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.5351` n `40` status `ready` deltaP `11.5299` edge `0.0253` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.5351` n `40` status `ready` deltaP `11.5299` edge `0.0253` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.2655` n `40` status `ready` deltaP `10.9328` edge `-0.0118` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.2655` n `40` status `ready` deltaP `10.9328` edge `-0.0118` maxDD `-0.7834`
- `risk_on_high->metal_24h` score `0.2619` n `40` status `ready` deltaP `-19.4403` edge `0.2246` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `0.2619` n `40` status `ready` deltaP `-19.4403` edge `0.2246` maxDD `-1.9133`
- `risk_on_high->crypto_major_1h` score `0.2131` n `40` status `ready` deltaP `10.8209` edge `0.0094` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2131` n `40` status `ready` deltaP `10.8209` edge `0.0094` maxDD `-2.3372`
- `risk_on_high->equity_24h` score `0.1227` n `40` status `ready` deltaP `29.2537` edge `-0.1848` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.1227` n `40` status `ready` deltaP `29.2537` edge `-0.1848` maxDD `0.0`
- `risk_on_high->fx_4h` score `0.0838` n `40` status `ready` deltaP `10.0373` edge `0.0029` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
