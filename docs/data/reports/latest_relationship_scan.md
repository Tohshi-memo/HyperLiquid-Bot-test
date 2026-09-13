# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T22:52:29.176597+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12657`

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

- `market_context_high->unknown_24h` score `5474.7096` n `56` status `ready` deltaP `10.2093` edge `456.1779` maxDD `-0.613`
- `news_risk_high->unknown_1h` score `435.8776` n `82` status `ready` deltaP `-5.5499` edge `36.4023` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.8539` n `82` status `ready` deltaP `36.5475` edge `1.3763` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3028` n `82` status `ready` deltaP `38.0236` edge `1.4188` maxDD `-9.098`
- `news_risk_high->equity_24h` score `10.1536` n `82` status `ready` deltaP `30.2019` edge `0.8228` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.4804` n `82` status `ready` deltaP `53.9739` edge `0.2812` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `5.1254` n `56` status `ready` deltaP `39.8276` edge `0.1616` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.9874` n `30` status `ready` deltaP `39.8276` edge `0.1501` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.9874` n `30` status `ready` deltaP `39.8276` edge `0.1501` maxDD `0.0`
- `news_risk_high->metal_24h` score `4.9487` n `82` status `ready` deltaP `28.381` edge `0.2686` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `3.4317` n `30` status `ready` deltaP `60.4023` edge `0.0478` maxDD `-0.1745`
- `risk_on_and_context->fx_24h` score `3.4317` n `30` status `ready` deltaP `60.4023` edge `0.0478` maxDD `-0.1745`
- `risk_on_high->crypto_alt_24h` score `1.9329` n `30` status `ready` deltaP `0.2874` edge `0.376` maxDD `-6.7415`
- `risk_on_and_context->crypto_alt_24h` score `1.9329` n `30` status `ready` deltaP `0.2874` edge `0.376` maxDD `-6.7415`
- `risk_on_high->commodity_4h` score `1.8342` n `52` status `ready` deltaP `25.129` edge `0.0203` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.8342` n `52` status `ready` deltaP `25.129` edge `0.0203` maxDD `-0.1313`
- `market_context_high->crypto_alt_24h` score `1.7516` n `56` status `ready` deltaP `1.835` edge `0.3375` maxDD `-12.6346`
- `market_context_high->fx_24h` score `1.4874` n `56` status `ready` deltaP `38.4976` edge `0.0208` maxDD `-1.9411`
- `market_context_high->commodity_4h` score `1.3781` n `129` status `ready` deltaP `19.5536` edge `0.0263` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.4481` n `82` status `ready` deltaP `12.9573` edge `0.0339` maxDD `-0.6935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
