# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T12:22:32.262307+00:00`
- Price records: `672`
- Market context records: `8091`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->equity_24h` score `20.3293` n `87` status `ready` deltaP `36.9051` edge `1.5391` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.3938` n `87` status `ready` deltaP `32.4205` edge `0.5313` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.294` n `87` status `ready` deltaP `35.8752` edge `0.452` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.8463` n `42` status `ready` deltaP `32.0921` edge `0.4504` maxDD `-0.1727`
- `news_risk_high->crypto_major_4h` score `3.6772` n `42` status `ready` deltaP `15.5415` edge `0.2579` maxDD `-2.0729`
- `news_risk_high->equity_1h` score `3.5649` n `43` status `ready` deltaP `28.9305` edge `0.1358` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.3049` n `87` status `ready` deltaP `31.5881` edge `0.0836` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.0829` n `87` status `ready` deltaP `19.7454` edge `0.1923` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7973` n `43` status `ready` deltaP `4.7556` edge `0.2291` maxDD `-0.8826`
- `news_risk_high->index_4h` score `2.5495` n `42` status `ready` deltaP `22.9674` edge `0.0784` maxDD `-0.191`
- `market_context_high->equity_1h` score `2.4797` n `87` status `ready` deltaP `15.3245` edge `0.1478` maxDD `-2.1322`
- `market_context_high->metal_4h` score `2.2719` n `87` status `ready` deltaP `20.8438` edge `0.1126` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.2058` n `87` status `ready` deltaP `29.8153` edge `0.0554` maxDD `-0.6283`
- `news_risk_high->metal_4h` score `1.3498` n `42` status `ready` deltaP `14.1115` edge `0.0652` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.2165` n `87` status `ready` deltaP `15.87` edge `0.0223` maxDD `-0.4716`
- `market_context_high->crypto_alt_4h` score `0.8737` n `87` status `ready` deltaP `6.3341` edge `0.1423` maxDD `-3.9374`
- `news_risk_high->crypto_major_1h` score `0.8199` n `43` status `ready` deltaP `3.7878` edge `0.0828` maxDD `-1.1783`
- `market_context_high->metal_1h` score `0.8003` n `87` status `ready` deltaP `11.2241` edge `0.0297` maxDD `-0.6936`
- `market_context_high->commodity_24h` score `0.7335` n `87` status `ready` deltaP `26.1857` edge `0.208` maxDD `-15.7497`
- `market_context_high->crypto_major_1h` score `0.667` n `87` status `ready` deltaP `10.0695` edge `0.0295` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
