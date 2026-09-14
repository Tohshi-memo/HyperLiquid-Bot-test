# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T01:52:30.328544+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11328`

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

- `news_risk_high->unknown_1h` score `442.2988` n `82` status `ready` deltaP `-5.5499` edge `36.9374` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.2252` n `82` status `ready` deltaP `37.0647` edge `1.4038` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.358` n `82` status `ready` deltaP `38.0236` edge `1.4234` maxDD `-9.098`
- `news_risk_high->equity_24h` score `10.8483` n `82` status `ready` deltaP `32.2708` edge `0.8669` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.7563` n `82` status `ready` deltaP `56.0429` edge `0.2904` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.1946` n `58` status `ready` deltaP `39.8276` edge `0.2507` maxDD `0.0`
- `risk_on_high->commodity_24h` score `5.843` n `35` status `ready` deltaP `39.8276` edge `0.2214` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.843` n `35` status `ready` deltaP `39.8276` edge `0.2214` maxDD `0.0`
- `risk_on_high->fx_24h` score `5.6034` n `35` status `ready` deltaP `62.1429` edge `0.0569` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.6034` n `35` status `ready` deltaP `62.1429` edge `0.0569` maxDD `-0.0054`
- `news_risk_high->metal_24h` score `5.1754` n `82` status `ready` deltaP `30.45` edge `0.2737` maxDD `-0.6334`
- `market_context_high->fx_24h` score `4.8371` n `58` status `ready` deltaP `54.6552` edge `0.0603` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9403` n `52` status `ready` deltaP `26.2899` edge `0.0214` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9403` n `52` status `ready` deltaP `26.2899` edge `0.0214` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8217` n `127` status `ready` deltaP `22.3378` edge `0.0447` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.6508` n `137` status `ready` deltaP `11.6144` edge `0.0145` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5484` n `82` status `ready` deltaP `14.4817` edge `0.0366` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.2871` n `127` status `ready` deltaP `11.0116` edge `0.011` maxDD `-0.1412`
- `market_context_high->fx_1h` score `0.1735` n `137` status `ready` deltaP `5.6613` edge `0.0025` maxDD `-0.063`
- `risk_on_high->commodity_1h` score `0.1354` n `52` status `ready` deltaP `5.9996` edge `0.0065` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
