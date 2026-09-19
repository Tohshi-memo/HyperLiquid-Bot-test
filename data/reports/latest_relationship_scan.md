# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T13:22:25.660651+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8540`

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

- `news_risk_high->crypto_major_24h` score `53.0452` n `72` status `ready` deltaP `32.118` edge `4.2955` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `46.5456` n `72` status `ready` deltaP `36.632` edge `3.7725` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `37.5279` n `143` status `ready` deltaP `-2.2578` edge `3.1657` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `10.4669` n `72` status `ready` deltaP `41.6667` edge `0.5987` maxDD `-0.0053`
- `risk_on_high->unknown_4h` score `8.3515` n `52` status `ready` deltaP `-9.076` edge `0.779` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `8.3515` n `52` status `ready` deltaP `-9.076` edge `0.779` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.2774` n `52` status `ready` deltaP `45.3125` edge `0.3877` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2774` n `52` status `ready` deltaP `45.3125` edge `0.3877` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.0685` n `143` status `ready` deltaP `38.3195` edge `0.3861` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.6267` n `86` status `ready` deltaP `24.174` edge `0.512` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.521` n `86` status `ready` deltaP `21.1997` edge `0.3612` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.2999` n `98` status `ready` deltaP `19.2228` edge `0.1934` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.6355` n `52` status `ready` deltaP `31.3203` edge `0.0458` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6355` n `52` status `ready` deltaP `31.3203` edge `0.0458` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5346` n `143` status `ready` deltaP `27.649` edge `0.0687` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.5109` n `98` status `ready` deltaP `21.1689` edge `0.1204` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.9173` n `72` status `ready` deltaP `24.4792` edge `0.081` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.061` n `143` status `ready` deltaP `15.5867` edge `0.0222` maxDD `-0.3491`
- `news_risk_high->fx_4h` score `0.9936` n `86` status `ready` deltaP `11.479` edge `0.0288` maxDD `-0.1357`
- `news_risk_high->equity_1h` score `0.7255` n `98` status `ready` deltaP `10.0819` edge `0.0338` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
