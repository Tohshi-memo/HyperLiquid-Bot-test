# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T20:18:14.165262+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8290`

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

- `market_context_high->unknown_4h` score `37.7824` n `149` status `ready` deltaP `-0.9208` edge `3.178` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `36.3173` n `40` status `ready` deltaP `34.0278` edge `2.9375` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `35.932` n `40` status `ready` deltaP `14.2708` edge `3.0151` maxDD `-6.6058`
- `risk_on_high->unknown_4h` score `11.6611` n `52` status `ready` deltaP `-8.1614` edge `1.0487` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.6611` n `52` status `ready` deltaP `-8.1614` edge `1.0487` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.5925` n `52` status `ready` deltaP `47.9167` edge `0.3966` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5925` n `52` status `ready` deltaP `47.9167` edge `0.3966` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.2646` n `85` status `ready` deltaP `27.3027` edge `0.6193` maxDD `-7.675`
- `market_context_high->commodity_24h` score `7.2934` n `149` status `ready` deltaP `41.2053` edge `0.3856` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `5.7679` n `40` status `ready` deltaP `22.1875` edge `0.4297` maxDD `-3.4232`
- `risk_on_high->commodity_4h` score `2.8465` n `52` status `ready` deltaP `32.9972` edge `0.0522` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8465` n `52` status `ready` deltaP `32.9972` edge `0.0522` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7462` n `149` status `ready` deltaP `29.4995` edge `0.074` maxDD `-0.345`
- `news_risk_high->crypto_major_4h` score `2.3255` n `85` status `ready` deltaP `18.1295` edge `0.347` maxDD `-10.9113`
- `news_risk_high->equity_4h` score `1.9434` n `85` status `ready` deltaP `17.4964` edge `0.1353` maxDD `-4.1995`
- `news_risk_high->metal_24h` score `1.554` n `40` status `ready` deltaP `11.4583` edge `0.0814` maxDD `-0.2629`
- `market_context_high->commodity_1h` score `1.1529` n `149` status `ready` deltaP `16.5103` edge `0.0237` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `1.075` n `85` status `ready` deltaP `13.2511` edge `0.0418` maxDD `-0.9112`
- `news_risk_high->crypto_alt_1h` score `1.0582` n `85` status `ready` deltaP `11.8193` edge `0.1356` maxDD `-3.6312`
- `news_risk_high->fx_4h` score `0.9294` n `85` status `ready` deltaP `11.2231` edge `0.0301` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
