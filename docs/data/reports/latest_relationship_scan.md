# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T06:22:13.177770+00:00`
- Price records: `672`
- Market context records: `948`
- Flow alert records: `2654`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `1320`

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

- `risk_on_high->crypto_major_24h` score `22.3047` n `30` status `ready` deltaP `34.5486` edge `1.6284` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `22.3047` n `30` status `ready` deltaP `34.5486` edge `1.6284` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `14.7512` n `167` status `ready` deltaP `31.5546` edge `1.0523` maxDD `-1.3382`
- `risk_on_high->crypto_alt_24h` score `14.4178` n `30` status `ready` deltaP `7.8125` edge `1.1494` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `14.4178` n `30` status `ready` deltaP `7.8125` edge `1.1494` maxDD `0.0`
- `risk_on_high->equity_24h` score `13.616` n `30` status `ready` deltaP `25.0` edge `0.968` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `13.616` n `30` status `ready` deltaP `25.0` edge `0.968` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.0254` n `167` status `ready` deltaP `7.8125` edge `0.6167` maxDD `0.0`
- `risk_on_high->index_24h` score `4.3169` n `30` status `ready` deltaP `26.7361` edge `0.1815` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.3169` n `30` status `ready` deltaP `26.7361` edge `0.1815` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.9331` n `30` status `ready` deltaP `8.4857` edge `0.2959` maxDD `-0.6435`
- `risk_on_and_context->equity_4h` score `3.9331` n `30` status `ready` deltaP `8.4857` edge `0.2959` maxDD `-0.6435`
- `risk_on_high->crypto_alt_4h` score `3.3547` n `30` status `ready` deltaP `23.689` edge `0.1421` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.3547` n `30` status `ready` deltaP `23.689` edge `0.1421` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `2.707` n `30` status `ready` deltaP `19.8272` edge `0.1306` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.707` n `30` status `ready` deltaP `19.8272` edge `0.1306` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.209` n `30` status `ready` deltaP `8.6382` edge `0.1353` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.209` n `30` status `ready` deltaP `8.6382` edge `0.1353` maxDD `-0.038`
- `risk_on_high->commodity_4h` score `1.1272` n `30` status `ready` deltaP `8.0793` edge `0.1591` maxDD `-1.1421`
- `risk_on_and_context->commodity_4h` score `1.1272` n `30` status `ready` deltaP `8.0793` edge `0.1591` maxDD `-1.1421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
