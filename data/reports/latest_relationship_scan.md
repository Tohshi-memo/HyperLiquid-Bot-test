# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T16:52:45.598460+00:00`
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

- `risk_on_high->unknown_4h` score `19.5432` n `133` status `ready` deltaP `7.4741` edge `1.6406` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.5432` n `133` status `ready` deltaP `7.4741` edge `1.6406` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.4573` n `133` status `ready` deltaP `-1.6524` edge `1.0235` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.4573` n `133` status `ready` deltaP `-1.6524` edge `1.0235` maxDD `-1.95`
- `market_context_high->unknown_4h` score `10.2156` n `212` status `ready` deltaP `9.2758` edge `0.859` maxDD `-2.563`
- `market_context_high->unknown_1h` score `9.1698` n `213` status `ready` deltaP `-0.8687` edge `0.833` maxDD `-2.0446`
- `news_risk_high->crypto_alt_24h` score `2.7307` n `51` status `ready` deltaP `19.1585` edge `0.1268` maxDD `-0.8236`
- `news_risk_high->commodity_4h` score `1.5887` n `51` status `ready` deltaP `12.3565` edge `0.0701` maxDD `-0.2737`
- `news_risk_high->commodity_24h` score `1.4875` n `51` status `ready` deltaP `10.4779` edge `0.0713` maxDD `-0.042`
- `news_risk_high->equity_1h` score `1.1987` n `51` status `ready` deltaP `12.5044` edge `0.0556` maxDD `-0.7924`
- `news_risk_high->index_1h` score `0.5969` n `51` status `ready` deltaP `12.161` edge `0.0092` maxDD `-0.1`
- `news_risk_high->metal_4h` score `0.5065` n `51` status `ready` deltaP `9.523` edge `0.0319` maxDD `-0.7692`
- `news_risk_high->crypto_major_4h` score `0.3605` n `51` status `ready` deltaP `5.1441` edge `0.095` maxDD `-4.3129`
- `news_risk_high->fx_4h` score `0.159` n `51` status `ready` deltaP `8.7757` edge `0.0004` maxDD `-0.9855`
- `risk_on_high->metal_1h` score `0.1109` n `133` status `ready` deltaP `12.5625` edge `0.0017` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1109` n `133` status `ready` deltaP `12.5625` edge `0.0017` maxDD `-1.699`
- `news_risk_high->metal_1h` score `-0.0174` n `51` status `ready` deltaP `3.5547` edge `0.0041` maxDD `-0.7361`
- `news_risk_high->equity_24h` score `-0.0767` n `51` status `ready` deltaP `3.942` edge `0.0772` maxDD `-5.0655`
- `market_context_high->equity_24h` score `-0.1984` n `167` status `ready` deltaP `12.29` edge `0.3361` maxDD `-20.7654`
- `risk_on_high->index_1h` score `-0.2143` n `133` status `ready` deltaP `3.0942` edge `-0.0036` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
