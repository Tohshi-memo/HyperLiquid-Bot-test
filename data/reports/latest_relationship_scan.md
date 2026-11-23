# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T08:07:29.229356+00:00`
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

- `market_context_high->unknown_1h` score `17983.6184` n `76` status `ready` deltaP `1.9855` edge `1498.6378` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `11851.1752` n `76` status `ready` deltaP `3.6746` edge `987.5873` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1317.0179` n `31` status `ready` deltaP `3.4286` edge `109.7462` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1170.6234` n `31` status `ready` deltaP `4.3962` edge `97.5283` maxDD `-0.119`
- `news_risk_high->equity_4h` score `10.9974` n `31` status `ready` deltaP `35.3954` edge `0.7287` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.397` n `31` status `ready` deltaP `23.4067` edge `0.7974` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.3123` n `31` status `ready` deltaP `12.5098` edge `0.8676` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.7735` n `31` status `ready` deltaP `18.9395` edge `0.2069` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.487` n `31` status `ready` deltaP `36.6149` edge `0.0725` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6771` n `31` status `ready` deltaP `31.3937` edge `0.0223` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3979` n `31` status `ready` deltaP `9.4118` edge `0.2908` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9622` n `31` status `ready` deltaP `7.6154` edge `0.2365` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5002` n `31` status `ready` deltaP `28.6845` edge `0.029` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4057` n `31` status `ready` deltaP `19.522` edge `0.1058` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.8367` n `31` status `ready` deltaP `18.1255` edge `0.0262` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.4988` n `76` status `ready` deltaP `15.958` edge `0.0163` maxDD `-0.3661`
- `news_risk_high->commodity_1h` score `-0.0309` n `31` status `ready` deltaP `1.5308` edge `0.0134` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.2299` n `76` status `ready` deltaP `3.1752` edge `0.0115` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.2972` n `76` status `ready` deltaP `0.7485` edge `0.0025` maxDD `-0.9806`
- `market_context_high->metal_4h` score `-1.0047` n `76` status `ready` deltaP `6.9159` edge `0.0106` maxDD `-6.9009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
