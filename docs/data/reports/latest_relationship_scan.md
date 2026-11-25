# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T18:07:36.589251+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3744`

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

- `market_context_high->unknown_1h` score `32178.0781` n `45` status `ready` deltaP `2.1656` edge `2681.5015` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21854.897` n `45` status `ready` deltaP `2.2629` edge `1821.2402` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `943.1231` n `31` status `ready` deltaP `2.3807` edge `78.5953` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `601.9495` n `31` status `ready` deltaP `3.4815` edge `50.1449` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `323.8055` n `31` status `ready` deltaP `5.7292` edge `26.9456` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.4187` n `31` status `ready` deltaP `52.0833` edge `3.521` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.5329` n `31` status `ready` deltaP `54.1667` edge `3.1833` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.6738` n `31` status `ready` deltaP `55.3819` edge `2.8536` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.035` n `31` status `ready` deltaP `41.2355` edge `0.7555` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `11.8083` n `31` status `ready` deltaP `27.2177` edge `0.8896` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `11.5226` n `31` status `ready` deltaP `38.2917` edge `0.753` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.4564` n `31` status `ready` deltaP `53.125` edge `0.2672` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `7.3539` n `31` status `ready` deltaP `18.4549` edge `0.9615` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.4862` n `31` status `ready` deltaP `47.267` edge `0.1549` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.8646` n `31` status `ready` deltaP `20.4365` edge `0.2045` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.4692` n `31` status `ready` deltaP `36.7673` edge `0.07` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.683` n `31` status `ready` deltaP `31.6931` edge `0.0208` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5997` n `31` status `ready` deltaP `11.2082` edge `0.3047` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.425` n `45` status `ready` deltaP `29.7832` edge `0.032` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.3547` n `31` status `ready` deltaP `13.304` edge `0.2489` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
