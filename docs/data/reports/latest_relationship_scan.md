# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T03:37:26.409529+00:00`
- Price records: `672`
- Market context records: `7630`
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

- `market_context_high->equity_24h` score `0.316` n `145` status `ready` deltaP `16.9771` edge `0.4179` maxDD `-34.5784`
- `market_context_high->index_1h` score `0.1039` n `146` status `ready` deltaP `7.4129` edge `0.0118` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1269` n `146` status `ready` deltaP `8.3053` edge `0.0244` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.157` n `146` status `ready` deltaP `2.8033` edge `0.0244` maxDD `-2.7243`
- `market_context_high->commodity_24h` score `-0.2027` n `145` status `ready` deltaP `12.3682` edge `0.059` maxDD `-7.0012`
- `market_context_high->unknown_24h` score `-0.2182` n `146` status `ready` deltaP `9.2751` edge `0.038` maxDD `-4.775`
- `market_context_high->commodity_1h` score `-0.3538` n `146` status `ready` deltaP `2.1288` edge `-0.0025` maxDD `-1.5641`
- `market_context_high->fx_24h` score `-0.3539` n `145` status `ready` deltaP `9.2803` edge `0.0174` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.4128` n `146` status `ready` deltaP `6.4277` edge `0.0556` maxDD `-7.7764`
- `market_context_high->commodity_4h` score `-0.5108` n `146` status `ready` deltaP `3.4415` edge `0.009` maxDD `-2.2943`
- `market_context_high->index_4h` score `-0.6486` n `146` status `ready` deltaP `8.7574` edge `0.0286` maxDD `-3.2774`
- `market_context_high->metal_1h` score `-0.68` n `146` status `ready` deltaP `0.6398` edge `0.0131` maxDD `-1.0307`
- `market_context_high->fx_1h` score `-0.6882` n `146` status `ready` deltaP `-0.8721` edge `-0.0016` maxDD `-0.6615`
- `market_context_high->crypto_alt_4h` score `-0.8686` n `146` status `ready` deltaP `3.8068` edge `0.0622` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.0911` n `146` status `ready` deltaP `9.1317` edge `0.067` maxDD `-14.4206`
- `market_context_high->equity_4h` score `-1.471` n `146` status `ready` deltaP `2.3669` edge `0.21` maxDD `-20.4824`
- `market_context_high->unknown_1h` score `-1.5686` n `146` status `ready` deltaP `-1.2837` edge `-0.0598` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.6764` n `146` status `ready` deltaP `-1.823` edge `0.0429` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-2.05` n `146` status `ready` deltaP `-3.2772` edge `0.0847` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.5716` n `146` status `ready` deltaP `-6.3529` edge `-0.0035` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
