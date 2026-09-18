# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T03:07:32.030458+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8568`

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

- `market_context_high->unknown_4h` score `36.8224` n `149` status `ready` deltaP `-0.0061` edge `3.0919` maxDD `-0.5326`
- `news_risk_high->unknown_4h` score `13.7342` n `68` status `ready` deltaP `-7.5861` edge `1.2233` maxDD `-0.9232`
- `risk_on_high->unknown_4h` score `10.7011` n `52` status `ready` deltaP `-7.2467` edge `0.9626` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `10.7011` n `52` status `ready` deltaP `-7.2467` edge `0.9626` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `9.0064` n `52` status `ready` deltaP `50.0` edge `0.4172` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.0064` n `52` status `ready` deltaP `50.0` edge `0.4172` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.7073` n `149` status `ready` deltaP `43.2886` edge `0.4062` maxDD `-0.8682`
- `news_risk_high->crypto_alt_24h` score `6.5237` n `38` status `ready` deltaP `27.0377` edge `0.5013` maxDD `-9.3661`
- `news_risk_high->index_24h` score `3.1196` n `38` status `ready` deltaP `22.6151` edge `0.1268` maxDD `-0.075`
- `risk_on_high->commodity_4h` score `3.0077` n `52` status `ready` deltaP `33.3021` edge `0.0636` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0077` n `52` status `ready` deltaP `33.3021` edge `0.0636` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.9074` n `149` status `ready` deltaP `29.8044` edge `0.0854` maxDD `-0.345`
- `news_risk_high->equity_24h` score `1.7367` n `38` status `ready` deltaP `-0.8041` edge `0.3275` maxDD `-6.5262`
- `risk_on_high->fx_24h` score `1.5298` n `52` status `ready` deltaP `23.5977` edge `-0.0256` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.5298` n `52` status `ready` deltaP `23.5977` edge `-0.0256` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.3949` n `149` status `ready` deltaP `20.8228` edge `-0.001` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.2308` n `149` status `ready` deltaP `17.1091` edge `0.0262` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `0.6753` n `68` status `ready` deltaP `9.7292` edge `0.0751` maxDD `-3.3619`
- `risk_on_high->commodity_1h` score `0.6075` n `52` status `ready` deltaP `10.1912` edge `0.0179` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6075` n `52` status `ready` deltaP `10.1912` edge `0.0179` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
