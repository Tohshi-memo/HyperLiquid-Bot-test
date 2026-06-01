# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T09:37:25.026598+00:00`
- Price records: `672`
- Market context records: `2549`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9252`

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

- `market_context_high->unknown_24h` score `5.6027` n `119` status `ready` deltaP `19.548` edge `0.3694` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.5571` n `150` status `ready` deltaP `24.1341` edge `0.5701` maxDD `-15.4319`
- `market_context_high->crypto_major_24h` score `4.7945` n `119` status `ready` deltaP `11.6363` edge `0.5873` maxDD `-15.2264`
- `market_context_high->crypto_major_4h` score `3.8879` n `150` status `ready` deltaP `17.2195` edge `0.3902` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.963` n `150` status `ready` deltaP `11.0488` edge `0.1949` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.1861` n `150` status `ready` deltaP `9.6866` edge `0.153` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.0592` n `119` status `ready` deltaP `18.2423` edge `0.025` maxDD `-2.0014`
- `market_context_high->index_24h` score `0.8238` n `119` status `ready` deltaP `7.5192` edge `0.1166` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.6813` n `150` status `ready` deltaP `8.0539` edge `0.1225` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.0527` n `119` status `ready` deltaP `-1.3509` edge `0.6652` maxDD `-39.9547`
- `market_context_high->index_4h` score `-0.1049` n `150` status `ready` deltaP `6.0162` edge `0.0353` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1881` n `150` status `ready` deltaP `3.02` edge `0.0332` maxDD `-2.8543`
- `market_context_high->index_1h` score `-0.2046` n `150` status `ready` deltaP `3.2775` edge `0.0105` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.4352` n `150` status `ready` deltaP `1.1976` edge `0.011` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.526` n `150` status `ready` deltaP `0.8164` edge `0.0042` maxDD `-0.278`
- `market_context_high->commodity_1h` score `-0.6222` n `150` status `ready` deltaP `3.3872` edge `0.0134` maxDD `-4.3601`
- `market_context_high->fx_24h` score `-0.7908` n `119` status `ready` deltaP `1.1978` edge `0.004` maxDD `-2.0693`
- `market_context_high->equity_1h` score `-0.825` n `150` status `ready` deltaP `-0.479` edge `0.0183` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-0.8285` n `150` status `ready` deltaP `3.7357` edge `0.0448` maxDD `-4.7664`
- `market_context_high->fx_4h` score `-0.8773` n `150` status `ready` deltaP `0.0387` edge `0.0126` maxDD `-0.8774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
