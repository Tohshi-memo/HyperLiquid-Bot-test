# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T12:22:23.209323+00:00`
- Price records: `672`
- Market context records: `865`
- Flow alert records: `2428`
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

- `risk_on_high->crypto_major_24h` score `22.4375` n `31` status `ready` deltaP `32.6389` edge `1.6522` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `22.4375` n `31` status `ready` deltaP `32.6389` edge `1.6522` maxDD `0.0`
- `risk_on_high->equity_24h` score `13.9762` n `31` status `ready` deltaP `25.3472` edge `0.9957` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `13.9762` n `31` status `ready` deltaP `25.3472` edge `0.9957` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `13.8346` n `31` status `ready` deltaP `7.8125` edge `1.1008` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.8346` n `31` status `ready` deltaP `7.8125` edge `1.1008` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `12.7202` n `165` status `ready` deltaP `28.3965` edge `0.9041` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.1541` n `165` status `ready` deltaP `7.2064` edge `0.4696` maxDD `-0.0508`
- `risk_on_high->index_24h` score `4.5845` n `31` status `ready` deltaP `27.9514` edge `0.1957` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.5845` n `31` status `ready` deltaP `27.9514` edge `0.1957` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4602` n `32` status `ready` deltaP `8.1555` edge `0.2705` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.4602` n `32` status `ready` deltaP `8.1555` edge `0.2705` maxDD `-0.9217`
- `risk_on_high->crypto_alt_4h` score `2.7556` n `32` status `ready` deltaP `21.5701` edge `0.1063` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.7556` n `32` status `ready` deltaP `21.5701` edge `0.1063` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `2.6976` n `32` status `ready` deltaP `19.6646` edge `0.1309` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.6976` n `32` status `ready` deltaP `19.6646` edge `0.1309` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.534` n `32` status `ready` deltaP `13.7957` edge `0.128` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.534` n `32` status `ready` deltaP `13.7957` edge `0.128` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `1.7473` n `31` status `ready` deltaP `-7.1236` edge `0.3392` maxDD `-1.7492`
- `risk_on_and_context->commodity_24h` score `1.7473` n `31` status `ready` deltaP `-7.1236` edge `0.3392` maxDD `-1.7492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
