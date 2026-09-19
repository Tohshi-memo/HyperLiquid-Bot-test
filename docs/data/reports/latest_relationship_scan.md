# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T17:52:27.820456+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8502`

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

- `news_risk_high->crypto_major_24h` score `51.5448` n `72` status `ready` deltaP `28.993` edge `4.1913` maxDD `-5.8019`
- `market_context_high->unknown_4h` score `45.495` n `127` status `ready` deltaP `-2.9443` edge `3.8342` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `45.1056` n `72` status `ready` deltaP `34.2014` edge `3.6687` maxDD `-9.3661`
- `risk_on_high->unknown_4h` score `22.843` n `37` status `ready` deltaP `-13.5423` edge `2.0164` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `22.843` n `37` status `ready` deltaP `-13.5423` edge `2.0164` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `9.4118` n `37` status `ready` deltaP `48.4375` edge `0.4614` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.4118` n `37` status `ready` deltaP `48.4375` edge `0.4614` maxDD `0.0`
- `news_risk_high->equity_24h` score `9.3145` n `72` status `ready` deltaP `38.5417` edge `0.5235` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.6333` n `127` status `ready` deltaP `40.5635` edge `0.4182` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.655` n `98` status `ready` deltaP `21.3134` edge `0.4501` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.2421` n `98` status `ready` deltaP `21.3134` edge `0.3372` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.2915` n `98` status `ready` deltaP `19.2228` edge `0.1927` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.5597` n `127` status `ready` deltaP `26.9878` edge `0.0752` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.3911` n `98` status `ready` deltaP `19.9713` edge `0.1184` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.2603` n `37` status `ready` deltaP `26.2855` edge `0.0481` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.2603` n `37` status `ready` deltaP `26.2855` edge `0.0481` maxDD `-0.1313`
- `news_risk_high->metal_24h` score `1.7273` n `72` status `ready` deltaP `22.5694` edge `0.0779` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.4423` n `127` status `ready` deltaP `17.9829` edge `0.0255` maxDD `-0.3491`
- `news_risk_high->metal_4h` score `0.8636` n `98` status `ready` deltaP `19.5868` edge `0.0468` maxDD `-2.0994`
- `risk_on_high->commodity_1h` score `0.8034` n `37` status `ready` deltaP `15.4718` edge `0.0184` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
