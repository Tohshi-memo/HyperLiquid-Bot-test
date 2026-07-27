# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T12:07:31.017806+00:00`
- Price records: `672`
- Market context records: `8090`
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

- `market_context_high->equity_24h` score `20.3209` n `87` status `ready` deltaP `36.9051` edge `1.5384` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.3938` n `87` status `ready` deltaP `32.4205` edge `0.5313` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.288` n `87` status `ready` deltaP `35.8752` edge `0.4515` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.8463` n `42` status `ready` deltaP `32.0921` edge `0.4504` maxDD `-0.1727`
- `news_risk_high->crypto_major_4h` score `3.6458` n `42` status `ready` deltaP `15.3891` edge `0.2563` maxDD `-2.0729`
- `news_risk_high->equity_1h` score `3.5589` n `43` status `ready` deltaP `28.9305` edge `0.1353` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.3049` n `87` status `ready` deltaP `31.5881` edge `0.0836` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.0805` n `87` status `ready` deltaP `19.7454` edge `0.1921` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7829` n `43` status `ready` deltaP `4.6059` edge `0.2289` maxDD `-0.8826`
- `news_risk_high->index_4h` score `2.5495` n `42` status `ready` deltaP `22.9674` edge `0.0784` maxDD `-0.191`
- `market_context_high->equity_1h` score `2.4737` n `87` status `ready` deltaP `15.3245` edge `0.1473` maxDD `-2.1322`
- `market_context_high->metal_4h` score `2.2707` n `87` status `ready` deltaP `20.8438` edge `0.1125` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.2232` n `87` status `ready` deltaP `29.9886` edge `0.0557` maxDD `-0.6283`
- `news_risk_high->metal_4h` score `1.3486` n `42` status `ready` deltaP `14.1115` edge `0.0651` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.2153` n `87` status `ready` deltaP `15.87` edge `0.0222` maxDD `-0.4716`
- `market_context_high->crypto_alt_4h` score `0.8459` n `87` status `ready` deltaP `6.1817` edge `0.141` maxDD `-3.9374`
- `market_context_high->metal_1h` score `0.8003` n `87` status `ready` deltaP `11.2241` edge `0.0297` maxDD `-0.6936`
- `news_risk_high->crypto_major_1h` score `0.7935` n `43` status `ready` deltaP `3.6381` edge `0.0816` maxDD `-1.1783`
- `market_context_high->commodity_24h` score `0.712` n `87` status `ready` deltaP `26.0124` edge `0.2064` maxDD `-15.7497`
- `market_context_high->crypto_major_1h` score `0.6406` n `87` status `ready` deltaP `9.9198` edge `0.0283` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
