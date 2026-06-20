# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T14:22:28.881229+00:00`
- Price records: `672`
- Market context records: `4216`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9808`

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

- `risk_on_high->unknown_4h` score `145.8535` n `40` status `ready` deltaP `-6.5244` edge `12.3798` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.8535` n `40` status `ready` deltaP `-6.5244` edge `12.3798` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `30.6956` n `215` status `ready` deltaP `1.3975` edge `2.7066` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `9.1739` n `209` status `ready` deltaP `-3.2588` edge `1.3292` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `7.3467` n `198` status `ready` deltaP `-12.1212` edge `1.0964` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.4539` n `40` status `ready` deltaP `4.4168` edge `0.4032` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.4539` n `40` status `ready` deltaP `4.4168` edge `0.4032` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `2.0285` n `40` status `ready` deltaP `32.4085` edge `-0.0423` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.0285` n `40` status `ready` deltaP `32.4085` edge `-0.0423` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.4272` n `40` status `ready` deltaP `13.6585` edge `0.0111` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.4272` n `40` status `ready` deltaP `13.6585` edge `0.0111` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.0547` n `41` status `ready` deltaP `4.3012` edge `0.0013` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0547` n `41` status `ready` deltaP `4.3012` edge `0.0013` maxDD `-0.1704`
- `risk_on_high->metal_4h` score `0.0128` n `40` status `ready` deltaP `8.5061` edge `-0.0215` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.0128` n `40` status `ready` deltaP `8.5061` edge `-0.0215` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `-0.044` n `41` status `ready` deltaP `8.0693` edge `-0.0185` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `-0.044` n `41` status `ready` deltaP `8.0693` edge `-0.0185` maxDD `-0.7834`
- `risk_on_high->fx_4h` score `-0.0465` n `40` status `ready` deltaP `7.6524` edge `0.0021` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `-0.0465` n `40` status `ready` deltaP `7.6524` edge `0.0021` maxDD `-0.3925`
- `risk_on_high->crypto_major_1h` score `-0.1537` n `41` status `ready` deltaP `7.5763` edge `-0.016` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
