# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T06:52:30.649473+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11184`

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

- `news_risk_high->unknown_4h` score `399.6686` n `78` status `ready` deltaP `-21.9981` edge `33.5417` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `22.4074` n `78` status `ready` deltaP `18.4028` edge `1.7446` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.1911` n `78` status `ready` deltaP `43.7767` edge `1.5132` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `15.805` n `78` status `ready` deltaP `33.3066` edge `1.2421` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.642` n `78` status `ready` deltaP `46.9017` edge `1.0855` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.5623` n `78` status `ready` deltaP `60.7238` edge `0.3263` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4217` n `78` status `ready` deltaP `37.7938` edge `0.3286` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.1185` n `52` status `ready` deltaP `39.2361` edge `0.2483` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1185` n `52` status `ready` deltaP `39.2361` edge `0.2483` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.8215` n `137` status `ready` deltaP `31.9368` edge `0.2414` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.9926` n `52` status `ready` deltaP `45.4727` edge `0.0338` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.9926` n `52` status `ready` deltaP `45.4727` edge `0.0338` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.5956` n `137` status `ready` deltaP `42.2863` edge `0.0393` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9761` n `52` status `ready` deltaP `25.2228` edge `0.0315` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9761` n `52` status `ready` deltaP `25.2228` edge `0.0315` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8759` n `149` status `ready` deltaP `21.7251` edge `0.0533` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8234` n `149` status `ready` deltaP `13.3666` edge `0.0172` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6308` n `78` status `ready` deltaP `16.2015` edge `0.0357` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.2206` n `52` status `ready` deltaP `7.7614` edge `0.0071` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2206` n `52` status `ready` deltaP `7.7614` edge `0.0071` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
