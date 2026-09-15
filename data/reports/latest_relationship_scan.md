# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T06:07:28.479429+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11164`

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

- `news_risk_high->unknown_4h` score `399.7838` n `78` status `ready` deltaP `-21.9981` edge `33.5513` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `22.6582` n `78` status `ready` deltaP `18.4028` edge `1.7655` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.0993` n `78` status `ready` deltaP `43.6031` edge `1.5067` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `15.6782` n `78` status `ready` deltaP `32.7858` edge `1.235` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.5463` n `78` status `ready` deltaP `46.3809` edge `1.081` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.5647` n `78` status `ready` deltaP `60.7238` edge `0.3265` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4157` n `78` status `ready` deltaP `37.7938` edge `0.3281` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.1758` n `52` status `ready` deltaP `39.7569` edge `0.2496` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1758` n `52` status `ready` deltaP `39.7569` edge `0.2496` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.8788` n `137` status `ready` deltaP `32.4576` edge `0.2427` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `4.0475` n `52` status `ready` deltaP `45.9936` edge `0.0349` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.0475` n `52` status `ready` deltaP `45.9936` edge `0.0349` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.6505` n `137` status `ready` deltaP `42.8072` edge `0.0404` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9713` n `52` status `ready` deltaP `25.2228` edge `0.0311` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9713` n `52` status `ready` deltaP `25.2228` edge `0.0311` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8598` n `148` status `ready` deltaP `21.5846` edge `0.0529` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.809` n `149` status `ready` deltaP `13.2169` edge `0.017` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6316` n `78` status `ready` deltaP `16.2015` edge `0.0358` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.2245` n `52` status `ready` deltaP `7.7614` edge `0.0076` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2245` n `52` status `ready` deltaP `7.7614` edge `0.0076` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
