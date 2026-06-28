# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T03:52:26.252871+00:00`
- Price records: `672`
- Market context records: `5003`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10290`

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

- `market_context_high->unknown_1h` score `15.1879` n `93` status `ready` deltaP `3.9679` edge `1.2893` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.2577` n `91` status `ready` deltaP `22.2544` edge `0.642` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.8487` n `91` status `ready` deltaP `18.0046` edge `0.5258` maxDD `-8.3416`
- `market_context_high->unknown_24h` score `5.2681` n `74` status `ready` deltaP `29.8142` edge `0.2745` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `5.1612` n `91` status `ready` deltaP `13.3041` edge `0.4808` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.2557` n `91` status `ready` deltaP `13.0562` edge `0.1255` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8632` n `93` status `ready` deltaP `8.0371` edge `0.0757` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8381` n `93` status `ready` deltaP `6.4033` edge `0.1189` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.565` n `91` status `ready` deltaP `4.5129` edge `0.1805` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3485` n `93` status `ready` deltaP `6.1039` edge `0.038` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1602` n `93` status `ready` deltaP `4.961` edge `0.0897` maxDD `-5.5126`
- `market_context_high->index_4h` score `0.1027` n `91` status `ready` deltaP `5.0589` edge `0.0417` maxDD `-1.0163`
- `market_context_high->fx_24h` score `-0.1726` n `74` status `ready` deltaP `7.3011` edge `0.0054` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.2707` n `93` status `ready` deltaP `2.4564` edge `0.0149` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5694` n `93` status `ready` deltaP `2.062` edge `0.0129` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.7376` n `91` status `ready` deltaP `4.9953` edge `-0.0026` maxDD `-5.021`
- `market_context_high->fx_4h` score `-0.9347` n `91` status `ready` deltaP `-2.8997` edge `-0.0021` maxDD `-1.205`
- `market_context_high->fx_1h` score `-1.7473` n `93` status `ready` deltaP `-11.8489` edge `-0.0056` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-4.1274` n `74` status `ready` deltaP `0.6944` edge `0.0117` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.1625` n `74` status `ready` deltaP `5.7948` edge `-0.0614` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
