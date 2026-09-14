# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T23:37:28.155337+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10512`

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

- `news_risk_high->unknown_4h` score `397.8992` n `78` status `ready` deltaP `-22.4554` edge `33.3973` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `24.9055` n `78` status `ready` deltaP `18.9236` edge `1.9493` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.4173` n `78` status `ready` deltaP `44.8184` edge `1.5251` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `15.8981` n `78` status `ready` deltaP `32.265` edge `1.2568` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.1016` n `78` status `ready` deltaP `43.7767` edge `1.0613` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7303` n `78` status `ready` deltaP `61.9391` edge `0.3322` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4457` n `78` status `ready` deltaP `37.7938` edge `0.3306` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.9129` n `52` status `ready` deltaP `37.3264` edge `0.2439` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9129` n `52` status `ready` deltaP `37.3264` edge `0.2439` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.0947` n `134` status `ready` deltaP `32.1025` edge `0.2479` maxDD `-0.6556`
- `risk_on_high->fx_24h` score `4.3134` n `52` status `ready` deltaP `48.5977` edge `0.0397` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.3134` n `52` status `ready` deltaP `48.5977` edge `0.0397` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.9097` n `134` status `ready` deltaP `45.2969` edge `0.0454` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9999` n `52` status `ready` deltaP `25.985` edge `0.0284` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9999` n `52` status `ready` deltaP `25.985` edge `0.0284` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8002` n `137` status `ready` deltaP `21.3949` edge `0.0492` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7538` n `137` status `ready` deltaP `12.5126` edge `0.0171` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7222` n `78` status `ready` deltaP `17.2686` edge `0.0403` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2384` n `52` status `ready` deltaP `6.8978` edge `0.0091` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2384` n `52` status `ready` deltaP `6.8978` edge `0.0091` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
