# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T05:37:29.435463+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11652`

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

- `news_risk_high->unknown_1h` score `443.7016` n `82` status `ready` deltaP `-5.8493` edge `37.0563` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.8287` n `82` status `ready` deltaP `39.4785` edge `1.438` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.073` n `82` status `ready` deltaP `37.1615` edge `1.4054` maxDD `-9.098`
- `news_risk_high->equity_24h` score `11.702` n `82` status `ready` deltaP `34.857` edge `0.9208` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.1144` n `82` status `ready` deltaP `58.6291` edge `0.303` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.749` n `73` status `ready` deltaP `39.8276` edge `0.2969` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.2618` n `41` status `ready` deltaP `39.8276` edge `0.2563` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2618` n `41` status `ready` deltaP `39.8276` edge `0.2563` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.5179` n `82` status `ready` deltaP `33.0362` edge `0.285` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `5.4096` n `41` status `ready` deltaP `59.9748` edge `0.0552` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.4096` n `41` status `ready` deltaP `59.9748` edge `0.0552` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.7547` n `73` status `ready` deltaP `54.1946` edge `0.0565` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.0035` n `52` status `ready` deltaP `26.8996` edge `0.0226` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0035` n `52` status `ready` deltaP `26.8996` edge `0.0226` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8038` n `137` status `ready` deltaP `22.3095` edge `0.0434` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7526` n `137` status `ready` deltaP `12.6623` edge `0.016` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5935` n `82` status `ready` deltaP `15.2439` edge `0.0373` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3348` n `137` status `ready` deltaP `11.9881` edge `0.0106` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.2372` n `52` status `ready` deltaP `7.0475` edge `0.008` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2372` n `52` status `ready` deltaP `7.0475` edge `0.008` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
