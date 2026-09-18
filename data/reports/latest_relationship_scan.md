# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T17:37:32.916900+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8278`

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

- `market_context_high->unknown_4h` score `39.585` n `149` status `ready` deltaP `-0.7683` edge `3.3272` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `20.8457` n `35` status `ready` deltaP `32.2421` edge `1.6601` maxDD `-9.3661`
- `risk_on_high->unknown_4h` score `13.4637` n `52` status `ready` deltaP `-8.0089` edge `1.1979` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.4637` n `52` status `ready` deltaP `-8.0089` edge `1.1979` maxDD `-0.4694`
- `news_risk_high->crypto_major_24h` score `9.7908` n `35` status `ready` deltaP `-0.5754` edge `1.4001` maxDD `-8.6161`
- `risk_on_high->commodity_24h` score `8.5949` n `52` status `ready` deltaP `47.9167` edge `0.3968` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5949` n `52` status `ready` deltaP `47.9167` edge `0.3968` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.2958` n `149` status `ready` deltaP `41.2053` edge `0.3858` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.7259` n `91` status `ready` deltaP `23.2394` edge `0.539` maxDD `-7.675`
- `risk_on_high->commodity_4h` score `2.7801` n `52` status `ready` deltaP `32.6923` edge `0.0487` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7801` n `52` status `ready` deltaP `32.6923` edge `0.0487` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.6798` n `149` status `ready` deltaP `29.1946` edge `0.0705` maxDD `-0.345`
- `news_risk_high->equity_4h` score `1.4746` n `91` status `ready` deltaP `14.4415` edge `0.1166` maxDD `-4.1995`
- `news_risk_high->crypto_major_4h` score `1.2949` n `91` status `ready` deltaP `14.8419` edge `0.3019` maxDD `-14.12`
- `market_context_high->commodity_1h` score `1.1397` n `149` status `ready` deltaP `16.5103` edge `0.0226` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `0.741` n `91` status `ready` deltaP `11.7359` edge `0.0328` maxDD `-1.6096`
- `risk_on_high->commodity_1h` score `0.5164` n `52` status `ready` deltaP `9.5924` edge `0.0143` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5164` n `52` status `ready` deltaP `9.5924` edge `0.0143` maxDD `-0.1507`
- `risk_on_high->fx_24h` score `0.4884` n `52` status `ready` deltaP `14.57` edge `-0.0522` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.4884` n `52` status `ready` deltaP `14.57` edge `-0.0522` maxDD `-0.0054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
