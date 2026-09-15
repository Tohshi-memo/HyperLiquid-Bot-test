# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T00:52:35.714163+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10836`

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

- `news_risk_high->unknown_4h` score `397.8932` n `78` status `ready` deltaP `-22.4554` edge `33.3968` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `24.5743` n `78` status `ready` deltaP `18.9236` edge `1.9217` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.2393` n `78` status `ready` deltaP `44.1239` edge `1.5149` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `15.7049` n `78` status `ready` deltaP `32.265` edge `1.2407` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.1527` n `78` status `ready` deltaP `43.9503` edge `1.0644` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.6742` n `78` status `ready` deltaP `61.4182` edge `0.331` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4541` n `78` status `ready` deltaP `37.7938` edge `0.3313` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.998` n `52` status `ready` deltaP `38.1944` edge `0.2452` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.998` n `52` status `ready` deltaP `38.1944` edge `0.2452` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.701` n `137` status `ready` deltaP `30.8951` edge `0.2383` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `4.2296` n `52` status `ready` deltaP `47.7297` edge `0.0385` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.2296` n `52` status `ready` deltaP `47.7297` edge `0.0385` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.8326` n `137` status `ready` deltaP `44.5433` edge `0.044` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9245` n `52` status `ready` deltaP `25.2228` edge `0.0272` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9245` n `52` status `ready` deltaP `25.2228` edge `0.0272` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7249` n `137` status `ready` deltaP `20.6327` edge `0.048` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7318` n `139` status `ready` deltaP `12.2367` edge `0.0171` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7277` n `78` status `ready` deltaP `17.2686` edge `0.041` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.223` n `52` status `ready` deltaP `7.6117` edge `0.0084` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.223` n `52` status `ready` deltaP `7.6117` edge `0.0084` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
