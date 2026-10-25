# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T01:52:31.409901+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7284`

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

- `market_context_high->unknown_4h` score `21.2289` n `95` status `ready` deltaP `0.8408` edge `1.797` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.5721` n `51` status `ready` deltaP `20.9865` edge `0.082` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.5832` n `95` status `ready` deltaP `8.389` edge `0.0489` maxDD `-1.165`
- `market_context_high->commodity_1h` score `-0.2278` n `107` status `ready` deltaP `3.1171` edge `0.0103` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.2898` n `107` status `ready` deltaP `-0.6128` edge `0.0024` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.671` n `95` status `ready` deltaP `-4.4977` edge `0.0042` maxDD `-0.4858`
- `market_context_high->metal_1h` score `-0.9884` n `107` status `ready` deltaP `0.3987` edge `-0.0056` maxDD `-1.6873`
- `market_context_high->index_1h` score `-1.0284` n `107` status `ready` deltaP `-1.9965` edge `-0.0072` maxDD `-1.2155`
- `market_context_high->fx_24h` score `-1.2468` n `51` status `ready` deltaP `-2.7573` edge `-0.0013` maxDD `-1.404`
- `market_context_high->crypto_major_1h` score `-1.4567` n `107` status `ready` deltaP `2.2595` edge `-0.0322` maxDD `-10.2363`
- `market_context_high->crypto_major_24h` score `-1.5752` n `51` status `ready` deltaP `3.5641` edge `-0.0046` maxDD `-13.0221`
- `market_context_high->equity_1h` score `-2.6045` n `107` status `ready` deltaP `-1.1347` edge `-0.0935` maxDD `-12.6279`
- `market_context_high->metal_4h` score `-3.0254` n `95` status `ready` deltaP `-6.5019` edge `-0.0311` maxDD `-5.8801`
- `market_context_high->metal_24h` score `-3.1069` n `51` status `ready` deltaP `-9.8345` edge `0.0016` maxDD `-6.9289`
- `market_context_high->crypto_alt_1h` score `-3.3168` n `107` status `ready` deltaP `-0.277` edge `-0.0612` maxDD `-14.0683`
- `market_context_high->index_4h` score `-4.5653` n `95` status `ready` deltaP `-19.8732` edge `-0.0511` maxDD `-5.0817`
- `market_context_high->crypto_alt_24h` score `-5.183` n `51` status `ready` deltaP `6.6381` edge `-0.1244` maxDD `-40.7472`
- `market_context_high->index_24h` score `-7.4626` n `51` status `ready` deltaP `-37.1426` edge `-0.1814` maxDD `-6.4296`
- `market_context_high->unknown_1h` score `-7.9509` n `107` status `ready` deltaP `0.5876` edge `-0.6176` maxDD `-1.5781`
- `market_context_high->crypto_major_4h` score `-12.2556` n `95` status `ready` deltaP `-20.0257` edge `-0.2966` maxDD `-40.6288`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
