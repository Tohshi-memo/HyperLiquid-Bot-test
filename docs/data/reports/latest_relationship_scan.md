# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T21:52:28.310413+00:00`
- Price records: `672`
- Market context records: `7294`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13807`

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

- `market_context_high->fx_1h` score `-0.1348` n `129` status `ready` deltaP `4.4626` edge `0.0019` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.6486` n `129` status `ready` deltaP `-1.2396` edge `-0.0147` maxDD `-1.8151`
- `market_context_high->crypto_alt_1h` score `-0.6945` n `129` status `ready` deltaP `-0.7137` edge `0.0196` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.7902` n `129` status `ready` deltaP `3.066` edge `0.0193` maxDD `-7.6171`
- `market_context_high->fx_4h` score `-0.8201` n `127` status `ready` deltaP `6.0512` edge `0.0145` maxDD `-1.4649`
- `market_context_high->fx_24h` score `-0.9589` n `123` status `ready` deltaP `-0.2022` edge `0.0012` maxDD `-2.1564`
- `market_context_high->commodity_4h` score `-1.1584` n `127` status `ready` deltaP `1.8914` edge `-0.0123` maxDD `-2.4139`
- `market_context_high->unknown_1h` score `-1.1966` n `129` status `ready` deltaP `0.7566` edge `-0.0961` maxDD `-1.3212`
- `market_context_high->unknown_4h` score `-1.3232` n `127` status `ready` deltaP `5.9847` edge `0.0857` maxDD `-6.2026`
- `market_context_high->index_1h` score `-1.4348` n `129` status `ready` deltaP `-6.4599` edge `-0.0102` maxDD `-2.3043`
- `market_context_high->metal_1h` score `-2.2627` n `129` status `ready` deltaP `-10.2992` edge `-0.0065` maxDD `-1.7383`
- `market_context_high->metal_4h` score `-2.5148` n `127` status `ready` deltaP `-10.1198` edge `-0.0094` maxDD `-4.6441`
- `market_context_high->commodity_24h` score `-3.0029` n `123` status `ready` deltaP `-5.6811` edge `-0.1326` maxDD `-2.3815`
- `market_context_high->crypto_alt_4h` score `-3.5598` n `127` status `ready` deltaP `0.1669` edge `-0.017` maxDD `-15.7942`
- `market_context_high->equity_1h` score `-4.6883` n `129` status `ready` deltaP `-10.3359` edge `-0.0724` maxDD `-15.2844`
- `market_context_high->crypto_major_4h` score `-4.9095` n `127` status `ready` deltaP `0.4957` edge `-0.023` maxDD `-23.4879`
- `market_context_high->index_4h` score `-5.2445` n `127` status `ready` deltaP `-14.9714` edge `-0.0631` maxDD `-11.5971`
- `market_context_high->unknown_24h` score `-5.6318` n `124` status `ready` deltaP `-10.2599` edge `-0.0524` maxDD `-15.8815`
- `market_context_high->metal_24h` score `-11.4489` n `124` status `ready` deltaP `-29.2955` edge `-0.1345` maxDD `-23.2749`
- `market_context_high->index_24h` score `-13.7077` n `123` status `ready` deltaP `-29.7349` edge `-0.1729` maxDD `-36.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
