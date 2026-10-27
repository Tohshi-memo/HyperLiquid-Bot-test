# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T10:22:37.597340+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9402`

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

- `market_context_high->unknown_4h` score `86.2401` n `135` status `ready` deltaP `5.4619` edge `7.1655` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `15.4847` n `135` status `ready` deltaP `1.5181` edge `1.3292` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.9` n `129` status `ready` deltaP `26.6293` edge `0.0496` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4979` n `135` status `ready` deltaP `11.0557` edge `0.0036` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4627` n `135` status `ready` deltaP `13.2012` edge `0.0104` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.0834` n `135` status `ready` deltaP `11.0945` edge `0.0114` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.3285` n `135` status `ready` deltaP `1.9783` edge `0.0095` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.4653` n `135` status `ready` deltaP `5.7363` edge `0.0304` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5391` n `135` status `ready` deltaP `0.0865` edge `-0.0014` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.6422` n `135` status `ready` deltaP `10.1479` edge `0.0041` maxDD `-4.6603`
- `market_context_high->fx_24h` score `-0.7025` n `129` status `ready` deltaP `7.3153` edge `0.0184` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.7511` n `135` status `ready` deltaP `3.7929` edge `0.034` maxDD `-1.0837`
- `market_context_high->metal_24h` score `-1.0462` n `129` status `ready` deltaP `14.1215` edge `0.0871` maxDD `-7.4744`
- `market_context_high->equity_1h` score `-1.3287` n `135` status `ready` deltaP `2.6391` edge `0.0033` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.932` n `135` status `ready` deltaP `-1.0413` edge `-0.0044` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.468` n `135` status `ready` deltaP `-3.1166` edge `-0.0227` maxDD `-5.6417`
- `market_context_high->equity_24h` score `-2.6379` n `129` status `ready` deltaP `6.7201` edge `0.0318` maxDD `-15.7143`
- `market_context_high->crypto_major_4h` score `-3.5548` n `135` status `ready` deltaP `4.5743` edge `-0.0543` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.6243` n `129` status `ready` deltaP `-1.3408` edge `-0.0982` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-4.7061` n `135` status `ready` deltaP `3.9194` edge `-0.1061` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
