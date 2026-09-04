# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T09:07:27.311179+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11484`

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

- `risk_on_high->unknown_4h` score `20.5669` n `133` status `ready` deltaP `8.5412` edge `1.7188` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.5669` n `133` status `ready` deltaP `8.5412` edge `1.7188` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `13.7973` n `182` status `ready` deltaP `11.8668` edge `1.1402` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `12.2324` n `133` status `ready` deltaP `-1.2033` edge `1.0851` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `12.2324` n `133` status `ready` deltaP `-1.2033` edge `1.0851` maxDD `-1.95`
- `market_context_high->unknown_1h` score `10.0059` n `193` status `ready` deltaP `0.2226` edge `0.8954` maxDD `-2.0446`
- `market_context_high->equity_24h` score `1.7669` n `164` status `ready` deltaP `16.8318` edge `0.4696` maxDD `-20.7654`
- `news_risk_high->commodity_4h` score `1.1046` n `63` status `ready` deltaP `9.2601` edge `0.0504` maxDD `-0.2737`
- `risk_on_high->equity_24h` score `0.7066` n `133` status `ready` deltaP `11.94` edge `0.3938` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `0.7066` n `133` status `ready` deltaP `11.94` edge `0.3938` maxDD `-19.828`
- `news_risk_high->commodity_24h` score `0.1948` n `63` status `ready` deltaP `6.126` edge `-0.0066` maxDD `-0.1071`
- `risk_on_high->metal_1h` score `0.128` n `133` status `ready` deltaP `12.5625` edge `0.0039` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.128` n `133` status `ready` deltaP `12.5625` edge `0.0039` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `0.0253` n `63` status `ready` deltaP `6.6059` edge `0.0027` maxDD `-0.9036`
- `news_risk_high->index_1h` score `-0.0468` n `63` status `ready` deltaP `4.8974` edge `-0.0033` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.1863` n `133` status `ready` deltaP `3.3936` edge `-0.002` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1863` n `133` status `ready` deltaP `3.3936` edge `-0.002` maxDD `-0.5605`
- `market_context_high->metal_1h` score `-0.3018` n `193` status `ready` deltaP `6.6838` edge `0.0024` maxDD `-2.1858`
- `risk_on_high->crypto_alt_1h` score `-0.3613` n `133` status `ready` deltaP `4.0025` edge `0.0449` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.3613` n `133` status `ready` deltaP `4.0025` edge `0.0449` maxDD `-5.4685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
