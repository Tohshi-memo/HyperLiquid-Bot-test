# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T16:22:48.786165+00:00`
- Price records: `672`
- Market context records: `4108`
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

- `risk_on_high->unknown_4h` score `144.7379` n `40` status `ready` deltaP `-9.1159` edge `12.3039` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.7379` n `40` status `ready` deltaP `-9.1159` edge `12.3039` maxDD `-10.864`
- `market_context_high->unknown_1h` score `44.1213` n `187` status `ready` deltaP `2.0454` edge `3.8209` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `34.6338` n `147` status `ready` deltaP `-8.5636` edge `3.3461` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `15.5006` n `178` status `ready` deltaP `-2.0092` edge `1.8474` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `2.6411` n `40` status `ready` deltaP `36.6768` edge `-0.0197` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `2.6411` n `40` status `ready` deltaP `36.6768` edge `-0.0197` maxDD `-0.0446`
- `risk_on_high->equity_1h` score `0.1364` n `40` status `ready` deltaP `10.6138` edge `-0.0203` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.1364` n `40` status `ready` deltaP `10.6138` edge `-0.0203` maxDD `-0.7937`
- `risk_on_high->crypto_major_4h` score `0.1231` n `40` status `ready` deltaP `17.0122` edge `-0.0366` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.1231` n `40` status `ready` deltaP `17.0122` edge `-0.0366` maxDD `-2.6576`
- `risk_on_high->fx_4h` score `0.1009` n `40` status `ready` deltaP `10.3963` edge `0.0027` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.1009` n `40` status `ready` deltaP `10.3963` edge `0.0027` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.056` n `40` status `ready` deltaP `4.4012` edge `0.0008` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.056` n `40` status `ready` deltaP `4.4012` edge `0.0008` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `-0.0776` n `40` status `ready` deltaP `9.9102` edge `-0.0218` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `-0.0776` n `40` status `ready` deltaP `9.9102` edge `-0.0218` maxDD `-2.3372`
- `market_context_high->equity_4h` score `-0.226` n `178` status `ready` deltaP `11.6487` edge `0.0566` maxDD `-6.9137`
- `risk_on_high->commodity_24h` score `-0.2772` n `40` status `ready` deltaP `-2.2569` edge `0.2201` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `-0.2772` n `40` status `ready` deltaP `-2.2569` edge `0.2201` maxDD `-12.9187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
