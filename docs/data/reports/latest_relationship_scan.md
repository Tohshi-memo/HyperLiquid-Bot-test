# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T04:37:28.315944+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11550`

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

- `news_risk_high->unknown_1h` score `443.7209` n `82` status `ready` deltaP `-5.999` edge `37.0589` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.6656` n `82` status `ready` deltaP `38.7889` edge `1.429` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.1738` n `82` status `ready` deltaP `37.5064` edge `1.4115` maxDD `-9.098`
- `news_risk_high->equity_24h` score `11.4693` n `82` status `ready` deltaP `34.1674` edge `0.906` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.0148` n `82` status `ready` deltaP `57.9394` edge `0.2993` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.6746` n `69` status `ready` deltaP `39.8276` edge `0.2907` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.3014` n `41` status `ready` deltaP `39.8276` edge `0.2596` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.3014` n `41` status `ready` deltaP `39.8276` edge `0.2596` maxDD `0.0`
- `risk_on_high->fx_24h` score `5.4923` n `41` status `ready` deltaP `60.6644` edge `0.0575` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.4923` n `41` status `ready` deltaP `60.6644` edge `0.0575` maxDD `-0.0054`
- `news_risk_high->metal_24h` score `5.4159` n `82` status `ready` deltaP `32.3465` edge `0.2811` maxDD `-0.6334`
- `market_context_high->fx_24h` score `4.7981` n `69` status `ready` deltaP `54.4077` edge `0.0587` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.0059` n `52` status `ready` deltaP `26.8996` edge `0.0228` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0059` n `52` status `ready` deltaP `26.8996` edge `0.0228` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8062` n `137` status `ready` deltaP `22.3095` edge `0.0436` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.6963` n `137` status `ready` deltaP `12.0635` edge `0.0153` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5919` n `82` status `ready` deltaP `15.2439` edge `0.0371` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3387` n `137` status `ready` deltaP `11.9881` edge `0.0111` maxDD `-0.1412`
- `market_context_high->fx_1h` score `0.2298` n `137` status `ready` deltaP `6.2601` edge `0.0032` maxDD `-0.063`
- `risk_on_high->commodity_1h` score `0.1809` n `52` status `ready` deltaP `6.4487` edge `0.0073` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
