# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T14:37:35.522166+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11070`

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

- `news_risk_high->unknown_4h` score `396.4562` n `78` status `ready` deltaP `-23.2176` edge `33.2822` maxDD `-4.1517`
- `news_risk_high->crypto_alt_24h` score `22.5693` n `78` status `ready` deltaP `47.2489` edge `1.6049` maxDD `-1.4626`
- `news_risk_high->unknown_24h` score `22.4615` n `78` status `ready` deltaP `20.8333` edge `1.7329` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `17.6569` n `78` status `ready` deltaP `38.515` edge `1.3617` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.1267` n `78` status `ready` deltaP `48.985` edge `1.1114` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.4273` n `78` status `ready` deltaP `59.6821` edge `0.322` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4366` n `78` status `ready` deltaP `37.6202` edge `0.331` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.022` n `52` status `ready` deltaP `38.1944` edge `0.2472` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.022` n `52` status `ready` deltaP `38.1944` edge `0.2472` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.725` n `137` status `ready` deltaP `30.8951` edge `0.2403` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.3701` n `52` status `ready` deltaP `40.0908` edge `0.0178` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.3701` n `52` status `ready` deltaP `40.0908` edge `0.0178` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.9731` n `137` status `ready` deltaP `36.9044` edge `0.0233` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.7198` n `52` status `ready` deltaP `23.6984` edge `0.0203` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.7198` n `52` status `ready` deltaP `23.6984` edge `0.0203` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.6195` n `149` status `ready` deltaP `20.2007` edge `0.0421` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7395` n `149` status `ready` deltaP `12.6181` edge `0.0152` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6957` n `78` status `ready` deltaP `17.2686` edge `0.0369` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.2038` n `149` status `ready` deltaP `10.0384` edge `0.0068` maxDD `-0.1412`
- `risk_on_high->metal_1h` score `0.1832` n `52` status `ready` deltaP `7.1626` edge `0.0063` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
