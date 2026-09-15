# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T07:07:32.538559+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11154`

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

- `news_risk_high->unknown_4h` score `399.6278` n `78` status `ready` deltaP `-21.9981` edge `33.5383` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `22.321` n `78` status `ready` deltaP `18.4028` edge `1.7374` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.2223` n `78` status `ready` deltaP `43.7767` edge `1.5158` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `15.8597` n `78` status `ready` deltaP `33.4803` edge `1.2455` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.6823` n `78` status `ready` deltaP `47.0753` edge `1.0877` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.5635` n `78` status `ready` deltaP `60.7238` edge `0.3264` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4265` n `78` status `ready` deltaP `37.7938` edge `0.329` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.0998` n `52` status `ready` deltaP `39.0625` edge `0.2479` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.0998` n `52` status `ready` deltaP `39.0625` edge `0.2479` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.8028` n `137` status `ready` deltaP `31.7632` edge `0.241` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.9727` n `52` status `ready` deltaP `45.2991` edge `0.0333` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.9727` n `52` status `ready` deltaP `45.2991` edge `0.0333` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.5757` n `137` status `ready` deltaP `42.1127` edge `0.0388` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9749` n `52` status `ready` deltaP `25.2228` edge `0.0314` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9749` n `52` status `ready` deltaP `25.2228` edge `0.0314` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8747` n `149` status `ready` deltaP `21.7251` edge `0.0532` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8234` n `149` status `ready` deltaP `13.3666` edge `0.0172` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6324` n `78` status `ready` deltaP `16.2015` edge `0.0359` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.2284` n `52` status `ready` deltaP `7.9111` edge `0.0071` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2284` n `52` status `ready` deltaP `7.9111` edge `0.0071` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
