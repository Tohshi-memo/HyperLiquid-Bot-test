# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T21:07:32.666609+00:00`
- Price records: `672`
- Market context records: `4972`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `17.7045` n `99` status `ready` deltaP `6.4901` edge `1.4822` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.9128` n `89` status `ready` deltaP `29.4876` edge `0.9309` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.4988` n `89` status `ready` deltaP `21.2267` edge `0.6058` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.1026` n `89` status `ready` deltaP `21.797` edge `0.5818` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.9083` n `86` status `ready` deltaP `27.6769` edge `0.3421` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.7199` n `89` status `ready` deltaP `13.2262` edge `0.1933` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.6482` n `89` status `ready` deltaP `12.8871` edge `0.126` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.8579` n `89` status `ready` deltaP `10.8095` edge `0.0456` maxDD `-0.6938`
- `market_context_high->equity_1h` score `0.5371` n `99` status `ready` deltaP `7.7255` edge `0.0747` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.4537` n `99` status `ready` deltaP `5.1458` edge `0.1277` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.3652` n `99` status `ready` deltaP `7.1645` edge `0.1013` maxDD `-5.5126`
- `market_context_high->metal_1h` score `-0.0138` n `99` status `ready` deltaP `3.2752` edge `0.035` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.4035` n `99` status `ready` deltaP `1.6271` edge `0.0129` maxDD `-0.7054`
- `market_context_high->commodity_1h` score `-0.4278` n `99` status `ready` deltaP `0.6184` edge `0.007` maxDD `-1.278`
- `market_context_high->fx_24h` score `-1.0838` n `86` status `ready` deltaP `-0.2099` edge `-0.0086` maxDD `-2.0918`
- `market_context_high->fx_4h` score `-1.1474` n `89` status `ready` deltaP `-6.9985` edge `-0.0034` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.2334` n `89` status `ready` deltaP `4.8523` edge `-0.0106` maxDD `-4.9624`
- `market_context_high->fx_1h` score `-1.5472` n `99` status `ready` deltaP `-9.7442` edge `-0.004` maxDD `-0.4646`
- `market_context_high->commodity_24h` score `-2.9552` n `86` status `ready` deltaP `16.7554` edge `0.0203` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-6.9914` n `86` status `ready` deltaP `-8.5392` edge `0.0198` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
