# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T12:09:08.090116+00:00`
- Price records: `672`
- Market context records: `7138`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11692`

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

- `market_context_high->fx_4h` score `0.7361` n `140` status `ready` deltaP `17.4216` edge `0.0152` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.162` n `152` status `ready` deltaP `4.3374` edge `0.0027` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.4706` n `152` status `ready` deltaP `-2.478` edge `0.0415` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.5931` n `152` status `ready` deltaP `0.1497` edge `0.026` maxDD `-5.91`
- `market_context_high->crypto_major_1h` score `-0.6475` n `152` status `ready` deltaP `3.4392` edge `0.0351` maxDD `-7.6171`
- `market_context_high->index_1h` score `-0.6957` n `152` status `ready` deltaP `2.0091` edge `-0.0049` maxDD `-2.3175`
- `market_context_high->commodity_1h` score `-0.7049` n `152` status `ready` deltaP `-1.7688` edge `-0.0165` maxDD `-1.9668`
- `market_context_high->metal_1h` score `-1.3581` n `152` status `ready` deltaP `-4.7786` edge `-0.0052` maxDD `-2.0897`
- `market_context_high->commodity_4h` score `-2.1648` n `140` status `ready` deltaP `-5.5749` edge `-0.0397` maxDD `-2.9494`
- `market_context_high->unknown_4h` score `-2.2205` n `140` status `ready` deltaP `-5.3006` edge `0.0196` maxDD `-5.2109`
- `market_context_high->metal_4h` score `-2.8091` n `140` status `ready` deltaP `-7.9181` edge `-0.0125` maxDD `-5.2551`
- `market_context_high->crypto_major_4h` score `-3.3898` n `140` status `ready` deltaP `0.392` edge `-0.0072` maxDD `-24.734`
- `market_context_high->equity_1h` score `-3.478` n `152` status `ready` deltaP `0.1576` edge `-0.0451` maxDD `-14.9961`
- `market_context_high->index_4h` score `-3.9966` n `140` status `ready` deltaP `-1.912` edge `-0.0504` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.4904` n `133` status `ready` deltaP `-13.4581` edge `-0.1536` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.9863` n `133` status `ready` deltaP `-16.0518` edge `-0.0258` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-5.4867` n `140` status `ready` deltaP `-3.5497` edge `-0.0436` maxDD `-23.1965`
- `market_context_high->unknown_24h` score `-10.1263` n `133` status `ready` deltaP `-32.8765` edge `-0.11` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.9434` n `140` status `ready` deltaP `-1.8728` edge `-0.2551` maxDD `-64.5491`
- `market_context_high->metal_24h` score `-14.4339` n `133` status `ready` deltaP `-29.5191` edge `-0.1879` maxDD `-40.7836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
