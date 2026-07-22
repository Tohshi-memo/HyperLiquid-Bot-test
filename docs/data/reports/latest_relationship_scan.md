# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T23:22:30.735801+00:00`
- Price records: `672`
- Market context records: `7611`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14551`

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

- `market_context_high->equity_24h` score `1.0734` n `145` status `ready` deltaP `16.9771` edge `0.515` maxDD `-34.5784`
- `market_context_high->unknown_24h` score `0.8495` n `146` status `ready` deltaP `12.2265` edge `0.1073` maxDD `-4.775`
- `market_context_high->commodity_24h` score `0.3258` n `145` status `ready` deltaP `15.3298` edge `0.0833` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.1163` n `146` status `ready` deltaP `7.5631` edge `0.0124` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.116` n `146` status `ready` deltaP `8.455` edge `0.0248` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.1796` n `146` status `ready` deltaP `2.6536` edge `0.0225` maxDD `-2.7243`
- `market_context_high->commodity_4h` score `-0.2093` n `146` status `ready` deltaP `6.0408` edge `0.0168` maxDD `-2.2943`
- `market_context_high->commodity_1h` score `-0.2468` n `146` status `ready` deltaP `3.9306` edge `-0.0008` maxDD `-1.5641`
- `market_context_high->fx_24h` score `-0.3371` n `145` status `ready` deltaP `9.2803` edge `0.0188` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.4018` n `146` status `ready` deltaP `6.5779` edge `0.056` maxDD `-7.7764`
- `market_context_high->index_4h` score `-0.5519` n `146` status `ready` deltaP `10.2865` edge `0.0308` maxDD `-3.2774`
- `market_context_high->metal_1h` score `-0.585` n `146` status `ready` deltaP `2.1368` edge `0.0153` maxDD `-1.0307`
- `market_context_high->fx_1h` score `-0.6654` n `146` status `ready` deltaP `-0.5718` edge `-0.0017` maxDD `-0.6615`
- `market_context_high->crypto_alt_4h` score `-0.9163` n `146` status `ready` deltaP `3.6543` edge `0.0571` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.0808` n `146` status `ready` deltaP `9.2841` edge `0.0673` maxDD `-14.4206`
- `market_context_high->equity_4h` score `-1.3889` n `146` status `ready` deltaP `3.2843` edge `0.2144` maxDD `-20.4824`
- `market_context_high->unknown_1h` score `-1.4511` n `146` status `ready` deltaP `-0.2358` edge `-0.057` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.6` n `146` status `ready` deltaP `-0.9084` edge `0.0466` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-1.8183` n `146` status `ready` deltaP `-2.0619` edge `0.1063` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.5642` n `146` status `ready` deltaP `-6.2` edge `-0.0039` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
