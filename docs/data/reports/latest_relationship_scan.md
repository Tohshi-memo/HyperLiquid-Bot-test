# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T16:52:30.952008+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8651`

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

- `market_context_high->unknown_4h` score `81.0358` n `135` status `ready` deltaP `4.5472` edge `6.7379` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `9.85` n `139` status `ready` deltaP `0.9392` edge `0.8635` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.9927` n `135` status `ready` deltaP `27.1875` edge `0.0536` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4621` n `139` status `ready` deltaP `10.6686` edge `0.0032` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4103` n `135` status `ready` deltaP `12.5915` edge `0.0101` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0643` n `139` status `ready` deltaP `8.8388` edge `0.0075` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.2373` n `139` status `ready` deltaP `2.7592` edge `0.0119` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.4242` n `135` status `ready` deltaP `6.0795` edge `0.046` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.4614` n `139` status `ready` deltaP `6.352` edge `0.0268` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5607` n `139` status `ready` deltaP `-0.21` edge `-0.0022` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-0.5783` n `135` status `ready` deltaP `9.4792` edge `0.0199` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.8281` n `135` status `ready` deltaP `8.0137` edge `-0.0055` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-0.9501` n `135` status `ready` deltaP `16.0995` edge `0.0913` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.375` n `139` status `ready` deltaP `2.6343` edge `-0.0026` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.8246` n `135` status `ready` deltaP `8.0671` edge `0.0906` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.9359` n `139` status `ready` deltaP `-0.8465` edge `-0.0062` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.8723` n `135` status `ready` deltaP `-6.7751` edge `-0.032` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.7977` n `135` status `ready` deltaP `3.2024` edge `-0.0763` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-3.8976` n `135` status `ready` deltaP `0.544` edge `-0.0176` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.3673` n `135` status `ready` deltaP `0.4133` edge `-0.1675` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
