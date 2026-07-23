# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T08:07:27.386532+00:00`
- Price records: `672`
- Market context records: `7650`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14697`

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

- `market_context_high->index_1h` score `0.0687` n `146` status `ready` deltaP `6.8123` edge `0.0113` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1199` n `146` status `ready` deltaP `8.455` edge `0.0243` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.224` n `146` status `ready` deltaP `2.0548` edge `0.0208` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3563` n `145` status `ready` deltaP `9.2803` edge `0.0172` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.4131` n `146` status `ready` deltaP `1.2279` edge `-0.0041` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.4885` n `146` status `ready` deltaP `5.5268` edge `0.0519` maxDD `-7.7764`
- `market_context_high->metal_1h` score `-0.6683` n `146` status `ready` deltaP `0.6398` edge `0.0146` maxDD `-1.0307`
- `market_context_high->commodity_4h` score `-0.7032` n `146` status `ready` deltaP `1.6066` edge `0.0052` maxDD `-2.2943`
- `market_context_high->index_4h` score `-0.7103` n `146` status `ready` deltaP `7.84` edge `0.0268` maxDD `-3.2774`
- `market_context_high->fx_1h` score `-0.7555` n `146` status `ready` deltaP `-1.6229` edge `-0.0022` maxDD `-0.6615`
- `market_context_high->commodity_24h` score `-0.7704` n `145` status `ready` deltaP `9.2323` edge `0.0326` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `-1.0591` n `146` status `ready` deltaP `2.5873` edge `0.0459` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.1594` n `146` status `ready` deltaP `9.4366` edge `0.0562` maxDD `-14.4206`
- `market_context_high->equity_24h` score `-1.1865` n `145` status `ready` deltaP `14.8865` edge `0.2392` maxDD `-34.5784`
- `market_context_high->unknown_1h` score `-1.4726` n `146` status `ready` deltaP `-0.6849` edge `-0.0558` maxDD `-1.3217`
- `market_context_high->equity_4h` score `-1.6341` n `146` status `ready` deltaP `1.4494` edge `0.1952` maxDD `-20.4824`
- `market_context_high->unknown_24h` score `-1.6886` n `146` status `ready` deltaP `6.1501` edge `-0.0637` maxDD `-4.775`
- `market_context_high->metal_4h` score `-1.7334` n `146` status `ready` deltaP `-2.8901` edge `0.0427` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-2.2153` n `146` status `ready` deltaP `-3.2772` edge `0.0635` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.7131` n `146` status `ready` deltaP `-7.882` edge `-0.0051` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
