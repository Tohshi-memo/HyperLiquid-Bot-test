# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T00:22:29.758812+00:00`
- Price records: `672`
- Market context records: `5093`
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

- `market_context_high->unknown_24h` score `21.333` n `79` status `ready` deltaP `27.7206` edge `1.6272` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `9.0339` n `112` status `ready` deltaP `3.7158` edge `0.7922` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `8.5541` n `100` status `ready` deltaP `22.1037` edge `0.6677` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.0036` n `100` status `ready` deltaP `14.4878` edge `0.4644` maxDD `-8.1881`
- `market_context_high->crypto_major_4h` score `2.6969` n `100` status `ready` deltaP `13.9451` edge `0.4646` maxDD `-12.612`
- `market_context_high->equity_4h` score `2.4176` n `100` status `ready` deltaP `13.8476` edge `0.2223` maxDD `-6.3852`
- `market_context_high->equity_1h` score `1.113` n `112` status `ready` deltaP `10.7143` edge `0.0745` maxDD `-2.5875`
- `market_context_high->index_4h` score `0.4985` n `100` status `ready` deltaP `10.2683` edge `0.0492` maxDD `-1.0893`
- `market_context_high->crypto_alt_1h` score `0.4795` n `112` status `ready` deltaP `6.5601` edge `0.1139` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.3985` n `112` status `ready` deltaP `7.1749` edge `0.1278` maxDD `-6.9639`
- `market_context_high->metal_1h` score `0.3565` n `112` status `ready` deltaP `9.5487` edge `0.0317` maxDD `-1.3057`
- `market_context_high->index_1h` score `0.3024` n `112` status `ready` deltaP `6.1003` edge `0.0152` maxDD `-0.4536`
- `market_context_high->metal_4h` score `-0.0135` n `100` status `ready` deltaP `5.7073` edge `0.0793` maxDD `-2.8597`
- `market_context_high->commodity_1h` score `-1.0905` n `112` status `ready` deltaP `-1.9194` edge `-0.0023` maxDD `-2.062`
- `market_context_high->commodity_4h` score `-1.4976` n `100` status `ready` deltaP `5.3841` edge `-0.0182` maxDD `-6.3996`
- `market_context_high->fx_24h` score `-1.5944` n `79` status `ready` deltaP `-3.4898` edge `-0.0084` maxDD `-1.7626`
- `market_context_high->fx_1h` score `-1.6515` n `112` status `ready` deltaP `-10.3989` edge `-0.0042` maxDD `-0.7944`
- `market_context_high->commodity_24h` score `-1.6565` n `79` status `ready` deltaP `7.7004` edge `0.0325` maxDD `-15.0303`
- `market_context_high->fx_4h` score `-2.2894` n `100` status `ready` deltaP `-10.9329` edge `-0.0106` maxDD `-1.9169`
- `market_context_high->metal_24h` score `-4.5153` n `79` status `ready` deltaP `-6.5995` edge `0.0106` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
