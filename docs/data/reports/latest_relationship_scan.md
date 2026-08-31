# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T05:07:27.533233+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11652`

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

- `risk_on_high->crypto_alt_24h` score `21.4666` n `55` status `ready` deltaP `47.4053` edge `1.5209` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `21.4666` n `55` status `ready` deltaP `47.4053` edge `1.5209` maxDD `-3.1772`
- `risk_on_high->crypto_major_24h` score `9.382` n `55` status `ready` deltaP `28.5196` edge `0.7335` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `9.382` n `55` status `ready` deltaP `28.5196` edge `0.7335` maxDD `-9.0103`
- `risk_on_high->unknown_4h` score `9.1146` n `97` status `ready` deltaP `26.6093` edge `0.6349` maxDD `-1.886`
- `risk_on_and_context->unknown_4h` score `9.1146` n `97` status `ready` deltaP `26.6093` edge `0.6349` maxDD `-1.886`
- `market_context_high->unknown_4h` score `7.1886` n `149` status `ready` deltaP `22.6101` edge `0.5046` maxDD `-2.1694`
- `risk_on_high->fx_24h` score `6.2301` n `55` status `ready` deltaP `69.7917` edge `0.0539` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.2301` n `55` status `ready` deltaP `69.7917` edge `0.0539` maxDD `0.0`
- `market_context_high->metal_24h` score `5.2216` n `96` status `ready` deltaP `37.1527` edge `0.2483` maxDD `-1.8678`
- `risk_on_high->metal_24h` score `4.402` n `55` status `ready` deltaP `40.5808` edge `0.1435` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.402` n `55` status `ready` deltaP `40.5808` edge `0.1435` maxDD `-0.7767`
- `market_context_high->crypto_alt_24h` score `4.243` n `96` status `ready` deltaP `21.875` edge `0.8171` maxDD `-27.517`
- `market_context_high->crypto_major_24h` score `3.4427` n `96` status `ready` deltaP `19.6181` edge `0.4052` maxDD `-17.2607`
- `risk_on_high->unknown_1h` score `2.6996` n `107` status `ready` deltaP `8.0125` edge `0.2292` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.6996` n `107` status `ready` deltaP `8.0125` edge `0.2292` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.477` n `159` status `ready` deltaP `7.3542` edge `0.2204` maxDD `-2.041`
- `market_context_high->fx_24h` score `0.9921` n `96` status `ready` deltaP `36.4584` edge `0.03` maxDD `-1.6688`
- `risk_on_high->commodity_24h` score `0.8241` n `55` status `ready` deltaP `9.6528` edge `0.1401` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.8241` n `55` status `ready` deltaP `9.6528` edge `0.1401` maxDD `-0.5706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
