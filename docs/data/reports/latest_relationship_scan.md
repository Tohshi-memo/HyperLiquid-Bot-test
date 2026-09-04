# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T06:52:30.419116+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11466`

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

- `risk_on_high->unknown_4h` score `21.0173` n `133` status `ready` deltaP `8.846` edge `1.7543` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `21.0173` n `133` status `ready` deltaP `8.846` edge `1.7543` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `14.627` n `174` status `ready` deltaP `11.2875` edge `1.2132` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `12.602` n `133` status `ready` deltaP `-0.7542` edge `1.1129` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `12.602` n `133` status `ready` deltaP `-0.7542` edge `1.1129` maxDD `-1.95`
- `market_context_high->unknown_1h` score `10.6665` n `184` status `ready` deltaP `0.6801` edge `0.9474` maxDD `-2.0446`
- `market_context_high->equity_24h` score `1.4609` n `155` status `ready` deltaP `16.801` edge `0.4443` maxDD `-20.7654`
- `risk_on_high->equity_24h` score `1.4388` n `133` status `ready` deltaP `13.5025` edge `0.4444` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `1.4388` n `133` status `ready` deltaP `13.5025` edge `0.4444` maxDD `-19.828`
- `news_risk_high->commodity_4h` score `0.2805` n `67` status `ready` deltaP `5.3376` edge `0.0363` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.1304` n `133` status `ready` deltaP `12.5625` edge `0.0042` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1304` n `133` status `ready` deltaP `12.5625` edge `0.0042` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.1154` n `67` status `ready` deltaP `3.5772` edge `-0.0033` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.1536` n `133` status `ready` deltaP `3.9924` edge `-0.0018` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1536` n `133` status `ready` deltaP `3.9924` edge `-0.0018` maxDD `-0.5605`
- `news_risk_high->commodity_1h` score `-0.1741` n `67` status `ready` deltaP `4.4575` edge `0.0004` maxDD `-0.9036`
- `news_risk_high->commodity_24h` score `-0.1985` n `67` status `ready` deltaP `4.2781` edge `-0.0258` maxDD `-0.2074`
- `risk_on_high->crypto_alt_1h` score `-0.2102` n `133` status `ready` deltaP `4.9007` edge `0.0515` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.2102` n `133` status `ready` deltaP `4.9007` edge `0.0515` maxDD `-5.4685`
- `news_risk_high->fx_4h` score `-0.3473` n `67` status `ready` deltaP `5.3832` edge `0.0008` maxDD `-1.2507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
