# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T23:22:41.929662+00:00`
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

- `market_context_high->unknown_4h` score `35.7666` n `149` status `ready` deltaP `0.1463` edge `3.0029` maxDD `-0.5326`
- `news_risk_high->unknown_4h` score `18.8915` n `71` status `ready` deltaP `-12.3218` edge `1.7334` maxDD `-4.1571`
- `risk_on_high->unknown_4h` score `9.6452` n `52` status `ready` deltaP `-7.0943` edge `0.8736` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.6452` n `52` status `ready` deltaP `-7.0943` edge `0.8736` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `9.1588` n `52` status `ready` deltaP `50.0` edge `0.4299` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.1588` n `52` status `ready` deltaP `50.0` edge `0.4299` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.5815` n `53` status `ready` deltaP `29.5696` edge `0.6559` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.8597` n `149` status `ready` deltaP `43.2886` edge `0.4189` maxDD `-0.8682`
- `news_risk_high->index_24h` score `4.4518` n `53` status `ready` deltaP `30.8078` edge `0.1832` maxDD `-0.075`
- `news_risk_high->equity_24h` score `3.4993` n `53` status `ready` deltaP `16.326` edge `0.5172` maxDD `-6.5262`
- `news_risk_high->crypto_major_24h` score `3.1762` n `53` status `ready` deltaP `9.66` edge `0.5423` maxDD `-13.2931`
- `risk_on_high->commodity_4h` score `3.0705` n `52` status `ready` deltaP `33.6069` edge `0.0668` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0705` n `52` status `ready` deltaP `33.6069` edge `0.0668` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.9702` n `149` status `ready` deltaP `30.1092` edge `0.0886` maxDD `-0.345`
- `risk_on_high->fx_24h` score `1.8137` n `52` status `ready` deltaP `26.2019` edge `-0.0193` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.8137` n `52` status `ready` deltaP `26.2019` edge `-0.0193` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.6789` n `149` status `ready` deltaP `23.427` edge `0.0053` maxDD `-0.0593`
- `news_risk_high->metal_24h` score `1.4294` n `53` status `ready` deltaP `16.1066` edge `0.1213` maxDD `-0.6334`
- `market_context_high->commodity_1h` score `1.2667` n `149` status `ready` deltaP `17.4085` edge `0.0272` maxDD `-0.3491`
- `news_risk_high->index_4h` score `1.1031` n `71` status `ready` deltaP `16.5321` edge `0.0283` maxDD `-0.3938`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
