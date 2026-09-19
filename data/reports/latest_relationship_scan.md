# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T06:07:27.729779+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8442`

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

- `news_risk_high->crypto_major_24h` score `59.0115` n `61` status `ready` deltaP `35.2829` edge `4.7716` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `52.6852` n `61` status `ready` deltaP `38.3311` edge `4.2728` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `35.9645` n `149` status `ready` deltaP `-1.8354` edge `3.0326` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `13.6265` n `61` status `ready` deltaP `47.9167` edge `0.8161` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.8431` n `52` status `ready` deltaP `-9.076` edge `0.9033` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.8431` n `52` status `ready` deltaP `-9.076` edge `0.9033` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.2652` n `52` status `ready` deltaP `44.9653` edge `0.389` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2652` n `52` status `ready` deltaP `44.9653` edge `0.389` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.995` n `77` status `ready` deltaP `25.9582` edge `0.6058` maxDD `-7.675`
- `market_context_high->commodity_24h` score `6.9661` n `149` status `ready` deltaP `38.2539` edge `0.378` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `5.438` n `77` status `ready` deltaP `22.5927` edge `0.42` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.2951` n `61` status `ready` deltaP `35.7468` edge `0.1354` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.295` n `81` status `ready` deltaP `17.1509` edge `0.2068` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6077` n `81` status `ready` deltaP `19.9194` edge `0.1368` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.52` n `52` status `ready` deltaP `30.1008` edge `0.0443` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.52` n `52` status `ready` deltaP `30.1008` edge `0.0443` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.4197` n `149` status `ready` deltaP `26.6031` edge `0.0661` maxDD `-0.345`
- `news_risk_high->fx_4h` score `1.4076` n `77` status `ready` deltaP `15.6419` edge `0.0349` maxDD `-0.084`
- `news_risk_high->fx_24h` score `1.1835` n `61` status `ready` deltaP `6.694` edge `0.0582` maxDD `-0.0029`
- `market_context_high->commodity_1h` score `1.0271` n `149` status `ready` deltaP `15.3127` edge `0.0212` maxDD `-0.3491`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
