# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T21:22:28.809482+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8194`

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

- `news_risk_high->crypto_major_24h` score `39.2333` n `39` status `ready` deltaP `17.9354` edge `3.2474` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `38.6293` n `39` status `ready` deltaP `33.7073` edge `3.1323` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `37.7824` n `149` status `ready` deltaP `-0.9208` edge `3.178` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `11.6611` n `52` status `ready` deltaP `-8.1614` edge `1.0487` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.6611` n `52` status `ready` deltaP `-8.1614` edge `1.0487` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.6068` n `83` status `ready` deltaP `28.7907` edge `0.6379` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.5841` n `52` status `ready` deltaP `47.9167` edge `0.3959` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5841` n `52` status `ready` deltaP `47.9167` edge `0.3959` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.285` n `149` status `ready` deltaP `41.2053` edge `0.3849` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `6.7984` n `39` status `ready` deltaP `25.788` edge `0.4772` maxDD `-2.9402`
- `risk_on_high->commodity_4h` score `2.8429` n `52` status `ready` deltaP `32.9972` edge `0.0519` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8429` n `52` status `ready` deltaP `32.9972` edge `0.0519` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7426` n `149` status `ready` deltaP `29.4995` edge `0.0737` maxDD `-0.345`
- `news_risk_high->crypto_major_4h` score `2.7345` n `83` status `ready` deltaP `19.334` edge `0.3667` maxDD `-9.6016`
- `news_risk_high->metal_24h` score `1.9892` n `39` status `ready` deltaP `15.2778` edge `0.0922` maxDD `-0.2629`
- `news_risk_high->equity_4h` score `1.8492` n `83` status `ready` deltaP `16.6636` edge `0.133` maxDD `-4.1995`
- `news_risk_high->crypto_alt_1h` score `1.7364` n `83` status `ready` deltaP `12.0807` edge `0.1406` maxDD `-3.4483`
- `market_context_high->commodity_1h` score `1.1481` n `149` status `ready` deltaP `16.5103` edge `0.0233` maxDD `-0.3491`
- `news_risk_high->fx_4h` score `1.0861` n `83` status `ready` deltaP `12.2575` edge `0.0313` maxDD `-0.134`
- `news_risk_high->equity_1h` score `1.0048` n `83` status `ready` deltaP `12.344` edge `0.042` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
