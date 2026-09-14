# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T05:52:27.905127+00:00`
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

- `news_risk_high->unknown_1h` score `443.5912` n `82` status `ready` deltaP `-5.8493` edge `37.0471` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.8773` n `82` status `ready` deltaP `39.6509` edge `1.4409` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.061` n `82` status `ready` deltaP `37.1615` edge `1.4044` maxDD `-9.098`
- `news_risk_high->equity_24h` score `11.7602` n `82` status `ready` deltaP `35.0294` edge `0.9245` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.139` n `82` status `ready` deltaP `58.8015` edge `0.3039` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `6.7574` n `74` status `ready` deltaP `39.8276` edge `0.2976` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.2534` n `41` status `ready` deltaP `39.8276` edge `0.2556` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2534` n `41` status `ready` deltaP `39.8276` edge `0.2556` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.5449` n `82` status `ready` deltaP `33.2086` edge `0.2861` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `5.3886` n `41` status `ready` deltaP `59.8024` edge `0.0546` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.3886` n `41` status `ready` deltaP `59.8024` edge `0.0546` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.7462` n `74` status `ready` deltaP `54.1333` edge `0.0562` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.0011` n `52` status `ready` deltaP `26.8996` edge `0.0224` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0011` n `52` status `ready` deltaP `26.8996` edge `0.0224` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8014` n `137` status `ready` deltaP `22.3095` edge `0.0432` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7658` n `137` status `ready` deltaP `12.812` edge `0.0161` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6022` n `82` status `ready` deltaP `15.3963` edge `0.0374` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3325` n `137` status `ready` deltaP `11.9881` edge `0.0103` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.2504` n `52` status `ready` deltaP `7.1972` edge `0.0081` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2504` n `52` status `ready` deltaP `7.1972` edge `0.0081` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
