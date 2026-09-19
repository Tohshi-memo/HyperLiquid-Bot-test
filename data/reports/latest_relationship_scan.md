# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T08:22:27.938226+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8486`

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

- `news_risk_high->crypto_major_24h` score `55.9526` n `70` status `ready` deltaP `35.4315` edge `4.5157` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `49.0243` n `70` status `ready` deltaP `39.3849` edge `3.9607` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `35.5107` n `147` status `ready` deltaP `-1.9724` edge `2.9957` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `11.8143` n `70` status `ready` deltaP `45.0992` edge `0.6881` maxDD `-0.0053`
- `risk_on_high->unknown_4h` score `8.3791` n `52` status `ready` deltaP `-9.076` edge `0.7813` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `8.3791` n `52` status `ready` deltaP `-9.076` edge `0.7813` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.2412` n `52` status `ready` deltaP `44.9653` edge `0.387` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2412` n `52` status `ready` deltaP `44.9653` edge `0.387` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.972` n `147` status `ready` deltaP `38.1626` edge `0.3791` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.7421` n `81` status `ready` deltaP `23.0974` edge `0.5288` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6113` n `81` status `ready` deltaP `19.9883` edge `0.3768` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3861` n `81` status `ready` deltaP `17.7497` edge `0.2104` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.7252` n `81` status `ready` deltaP `20.9673` edge `0.1396` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.6307` n `52` status `ready` deltaP `31.3203` edge `0.0454` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6307` n `52` status `ready` deltaP `31.3203` edge `0.0454` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5102` n `147` status `ready` deltaP `27.5396` edge `0.0674` maxDD `-0.345`
- `news_risk_high->metal_24h` score `2.2708` n `70` status `ready` deltaP `25.9276` edge `0.0869` maxDD `-1.9749`
- `news_risk_high->fx_4h` score `1.2838` n `81` status `ready` deltaP `14.4554` edge `0.0325` maxDD `-0.084`
- `market_context_high->commodity_1h` score `1.0059` n `147` status `ready` deltaP `15.0332` edge `0.0213` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `0.8119` n `81` status `ready` deltaP `10.0078` edge `0.0415` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
