# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T01:52:28.161962+00:00`
- Price records: `672`
- Market context records: `7623`
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

- `market_context_high->equity_24h` score `0.6741` n `145` status `ready` deltaP `16.9771` edge `0.4638` maxDD `-34.5784`
- `market_context_high->unknown_24h` score `0.2318` n `146` status `ready` deltaP `10.4904` edge `0.0674` maxDD `-4.775`
- `market_context_high->index_1h` score `0.0555` n `146` status `ready` deltaP `6.6622` edge `0.0106` maxDD `-0.8324`
- `market_context_high->commodity_24h` score `0.0148` n `145` status `ready` deltaP `13.5877` edge `0.069` maxDD `-7.0012`
- `market_context_high->crypto_major_1h` score `-0.169` n `146` status `ready` deltaP `7.8562` edge `0.022` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2248` n `146` status `ready` deltaP `2.0548` edge `0.0207` maxDD `-2.7243`
- `market_context_high->commodity_1h` score `-0.2992` n `146` status `ready` deltaP `3.0297` edge `-0.0015` maxDD `-1.5641`
- `market_context_high->fx_24h` score `-0.3479` n `145` status `ready` deltaP `9.2803` edge `0.0179` maxDD `-3.0343`
- `market_context_high->commodity_4h` score `-0.394` n `146` status `ready` deltaP `4.5118` edge `0.0116` maxDD `-2.2943`
- `market_context_high->equity_1h` score `-0.4947` n `146` status `ready` deltaP `5.677` edge `0.0501` maxDD `-7.7764`
- `market_context_high->index_4h` score `-0.6319` n `146` status `ready` deltaP `9.0633` edge `0.0287` maxDD `-3.2774`
- `market_context_high->fx_1h` score `-0.6377` n `146` status `ready` deltaP `-0.2715` edge `-0.0014` maxDD `-0.6615`
- `market_context_high->metal_1h` score `-0.6621` n `146` status `ready` deltaP `0.9392` edge `0.0134` maxDD `-1.0307`
- `market_context_high->crypto_alt_4h` score `-0.9282` n `146` status `ready` deltaP `3.3495` edge `0.0576` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.1846` n `146` status `ready` deltaP `8.217` edge `0.0611` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.4739` n `146` status `ready` deltaP `-0.5352` edge `-0.0569` maxDD `-1.3217`
- `market_context_high->equity_4h` score `-1.5073` n `146` status `ready` deltaP `1.9081` edge `0.2084` maxDD `-20.4824`
- `market_context_high->metal_4h` score `-1.6409` n `146` status `ready` deltaP `-1.3657` edge `0.0444` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-1.9961` n `146` status `ready` deltaP `-3.2772` edge `0.0916` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.574` n `146` status `ready` deltaP `-6.3529` edge `-0.0037` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
