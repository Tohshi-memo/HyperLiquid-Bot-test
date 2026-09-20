# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T00:52:26.454846+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9064`

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

- `news_risk_high->crypto_major_24h` score `50.8422` n `72` status `ready` deltaP `26.7361` edge `4.1478` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `44.0005` n `72` status `ready` deltaP `32.1181` edge `3.5905` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `17.5743` n `101` status `ready` deltaP `-5.7821` edge `1.5264` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `8.3488` n `72` status `ready` deltaP `36.8055` edge `0.4546` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.9097` n `99` status `ready` deltaP `39.2046` edge `0.4503` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.9966` n `98` status `ready` deltaP `22.8378` edge `0.4684` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6766` n `98` status `ready` deltaP `23.2951` edge `0.3602` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.7646` n `101` status `ready` deltaP `34.3863` edge `0.0978` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.2245` n `98` status `ready` deltaP `18.3246` edge `0.1931` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.4451` n `98` status `ready` deltaP `20.121` edge `0.1219` maxDD `-2.8494`
- `market_context_high->commodity_1h` score `1.7059` n `101` status `ready` deltaP `20.423` edge `0.0312` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.6635` n `72` status `ready` deltaP `22.2222` edge `0.0749` maxDD `-2.4203`
- `market_context_high->fx_4h` score `1.1344` n `101` status `ready` deltaP `20.9007` edge `0.002` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.8077` n `98` status `ready` deltaP `18.9771` edge `0.0462` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.7063` n `98` status `ready` deltaP `15.4558` edge `0.016` maxDD `-0.8144`
- `news_risk_high->fx_24h` score `0.701` n `72` status `ready` deltaP `5.2084` edge `0.0419` maxDD `-0.1231`
- `market_context_high->fx_24h` score `0.601` n `99` status `ready` deltaP `11.1427` edge `-0.02` maxDD `-0.0027`
- `news_risk_high->equity_1h` score `0.4162` n `98` status `ready` deltaP `6.6663` edge `0.0308` maxDD `-0.9112`
- `market_context_high->fx_1h` score `0.3011` n `101` status `ready` deltaP `7.2864` edge `0.0023` maxDD `-0.063`
- `news_risk_high->commodity_24h` score `-0.0899` n `72` status `ready` deltaP `13.1945` edge `0.0311` maxDD `-3.4467`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
