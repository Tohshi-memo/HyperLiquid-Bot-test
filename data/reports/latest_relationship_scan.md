# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T06:52:32.969707+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11550`

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

- `news_risk_high->unknown_1h` score `443.5649` n `82` status `ready` deltaP `-5.999` edge `37.0459` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.9961` n `82` status `ready` deltaP `40.3406` edge `1.4462` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.8811` n `82` status `ready` deltaP `36.4719` edge `1.394` maxDD `-9.098`
- `news_risk_high->equity_24h` score `11.9462` n `82` status `ready` deltaP `35.7191` edge `0.9354` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.2265` n `82` status `ready` deltaP `59.4911` edge `0.3066` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.7838` n `78` status `ready` deltaP `39.8276` edge `0.2998` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.2198` n `41` status `ready` deltaP `39.8276` edge `0.2528` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2198` n `41` status `ready` deltaP `39.8276` edge `0.2528` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.6385` n `82` status `ready` deltaP `33.8983` edge `0.2893` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `5.3082` n `41` status `ready` deltaP `59.1127` edge `0.0525` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.3082` n `41` status `ready` deltaP `59.1127` edge `0.0525` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.7147` n `78` status `ready` deltaP `53.8594` edge `0.0554` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9781` n `52` status `ready` deltaP `26.7472` edge `0.0215` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9781` n `52` status `ready` deltaP `26.7472` edge `0.0215` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7784` n `137` status `ready` deltaP `22.1571` edge `0.0423` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7909` n `137` status `ready` deltaP `13.1114` edge `0.0162` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6386` n `82` status `ready` deltaP `16.0061` edge `0.038` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.327` n `137` status `ready` deltaP `11.9881` edge `0.0096` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.2755` n `52` status `ready` deltaP `7.4966` edge `0.0082` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2755` n `52` status `ready` deltaP `7.4966` edge `0.0082` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
