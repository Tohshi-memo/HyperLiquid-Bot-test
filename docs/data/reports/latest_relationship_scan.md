# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T21:07:31.565888+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8884`

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

- `news_risk_high->unknown_4h` score `459.4977` n `72` status `ready` deltaP `-12.0088` edge `38.4485` maxDD `-4.1571`
- `risk_on_high->commodity_24h` score `9.2668` n `52` status `ready` deltaP `50.0` edge `0.4389` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.2668` n `52` status `ready` deltaP `50.0` edge `0.4389` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.1707` n `62` status `ready` deltaP `27.9906` edge `0.6322` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.9677` n `149` status `ready` deltaP `43.2886` edge `0.4279` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `6.5967` n `62` status `ready` deltaP `22.6254` edge `0.5763` maxDD `-6.5262`
- `news_risk_high->index_24h` score `4.9316` n `62` status `ready` deltaP `33.8206` edge `0.2031` maxDD `-0.075`
- `news_risk_high->crypto_major_24h` score `4.2824` n `62` status `ready` deltaP `15.1377` edge `0.6476` maxDD `-13.2931`
- `risk_on_high->commodity_4h` score `3.0813` n `52` status `ready` deltaP `33.6069` edge `0.0677` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0813` n `52` status `ready` deltaP `33.6069` edge `0.0677` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.981` n `149` status `ready` deltaP `30.1092` edge `0.0895` maxDD `-0.345`
- `news_risk_high->metal_24h` score `2.9808` n `62` status `ready` deltaP `21.8582` edge `0.1481` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `1.8739` n `52` status `ready` deltaP `26.5491` edge `-0.0166` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.8739` n `52` status `ready` deltaP `26.5491` edge `-0.0166` maxDD `-0.0054`
- `news_risk_high->index_4h` score `1.8647` n `72` status `ready` deltaP `25.4065` edge `0.0326` maxDD `-0.3938`
- `market_context_high->fx_24h` score `1.739` n `149` status `ready` deltaP `23.7742` edge `0.008` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.2535` n `149` status `ready` deltaP `17.2588` edge `0.0271` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.6303` n `52` status `ready` deltaP `10.3409` edge `0.0188` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6303` n `52` status `ready` deltaP `10.3409` edge `0.0188` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2143` n `149` status `ready` deltaP `10.4957` edge `0.0051` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
