# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T14:52:26.507332+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13774`

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

- `market_context_high->fx_4h` score `0.1061` n `116` status `ready` deltaP `8.1686` edge `0.0094` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.0837` n `128` status `ready` deltaP `9.1083` edge `0.0031` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1099` n `128` status `ready` deltaP `2.6104` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2402` n `128` status `ready` deltaP `5.9974` edge `0.032` maxDD `-4.8885`
- `market_context_high->metal_1h` score `-0.326` n `128` status `ready` deltaP `0.5146` edge `-0.0056` maxDD `-0.503`
- `market_context_high->metal_4h` score `-0.4272` n `116` status `ready` deltaP `3.7374` edge `-0.0221` maxDD `-1.273`
- `market_context_high->index_4h` score `-0.5015` n `116` status `ready` deltaP `3.1907` edge `0.0113` maxDD `-2.0822`
- `market_context_high->commodity_24h` score `-0.5113` n `105` status `ready` deltaP `4.0675` edge `0.1136` maxDD `-4.666`
- `market_context_high->unknown_1h` score `-0.5986` n `128` status `ready` deltaP `8.7201` edge `-0.0853` maxDD `-0.4843`
- `market_context_high->commodity_1h` score `-0.6737` n `128` status `ready` deltaP `-4.5565` edge `0.0006` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.7036` n `116` status `ready` deltaP `-2.1552` edge `0.0092` maxDD `-2.4692`
- `market_context_high->equity_4h` score `-0.7336` n `116` status `ready` deltaP `1.3509` edge `0.0907` maxDD `-10.8339`
- `market_context_high->crypto_alt_1h` score `-0.7862` n `128` status `ready` deltaP `0.1263` edge `0.0138` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.2633` n `128` status `ready` deltaP `-1.7496` edge `-0.0478` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-2.0945` n `116` status `ready` deltaP `1.2826` edge `-0.0561` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.924` n `105` status `ready` deltaP `-11.6072` edge `-0.0053` maxDD `-2.2121`
- `market_context_high->unknown_4h` score `-3.8389` n `116` status `ready` deltaP `19.8013` edge `-0.408` maxDD `-0.5133`
- `market_context_high->index_24h` score `-4.2108` n `105` status `ready` deltaP `-5.9425` edge `-0.05` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-4.35` n `116` status `ready` deltaP `-1.2458` edge `-0.2521` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-4.5527` n `105` status `ready` deltaP `-17.0685` edge `-0.1391` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
