# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T03:22:28.621612+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8580`

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

- `market_context_high->unknown_4h` score `37.2868` n `149` status `ready` deltaP `-0.0061` edge `3.1306` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `11.1655` n `52` status `ready` deltaP `-7.2467` edge `1.0013` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.1655` n `52` status `ready` deltaP `-7.2467` edge `1.0013` maxDD `-0.4694`
- `news_risk_high->unknown_4h` score `9.7262` n `68` status `ready` deltaP `-7.5861` edge `0.8893` maxDD `-0.9232`
- `risk_on_high->commodity_24h` score `8.9992` n `52` status `ready` deltaP `50.0` edge `0.4166` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.9992` n `52` status `ready` deltaP `50.0` edge `0.4166` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.7001` n `149` status `ready` deltaP `43.2886` edge `0.4056` maxDD `-0.8682`
- `news_risk_high->crypto_alt_24h` score `6.0522` n `37` status `ready` deltaP `26.4687` edge `0.4658` maxDD `-9.3661`
- `risk_on_high->commodity_4h` score `3.0041` n `52` status `ready` deltaP `33.3021` edge `0.0633` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0041` n `52` status `ready` deltaP `33.3021` edge `0.0633` maxDD `-0.1313`
- `news_risk_high->index_24h` score `2.9994` n `37` status `ready` deltaP `21.8328` edge `0.122` maxDD `-0.075`
- `market_context_high->commodity_4h` score `2.9038` n `149` status `ready` deltaP `29.8044` edge `0.0851` maxDD `-0.345`
- `risk_on_high->fx_24h` score `1.5087` n `52` status `ready` deltaP `23.4241` edge `-0.0262` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.5087` n `52` status `ready` deltaP `23.4241` edge `-0.0262` maxDD `-0.0054`
- `news_risk_high->equity_24h` score `1.3827` n `37` status `ready` deltaP `-2.44` edge `0.3089` maxDD `-6.5262`
- `market_context_high->fx_24h` score `1.3738` n `149` status `ready` deltaP `20.6492` edge `-0.0016` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.2451` n `149` status `ready` deltaP `17.2588` edge `0.0264` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `0.6549` n `68` status `ready` deltaP `9.7292` edge `0.0734` maxDD `-3.3619`
- `risk_on_high->commodity_1h` score `0.6219` n `52` status `ready` deltaP `10.3409` edge `0.0181` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6219` n `52` status `ready` deltaP `10.3409` edge `0.0181` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
