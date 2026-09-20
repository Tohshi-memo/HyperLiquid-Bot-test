# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T01:07:26.248490+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9092`

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

- `news_risk_high->crypto_major_24h` score `49.7427` n `73` status `ready` deltaP `25.4424` edge `4.0648` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `43.3199` n `73` status `ready` deltaP `32.0396` edge `3.5343` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `18.1933` n `100` status `ready` deltaP `-5.9207` edge `1.5789` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `8.1685` n `73` status `ready` deltaP `36.6509` edge `0.4406` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.8895` n `98` status `ready` deltaP `39.1015` edge `0.4493` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.9942` n `98` status `ready` deltaP `22.8378` edge `0.4682` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.679` n `98` status `ready` deltaP `23.2951` edge `0.3604` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.7611` n `100` status `ready` deltaP `34.2378` edge `0.0985` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.2245` n `98` status `ready` deltaP `18.3246` edge `0.1931` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.4582` n `98` status `ready` deltaP `20.2707` edge `0.122` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.6554` n `73` status `ready` deltaP `22.3911` edge `0.0731` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.6314` n `101` status `ready` deltaP `19.5826` edge `0.0306` maxDD `-0.3491`
- `market_context_high->fx_4h` score `1.1169` n `100` status `ready` deltaP `20.6829` edge `0.002` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.8199` n `98` status `ready` deltaP `19.1295` edge `0.0462` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.7183` n `98` status `ready` deltaP `15.6055` edge `0.016` maxDD `-0.8144`
- `market_context_high->fx_24h` score `0.6153` n `98` status `ready` deltaP `11.306` edge `-0.0199` maxDD `-0.0027`
- `news_risk_high->fx_24h` score `0.5318` n `73` status `ready` deltaP `4.1072` edge `0.0397` maxDD `-0.1548`
- `news_risk_high->equity_1h` score `0.415` n `98` status `ready` deltaP `6.6663` edge `0.0307` maxDD `-0.9112`
- `market_context_high->fx_1h` score `0.3035` n `101` status `ready` deltaP `7.2864` edge `0.0025` maxDD `-0.063`
- `news_risk_high->commodity_24h` score `-0.0595` n `73` status `ready` deltaP `13.6892` edge `0.0317` maxDD `-3.4467`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
