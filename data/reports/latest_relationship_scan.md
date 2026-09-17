# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T12:52:29.443886+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8658`

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

- `news_risk_high->unknown_4h` score `384.4384` n `83` status `ready` deltaP `-22.4251` edge `32.2755` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `12.3543` n `83` status `ready` deltaP `31.5805` edge `0.9569` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `11.9334` n `83` status `ready` deltaP `23.6467` edge `1.0363` maxDD `-13.2931`
- `risk_on_high->commodity_24h` score `9.2908` n `52` status `ready` deltaP `50.0` edge `0.4409` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.2908` n `52` status `ready` deltaP `50.0` edge `0.4409` maxDD `0.0`
- `news_risk_high->equity_24h` score `8.5666` n `83` status `ready` deltaP `32.8795` edge `0.6721` maxDD `-6.5262`
- `market_context_high->commodity_24h` score `7.9917` n `149` status `ready` deltaP `43.2886` edge `0.4299` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.6783` n `83` status `ready` deltaP `38.3095` edge `0.2354` maxDD `-0.075`
- `news_risk_high->metal_24h` score `3.8941` n `83` status `ready` deltaP `30.9488` edge `0.1636` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.7743` n `52` status `ready` deltaP `31.9301` edge `0.0533` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7743` n `52` status `ready` deltaP `31.9301` edge `0.0533` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.674` n `149` status `ready` deltaP `28.4324` edge `0.0751` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.378` n `52` status `ready` deltaP `31.4102` edge `-0.007` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.378` n `52` status `ready` deltaP `31.4102` edge `-0.007` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2431` n `149` status `ready` deltaP `28.6353` edge `0.0176` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.1696` n `149` status `ready` deltaP `16.66` edge `0.0241` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.5464` n `52` status `ready` deltaP `9.7421` edge `0.0158` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5464` n `52` status `ready` deltaP `9.7421` edge `0.0158` maxDD `-0.1507`
- `news_risk_high->index_4h` score `0.127` n `83` status `ready` deltaP `8.6872` edge `0.0212` maxDD `-0.6935`
- `market_context_high->fx_1h` score `0.0883` n `149` status `ready` deltaP `5.2506` edge `0.0021` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
