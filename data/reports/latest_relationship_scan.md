# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T07:22:37.750319+00:00`
- Price records: `672`
- Market context records: `4070`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10216`

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

- `risk_on_high->unknown_4h` score `144.9797` n `40` status `ready` deltaP `-6.8293` edge `12.3088` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.9797` n `40` status `ready` deltaP `-6.8293` edge `12.3088` maxDD `-10.864`
- `market_context_high->unknown_1h` score `51.1316` n `172` status `ready` deltaP `2.1794` edge `4.4042` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.2813` n `144` status `ready` deltaP `-8.1997` edge `3.5643` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `17.014` n `172` status `ready` deltaP `-0.9572` edge `1.9665` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `3.7324` n `40` status `ready` deltaP `38.0488` edge `0.0621` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.7324` n `40` status `ready` deltaP `38.0488` edge `0.0621` maxDD `-0.0446`
- `risk_on_high->equity_24h` score `1.857` n `40` status `ready` deltaP `30.5026` edge `-0.0486` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.857` n `40` status `ready` deltaP `30.5026` edge `-0.0486` maxDD `0.0`
- `market_context_high->index_24h` score `1.6286` n `144` status `ready` deltaP `18.1976` edge `0.0144` maxDD `0.0`
- `market_context_high->equity_4h` score `1.3571` n `172` status `ready` deltaP `14.9674` edge `0.1664` maxDD `-6.9137`
- `risk_on_high->crypto_major_4h` score `1.1077` n `40` status `ready` deltaP `19.2988` edge `0.0302` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.1077` n `40` status `ready` deltaP `19.2988` edge `0.0302` maxDD `-2.6576`
- `market_context_high->equity_1h` score `0.7814` n `172` status `ready` deltaP `5.9219` edge `0.0816` maxDD `-2.144`
- `risk_on_high->equity_1h` score `0.4856` n `40` status `ready` deltaP `11.2126` edge `0.0048` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4856` n `40` status `ready` deltaP `11.2126` edge `0.0048` maxDD `-0.7937`
- `risk_on_high->metal_4h` score `0.2191` n `40` status `ready` deltaP `11.7073` edge `-0.0164` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.2191` n `40` status `ready` deltaP `11.7073` edge `-0.0164` maxDD `-1.3516`
- `risk_on_high->crypto_major_1h` score `0.1726` n `40` status `ready` deltaP `12.1557` edge `-0.0047` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.1726` n `40` status `ready` deltaP `12.1557` edge `-0.0047` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
