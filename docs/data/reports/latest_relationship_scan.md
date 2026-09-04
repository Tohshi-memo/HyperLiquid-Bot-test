# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T09:37:29.832412+00:00`
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

- `risk_on_high->unknown_4h` score `20.4213` n `133` status `ready` deltaP `8.2363` edge `1.7087` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.4213` n `133` status `ready` deltaP `8.2363` edge `1.7087` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `13.5845` n `183` status `ready` deltaP `11.667` edge `1.1238` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `12.1245` n `133` status `ready` deltaP `-1.353` edge `1.0771` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `12.1245` n `133` status `ready` deltaP `-1.353` edge `1.0771` maxDD `-1.95`
- `market_context_high->unknown_1h` score `9.942` n `195` status `ready` deltaP `0.413` edge `0.8888` maxDD `-2.0446`
- `market_context_high->equity_24h` score `1.8508` n `166` status `ready` deltaP `16.8152` edge `0.4767` maxDD `-20.7654`
- `news_risk_high->commodity_4h` score `1.3688` n `61` status `ready` deltaP `11.4979` edge `0.0575` maxDD `-0.2737`
- `news_risk_high->commodity_24h` score `0.5562` n `61` status `ready` deltaP `8.7802` edge `0.0051` maxDD `-0.0495`
- `risk_on_high->equity_24h` score `0.536` n `133` status `ready` deltaP `11.5928` edge `0.3819` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `0.536` n `133` status `ready` deltaP `11.5928` edge `0.3819` maxDD `-19.828`
- `risk_on_high->metal_1h` score `0.149` n `133` status `ready` deltaP `12.8619` edge `0.0046` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.149` n `133` status `ready` deltaP `12.8619` edge `0.0046` maxDD `-1.699`
- `news_risk_high->crypto_alt_24h` score `0.0137` n `61` status `ready` deltaP `14.8195` edge `0.0199` maxDD `-7.3552`
- `news_risk_high->index_1h` score `-0.0268` n `61` status `ready` deltaP `5.2812` edge `-0.0033` maxDD `-0.8275`
- `news_risk_high->commodity_1h` score `-0.0633` n `61` status `ready` deltaP `5.5586` edge `0.0023` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1785` n `133` status `ready` deltaP `3.5433` edge `-0.002` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1785` n `133` status `ready` deltaP `3.5433` edge `-0.002` maxDD `-0.5605`
- `news_risk_high->equity_24h` score `-0.3201` n `61` status `ready` deltaP `1.3006` edge `0.0863` maxDD `-6.8805`
- `market_context_high->metal_1h` score `-0.3235` n `195` status `ready` deltaP `6.388` edge `0.0016` maxDD `-2.1858`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
