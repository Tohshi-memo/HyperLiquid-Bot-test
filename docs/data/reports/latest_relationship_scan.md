# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T23:37:29.733770+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8098`

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

- `news_risk_high->crypto_major_24h` score `58.6092` n `39` status `ready` deltaP `32.2783` edge `4.7581` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `53.6857` n `39` status `ready` deltaP `33.7073` edge `4.387` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `37.8843` n `149` status `ready` deltaP `-1.0732` edge `3.1875` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `13.4771` n `39` status `ready` deltaP `47.3024` edge `0.8225` maxDD `-0.5137`
- `risk_on_high->unknown_4h` score `11.7629` n `52` status `ready` deltaP `-8.3138` edge `1.0582` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.7629` n `52` status `ready` deltaP `-8.3138` edge `1.0582` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.9932` n `74` status `ready` deltaP `28.6709` edge `0.6709` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.5666` n `52` status `ready` deltaP `47.7431` edge `0.3956` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5666` n `52` status `ready` deltaP `47.7431` edge `0.3956` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.2675` n `149` status `ready` deltaP `41.0317` edge `0.3846` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `6.0236` n `74` status `ready` deltaP `25.2472` edge `0.4511` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.4607` n `39` status `ready` deltaP `32.0112` edge `0.1741` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.2926` n `74` status `ready` deltaP `18.1866` edge `0.1997` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.929` n `74` status `ready` deltaP `22.2407` edge `0.1481` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.7979` n `52` status `ready` deltaP `32.5399` edge `0.0512` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7979` n `52` status `ready` deltaP `32.5399` edge `0.0512` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.6976` n `149` status `ready` deltaP `29.0422` edge `0.073` maxDD `-0.345`
- `news_risk_high->equity_4h` score `1.5834` n `74` status `ready` deltaP `13.1469` edge `0.1343` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.442` n `74` status `ready` deltaP `15.7877` edge `0.0368` maxDD `-0.084`
- `news_risk_high->fx_24h` score `1.3289` n `39` status `ready` deltaP `4.6341` edge `0.0885` maxDD `-0.0255`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
