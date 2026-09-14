# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T18:07:31.210807+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10692`

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

- `news_risk_high->unknown_4h` score `394.9546` n `78` status `ready` deltaP `-22.303` edge `33.1509` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `21.9583` n `78` status `ready` deltaP `46.9017` edge `1.5563` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `17.1693` n `78` status `ready` deltaP `34.1747` edge `1.35` maxDD `-9.098`
- `news_risk_high->equity_24h` score `13.3412` n `78` status `ready` deltaP `39.9572` edge `1.0234` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7099` n `78` status `ready` deltaP `61.9391` edge `0.3305` maxDD `-0.075`
- `market_context_high->commodity_24h` score `6.6864` n `116` status `ready` deltaP `37.5` edge `0.3072` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.3761` n `78` status `ready` deltaP `37.7938` edge `0.3248` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.0324` n `51` status `ready` deltaP `37.5` edge `0.2527` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.0324` n `51` status `ready` deltaP `37.5` edge `0.2527` maxDD `0.0`
- `risk_on_high->fx_24h` score `4.6621` n `51` status `ready` deltaP `52.2059` edge `0.0447` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.6621` n `51` status `ready` deltaP `52.2059` edge `0.0447` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.2714` n `116` status `ready` deltaP `48.9943` edge `0.0509` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.0113` n `52` status `ready` deltaP `26.4423` edge `0.0263` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0113` n `52` status `ready` deltaP `26.4423` edge `0.0263` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8116` n `137` status `ready` deltaP `21.8522` edge `0.0471` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.791` n `137` status `ready` deltaP `12.9617` edge `0.0172` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6438` n `78` status `ready` deltaP `15.8966` edge `0.0394` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2755` n `52` status `ready` deltaP `7.3469` edge `0.0092` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2755` n `52` status `ready` deltaP `7.3469` edge `0.0092` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2194` n `137` status `ready` deltaP `10.1589` edge `0.008` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
