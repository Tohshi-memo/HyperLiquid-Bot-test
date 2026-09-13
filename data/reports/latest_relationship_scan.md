# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T15:37:29.533135+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13438`

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

- `market_context_high->unknown_24h` score `17868.3389` n `56` status `ready` deltaP `8.596` edge `1488.9911` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `9830.3147` n `34` status `ready` deltaP `13.4279` edge `819.1091` maxDD `-0.1252`
- `risk_on_and_context->unknown_24h` score `9830.3147` n `34` status `ready` deltaP `13.4279` edge `819.1091` maxDD `-0.1252`
- `news_risk_high->unknown_1h` score `421.3719` n `82` status `ready` deltaP `-4.8014` edge `35.1885` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.4183` n `82` status `ready` deltaP `35.1682` edge `1.3492` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3544` n `82` status `ready` deltaP `38.0236` edge `1.4231` maxDD `-9.098`
- `news_risk_high->equity_24h` score `8.6712` n `82` status `ready` deltaP `25.2019` edge `0.7326` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.8776` n `82` status `ready` deltaP `48.9739` edge `0.2643` maxDD `-0.0797`
- `risk_on_high->crypto_alt_24h` score `5.0717` n `34` status `ready` deltaP `19.8885` edge `0.5818` maxDD `-3.467`
- `risk_on_and_context->crypto_alt_24h` score `5.0717` n `34` status `ready` deltaP `19.8885` edge `0.5818` maxDD `-3.467`
- `news_risk_high->metal_24h` score `4.5588` n `82` status `ready` deltaP `24.2431` edge `0.2637` maxDD `-0.6334`
- `market_context_high->crypto_alt_24h` score `4.5262` n `56` status `ready` deltaP `14.7414` edge `0.5912` maxDD `-6.0692`
- `market_context_high->commodity_24h` score `4.1894` n `56` status `ready` deltaP `39.8276` edge `0.0836` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.181` n `34` status `ready` deltaP `39.8276` edge `0.0829` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.181` n `34` status `ready` deltaP `39.8276` edge `0.0829` maxDD `0.0`
- `market_context_high->metal_24h` score `2.1932` n `56` status `ready` deltaP `17.0567` edge `0.1309` maxDD `-0.9478`
- `risk_on_high->index_24h` score `1.4718` n `34` status `ready` deltaP `35.4158` edge `0.0279` maxDD `-2.6916`
- `risk_on_and_context->index_24h` score `1.4718` n `34` status `ready` deltaP `35.4158` edge `0.0279` maxDD `-2.6916`
- `market_context_high->index_24h` score `1.1116` n `56` status `ready` deltaP `34.4705` edge `0.0336` maxDD `-4.0048`
- `risk_on_high->metal_24h` score `0.7468` n `34` status `ready` deltaP `6.2373` edge `0.1057` maxDD `-0.7896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
