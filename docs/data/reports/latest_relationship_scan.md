# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T03:22:29.399466+00:00`
- Price records: `672`
- Market context records: `7629`
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

- `market_context_high->equity_24h` score `0.38` n `145` status `ready` deltaP `16.9771` edge `0.4261` maxDD `-34.5784`
- `market_context_high->index_1h` score `0.1039` n `146` status `ready` deltaP `7.4129` edge `0.0118` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1183` n `146` status `ready` deltaP `8.455` edge `0.0245` maxDD `-4.0162`
- `market_context_high->unknown_24h` score `-0.1528` n `146` status `ready` deltaP `9.4487` edge `0.0423` maxDD `-4.775`
- `market_context_high->crypto_alt_1h` score `-0.1578` n `146` status `ready` deltaP `2.8033` edge `0.0243` maxDD `-2.7243`
- `market_context_high->commodity_24h` score `-0.1696` n `145` status `ready` deltaP `12.5424` edge `0.0606` maxDD `-7.0012`
- `market_context_high->commodity_1h` score `-0.3444` n `146` status `ready` deltaP `2.2789` edge `-0.0023` maxDD `-1.5641`
- `market_context_high->fx_24h` score `-0.3539` n `145` status `ready` deltaP `9.2803` edge `0.0174` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.412` n `146` status `ready` deltaP `6.4277` edge `0.0557` maxDD `-7.7764`
- `market_context_high->commodity_4h` score `-0.4938` n `146` status `ready` deltaP `3.5944` edge `0.0094` maxDD `-2.2943`
- `market_context_high->index_4h` score `-0.6399` n `146` status `ready` deltaP `8.9103` edge `0.0287` maxDD `-3.2774`
- `market_context_high->fx_1h` score `-0.675` n `146` status `ready` deltaP `-0.722` edge `-0.0015` maxDD `-0.6615`
- `market_context_high->metal_1h` score `-0.68` n `146` status `ready` deltaP `0.6398` edge `0.0131` maxDD `-1.0307`
- `market_context_high->crypto_alt_4h` score `-0.8686` n `146` status `ready` deltaP `3.8068` edge `0.0622` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.0934` n `146` status `ready` deltaP `9.1317` edge `0.0667` maxDD `-14.4206`
- `market_context_high->equity_4h` score `-1.4599` n `146` status `ready` deltaP `2.5198` edge `0.2104` maxDD `-20.4824`
- `market_context_high->unknown_1h` score `-1.5638` n `146` status `ready` deltaP `-1.2837` edge `-0.0594` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.6653` n `146` status `ready` deltaP `-1.6706` edge `0.0433` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-2.0398` n `146` status `ready` deltaP `-3.2772` edge `0.086` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.5716` n `146` status `ready` deltaP `-6.3529` edge `-0.0035` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
