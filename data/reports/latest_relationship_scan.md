# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T15:52:25.104895+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10784`

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

- `risk_on_high->unknown_4h` score `20.3486` n `133` status `ready` deltaP `7.6265` edge `1.7067` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.3486` n `133` status `ready` deltaP `7.6265` edge `1.7067` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.4561` n `133` status `ready` deltaP `-1.5027` edge `1.0224` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.4561` n `133` status `ready` deltaP `-1.5027` edge `1.0224` maxDD `-1.95`
- `market_context_high->unknown_4h` score `9.3115` n `208` status `ready` deltaP `9.0291` edge `0.7853` maxDD `-2.563`
- `market_context_high->unknown_1h` score `9.2806` n `212` status `ready` deltaP `-0.8785` edge `0.8423` maxDD `-2.0446`
- `news_risk_high->crypto_alt_24h` score `2.4395` n `55` status `ready` deltaP `19.7475` edge `0.0986` maxDD `-0.8236`
- `news_risk_high->commodity_4h` score `1.5821` n `55` status `ready` deltaP `12.8298` edge `0.0664` maxDD `-0.2737`
- `news_risk_high->commodity_24h` score `1.194` n `55` status `ready` deltaP `9.9432` edge `0.0505` maxDD `-0.0495`
- `news_risk_high->index_1h` score `0.4327` n `55` status `ready` deltaP `9.7224` edge `0.0058` maxDD `-0.2109`
- `news_risk_high->equity_1h` score `0.429` n `55` status `ready` deltaP `7.9695` edge `0.0428` maxDD `-0.9411`
- `risk_on_high->metal_1h` score `0.0961` n `133` status `ready` deltaP `12.2631` edge `0.0018` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0961` n `133` status `ready` deltaP `12.2631` edge `0.0018` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `0.0177` n `55` status `ready` deltaP `6.7502` edge `0.0011` maxDD `-0.9036`
- `market_context_high->equity_24h` score `-0.0338` n `167` status `ready` deltaP `12.6372` edge `0.3475` maxDD `-20.7654`
- `news_risk_high->metal_4h` score `-0.0681` n `55` status `ready` deltaP `5.122` edge `0.0145` maxDD `-1.5901`
- `news_risk_high->metal_1h` score `-0.1441` n `55` status `ready` deltaP `2.8988` edge `-0.0005` maxDD `-0.9839`
- `news_risk_high->fx_4h` score `-0.1547` n `55` status `ready` deltaP `5.363` edge `-0.001` maxDD `-1.1448`
- `news_risk_high->equity_24h` score `-0.1572` n `55` status `ready` deltaP `3.2197` edge `0.0717` maxDD `-5.0655`
- `risk_on_high->index_1h` score `-0.1863` n `133` status `ready` deltaP `3.5433` edge `-0.003` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
