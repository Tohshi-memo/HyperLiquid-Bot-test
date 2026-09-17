# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T23:07:30.304563+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8684`

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

- `news_risk_high->unknown_4h` score `242.1515` n `71` status `ready` deltaP `-12.3218` edge `20.3384` maxDD `-4.1571`
- `risk_on_high->commodity_24h` score `9.172` n `52` status `ready` deltaP `50.0` edge `0.431` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.172` n `52` status `ready` deltaP `50.0` edge `0.431` maxDD `0.0`
- `market_context_high->unknown_4h` score `8.6694` n `149` status `ready` deltaP `0.1463` edge `0.7448` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `8.3611` n `54` status `ready` deltaP `28.2407` edge `0.6464` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.8729` n `149` status `ready` deltaP `43.2886` edge `0.42` maxDD `-0.8682`
- `news_risk_high->index_24h` score `4.5125` n `54` status `ready` deltaP `31.1921` edge `0.1857` maxDD `-0.075`
- `news_risk_high->equity_24h` score `3.5941` n `54` status `ready` deltaP `17.1296` edge `0.524` maxDD `-6.5262`
- `news_risk_high->crypto_major_24h` score `3.2827` n `54` status `ready` deltaP `10.3588` edge `0.5513` maxDD `-13.2931`
- `risk_on_high->commodity_4h` score `3.0741` n `52` status `ready` deltaP `33.6069` edge `0.0671` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0741` n `52` status `ready` deltaP `33.6069` edge `0.0671` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.9738` n `149` status `ready` deltaP `30.1092` edge `0.0889` maxDD `-0.345`
- `risk_on_high->fx_24h` score `1.8185` n `52` status `ready` deltaP `26.2019` edge `-0.0189` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.8185` n `52` status `ready` deltaP `26.2019` edge `-0.0189` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.6837` n `149` status `ready` deltaP `23.427` edge `0.0057` maxDD `-0.0593`
- `news_risk_high->metal_24h` score `1.4925` n `54` status `ready` deltaP `16.8403` edge `0.1245` maxDD `-0.6334`
- `market_context_high->commodity_1h` score `1.2667` n `149` status `ready` deltaP `17.4085` edge `0.0272` maxDD `-0.3491`
- `news_risk_high->index_4h` score `1.2132` n `71` status `ready` deltaP `17.7881` edge `0.0291` maxDD `-0.3938`
- `risk_on_high->commodity_1h` score `0.6434` n `52` status `ready` deltaP `10.4906` edge `0.0189` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6434` n `52` status `ready` deltaP `10.4906` edge `0.0189` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
