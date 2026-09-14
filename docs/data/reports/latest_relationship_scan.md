# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T13:22:43.932446+00:00`
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

- `news_risk_high->unknown_4h` score `382.4747` n `80` status `ready` deltaP `-20.4573` edge `32.0986` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `21.0643` n `80` status `ready` deltaP `44.0278` edge `1.5026` maxDD `-1.5939`
- `news_risk_high->crypto_major_24h` score `17.2286` n `80` status `ready` deltaP `34.2708` edge `1.3543` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.6287` n `80` status `ready` deltaP `37.3958` edge `0.9811` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.5354` n `80` status `ready` deltaP `61.4236` edge `0.3194` maxDD `-0.075`
- `market_context_high->commodity_24h` score `7.1683` n `99` status `ready` deltaP `40.1042` edge `0.33` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.1555` n `41` status `ready` deltaP `40.1042` edge `0.2456` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1555` n `41` status `ready` deltaP `40.1042` edge `0.2456` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.1287` n `80` status `ready` deltaP `36.6667` edge `0.3117` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `4.8925` n `41` status `ready` deltaP `55.0263` edge `0.0451` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.8925` n `41` status `ready` deltaP `55.0263` edge `0.0451` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.4799` n `99` status `ready` deltaP `51.4047` edge `0.0522` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9995` n `52` status `ready` deltaP `26.5947` edge `0.0243` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9995` n `52` status `ready` deltaP `26.5947` edge `0.0243` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7998` n `137` status `ready` deltaP `22.0046` edge `0.0451` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.6951` n `137` status `ready` deltaP `12.0635` edge `0.0152` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6708` n `80` status `ready` deltaP `16.2805` edge `0.0403` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.289` n `137` status `ready` deltaP `11.3784` edge `0.0088` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.1797` n `52` status `ready` deltaP `6.4487` edge `0.0072` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.1797` n `52` status `ready` deltaP `6.4487` edge `0.0072` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
