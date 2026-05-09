# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T14:07:13.595474+00:00`
- Price records: `672`
- Market context records: `872`
- Flow alert records: `2450`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1386`

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

- `risk_on_high->crypto_major_24h` score `22.1999` n `31` status `ready` deltaP `32.6389` edge `1.6324` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `22.1999` n `31` status `ready` deltaP `32.6389` edge `1.6324` maxDD `0.0`
- `risk_on_high->equity_24h` score `13.6738` n `31` status `ready` deltaP `25.3472` edge `0.9705` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `13.6738` n `31` status `ready` deltaP `25.3472` edge `0.9705` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `13.6078` n `31` status `ready` deltaP `7.8125` edge `1.0819` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.6078` n `31` status `ready` deltaP `7.8125` edge `1.0819` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.3094` n `165` status `ready` deltaP `28.3965` edge `0.9532` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.7193` n `165` status `ready` deltaP `7.2064` edge `0.5167` maxDD `-0.0508`
- `risk_on_high->index_24h` score `4.4741` n `31` status `ready` deltaP `27.9514` edge `0.1865` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.4741` n `31` status `ready` deltaP `27.9514` edge `0.1865` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4298` n `32` status `ready` deltaP `7.8506` edge `0.27` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.4298` n `32` status `ready` deltaP `7.8506` edge `0.27` maxDD `-0.9217`
- `risk_on_high->crypto_alt_4h` score `3.0653` n `32` status `ready` deltaP `22.6372` edge `0.125` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.0653` n `32` status `ready` deltaP `22.6372` edge `0.125` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `2.8622` n `32` status `ready` deltaP `20.7317` edge `0.1375` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.8622` n `32` status `ready` deltaP `20.7317` edge `0.1375` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.5522` n `32` status `ready` deltaP `13.9482` edge `0.1285` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.5522` n `32` status `ready` deltaP `13.9482` edge `0.1285` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `1.7144` n `31` status `ready` deltaP `-7.4709` edge `0.3373` maxDD `-1.7492`
- `risk_on_and_context->commodity_24h` score `1.7144` n `31` status `ready` deltaP `-7.4709` edge `0.3373` maxDD `-1.7492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
