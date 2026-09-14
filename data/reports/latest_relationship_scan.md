# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T20:37:39.560510+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10758`

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

- `news_risk_high->unknown_4h` score `396.9104` n `78` status `ready` deltaP `-22.4554` edge `33.3149` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `23.9443` n `78` status `ready` deltaP `18.9236` edge `1.8692` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.8814` n `78` status `ready` deltaP `46.5545` edge `1.5522` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `16.6423` n `78` status `ready` deltaP `33.8275` edge `1.3084` maxDD `-9.098`
- `news_risk_high->equity_24h` score `13.7489` n `78` status `ready` deltaP `41.6934` edge `1.0458` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7291` n `78` status `ready` deltaP `61.9391` edge `0.3321` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4313` n `78` status `ready` deltaP `37.7938` edge `0.3294` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `6.3324` n `122` status `ready` deltaP `36.2847` edge `0.2858` maxDD `0.0`
- `risk_on_high->commodity_24h` score `5.8752` n `51` status `ready` deltaP `36.2847` edge `0.2477` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.8752` n `51` status `ready` deltaP `36.2847` edge `0.2477` maxDD `0.0`
- `risk_on_high->fx_24h` score `4.4956` n `51` status `ready` deltaP `50.4698` edge `0.0424` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.4956` n `51` status `ready` deltaP `50.4698` edge `0.0424` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.1349` n `122` status `ready` deltaP `47.5126` edge `0.0494` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.1385` n `52` status `ready` deltaP `27.3569` edge `0.0308` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.1385` n `52` status `ready` deltaP `27.3569` edge `0.0308` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.9388` n `137` status `ready` deltaP `22.7668` edge `0.0516` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7802` n `137` status `ready` deltaP `12.812` edge `0.0173` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6258` n `78` status `ready` deltaP `15.7442` edge `0.0381` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2648` n `52` status `ready` deltaP `7.1972` edge `0.0093` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2648` n `52` status `ready` deltaP `7.1972` edge `0.0093` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
