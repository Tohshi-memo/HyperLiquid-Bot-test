# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T00:22:31.200894+00:00`
- Price records: `672`
- Market context records: `7616`
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

- `market_context_high->equity_24h` score `0.9151` n `145` status `ready` deltaP `16.9771` edge `0.4947` maxDD `-34.5784`
- `market_context_high->unknown_24h` score `0.6115` n `146` status `ready` deltaP `11.5321` edge `0.0921` maxDD `-4.775`
- `market_context_high->commodity_24h` score `0.1969` n `145` status `ready` deltaP `14.633` edge `0.0772` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.1039` n `146` status `ready` deltaP `7.4129` edge `0.0118` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1643` n `146` status `ready` deltaP `7.8562` edge `0.0226` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2022` n `146` status `ready` deltaP `2.3542` edge `0.0216` maxDD `-2.7243`
- `market_context_high->commodity_1h` score `-0.2648` n `146` status `ready` deltaP `3.6303` edge `-0.0011` maxDD `-1.5641`
- `market_context_high->commodity_4h` score `-0.2834` n `146` status `ready` deltaP `5.4292` edge `0.0147` maxDD `-2.2943`
- `market_context_high->fx_24h` score `-0.3455` n `145` status `ready` deltaP `9.2803` edge `0.0181` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.4338` n `146` status `ready` deltaP `6.2776` edge `0.0539` maxDD `-7.7764`
- `market_context_high->index_4h` score `-0.5812` n `146` status `ready` deltaP `9.8278` edge `0.0301` maxDD `-3.2774`
- `market_context_high->metal_1h` score `-0.6045` n `146` status `ready` deltaP `1.8374` edge `0.0148` maxDD `-1.0307`
- `market_context_high->fx_1h` score `-0.6906` n `146` status `ready` deltaP `-0.8721` edge `-0.0018` maxDD `-0.6615`
- `market_context_high->crypto_alt_4h` score `-0.9353` n `146` status `ready` deltaP `3.3495` edge `0.0567` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.1414` n `146` status `ready` deltaP `8.6744` edge `0.0636` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.4151` n `146` status `ready` deltaP `-0.0861` edge `-0.055` maxDD `-1.3217`
- `market_context_high->equity_4h` score `-1.4418` n `146` status `ready` deltaP `2.6727` edge `0.2117` maxDD `-20.4824`
- `market_context_high->metal_4h` score `-1.6078` n `146` status `ready` deltaP `-0.9084` edge `0.0456` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-1.9106` n `146` status `ready` deltaP `-2.7564` edge `0.0991` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.5776` n `146` status `ready` deltaP `-6.3529` edge `-0.004` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
