# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T16:52:40.278761+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8456`

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

- `market_context_high->unknown_4h` score `39.8626` n `149` status `ready` deltaP `-0.4634` edge `3.3483` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `19.4309` n `35` status `ready` deltaP `32.2421` edge `1.5422` maxDD `-9.3661`
- `risk_on_high->unknown_4h` score `13.7413` n `52` status `ready` deltaP `-7.704` edge `1.219` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.7413` n `52` status `ready` deltaP `-7.704` edge `1.219` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.5937` n `52` status `ready` deltaP `47.9167` edge `0.3967` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5937` n `52` status `ready` deltaP `47.9167` edge `0.3967` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `8.4706` n `35` status `ready` deltaP `-2.9117` edge `1.2515` maxDD `-9.0221`
- `market_context_high->commodity_24h` score `7.2946` n `149` status `ready` deltaP `41.2053` edge `0.3857` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.5722` n `92` status `ready` deltaP `22.8128` edge `0.5332` maxDD `-7.675`
- `risk_on_high->commodity_4h` score `2.7473` n `52` status `ready` deltaP `32.3874` edge `0.048` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7473` n `52` status `ready` deltaP `32.3874` edge `0.048` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.647` n `149` status `ready` deltaP `28.8897` edge `0.0698` maxDD `-0.345`
- `news_risk_high->equity_4h` score `1.4313` n `92` status `ready` deltaP `14.1702` edge `0.1148` maxDD `-4.1995`
- `news_risk_high->crypto_major_4h` score `1.2431` n `92` status `ready` deltaP `14.5347` edge `0.3064` maxDD `-14.5137`
- `market_context_high->commodity_1h` score `1.1385` n `149` status `ready` deltaP `16.5103` edge `0.0225` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `0.8148` n `92` status `ready` deltaP `12.3275` edge `0.035` maxDD `-1.6096`
- `risk_on_high->fx_24h` score `0.5421` n `52` status `ready` deltaP `15.0908` edge `-0.0512` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.5421` n `52` status `ready` deltaP `15.0908` edge `-0.0512` maxDD `-0.0054`
- `risk_on_high->commodity_1h` score `0.5152` n `52` status `ready` deltaP `9.5924` edge `0.0142` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5152` n `52` status `ready` deltaP `9.5924` edge `0.0142` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
