# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T17:22:30.026534+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8494`

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

- `market_context_high->unknown_4h` score `39.8108` n `149` status `ready` deltaP `-0.6159` edge `3.345` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `20.4226` n `36` status `ready` deltaP `32.6389` edge `1.6222` maxDD `-9.3661`
- `risk_on_high->unknown_4h` score `13.6895` n `52` status `ready` deltaP `-7.8565` edge `1.2157` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.6895` n `52` status `ready` deltaP `-7.8565` edge `1.2157` maxDD `-0.4694`
- `news_risk_high->crypto_major_24h` score `9.323` n `36` status `ready` deltaP `-1.9097` edge `1.3541` maxDD `-9.0221`
- `risk_on_high->commodity_24h` score `8.5937` n `52` status `ready` deltaP `47.9167` edge `0.3967` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5937` n `52` status `ready` deltaP `47.9167` edge `0.3967` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.2946` n `149` status `ready` deltaP `41.2053` edge `0.3857` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.4746` n `92` status `ready` deltaP `22.508` edge `0.5271` maxDD `-7.675`
- `risk_on_high->commodity_4h` score `2.7643` n `52` status `ready` deltaP `32.5399` edge `0.0484` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7643` n `52` status `ready` deltaP `32.5399` edge `0.0484` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.664` n `149` status `ready` deltaP `29.0422` edge `0.0702` maxDD `-0.345`
- `news_risk_high->equity_4h` score `1.3913` n `92` status `ready` deltaP `13.8653` edge `0.1135` maxDD `-4.1995`
- `news_risk_high->crypto_major_4h` score `1.154` n `92` status `ready` deltaP `14.2298` edge `0.297` maxDD `-14.5137`
- `market_context_high->commodity_1h` score `1.1421` n `149` status `ready` deltaP `16.5103` edge `0.0228` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `0.8016` n `92` status `ready` deltaP `12.1778` edge `0.0349` maxDD `-1.6096`
- `risk_on_high->commodity_1h` score `0.5188` n `52` status `ready` deltaP `9.5924` edge `0.0145` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5188` n `52` status `ready` deltaP `9.5924` edge `0.0145` maxDD `-0.1507`
- `risk_on_high->fx_24h` score `0.5059` n `52` status `ready` deltaP `14.7436` edge `-0.0519` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.5059` n `52` status `ready` deltaP `14.7436` edge `-0.0519` maxDD `-0.0054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
