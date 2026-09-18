# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T02:37:31.895639+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->unknown_4h` score `35.8766` n `149` status `ready` deltaP `-0.1586` edge `3.0141` maxDD `-0.5326`
- `news_risk_high->unknown_4h` score `21.9362` n `68` status `ready` deltaP `-6.268` edge `1.8967` maxDD `-0.8184`
- `risk_on_high->unknown_4h` score `9.7553` n `52` status `ready` deltaP `-7.3992` edge `0.8848` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.7553` n `52` status `ready` deltaP `-7.3992` edge `0.8848` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `9.0232` n `52` status `ready` deltaP `50.0` edge `0.4186` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.0232` n `52` status `ready` deltaP `50.0` edge `0.4186` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.7241` n `149` status `ready` deltaP `43.2886` edge `0.4076` maxDD `-0.8682`
- `news_risk_high->crypto_alt_24h` score `7.2223` n `40` status `ready` deltaP `28.0903` edge `0.5525` maxDD `-9.3661`
- `news_risk_high->index_24h` score `3.3518` n `40` status `ready` deltaP `24.0625` edge `0.1365` maxDD `-0.075`
- `risk_on_high->commodity_4h` score `3.0197` n `52` status `ready` deltaP `33.3021` edge `0.0646` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0197` n `52` status `ready` deltaP `33.3021` edge `0.0646` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.9194` n `149` status `ready` deltaP `29.8044` edge `0.0864` maxDD `-0.345`
- `news_risk_high->equity_24h` score `2.382` n `40` status `ready` deltaP `2.2222` edge `0.3611` maxDD `-6.5262`
- `risk_on_high->fx_24h` score `1.5684` n `52` status `ready` deltaP `23.945` edge `-0.0247` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.5684` n `52` status `ready` deltaP `23.945` edge `-0.0247` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.4335` n `149` status `ready` deltaP `21.1701` edge `-0.0001` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.2439` n `149` status `ready` deltaP `17.2588` edge `0.0263` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `0.7401` n `68` status `ready` deltaP `9.7292` edge `0.0805` maxDD `-3.3619`
- `risk_on_high->commodity_1h` score `0.6207` n `52` status `ready` deltaP `10.3409` edge `0.018` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6207` n `52` status `ready` deltaP `10.3409` edge `0.018` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
