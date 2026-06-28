# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T21:07:27.009678+00:00`
- Price records: `672`
- Market context records: `5078`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10338`

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

- `market_context_high->unknown_24h` score `12.4211` n `77` status `ready` deltaP `27.4576` edge `0.8863` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `12.3843` n `103` status `ready` deltaP `3.8428` edge `1.0565` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.5316` n `91` status `ready` deltaP `20.8825` edge `0.7573` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `7.2916` n `91` status `ready` deltaP `21.7904` edge `0.5843` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `6.5514` n `91` status `ready` deltaP `20.2024` edge `0.5697` maxDD `-8.3416`
- `market_context_high->equity_4h` score `1.9713` n `91` status `ready` deltaP `9.004` edge `0.2174` maxDD `-6.3852`
- `market_context_high->crypto_alt_1h` score `1.095` n `103` status `ready` deltaP `7.4356` edge `0.1227` maxDD `-3.8153`
- `market_context_high->crypto_major_1h` score `1.0884` n `103` status `ready` deltaP `8.6376` edge `0.1356` maxDD `-5.1989`
- `market_context_high->metal_1h` score `0.8162` n `103` status `ready` deltaP `11.8452` edge `0.0387` maxDD `-1.3057`
- `market_context_high->metal_4h` score `0.767` n `91` status `ready` deltaP `9.1816` edge `0.1106` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.6143` n `103` status `ready` deltaP `9.0009` edge `0.0761` maxDD `-2.5875`
- `market_context_high->index_4h` score `0.2502` n `91` status `ready` deltaP `7.8096` edge `0.0449` maxDD `-1.0893`
- `market_context_high->index_1h` score `0.0906` n `103` status `ready` deltaP `4.6683` edge `0.0147` maxDD `-0.4031`
- `market_context_high->commodity_4h` score `-0.3771` n `91` status `ready` deltaP `10.0325` edge `0.0143` maxDD `-4.0087`
- `market_context_high->fx_24h` score `-0.5813` n `77` status `ready` deltaP `0.5659` edge `-0.0021` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.6218` n `103` status `ready` deltaP `0.9389` edge `0.0079` maxDD `-1.278`
- `market_context_high->fx_4h` score `-1.0349` n `91` status `ready` deltaP `-4.7608` edge `-0.002` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.0897` n `103` status `ready` deltaP `-10.8613` edge `-0.0046` maxDD `-0.6825`
- `market_context_high->commodity_24h` score `-2.1106` n `77` status `ready` deltaP `9.33` edge `0.0237` maxDD `-18.5187`
- `market_context_high->metal_24h` score `-4.1469` n `77` status `ready` deltaP `-2.0045` edge `0.0272` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
