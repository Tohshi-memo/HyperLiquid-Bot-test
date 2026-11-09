# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T06:07:31.555151+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8718`

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

- `market_context_high->equity_24h` score `9.866` n `32` status `ready` deltaP `16.4931` edge `0.9495` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.5157` n `32` status `ready` deltaP `7.8125` edge `0.2163` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.3896` n `32` status `ready` deltaP `16.6667` edge `0.1133` maxDD `-2.3671`
- `market_context_high->commodity_4h` score `0.9626` n `68` status `ready` deltaP `7.0391` edge `0.0805` maxDD `-1.1102`
- `market_context_high->metal_4h` score `0.8592` n `68` status `ready` deltaP `12.7331` edge `0.0778` maxDD `-1.2025`
- `market_context_high->metal_1h` score `0.7414` n `80` status `ready` deltaP `9.8503` edge `0.0289` maxDD `-0.6226`
- `market_context_high->fx_24h` score `0.6916` n `32` status `ready` deltaP `10.7639` edge `-0.0053` maxDD `-0.0397`
- `market_context_high->index_4h` score `0.2273` n `68` status `ready` deltaP `13.3339` edge `0.0331` maxDD `-2.4279`
- `market_context_high->equity_1h` score `-0.0315` n `80` status `ready` deltaP `-1.0554` edge `0.1227` maxDD `-5.5762`
- `market_context_high->commodity_1h` score `-0.1121` n `80` status `ready` deltaP `5.3593` edge `0.0137` maxDD `-1.7019`
- `market_context_high->index_1h` score `-0.3742` n `80` status `ready` deltaP `-0.9057` edge `0.0164` maxDD `-0.6664`
- `market_context_high->crypto_alt_1h` score `-0.9634` n `80` status `ready` deltaP `6.7889` edge `0.0205` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-1.1433` n `80` status `ready` deltaP `-14.5434` edge `-0.0048` maxDD `-0.5856`
- `market_context_high->equity_4h` score `-1.4407` n `68` status `ready` deltaP `9.7919` edge `0.128` maxDD `-24.9053`
- `market_context_high->metal_24h` score `-1.66` n `32` status `ready` deltaP `-0.3472` edge `-0.1552` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.0098` n `68` status `ready` deltaP `-11.2178` edge `-0.0101` maxDD `-1.8223`
- `market_context_high->crypto_major_1h` score `-2.0993` n `80` status `ready` deltaP `-0.0075` edge `-0.0592` maxDD `-11.7911`
- `market_context_high->crypto_major_24h` score `-4.6282` n `32` status `ready` deltaP `-4.8611` edge `0.011` maxDD `-23.1423`
- `market_context_high->crypto_alt_4h` score `-6.7598` n `68` status `ready` deltaP `5.6492` edge `-0.1341` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-9.1834` n `32` status `ready` deltaP `-18.75` edge `-0.1824` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
