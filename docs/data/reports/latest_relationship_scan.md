# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T01:07:23.961213+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11824`

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

- `news_risk_high->equity_4h` score `7.2885` n `36` status `ready` deltaP `39.1768` edge `0.3462` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.2745` n `32` status `ready` deltaP `15.7774` edge `0.1026` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.2745` n `32` status `ready` deltaP `15.7774` edge `0.1026` maxDD `-0.1258`
- `news_risk_high->index_4h` score `2.1546` n `36` status `ready` deltaP `24.0345` edge `0.0325` maxDD `-0.0546`
- `risk_on_high->crypto_major_24h` score `2.109` n `32` status `ready` deltaP `15.9722` edge `0.2795` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.109` n `32` status `ready` deltaP `15.9722` edge `0.2795` maxDD `-6.2481`
- `risk_on_high->commodity_24h` score `2.1039` n `32` status `ready` deltaP `18.2292` edge `0.0538` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.1039` n `32` status `ready` deltaP `18.2292` edge `0.0538` maxDD `0.0`
- `news_risk_high->equity_1h` score `1.7238` n `36` status `ready` deltaP `8.7326` edge `0.1173` maxDD `-0.5496`
- `risk_on_high->fx_24h` score `1.7145` n `32` status `ready` deltaP `19.0972` edge `0.034` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.7145` n `32` status `ready` deltaP `19.0972` edge `0.034` maxDD `-0.1418`
- `risk_on_high->commodity_1h` score `1.1496` n `32` status `ready` deltaP `12.6123` edge `0.035` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1496` n `32` status `ready` deltaP `12.6123` edge `0.035` maxDD `-0.1957`
- `market_context_high->commodity_4h` score `1.0929` n `161` status `ready` deltaP `13.4288` edge `0.0654` maxDD `-2.1077`
- `risk_on_high->fx_4h` score `1.0023` n `32` status `ready` deltaP `11.5091` edge `0.0209` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0023` n `32` status `ready` deltaP `11.5091` edge `0.0209` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.8757` n `161` status `ready` deltaP `10.943` edge `0.0297` maxDD `-0.3742`
- `risk_on_high->index_1h` score `0.2781` n `32` status `ready` deltaP `9.6557` edge `0.0088` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2781` n `32` status `ready` deltaP `9.6557` edge `0.0088` maxDD `-0.3343`
- `risk_on_high->index_24h` score `0.2358` n `32` status `ready` deltaP `5.7292` edge `0.0119` maxDD `-0.4355`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
