# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T01:22:23.859419+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10858`

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

- `news_risk_high->unknown_4h` score `400.1492` n `78` status `ready` deltaP `-22.4554` edge `33.5848` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `24.5983` n `78` status `ready` deltaP `18.9236` edge `1.9237` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.1659` n `78` status `ready` deltaP `43.7767` edge `1.5111` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `15.6377` n `78` status `ready` deltaP `32.265` edge `1.2351` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.1491` n `78` status `ready` deltaP `43.9503` edge `1.0641` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.6392` n `78` status `ready` deltaP `61.071` edge `0.3304` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4469` n `78` status `ready` deltaP `37.7938` edge `0.3307` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.0401` n `52` status `ready` deltaP `38.5417` edge `0.2464` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.0401` n `52` status `ready` deltaP `38.5417` edge `0.2464` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.7432` n `137` status `ready` deltaP `31.2424` edge `0.2395` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `4.197` n `52` status `ready` deltaP `47.3825` edge `0.0381` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.197` n `52` status `ready` deltaP `47.3825` edge `0.0381` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.8` n `137` status `ready` deltaP `44.1961` edge `0.0436` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9111` n `52` status `ready` deltaP `25.0703` edge `0.0271` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9111` n `52` status `ready` deltaP `25.0703` edge `0.0271` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7115` n `137` status `ready` deltaP `20.4802` edge `0.0479` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.7284` n `78` status `ready` deltaP `17.2686` edge `0.0411` maxDD `-0.6935`
- `market_context_high->commodity_1h` score `0.6926` n `141` status `ready` deltaP `11.837` edge `0.0165` maxDD `-0.3491`
- `risk_on_high->metal_1h` score `0.2292` n `52` status `ready` deltaP `7.7614` edge `0.0082` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2292` n `52` status `ready` deltaP `7.7614` edge `0.0082` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
