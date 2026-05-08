# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T14:22:11.987640+00:00`
- Price records: `653`
- Market context records: `763`
- Flow alert records: `2152`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1170`

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

- `market_context_high->crypto_major_24h` score `13.371` n `147` status `ready` deltaP `31.731` edge `0.9361` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.7791` n `147` status `ready` deltaP `7.3987` edge `0.5204` maxDD `-0.0508`
- `risk_on_high->metal_1h` score `1.2998` n `32` status `ready` deltaP `15.0183` edge `0.0312` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.2998` n `32` status `ready` deltaP `15.0183` edge `0.0312` maxDD `-0.5074`
- `market_context_high->index_24h` score `0.5665` n `147` status `ready` deltaP `3.3927` edge `0.2241` maxDD `-5.9609`
- `risk_on_high->fx_1h` score `0.4268` n `32` status `ready` deltaP `10.5862` edge `0.0031` maxDD `-0.1827`
- `risk_on_and_context->fx_1h` score `0.4268` n `32` status `ready` deltaP `10.5862` edge `0.0031` maxDD `-0.1827`
- `risk_on_high->commodity_1h` score `0.2116` n `32` status `ready` deltaP `6.7684` edge `0.0196` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.2116` n `32` status `ready` deltaP `6.7684` edge `0.0196` maxDD `-0.6739`
- `risk_on_high->crypto_major_1h` score `0.1292` n `32` status `ready` deltaP `6.9867` edge `-0.0015` maxDD `-0.948`
- `risk_on_and_context->crypto_major_1h` score `0.1292` n `32` status `ready` deltaP `6.9867` edge `-0.0015` maxDD `-0.948`
- `market_context_high->equity_24h` score `0.0236` n `147` status `ready` deltaP `1.9116` edge `0.2497` maxDD `-10.5047`
- `risk_on_high->crypto_alt_1h` score `-0.3433` n `32` status `ready` deltaP `3.7943` edge `-0.0215` maxDD `-0.9258`
- `risk_on_and_context->crypto_alt_1h` score `-0.3433` n `32` status `ready` deltaP `3.7943` edge `-0.0215` maxDD `-0.9258`
- `risk_on_high->index_1h` score `-0.3603` n `32` status `ready` deltaP `-1.5552` edge `0.0087` maxDD `-0.2687`
- `risk_on_and_context->index_1h` score `-0.3603` n `32` status `ready` deltaP `-1.5552` edge `0.0087` maxDD `-0.2687`
- `market_context_high->fx_4h` score `-0.3818` n `167` status `ready` deltaP `4.5293` edge `0.008` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.5064` n `179` status `ready` deltaP `1.6396` edge `0.0095` maxDD `-2.8282`
- `market_context_high->fx_1h` score `-0.5153` n `179` status `ready` deltaP `1.9444` edge `0.0019` maxDD `-0.291`
- `market_context_high->equity_1h` score `-0.5663` n `179` status `ready` deltaP `-0.2209` edge `0.0099` maxDD `-4.4826`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
