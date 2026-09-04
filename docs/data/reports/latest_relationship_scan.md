# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T15:07:48.714187+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10928`

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

- `risk_on_high->unknown_4h` score `20.374` n `133` status `ready` deltaP `7.779` edge `1.7078` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.374` n `133` status `ready` deltaP `7.779` edge `1.7078` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.3877` n `133` status `ready` deltaP `-1.353` edge `1.0157` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.3877` n `133` status `ready` deltaP `-1.353` edge `1.0157` maxDD `-1.95`
- `market_context_high->unknown_4h` score `9.7117` n `205` status `ready` deltaP `8.872` edge `0.8197` maxDD `-2.563`
- `market_context_high->unknown_1h` score `9.2122` n `212` status `ready` deltaP `-0.7288` edge `0.8356` maxDD `-2.0446`
- `news_risk_high->commodity_4h` score `1.5116` n `57` status `ready` deltaP `12.2486` edge `0.0644` maxDD `-0.2737`
- `news_risk_high->crypto_alt_24h` score `1.2903` n `57` status `ready` deltaP `16.8129` edge `0.0355` maxDD `-1.8713`
- `news_risk_high->commodity_24h` score `1.1275` n `57` status `ready` deltaP `10.5811` edge `0.0407` maxDD `-0.0495`
- `news_risk_high->index_1h` score `0.2593` n `57` status `ready` deltaP `7.703` edge `0.0009` maxDD `-0.5204`
- `market_context_high->equity_24h` score `0.1458` n `167` status `ready` deltaP `13.1581` edge `0.359` maxDD `-20.7654`
- `risk_on_high->metal_1h` score `0.1413` n `133` status `ready` deltaP `12.7122` edge `0.0046` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1413` n `133` status `ready` deltaP `12.7122` edge `0.0046` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `-0.011` n `57` status `ready` deltaP `6.2717` edge `0.0019` maxDD `-0.9036`
- `news_risk_high->equity_1h` score `-0.0259` n `57` status `ready` deltaP `5.9723` edge `0.0175` maxDD `-2.5179`
- `risk_on_high->index_1h` score `-0.1723` n `133` status `ready` deltaP `3.693` edge `-0.0022` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1723` n `133` status `ready` deltaP `3.693` edge `-0.0022` maxDD `-0.5605`
- `risk_on_high->crypto_alt_1h` score `-0.276` n `133` status `ready` deltaP `3.7031` edge `0.054` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.276` n `133` status `ready` deltaP `3.7031` edge `0.054` maxDD `-5.4685`
- `news_risk_high->fx_4h` score `-0.3466` n `57` status `ready` deltaP `3.7681` edge `-0.0015` maxDD `-1.2001`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
