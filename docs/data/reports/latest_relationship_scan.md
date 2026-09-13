# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T23:37:30.561870+00:00`
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

- `market_context_high->unknown_24h` score `931.1448` n `56` status `ready` deltaP `10.2093` edge `77.5475` maxDD `-0.613`
- `news_risk_high->unknown_1h` score `435.5908` n `82` status `ready` deltaP `-5.5499` edge `36.3784` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.975` n `82` status `ready` deltaP `36.8923` edge `1.3841` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3376` n `82` status `ready` deltaP `38.0236` edge `1.4217` maxDD `-9.098`
- `news_risk_high->equity_24h` score `10.3162` n `82` status `ready` deltaP `30.7191` edge `0.8329` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.5433` n `82` status `ready` deltaP `54.4911` edge `0.283` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `5.3978` n `56` status `ready` deltaP `39.8276` edge `0.1843` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.0021` n `82` status `ready` deltaP `28.8983` edge `0.2696` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.9586` n `30` status `ready` deltaP `39.8276` edge `0.1477` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.9586` n `30` status `ready` deltaP `39.8276` edge `0.1477` maxDD `0.0`
- `risk_on_high->fx_24h` score `3.3963` n `30` status `ready` deltaP `59.885` edge `0.0467` maxDD `-0.1745`
- `risk_on_and_context->fx_24h` score `3.3963` n `30` status `ready` deltaP `59.885` edge `0.0467` maxDD `-0.1745`
- `risk_on_high->crypto_alt_24h` score `2.0117` n `30` status `ready` deltaP `0.6322` edge `0.3838` maxDD `-6.7415`
- `risk_on_and_context->crypto_alt_24h` score `2.0117` n `30` status `ready` deltaP `0.6322` edge `0.3838` maxDD `-6.7415`
- `market_context_high->fx_24h` score `1.9555` n `56` status `ready` deltaP `43.3374` edge `0.0303` maxDD `-1.4804`
- `risk_on_high->commodity_4h` score `1.7784` n `52` status `ready` deltaP `24.6716` edge `0.0187` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.7784` n `52` status `ready` deltaP `24.6716` edge `0.0187` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.5269` n `127` status `ready` deltaP `21.0678` edge `0.0286` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.4742` n `82` status `ready` deltaP `13.4146` edge `0.0342` maxDD `-0.6935`
- `market_context_high->commodity_1h` score `0.4147` n `137` status `ready` deltaP `9.1438` edge `0.0113` maxDD `-0.3491`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
