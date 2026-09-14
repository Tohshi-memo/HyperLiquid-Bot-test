# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T13:37:33.847640+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11190`

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

- `news_risk_high->unknown_4h` score `388.9577` n `79` status `ready` deltaP `-19.8345` edge `32.6347` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `21.3549` n `79` status `ready` deltaP `45.1037` edge `1.518` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `17.5692` n `79` status `ready` deltaP `35.0782` edge `1.3773` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.6711` n `79` status `ready` deltaP `37.2055` edge `0.9859` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.5738` n `79` status `ready` deltaP `61.4231` edge `0.3226` maxDD `-0.075`
- `market_context_high->commodity_24h` score `7.1575` n `100` status `ready` deltaP `40.1042` edge `0.3291` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.1483` n `41` status `ready` deltaP `40.1042` edge `0.245` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1483` n `41` status `ready` deltaP `40.1042` edge `0.245` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.1306` n `79` status `ready` deltaP `36.5397` edge `0.3127` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `4.875` n `41` status `ready` deltaP `54.8527` edge `0.0448` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.875` n `41` status `ready` deltaP `54.8527` edge `0.0448` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.4744` n `100` status `ready` deltaP `51.2917` edge `0.0525` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9983` n `52` status `ready` deltaP `26.5947` edge `0.0242` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9983` n `52` status `ready` deltaP `26.5947` edge `0.0242` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7986` n `137` status `ready` deltaP `22.0046` edge `0.045` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.6999` n `137` status `ready` deltaP `12.0635` edge `0.0156` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6437` n `79` status `ready` deltaP `15.79` edge `0.0401` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.2803` n `137` status `ready` deltaP `11.226` edge `0.0087` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.1845` n `52` status `ready` deltaP `6.4487` edge `0.0076` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.1845` n `52` status `ready` deltaP `6.4487` edge `0.0076` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
