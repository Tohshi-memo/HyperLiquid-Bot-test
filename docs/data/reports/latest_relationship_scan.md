# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T16:37:25.953995+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `risk_on_high->crypto_major_24h` score `2.7054` n `32` status `ready` deltaP `18.5764` edge `0.3386` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.7054` n `32` status `ready` deltaP `18.5764` edge `0.3386` maxDD `-6.2481`
- `risk_on_high->commodity_4h` score `2.2727` n `32` status `ready` deltaP `15.3201` edge `0.1055` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.2727` n `32` status `ready` deltaP `15.3201` edge `0.1055` maxDD `-0.1258`
- `risk_on_high->commodity_24h` score `1.8387` n `32` status `ready` deltaP `17.0139` edge `0.0398` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `1.8387` n `32` status `ready` deltaP `17.0139` edge `0.0398` maxDD `0.0`
- `news_risk_high->equity_1h` score `1.7717` n `36` status `ready` deltaP `8.8823` edge `0.1203` maxDD `-0.5496`
- `risk_on_high->fx_24h` score `1.7423` n `32` status `ready` deltaP `19.4444` edge `0.034` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.7423` n `32` status `ready` deltaP `19.4444` edge `0.034` maxDD `-0.1418`
- `risk_on_high->equity_24h` score `1.5495` n `32` status `ready` deltaP `4.5139` edge `0.3465` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `1.5495` n `32` status `ready` deltaP `4.5139` edge `0.3465` maxDD `-11.2348`
- `risk_on_high->index_24h` score `1.2276` n `32` status `ready` deltaP `11.6319` edge `0.0552` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `1.2276` n `32` status `ready` deltaP `11.6319` edge `0.0552` maxDD `-0.4355`
- `risk_on_high->commodity_1h` score `1.1604` n `32` status `ready` deltaP `12.6123` edge `0.0359` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1604` n `32` status `ready` deltaP `12.6123` edge `0.0359` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9633` n `32` status `ready` deltaP `11.0518` edge `0.0207` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9633` n `32` status `ready` deltaP `11.0518` edge `0.0207` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.8016` n `172` status `ready` deltaP `11.0323` edge `0.0571` maxDD `-2.1077`
- `market_context_high->commodity_1h` score `0.6797` n `172` status `ready` deltaP `9.56` edge `0.0251` maxDD `-0.5752`
- `risk_on_high->index_1h` score `0.3147` n `32` status `ready` deltaP `10.2545` edge `0.0095` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
