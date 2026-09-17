# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T05:52:31.896702+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10533`

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

- `news_risk_high->unknown_4h` score `384.803` n `83` status `ready` deltaP `-20.7483` edge `32.2947` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `15.4372` n `83` status `ready` deltaP `36.4416` edge `1.1814` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `14.1679` n `83` status `ready` deltaP `28.5078` edge `1.1901` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `10.4639` n `83` status `ready` deltaP `37.7406` edge `0.7978` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `8.2083` n `52` status `ready` deltaP `45.1389` edge `0.3831` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2083` n `52` status `ready` deltaP `45.1389` edge `0.3831` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.9092` n `149` status `ready` deltaP `38.4275` edge `0.3721` maxDD `-0.8682`
- `news_risk_high->index_24h` score `6.2448` n `83` status `ready` deltaP `43.1706` edge `0.2502` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.4358` n `83` status `ready` deltaP `31.9905` edge `0.2018` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.6157` n `52` status `ready` deltaP `33.8408` edge `-0.0034` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.6157` n `52` status `ready` deltaP `33.8408` edge `-0.0034` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.4808` n `149` status `ready` deltaP `31.0659` edge `0.0212` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.164` n `52` status `ready` deltaP `27.6618` edge `0.0309` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.164` n `52` status `ready` deltaP `27.6618` edge `0.0309` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.0638` n `149` status `ready` deltaP `24.1641` edge `0.0527` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9024` n `149` status `ready` deltaP `14.2648` edge `0.0178` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.411` n `83` status `ready` deltaP `12.4982` edge `0.0322` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2791` n `52` status `ready` deltaP `7.3469` edge `0.0095` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2791` n `52` status `ready` deltaP `7.3469` edge `0.0095` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1529` n `52` status `ready` deltaP `6.4141` edge `0.0074` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
