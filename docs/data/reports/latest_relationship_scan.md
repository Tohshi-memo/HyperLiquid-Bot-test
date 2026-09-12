# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T17:37:27.224181+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12899`

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

- `market_context_high->unknown_24h` score `7885.9204` n `85` status `ready` deltaP `13.0985` edge `657.0779` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `5354.4445` n `43` status `ready` deltaP `15.4514` edge `446.1007` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5354.4445` n `43` status `ready` deltaP `15.4514` edge `446.1007` maxDD `0.0`
- `news_risk_high->unknown_1h` score `382.9191` n `82` status `ready` deltaP `-5.2505` edge `31.9871` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `21.5225` n `66` status `ready` deltaP `47.5694` edge `1.5865` maxDD `-6.4735`
- `news_risk_high->crypto_alt_24h` score `16.9918` n `66` status `ready` deltaP `28.9615` edge `1.2717` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `16.5947` n `43` status `ready` deltaP `38.5457` edge `1.1489` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `16.5947` n `43` status `ready` deltaP `38.5457` edge `1.1489` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `14.6396` n `85` status `ready` deltaP `31.3501` edge `1.0937` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `10.1341` n `66` status `ready` deltaP `27.1622` edge `0.7207` maxDD `-2.2486`
- `risk_on_high->equity_24h` score `9.6599` n `43` status `ready` deltaP `40.7986` edge `0.533` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.6599` n `43` status `ready` deltaP `40.7986` edge `0.533` maxDD `0.0`
- `market_context_high->equity_24h` score `9.3143` n `85` status `ready` deltaP `40.7986` edge `0.5042` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.4713` n `45` status `ready` deltaP `41.6565` edge `0.4654` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.4713` n `45` status `ready` deltaP `41.6565` edge `0.4654` maxDD `-1.9733`
- `news_risk_high->index_24h` score `7.0537` n `66` status `ready` deltaP `45.9911` edge `0.2947` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `6.8856` n `66` status `ready` deltaP `43.9078` edge `0.3158` maxDD `-0.4441`
- `risk_on_high->index_24h` score `4.9113` n `43` status `ready` deltaP `49.6205` edge `0.0827` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.9113` n `43` status `ready` deltaP `49.6205` edge `0.0827` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.1104` n `45` status `ready` deltaP `36.2331` edge `0.1103` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
