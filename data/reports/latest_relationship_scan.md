# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T18:07:35.266670+00:00`
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

- `market_context_high->unknown_4h` score `39.5814` n `149` status `ready` deltaP `-0.7683` edge `3.3269` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `23.7586` n `36` status `ready` deltaP `32.6389` edge `1.9002` maxDD `-9.3661`
- `risk_on_high->unknown_4h` score `13.4601` n `52` status `ready` deltaP `-8.0089` edge `1.1976` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.4601` n `52` status `ready` deltaP `-8.0089` edge `1.1976` maxDD `-0.4694`
- `news_risk_high->crypto_major_24h` score `12.4578` n `36` status `ready` deltaP `3.125` edge `1.7081` maxDD `-7.8757`
- `risk_on_high->commodity_24h` score `8.5961` n `52` status `ready` deltaP `47.9167` edge `0.3969` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5961` n `52` status `ready` deltaP `47.9167` edge `0.3969` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.297` n `149` status `ready` deltaP `41.2053` edge `0.3859` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `7.0098` n `90` status `ready` deltaP `23.8381` edge `0.5545` maxDD `-7.675`
- `risk_on_high->commodity_4h` score `2.7885` n `52` status `ready` deltaP `32.6923` edge `0.0494` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7885` n `52` status `ready` deltaP `32.6923` edge `0.0494` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.6882` n `149` status `ready` deltaP `29.1946` edge `0.0712` maxDD `-0.345`
- `news_risk_high->equity_4h` score `1.5326` n `90` status `ready` deltaP `14.8815` edge `0.1185` maxDD `-4.1995`
- `news_risk_high->crypto_major_4h` score `1.5259` n `90` status `ready` deltaP `15.3184` edge `0.3119` maxDD `-13.1382`
- `market_context_high->commodity_1h` score `1.1265` n `149` status `ready` deltaP `16.3606` edge `0.0225` maxDD `-0.3491`
- `news_risk_high->equity_24h` score `0.8564` n `36` status `ready` deltaP `6.25` edge `0.2061` maxDD `-5.0382`
- `risk_on_high->commodity_1h` score `0.5032` n `52` status `ready` deltaP `9.4427` edge `0.0142` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5032` n `52` status `ready` deltaP `9.4427` edge `0.0142` maxDD `-0.1507`
- `risk_on_high->fx_24h` score `0.451` n `52` status `ready` deltaP `14.2227` edge `-0.053` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.451` n `52` status `ready` deltaP `14.2227` edge `-0.053` maxDD `-0.0054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
