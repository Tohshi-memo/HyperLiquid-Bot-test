# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T08:22:31.252393+00:00`
- Price records: `672`
- Market context records: `7651`
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

- `market_context_high->index_1h` score `0.0594` n `146` status `ready` deltaP `6.6622` edge `0.0111` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1448` n `146` status `ready` deltaP `8.3053` edge `0.0221` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2459` n `146` status `ready` deltaP `1.9051` edge `0.019` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3563` n `145` status `ready` deltaP `9.2803` edge `0.0172` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.4045` n `146` status `ready` deltaP `1.378` edge `-0.004` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.5064` n `146` status `ready` deltaP `5.3767` edge `0.0506` maxDD `-7.7764`
- `market_context_high->metal_1h` score `-0.659` n `146` status `ready` deltaP `0.7895` edge `0.0148` maxDD `-1.0307`
- `market_context_high->commodity_4h` score `-0.7056` n `146` status `ready` deltaP `1.6066` edge `0.005` maxDD `-2.2943`
- `market_context_high->index_4h` score `-0.7111` n `146` status `ready` deltaP `7.84` edge `0.0267` maxDD `-3.2774`
- `market_context_high->fx_1h` score `-0.7675` n `146` status `ready` deltaP `-1.773` edge `-0.0022` maxDD `-0.6615`
- `market_context_high->commodity_24h` score `-0.7987` n `145` status `ready` deltaP `9.0581` edge `0.0314` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `-1.0764` n `146` status `ready` deltaP `2.4348` edge `0.0447` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.1688` n `146` status `ready` deltaP `9.4366` edge `0.055` maxDD `-14.4206`
- `market_context_high->equity_24h` score `-1.2814` n `145` status `ready` deltaP `14.7123` edge `0.2282` maxDD `-34.5784`
- `market_context_high->unknown_1h` score `-1.475` n `146` status `ready` deltaP `-0.6849` edge `-0.056` maxDD `-1.3217`
- `market_context_high->equity_4h` score `-1.653` n `146` status `ready` deltaP `1.2965` edge `0.1938` maxDD `-20.4824`
- `market_context_high->metal_4h` score `-1.7288` n `146` status `ready` deltaP `-2.8901` edge `0.0433` maxDD `-4.6535`
- `market_context_high->unknown_24h` score `-1.9569` n `146` status `ready` deltaP `5.9765` edge `-0.0849` maxDD `-4.775`
- `market_context_high->metal_24h` score `-2.2216` n `146` status `ready` deltaP `-3.2772` edge `0.0627` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.7266` n `146` status `ready` deltaP `-8.0349` edge `-0.0052` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
