# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T11:22:36.217335+00:00`
- Price records: `672`
- Market context records: `4087`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10240`

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

- `risk_on_high->unknown_4h` score `144.6509` n `40` status `ready` deltaP `-8.6585` edge `12.2936` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.6509` n `40` status `ready` deltaP `-8.6585` edge `12.2936` maxDD `-10.864`
- `market_context_high->unknown_1h` score `48.6611` n `177` status `ready` deltaP `2.3487` edge `4.1972` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.0848` n `144` status `ready` deltaP `-9.0663` edge `3.5537` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `16.6853` n `172` status `ready` deltaP `-2.7864` edge `1.9513` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `3.4178` n `40` status `ready` deltaP `36.9817` edge `0.043` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.4178` n `40` status `ready` deltaP `36.9817` edge `0.043` maxDD `-0.0446`
- `market_context_high->equity_4h` score `1.0426` n `172` status `ready` deltaP `13.9003` edge `0.1473` maxDD `-6.9137`
- `market_context_high->equity_1h` score `0.6352` n `177` status `ready` deltaP `4.9951` edge `0.0756` maxDD `-2.144`
- `market_context_high->index_24h` score `0.532` n `144` status `ready` deltaP `15.4246` edge `-0.0585` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.4364` n `40` status `ready` deltaP `10.9132` edge `0.0027` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4364` n `40` status `ready` deltaP `10.9132` edge `0.0027` maxDD `-0.7937`
- `risk_on_high->crypto_major_4h` score `0.3439` n `40` status `ready` deltaP `17.0122` edge `-0.0182` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.3439` n `40` status `ready` deltaP `17.0122` edge `-0.0182` maxDD `-2.6576`
- `risk_on_high->fx_4h` score `0.1903` n `40` status `ready` deltaP `11.9207` edge `0.004` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.1903` n `40` status `ready` deltaP `11.9207` edge `0.004` maxDD `-0.3925`
- `risk_on_high->metal_4h` score `0.0712` n `40` status `ready` deltaP `11.0976` edge `-0.0313` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.0712` n `40` status `ready` deltaP `11.0976` edge `-0.0313` maxDD `-1.3516`
- `risk_on_high->fx_1h` score `0.0575` n `40` status `ready` deltaP `4.4012` edge `0.001` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0575` n `40` status `ready` deltaP `4.4012` edge `0.001` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
