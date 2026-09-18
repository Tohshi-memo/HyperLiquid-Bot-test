# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T19:22:27.976395+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8296`

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

- `market_context_high->unknown_4h` score `38.8936` n `149` status `ready` deltaP `-0.9208` edge `3.2706` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `32.4562` n `36` status `ready` deltaP `32.6389` edge `2.625` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `20.2715` n `36` status `ready` deltaP `10.9375` edge `2.6419` maxDD `-6.6058`
- `risk_on_high->unknown_4h` score `12.7723` n `52` status `ready` deltaP `-8.1614` edge `1.1413` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `12.7723` n `52` status `ready` deltaP `-8.1614` edge `1.1413` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.6033` n `52` status `ready` deltaP `47.9167` edge `0.3975` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.6033` n `52` status `ready` deltaP `47.9167` edge `0.3975` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.4106` n `85` status `ready` deltaP `27.9125` edge `0.6274` maxDD `-7.675`
- `market_context_high->commodity_24h` score `7.3042` n `149` status `ready` deltaP `41.2053` edge `0.3865` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `4.6838` n `36` status `ready` deltaP `19.2708` edge `0.3588` maxDD `-3.4232`
- `risk_on_high->commodity_4h` score `2.8357` n `52` status `ready` deltaP `32.9972` edge `0.0513` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8357` n `52` status `ready` deltaP `32.9972` edge `0.0513` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7354` n `149` status `ready` deltaP `29.4995` edge `0.0731` maxDD `-0.345`
- `news_risk_high->crypto_major_4h` score `2.4219` n `85` status `ready` deltaP `18.7392` edge `0.3553` maxDD `-10.9113`
- `news_risk_high->equity_4h` score `2.051` n `85` status `ready` deltaP `18.1062` edge `0.1402` maxDD `-4.1995`
- `market_context_high->commodity_1h` score `1.1768` n `149` status `ready` deltaP `16.8097` edge `0.0237` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `1.1517` n `85` status `ready` deltaP `13.8499` edge `0.0442` maxDD `-0.9112`
- `news_risk_high->crypto_alt_1h` score `1.0645` n `85` status `ready` deltaP `11.969` edge `0.1354` maxDD `-3.6312`
- `news_risk_high->fx_4h` score `0.9806` n `85` status `ready` deltaP `11.8329` edge `0.0303` maxDD `-0.1976`
- `news_risk_high->metal_24h` score `0.9207` n `36` status `ready` deltaP `7.2916` edge `0.0564` maxDD `-0.2629`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
