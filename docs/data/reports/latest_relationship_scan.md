# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T04:37:28.542390+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8080`

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

- `market_context_high->unknown_24h` score `7118.0683` n `42` status `ready` deltaP `1.3889` edge `593.1631` maxDD `0.0`
- `market_context_high->unknown_4h` score `471.8289` n `45` status `ready` deltaP `9.1463` edge `39.2581` maxDD `0.0`
- `market_context_high->unknown_1h` score `79.1738` n `47` status `ready` deltaP `4.7809` edge `6.577` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.0318` n `42` status `ready` deltaP `42.2371` edge `1.328` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.8574` n `94` status `ready` deltaP `34.2605` edge `1.062` maxDD `-6.8493`
- `market_context_high->commodity_24h` score `6.8716` n `42` status `ready` deltaP `44.5685` edge `0.3066` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.7604` n `45` status `ready` deltaP `29.6545` edge `0.3951` maxDD `-1.6876`
- `market_context_high->index_24h` score `6.459` n `42` status `ready` deltaP `49.1319` edge `0.2107` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.364` n `45` status `ready` deltaP `28.5637` edge `0.2902` maxDD `-1.6901`
- `market_context_high->equity_4h` score `4.4107` n `45` status `ready` deltaP `6.189` edge `0.3965` maxDD `-2.283`
- `market_context_high->commodity_4h` score `2.8883` n `45` status `ready` deltaP `30.0` edge `0.0664` maxDD `-1.0567`
- `news_risk_high->crypto_alt_4h` score `2.2276` n `126` status `ready` deltaP `8.8608` edge `0.2652` maxDD `-7.4246`
- `market_context_high->equity_1h` score `1.8872` n `47` status `ready` deltaP `4.7203` edge `0.1783` maxDD `-1.5336`
- `market_context_high->crypto_alt_24h` score `1.3115` n `42` status `ready` deltaP `-11.4335` edge `0.3373` maxDD `-8.8096`
- `market_context_high->crypto_alt_1h` score `1.191` n `47` status `ready` deltaP `3.1915` edge `0.1392` maxDD `-2.2314`
- `market_context_high->crypto_major_1h` score `1.1241` n `47` status `ready` deltaP `4.7203` edge `0.1131` maxDD `-1.4048`
- `market_context_high->fx_1h` score `1.1125` n `47` status `ready` deltaP `15.2089` edge `0.0089` maxDD `-0.0736`
- `market_context_high->metal_4h` score `0.8547` n `45` status `ready` deltaP `15.6402` edge `0.0478` maxDD `-0.7323`
- `market_context_high->crypto_major_24h` score `0.5342` n `42` status `ready` deltaP `-0.3968` edge `0.1388` maxDD `-3.0799`
- `market_context_high->metal_1h` score `0.2927` n `47` status `ready` deltaP `7.2334` edge `0.015` maxDD `-0.3895`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
