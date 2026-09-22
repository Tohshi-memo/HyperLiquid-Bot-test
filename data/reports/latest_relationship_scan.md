# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T04:52:27.467551+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9986`

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

- `market_context_high->unknown_4h` score `49.8478` n `46` status `ready` deltaP `7.3171` edge `4.1052` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `35.5434` n `46` status `ready` deltaP `22.3883` edge `2.8283` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `20.0616` n `46` status `ready` deltaP `21.1806` edge `1.5306` maxDD `0.0`
- `market_context_high->equity_24h` score `17.3467` n `46` status `ready` deltaP `15.6175` edge `1.3515` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `7.8263` n `101` status `ready` deltaP `-2.9669` edge `1.3578` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.6688` n `46` status `ready` deltaP `20.1314` edge `0.3469` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `3.5807` n `101` status `ready` deltaP `-2.5818` edge `0.8037` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.7782` n `101` status `ready` deltaP `34.1343` edge `0.2592` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.6855` n `101` status `ready` deltaP `13.2788` edge `0.2562` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.2486` n `101` status `ready` deltaP `13.6865` edge `0.1427` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.1584` n `101` status `ready` deltaP `16.3276` edge `0.1968` maxDD `-8.0625`
- `market_context_high->index_4h` score `1.9725` n `46` status `ready` deltaP `23.3165` edge `0.0223` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.5616` n `101` status `ready` deltaP `15.3332` edge `0.0802` maxDD `-2.8494`
- `market_context_high->crypto_alt_4h` score `1.1299` n `46` status `ready` deltaP `8.974` edge `0.0938` maxDD `-2.7574`
- `market_context_high->equity_4h` score `1.0704` n `46` status `ready` deltaP `8.1389` edge `0.0656` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.8893` n `46` status `ready` deltaP `7.062` edge `0.0513` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.7997` n `101` status `ready` deltaP `14.5858` edge `0.033` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6196` n `46` status `ready` deltaP `9.9063` edge `0.0109` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5562` n `101` status `ready` deltaP `13.9992` edge `0.0132` maxDD `-0.8144`
- `market_context_high->crypto_major_1h` score `0.4738` n `46` status `ready` deltaP `0.7616` edge `0.0867` maxDD `-2.1836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
