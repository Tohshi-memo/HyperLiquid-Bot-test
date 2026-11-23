# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T06:07:25.596039+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5234`

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

- `market_context_high->unknown_1h` score `16015.2185` n `84` status `ready` deltaP `1.5469` edge `1334.6074` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `10754.1505` n `82` status `ready` deltaP `3.5061` edge `896.1697` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1336.8491` n `31` status `ready` deltaP `3.4286` edge `111.3988` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1169.0953` n `31` status `ready` deltaP `3.9388` edge `97.404` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.2507` n `31` status `ready` deltaP `36.4625` edge `0.7427` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.6694` n `31` status `ready` deltaP `24.3214` edge `0.814` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.4227` n `31` status `ready` deltaP `12.9671` edge `0.8787` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.7675` n `31` status `ready` deltaP `18.7898` edge `0.2074` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4614` n `31` status `ready` deltaP `36.31` edge `0.0724` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6387` n `31` status `ready` deltaP `30.9446` edge `0.0221` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3722` n `31` status `ready` deltaP `9.1124` edge `0.2895` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.984` n `31` status `ready` deltaP `7.7651` edge `0.2383` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5026` n `31` status `ready` deltaP `28.6845` edge `0.0293` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4726` n `31` status `ready` deltaP `20.2842` edge `0.1093` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.8382` n `31` status `ready` deltaP `18.1255` edge `0.0264` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.0399` n `82` status `ready` deltaP `9.9085` edge `0.0123` maxDD `-0.5264`
- `news_risk_high->commodity_1h` score `-0.0873` n `31` status `ready` deltaP `1.0817` edge `0.0117` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.1484` n `84` status `ready` deltaP `3.3005` edge `0.0108` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.1874` n `84` status `ready` deltaP `2.6804` edge `0.0037` maxDD `-0.9806`
- `market_context_high->commodity_1h` score `-1.0904` n `84` status `ready` deltaP `-4.4483` edge `-0.0166` maxDD `-3.1494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
