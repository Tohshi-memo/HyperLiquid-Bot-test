# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T14:37:27.785949+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8594`

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

- `news_risk_high->crypto_major_24h` score `52.5245` n `72` status `ready` deltaP `31.25` edge `4.2579` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `46.0778` n `72` status `ready` deltaP `35.7639` edge `3.7393` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `39.0711` n `140` status `ready` deltaP `-2.4826` edge `3.2958` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `10.1155` n `72` status `ready` deltaP `40.7986` edge `0.5752` maxDD `-0.0053`
- `risk_on_high->unknown_4h` score `10.0205` n `50` status `ready` deltaP `-9.7683` edge `0.9227` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `10.0205` n `50` status `ready` deltaP `-9.7683` edge `0.9227` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.4596` n `50` status `ready` deltaP `46.1806` edge `0.3971` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.4596` n `50` status `ready` deltaP `46.1806` edge `0.3971` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.2076` n `140` status `ready` deltaP `39.0377` edge `0.3929` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.6145` n `91` status `ready` deltaP `25.1324` edge `0.5046` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.5619` n `91` status `ready` deltaP `21.6514` edge `0.3616` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.2795` n `98` status `ready` deltaP `19.0731` edge `0.1927` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.5981` n `50` status `ready` deltaP `30.628` edge `0.0473` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.5981` n `50` status `ready` deltaP `30.628` edge `0.0473` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5154` n `140` status `ready` deltaP `27.1994` edge `0.0701` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.4749` n `98` status `ready` deltaP `20.8695` edge `0.1194` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.8298` n `72` status `ready` deltaP `23.6111` edge `0.0795` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.2046` n `140` status `ready` deltaP `16.0265` edge `0.0229` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.7702` n `50` status `ready` deltaP `11.4551` edge `0.0147` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.7702` n `50` status `ready` deltaP `11.4551` edge `0.0147` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
