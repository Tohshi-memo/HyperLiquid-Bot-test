# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T18:47:00.875294+00:00`
- Price records: `672`
- Market context records: `8013`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11816`

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

- `market_context_high->equity_24h` score `15.977` n `88` status `ready` deltaP `25.26` edge `1.2972` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.8392` n `88` status `ready` deltaP `35.8752` edge `0.4141` maxDD `0.0`
- `market_context_high->equity_4h` score `6.2118` n `101` status `ready` deltaP `24.0351` edge `0.4467` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `2.784` n `88` status `ready` deltaP `23.0837` edge `0.2144` maxDD `-6.2367`
- `market_context_high->metal_4h` score `2.578` n `101` status `ready` deltaP `23.5001` edge `0.1204` maxDD `-0.979`
- `market_context_high->index_4h` score `2.402` n `101` status `ready` deltaP `25.0282` edge `0.0693` maxDD `-0.8791`
- `market_context_high->index_24h` score `1.9732` n `88` status `ready` deltaP `11.6039` edge `0.1541` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.6646` n `101` status `ready` deltaP `13.8258` edge `0.1283` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.4331` n `88` status `ready` deltaP `26.4298` edge `0.0381` maxDD `-2.5901`
- `market_context_high->index_1h` score `0.8358` n `101` status `ready` deltaP `13.7339` edge `0.0211` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6635` n `101` status `ready` deltaP `9.5897` edge `0.0292` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.6027` n `101` status `ready` deltaP `11.3283` edge `0.0428` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.5516` n `101` status `ready` deltaP `8.8762` edge `0.1586` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.486` n `101` status `ready` deltaP `5.2971` edge `0.1169` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `0.0401` n `101` status `ready` deltaP `1.9342` edge `0.0355` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.2798` n `101` status `ready` deltaP `-0.0222` edge `0.001` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.4142` n `101` status `ready` deltaP `5.5126` edge `0.0035` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.5607` n `101` status `ready` deltaP `-0.7604` edge `-0.0045` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.2012` n `101` status `ready` deltaP `0.1928` edge `-0.0051` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.9075` n `101` status `ready` deltaP `7.2419` edge `-0.1649` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
