# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T08:52:29.125390+00:00`
- Price records: `672`
- Market context records: `4708`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9638`

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

- `market_context_high->unknown_1h` score `76.916` n `144` status `ready` deltaP `13.7143` edge `6.36` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.2054` n `139` status `ready` deltaP `12.5286` edge `0.4713` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.7313` n `135` status `ready` deltaP `14.2709` edge `0.2248` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3178` n `144` status `ready` deltaP `2.258` edge `0.0238` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.6892` n `139` status `ready` deltaP `4.9384` edge `-0.009` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.9541` n `139` status `ready` deltaP `-1.7372` edge `-0.0025` maxDD `-1.9927`
- `market_context_high->commodity_4h` score `-1.0812` n `139` status `ready` deltaP `7.2809` edge `0.0236` maxDD `-9.1941`
- `market_context_high->equity_1h` score `-1.1798` n `144` status `ready` deltaP `-1.5926` edge `0.011` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-1.1972` n `139` status `ready` deltaP `1.8654` edge `0.011` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-1.2828` n `144` status `ready` deltaP `-4.9859` edge `-0.0057` maxDD `-1.1038`
- `market_context_high->index_1h` score `-1.6433` n `144` status `ready` deltaP `-3.9338` edge `-0.0103` maxDD `-2.6999`
- `market_context_high->crypto_alt_1h` score `-3.2478` n `144` status `ready` deltaP `-1.3889` edge `-0.0784` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-3.7745` n `144` status `ready` deltaP `-1.8796` edge `-0.0961` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-4.4408` n `135` status `ready` deltaP `16.5856` edge `0.0698` maxDD `-30.7016`
- `market_context_high->metal_1h` score `-4.4437` n `144` status `ready` deltaP `-5.4766` edge `-0.077` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.7925` n `135` status `ready` deltaP `-13.044` edge `-0.0164` maxDD `-5.3476`
- `market_context_high->crypto_alt_4h` score `-8.1074` n `139` status `ready` deltaP `-1.6034` edge `-0.163` maxDD `-63.9243`
- `market_context_high->index_24h` score `-8.3999` n `135` status `ready` deltaP `-10.6366` edge `-0.0916` maxDD `-29.3321`
- `market_context_high->metal_4h` score `-8.8219` n `139` status `ready` deltaP `1.94` edge `-0.2586` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-10.9854` n `139` status `ready` deltaP `-2.0179` edge `-0.3049` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
