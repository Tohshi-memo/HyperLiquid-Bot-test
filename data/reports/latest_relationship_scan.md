# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T03:52:38.224780+00:00`
- Price records: `672`
- Market context records: `4055`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10432`

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

- `risk_on_high->unknown_4h` score `144.9861` n `40` status `ready` deltaP `-7.439` edge `12.3134` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.9861` n `40` status `ready` deltaP `-7.439` edge `12.3134` maxDD `-10.864`
- `market_context_high->unknown_24h` score `37.5833` n `144` status `ready` deltaP `-7.6798` edge `3.586` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `19.7535` n `163` status `ready` deltaP `0.0917` edge `2.1878` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `3.8582` n `40` status `ready` deltaP `38.811` edge `0.0675` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.8582` n `40` status `ready` deltaP `38.811` edge `0.0675` maxDD `-0.0446`
- `risk_on_high->equity_24h` score `3.4767` n `40` status `ready` deltaP `32.9289` edge `0.0702` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.4767` n `40` status `ready` deltaP `32.9289` edge `0.0702` maxDD `0.0`
- `market_context_high->index_24h` score `2.0011` n `144` status `ready` deltaP `19.9295` edge `0.0551` maxDD `-1.3629`
- `risk_on_high->crypto_major_4h` score `1.374` n `40` status `ready` deltaP `20.2134` edge `0.0463` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.374` n `40` status `ready` deltaP `20.2134` edge `0.0463` maxDD `-2.6576`
- `market_context_high->equity_4h` score `1.3339` n `163` status `ready` deltaP `14.3171` edge `0.1688` maxDD `-6.9137`
- `market_context_high->equity_1h` score `0.8312` n `173` status `ready` deltaP `6.4397` edge `0.0823` maxDD `-2.144`
- `risk_on_high->equity_1h` score `0.4987` n `40` status `ready` deltaP `11.512` edge `0.0039` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4987` n `40` status `ready` deltaP `11.512` edge `0.0039` maxDD `-0.7937`
- `risk_on_high->crypto_major_1h` score `0.2022` n `40` status `ready` deltaP `12.6048` edge `-0.0039` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2022` n `40` status `ready` deltaP `12.6048` edge `-0.0039` maxDD `-2.3372`
- `risk_on_high->metal_4h` score `0.1822` n `40` status `ready` deltaP `11.4024` edge `-0.0191` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1822` n `40` status `ready` deltaP `11.4024` edge `-0.0191` maxDD `-1.3516`
- `risk_on_high->fx_1h` score `-0.0055` n `40` status `ready` deltaP `3.3533` edge `-0.0001` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
