# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T16:52:37.208424+00:00`
- Price records: `672`
- Market context records: `4110`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10552`

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

- `risk_on_high->unknown_4h` score `144.7223` n `40` status `ready` deltaP `-9.1159` edge `12.3026` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.7223` n `40` status `ready` deltaP `-9.1159` edge `12.3026` maxDD `-10.864`
- `market_context_high->unknown_1h` score `43.2257` n `189` status `ready` deltaP `1.6658` edge `3.7488` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `34.6067` n `147` status `ready` deltaP `-8.7372` edge `3.345` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `15.1529` n `180` status `ready` deltaP `-1.6159` edge `1.8158` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `2.7866` n `40` status `ready` deltaP `36.9817` edge `-0.0096` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `2.7866` n `40` status `ready` deltaP `36.9817` edge `-0.0096` maxDD `-0.0446`
- `risk_on_high->crypto_major_4h` score `0.2603` n `40` status `ready` deltaP `17.3171` edge `-0.0272` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.2603` n `40` status `ready` deltaP `17.3171` edge `-0.0272` maxDD `-2.6576`
- `risk_on_high->equity_1h` score `0.1748` n `40` status `ready` deltaP `10.7635` edge `-0.0181` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.1748` n `40` status `ready` deltaP `10.7635` edge `-0.0181` maxDD `-0.7937`
- `risk_on_high->fx_4h` score `0.0804` n `40` status `ready` deltaP `10.0915` edge `0.0021` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0804` n `40` status `ready` deltaP `10.0915` edge `0.0021` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0389` n `40` status `ready` deltaP `4.1018` edge `0.0006` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0389` n `40` status `ready` deltaP `4.1018` edge `0.0006` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `-0.0355` n `40` status `ready` deltaP `10.2096` edge `-0.0184` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `-0.0355` n `40` status `ready` deltaP `10.2096` edge `-0.0184` maxDD `-2.3372`
- `risk_on_high->commodity_24h` score `-0.1198` n `40` status `ready` deltaP `-1.9097` edge `0.2309` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `-0.1198` n `40` status `ready` deltaP `-1.9097` edge `0.2309` maxDD `-12.9187`
- `market_context_high->fx_1h` score `-0.2713` n `189` status `ready` deltaP `2.0119` edge `0.0003` maxDD `-0.546`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
