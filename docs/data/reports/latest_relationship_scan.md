# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T11:07:37.587202+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9120`

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

- `market_context_high->unknown_4h` score `82.4505` n `135` status `ready` deltaP `5.4619` edge `6.8497` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `15.3288` n `135` status `ready` deltaP `1.2187` edge `1.3182` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.9709` n `132` status `ready` deltaP `26.7055` edge `0.055` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4847` n `135` status `ready` deltaP `10.906` edge `0.0035` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4627` n `135` status `ready` deltaP `13.2012` edge `0.0104` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.0647` n `135` status `ready` deltaP `10.7951` edge `0.011` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.2938` n `135` status `ready` deltaP `2.2777` edge `0.0104` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.4646` n `135` status `ready` deltaP `5.886` edge `0.0295` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5585` n `135` status `ready` deltaP `-0.2129` edge `-0.0019` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.673` n `135` status `ready` deltaP `9.6906` edge `0.0032` maxDD `-4.6603`
- `market_context_high->fx_24h` score `-0.7422` n `132` status `ready` deltaP `6.6724` edge `0.0176` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.7573` n `135` status `ready` deltaP `3.6405` edge `0.0345` maxDD `-1.0837`
- `market_context_high->metal_24h` score `-1.2797` n `132` status `ready` deltaP `13.1348` edge `0.0836` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.3653` n `135` status `ready` deltaP `2.3397` edge `0.0006` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.932` n `135` status `ready` deltaP `-0.8916` edge `-0.0054` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.3954` n `132` status `ready` deltaP `7.2015` edge `0.0488` maxDD `-15.7143`
- `market_context_high->index_4h` score `-2.4996` n `135` status `ready` deltaP `-3.4215` edge `-0.0233` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.5351` n `135` status `ready` deltaP `4.7267` edge `-0.0528` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.5771` n `132` status `ready` deltaP `-1.3642` edge `-0.092` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-4.7531` n `135` status `ready` deltaP `3.6145` edge `-0.1101` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
