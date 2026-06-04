# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T10:37:25.317721+00:00`
- Price records: `672`
- Market context records: `2858`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9187`

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

- `market_context_high->crypto_alt_24h` score `4.3289` n `142` status `ready` deltaP `3.9173` edge `0.7263` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `3.4316` n `142` status `ready` deltaP `5.9003` edge `0.2931` maxDD `-1.7175`
- `market_context_high->equity_24h` score `1.6621` n `142` status `ready` deltaP `5.2621` edge `0.3038` maxDD `-12.6963`
- `market_context_high->commodity_24h` score `1.3373` n `142` status `ready` deltaP `14.1627` edge `0.3264` maxDD `-12.4171`
- `market_context_high->index_24h` score `1.0159` n `142` status `ready` deltaP `7.4604` edge `0.133` maxDD `-2.5127`
- `market_context_high->unknown_4h` score `0.9154` n `142` status `ready` deltaP `6.0331` edge `0.1414` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.4015` n `142` status `ready` deltaP `13.7582` edge `0.0439` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.157` n `142` status `ready` deltaP `4.7799` edge `0.0543` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0836` n `142` status `ready` deltaP `4.0483` edge `0.0117` maxDD `-1.2855`
- `market_context_high->crypto_alt_1h` score `-0.6016` n `142` status `ready` deltaP `5.0962` edge `0.0649` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.6163` n `142` status `ready` deltaP `-0.5819` edge `0.0002` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.6952` n `142` status `ready` deltaP `-2.334` edge `0.002` maxDD `-0.2164`
- `market_context_high->equity_4h` score `-0.7434` n `142` status `ready` deltaP `3.1819` edge `0.0548` maxDD `-5.7037`
- `market_context_high->metal_1h` score `-0.7689` n `142` status `ready` deltaP `-0.6157` edge `-0.0099` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.8009` n `142` status `ready` deltaP `4.3751` edge `0.0551` maxDD `-9.622`
- `market_context_high->equity_1h` score `-0.8487` n `142` status `ready` deltaP `-2.3003` edge `0.0279` maxDD `-2.6634`
- `market_context_high->crypto_alt_4h` score `-0.9439` n `142` status `ready` deltaP `13.7281` edge `0.2639` maxDD `-28.7261`
- `market_context_high->fx_4h` score `-1.2381` n `142` status `ready` deltaP `-4.5152` edge `0.0048` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2698` n `142` status `ready` deltaP `2.4476` edge `0.0129` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.3975` n `142` status `ready` deltaP `-1.8852` edge `-0.0167` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
