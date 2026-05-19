# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T01:37:13.972272+00:00`
- Price records: `672`
- Market context records: `1174`
- Flow alert records: `5283`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `20.6123` n `143` status `ready` deltaP `45.9875` edge `1.5243` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `10.145` n `143` status `ready` deltaP `22.2077` edge `0.899` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.2453` n `143` status `ready` deltaP `20.457` edge `0.5604` maxDD `-6.4404`
- `market_context_high->metal_24h` score `5.6847` n `143` status `ready` deltaP `-2.9332` edge `0.66` maxDD `-6.3373`
- `market_context_high->index_24h` score `5.5698` n `143` status `ready` deltaP `20.1195` edge `0.3858` maxDD `-3.4627`
- `market_context_high->equity_4h` score `2.5569` n `153` status `ready` deltaP `13.1705` edge `0.1916` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.234` n `153` status `ready` deltaP `9.8149` edge `0.1057` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5739` n `153` status `ready` deltaP `8.3274` edge `0.024` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3363` n `153` status `ready` deltaP `3.0586` edge `0.0454` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1486` n `153` status `ready` deltaP `8.6484` edge `0.0003` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `0.1019` n `153` status `ready` deltaP `8.3223` edge `0.1497` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `-0.0716` n `153` status `ready` deltaP `6.0741` edge `0.0269` maxDD `-4.1256`
- `market_context_high->unknown_4h` score `-0.0802` n `153` status `ready` deltaP `6.3406` edge `0.0727` maxDD `-6.7322`
- `market_context_high->metal_1h` score `-0.3866` n `153` status `ready` deltaP `6.0634` edge `-0.0116` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.5087` n `153` status `ready` deltaP `1.678` edge `0.0307` maxDD `-3.4088`
- `market_context_high->unknown_24h` score `-0.5861` n `143` status `ready` deltaP `4.0684` edge `0.197` maxDD `-10.1706`
- `market_context_high->commodity_1h` score `-0.842` n `153` status `ready` deltaP `-3.4451` edge `-0.0042` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-1.0189` n `153` status `ready` deltaP `-3.8976` edge `-0.005` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.3603` n `153` status `ready` deltaP `3.795` edge `0.0968` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-1.8878` n `153` status `ready` deltaP `5.0375` edge `-0.0802` maxDD `-9.2991`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
