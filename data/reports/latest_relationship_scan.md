# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T19:07:34.386401+00:00`
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

- `market_context_high->unknown_4h` score `38.9428` n `149` status `ready` deltaP `-0.9208` edge `3.2747` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `30.631` n `36` status `ready` deltaP `32.6389` edge `2.4729` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `18.7833` n `36` status `ready` deltaP `10.9375` edge `2.4511` maxDD `-6.6058`
- `risk_on_high->unknown_4h` score `12.8215` n `52` status `ready` deltaP `-8.1614` edge `1.1454` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `12.8215` n `52` status `ready` deltaP `-8.1614` edge `1.1454` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.6045` n `52` status `ready` deltaP `47.9167` edge `0.3976` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.6045` n `52` status `ready` deltaP `47.9167` edge `0.3976` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.181` n `86` status `ready` deltaP `27.0526` edge `0.614` maxDD `-7.675`
- `market_context_high->commodity_24h` score `7.3054` n `149` status `ready` deltaP `41.2053` edge `0.3866` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `4.0085` n `36` status `ready` deltaP `16.6667` edge `0.3264` maxDD `-3.6111`
- `risk_on_high->commodity_4h` score `2.8321` n `52` status `ready` deltaP `32.9972` edge `0.051` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8321` n `52` status `ready` deltaP `32.9972` edge `0.051` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7318` n `149` status `ready` deltaP `29.4995` edge `0.0728` maxDD `-0.345`
- `news_risk_high->crypto_major_4h` score `2.2809` n `86` status `ready` deltaP `18.0162` edge `0.3489` maxDD `-11.1265`
- `news_risk_high->equity_4h` score `1.9628` n `86` status `ready` deltaP `17.4241` edge `0.1374` maxDD `-4.1995`
- `market_context_high->commodity_1h` score `1.1624` n `149` status `ready` deltaP `16.66` edge `0.0235` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `1.0817` n `86` status `ready` deltaP `13.2746` edge `0.0422` maxDD `-0.9112`
- `news_risk_high->crypto_alt_1h` score `0.9495` n `86` status `ready` deltaP `11.339` edge `0.13` maxDD `-4.0426`
- `news_risk_high->fx_4h` score `0.8587` n `86` status `ready` deltaP `11.0395` edge `0.0297` maxDD `-0.2057`
- `news_risk_high->metal_24h` score `0.8115` n `36` status `ready` deltaP `7.2916` edge `0.0473` maxDD `-0.2629`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
