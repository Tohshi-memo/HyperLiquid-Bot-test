# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T21:22:32.624734+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8884`

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

- `news_risk_high->unknown_4h` score `459.8457` n `72` status `ready` deltaP `-12.0088` edge `38.4775` maxDD `-4.1571`
- `risk_on_high->commodity_24h` score `9.2596` n `52` status `ready` deltaP `50.0` edge `0.4383` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.2596` n `52` status `ready` deltaP `50.0` edge `0.4383` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.154` n `61` status `ready` deltaP `27.6468` edge `0.6331` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.9605` n `149` status `ready` deltaP `43.2886` edge `0.4273` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `6.4833` n `61` status `ready` deltaP `22.0173` edge `0.5709` maxDD `-6.5262`
- `news_risk_high->index_24h` score `4.8855` n `61` status `ready` deltaP `33.5297` edge `0.2012` maxDD `-0.075`
- `news_risk_high->crypto_major_24h` score `4.1753` n `61` status `ready` deltaP `14.6089` edge `0.6374` maxDD `-13.2931`
- `risk_on_high->commodity_4h` score `3.0837` n `52` status `ready` deltaP `33.6069` edge `0.0679` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0837` n `52` status `ready` deltaP `33.6069` edge `0.0679` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.9834` n `149` status `ready` deltaP `30.1092` edge `0.0897` maxDD `-0.345`
- `news_risk_high->metal_24h` score `2.9004` n `61` status `ready` deltaP `21.303` edge `0.1451` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `1.8703` n `52` status `ready` deltaP `26.5491` edge `-0.0169` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.8703` n `52` status `ready` deltaP `26.5491` edge `-0.0169` maxDD `-0.0054`
- `news_risk_high->index_4h` score `1.8659` n `72` status `ready` deltaP `25.4065` edge `0.0327` maxDD `-0.3938`
- `market_context_high->fx_24h` score `1.7354` n `149` status `ready` deltaP `23.7742` edge `0.0077` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.2667` n `149` status `ready` deltaP `17.4085` edge `0.0272` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.6434` n `52` status `ready` deltaP `10.4906` edge `0.0189` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6434` n `52` status `ready` deltaP `10.4906` edge `0.0189` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.223` n `149` status `ready` deltaP `10.6482` edge `0.0052` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
