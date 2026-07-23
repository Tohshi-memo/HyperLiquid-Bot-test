# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T07:37:24.656206+00:00`
- Price records: `672`
- Market context records: `7647`
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
- `market_context_high->crypto_major_1h` score `-0.1097` n `146` status `ready` deltaP `8.455` edge `0.0256` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2147` n `146` status `ready` deltaP `2.0548` edge `0.022` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3563` n `145` status `ready` deltaP `9.2803` edge `0.0172` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.4202` n `146` status `ready` deltaP `1.0777` edge `-0.004` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.4729` n `146` status `ready` deltaP `5.677` edge `0.0529` maxDD `-7.7764`
- `market_context_high->metal_1h` score `-0.6722` n `146` status `ready` deltaP `0.6398` edge `0.0141` maxDD `-1.0307`
- `market_context_high->commodity_4h` score `-0.6996` n `146` status `ready` deltaP `1.6066` edge `0.0055` maxDD `-2.2943`
- `market_context_high->index_4h` score `-0.7088` n `146` status `ready` deltaP `7.84` edge `0.027` maxDD `-3.2774`
- `market_context_high->commodity_24h` score `-0.7113` n `145` status `ready` deltaP `9.5807` edge `0.0352` maxDD `-7.0012`
- `market_context_high->fx_1h` score `-0.7422` n `146` status `ready` deltaP `-1.4727` edge `-0.0021` maxDD `-0.6615`
- `market_context_high->equity_24h` score `-1.0038` n `145` status `ready` deltaP `15.2349` edge `0.2603` maxDD `-34.5784`
- `market_context_high->crypto_alt_4h` score `-1.0214` n `146` status `ready` deltaP `2.8921` edge `0.0487` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.1407` n `146` status `ready` deltaP `9.4366` edge `0.0586` maxDD `-14.4206`
- `market_context_high->unknown_24h` score `-1.1581` n `146` status `ready` deltaP `6.4974` edge `-0.0218` maxDD `-4.775`
- `market_context_high->unknown_1h` score `-1.4415` n `146` status `ready` deltaP `-0.3855` edge `-0.0552` maxDD `-1.3217`
- `market_context_high->equity_4h` score `-1.6106` n `146` status `ready` deltaP `1.6023` edge `0.1972` maxDD `-20.4824`
- `market_context_high->metal_4h` score `-1.7412` n `146` status `ready` deltaP `-2.8901` edge `0.0417` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-2.2021` n `146` status `ready` deltaP `-3.2772` edge `0.0652` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.6851` n `146` status `ready` deltaP `-7.5761` edge `-0.0048` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
