# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T20:22:28.980767+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9004`

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

- `news_risk_high->unknown_4h` score `436.8526` n `75` status `ready` deltaP `-14.6626` edge `36.5791` maxDD `-4.1571`
- `risk_on_high->commodity_24h` score `9.2872` n `52` status `ready` deltaP `50.0` edge `0.4406` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.2872` n `52` status `ready` deltaP `50.0` edge `0.4406` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.3837` n `65` status `ready` deltaP `28.9583` edge `0.6435` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.9881` n `149` status `ready` deltaP `43.2886` edge `0.4296` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `6.9581` n `65` status `ready` deltaP `24.3376` edge `0.595` maxDD `-6.5262`
- `news_risk_high->index_24h` score `5.0763` n `65` status `ready` deltaP `34.6394` edge `0.2097` maxDD `-0.075`
- `news_risk_high->crypto_major_24h` score `4.6453` n `65` status `ready` deltaP `16.6266` edge `0.6842` maxDD `-13.2931`
- `news_risk_high->metal_24h` score `3.1923` n `65` status `ready` deltaP `23.4215` edge `0.1553` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `3.0401` n `52` status `ready` deltaP `33.3021` edge `0.0663` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0401` n `52` status `ready` deltaP `33.3021` edge `0.0663` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.9398` n `149` status `ready` deltaP `29.8044` edge `0.0881` maxDD `-0.345`
- `risk_on_high->fx_24h` score `1.8811` n `52` status `ready` deltaP `26.5491` edge `-0.016` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.8811` n `52` status `ready` deltaP `26.5491` edge `-0.016` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.7462` n `149` status `ready` deltaP `23.7742` edge `0.0086` maxDD `-0.0593`
- `news_risk_high->index_4h` score `1.5668` n `75` status `ready` deltaP `22.0732` edge `0.03` maxDD `-0.3938`
- `market_context_high->commodity_1h` score `1.2332` n `149` status `ready` deltaP `17.1091` edge `0.0264` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.6099` n `52` status `ready` deltaP `10.1912` edge `0.0181` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6099` n `52` status `ready` deltaP `10.1912` edge `0.0181` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2135` n `149` status `ready` deltaP `10.4957` edge `0.005` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
