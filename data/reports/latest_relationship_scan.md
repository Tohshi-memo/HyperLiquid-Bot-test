# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T03:22:25.400618+00:00`
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

- `news_risk_high->unknown_4h` score `380.1708` n `83` status `ready` deltaP `-20.9007` edge `31.9097` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `16.4401` n `83` status `ready` deltaP `38.1777` edge `1.2534` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `15.0459` n `83` status `ready` deltaP `30.2439` edge `1.2517` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `11.2592` n `83` status `ready` deltaP `39.4767` edge `0.8525` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `7.7478` n `52` status `ready` deltaP `43.4028` edge `0.3563` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.7478` n `52` status `ready` deltaP `43.4028` edge `0.3563` maxDD `0.0`
- `news_risk_high->index_24h` score `6.4725` n `83` status `ready` deltaP `44.9067` edge `0.2576` maxDD `-0.075`
- `market_context_high->commodity_24h` score `6.4487` n `149` status `ready` deltaP `36.6914` edge `0.3453` maxDD `-0.8682`
- `news_risk_high->metal_24h` score `4.6638` n `83` status `ready` deltaP `31.9905` edge `0.2208` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.5898` n `52` status `ready` deltaP `33.6672` edge `-0.0044` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.5898` n `52` status `ready` deltaP `33.6672` edge `-0.0044` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.4549` n `149` status `ready` deltaP `30.8923` edge `0.0202` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.2052` n `52` status `ready` deltaP `27.9667` edge `0.0323` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.2052` n `52` status `ready` deltaP `27.9667` edge `0.0323` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.105` n `149` status `ready` deltaP `24.469` edge `0.0541` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9048` n `149` status `ready` deltaP `14.2648` edge `0.018` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3659` n `83` status `ready` deltaP `11.736` edge `0.0315` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2815` n `52` status `ready` deltaP `7.3469` edge `0.0097` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2815` n `52` status `ready` deltaP `7.3469` edge `0.0097` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1552` n `52` status `ready` deltaP `6.4141` edge `0.0077` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
