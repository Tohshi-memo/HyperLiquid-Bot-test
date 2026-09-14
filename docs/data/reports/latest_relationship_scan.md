# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T02:22:28.448314+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11352`

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

- `news_risk_high->unknown_1h` score `444.5524` n `82` status `ready` deltaP `-5.5499` edge `37.1252` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.3224` n `82` status `ready` deltaP `37.4096` edge `1.4096` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.364` n `82` status `ready` deltaP `38.0236` edge `1.4239` maxDD `-9.098`
- `news_risk_high->equity_24h` score `10.9599` n `82` status `ready` deltaP `32.6156` edge `0.8739` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.8019` n `82` status `ready` deltaP `56.3877` edge `0.2919` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.2822` n `60` status `ready` deltaP `39.8276` edge `0.258` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.017` n `37` status `ready` deltaP `39.8276` edge `0.2359` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.017` n `37` status `ready` deltaP `39.8276` edge `0.2359` maxDD `0.0`
- `risk_on_high->fx_24h` score `5.6086` n `37` status `ready` deltaP `61.9525` edge `0.0586` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.6086` n `37` status `ready` deltaP `61.9525` edge `0.0586` maxDD `-0.0054`
- `news_risk_high->metal_24h` score `5.2186` n `82` status `ready` deltaP `30.7948` edge `0.275` maxDD `-0.6334`
- `market_context_high->fx_24h` score `4.8443` n `60` status `ready` deltaP `54.6552` edge `0.0609` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9695` n `52` status `ready` deltaP `26.5947` edge `0.0218` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9695` n `52` status `ready` deltaP `26.5947` edge `0.0218` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.734` n `129` status `ready` deltaP `21.4218` edge `0.0435` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.6819` n `137` status `ready` deltaP `11.9138` edge `0.0151` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5563` n `82` status `ready` deltaP `14.6341` edge `0.0366` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3247` n `129` status `ready` deltaP `11.6586` edge `0.0115` maxDD `-0.1412`
- `market_context_high->fx_1h` score `0.1771` n `137` status `ready` deltaP `5.6613` edge `0.0028` maxDD `-0.063`
- `risk_on_high->commodity_1h` score `0.1665` n `52` status `ready` deltaP `6.299` edge `0.0071` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
