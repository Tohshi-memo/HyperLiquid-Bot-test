# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T01:22:27.851182+00:00`
- Price records: `672`
- Market context records: `5097`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10340`

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

- `market_context_high->unknown_24h` score `20.0255` n `79` status `ready` deltaP `27.547` edge `1.5194` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.2613` n `116` status `ready` deltaP `4.5736` edge `0.7221` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `8.2439` n `104` status `ready` deltaP `21.6463` edge `0.6449` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `2.9101` n `104` status `ready` deltaP `13.485` edge `0.4431` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.3284` n `104` status `ready` deltaP `12.5235` edge `0.4424` maxDD `-13.8566`
- `market_context_high->equity_4h` score `1.2708` n `104` status `ready` deltaP `11.9958` edge `0.1961` maxDD `-6.3852`
- `market_context_high->crypto_alt_1h` score `0.484` n `116` status `ready` deltaP `6.7055` edge `0.1135` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.4762` n `116` status `ready` deltaP `9.2195` edge `0.0589` maxDD `-2.745`
- `market_context_high->crypto_major_1h` score `0.3859` n `116` status `ready` deltaP `7.4127` edge `0.1246` maxDD `-6.9639`
- `market_context_high->metal_1h` score `0.336` n `116` status `ready` deltaP `9.364` edge `0.0303` maxDD `-1.3057`
- `market_context_high->index_4h` score `0.1599` n `104` status `ready` deltaP `8.2669` edge `0.0415` maxDD `-1.0893`
- `market_context_high->index_1h` score `-0.0303` n `116` status `ready` deltaP `5.3221` edge `0.011` maxDD `-1.0296`
- `market_context_high->metal_4h` score `-0.2775` n `104` status `ready` deltaP `3.9752` edge `0.0689` maxDD `-3.8114`
- `market_context_high->commodity_1h` score `-0.9713` n `116` status `ready` deltaP `-0.6401` edge `-0.0009` maxDD `-2.062`
- `market_context_high->fx_1h` score `-1.518` n `116` status `ready` deltaP `-8.9253` edge `-0.0029` maxDD `-0.7944`
- `market_context_high->fx_24h` score `-1.5455` n `79` status `ready` deltaP `-2.9689` edge `-0.0078` maxDD `-1.7626`
- `market_context_high->commodity_24h` score `-1.6745` n `79` status `ready` deltaP `7.7004` edge `0.0302` maxDD `-15.0303`
- `market_context_high->commodity_4h` score `-1.881` n `104` status `ready` deltaP `3.5764` edge `-0.0226` maxDD `-6.9729`
- `market_context_high->fx_4h` score `-2.0782` n `104` status `ready` deltaP `-8.5483` edge `-0.0089` maxDD `-1.9169`
- `market_context_high->metal_24h` score `-4.5207` n `79` status `ready` deltaP `-6.5995` edge `0.0099` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
