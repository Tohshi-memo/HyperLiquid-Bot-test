# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T15:07:29.745079+00:00`
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

- `risk_on_high->crypto_major_24h` score `2.8867` n `32` status `ready` deltaP `19.6181` edge `0.3549` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.8867` n `32` status `ready` deltaP `19.6181` edge `0.3549` maxDD `-6.2481`
- `risk_on_high->commodity_4h` score `2.3163` n `32` status `ready` deltaP `15.625` edge `0.1071` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.3163` n `32` status `ready` deltaP `15.625` edge `0.1071` maxDD `-0.1258`
- `risk_on_high->equity_24h` score `1.9976` n `32` status `ready` deltaP `5.5556` edge `0.397` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `1.9976` n `32` status `ready` deltaP `5.5556` edge `0.397` maxDD `-11.2348`
- `risk_on_high->commodity_24h` score `1.97` n `32` status `ready` deltaP `18.0556` edge `0.0438` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `1.97` n `32` status `ready` deltaP `18.0556` edge `0.0438` maxDD `0.0`
- `risk_on_high->fx_24h` score `1.7888` n `32` status `ready` deltaP `19.9653` edge `0.0344` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.7888` n `32` status `ready` deltaP `19.9653` edge `0.0344` maxDD `-0.1418`
- `news_risk_high->equity_1h` score `1.4863` n `32` status `ready` deltaP `5.1647` edge `0.1213` maxDD `-0.5496`
- `risk_on_high->index_24h` score `1.3914` n `32` status `ready` deltaP `12.6736` edge `0.0619` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `1.3914` n `32` status `ready` deltaP `12.6736` edge `0.0619` maxDD `-0.4355`
- `risk_on_high->commodity_1h` score `1.1473` n `32` status `ready` deltaP `12.4626` edge `0.0358` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1473` n `32` status `ready` deltaP `12.4626` edge `0.0358` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9767` n `32` status `ready` deltaP `11.2043` edge `0.0208` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9767` n `32` status `ready` deltaP `11.2043` edge `0.0208` maxDD `-0.1285`
- `news_risk_high->index_1h` score `0.7881` n `32` status `ready` deltaP `9.9551` edge `0.0219` maxDD `-0.141`
- `market_context_high->commodity_1h` score `0.6977` n `177` status `ready` deltaP `9.8143` edge `0.0249` maxDD `-0.5752`
- `market_context_high->commodity_4h` score `0.5764` n `177` status `ready` deltaP `9.2514` edge `0.0502` maxDD `-2.1077`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
