# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T16:22:34.159194+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10024`

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

- `market_context_high->unknown_1h` score `87.6583` n `47` status `ready` deltaP `10.116` edge `7.2445` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `43.4477` n `47` status `ready` deltaP `30.4226` edge `3.4571` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.1316` n `47` status `ready` deltaP `24.782` edge `2.3004` maxDD `-2.7051`
- `market_context_high->equity_24h` score `24.376` n `47` status `ready` deltaP `28.8601` edge `1.8745` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8509` n `47` status `ready` deltaP `34.9364` edge `0.4343` maxDD `-0.3705`
- `news_risk_high->crypto_major_24h` score `5.2818` n `93` status `ready` deltaP `1.3217` edge `1.5726` maxDD `-63.6743`
- `market_context_high->metal_24h` score `3.684` n `47` status `ready` deltaP `31.7598` edge `0.1191` maxDD `-0.2401`
- `news_risk_high->crypto_alt_24h` score `3.2754` n `93` status `ready` deltaP `-1.0473` edge `1.1282` maxDD `-49.7699`
- `market_context_high->index_4h` score `3.1212` n `47` status `ready` deltaP `35.5507` edge `0.0385` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.7538` n `114` status `ready` deltaP `13.0975` edge `0.1912` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.6529` n `47` status `ready` deltaP `17.9067` edge `0.1435` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.3739` n `114` status `ready` deltaP `16.0705` edge `0.1342` maxDD `-1.8141`
- `news_risk_high->crypto_major_4h` score `1.6877` n `110` status `ready` deltaP `15.2245` edge `0.2523` maxDD `-13.719`
- `news_risk_high->fx_4h` score `1.608` n `110` status `ready` deltaP `23.5338` edge `0.0407` maxDD `-0.421`
- `news_risk_high->crypto_alt_4h` score `1.1945` n `110` status `ready` deltaP `7.6303` edge `0.2938` maxDD `-15.9436`
- `news_risk_high->metal_24h` score `1.1611` n `93` status `ready` deltaP `25.0336` edge `0.1268` maxDD `-7.2536`
- `news_risk_high->fx_24h` score `1.1401` n `93` status `ready` deltaP `28.1978` edge `0.1213` maxDD `-1.7159`
- `market_context_high->index_1h` score `1.0302` n `47` status `ready` deltaP `15.3586` edge `0.0113` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9703` n `47` status `ready` deltaP `11.4664` edge `0.0447` maxDD `-1.5564`
- `news_risk_high->commodity_24h` score `0.8299` n `93` status `ready` deltaP `14.9921` edge `0.0871` maxDD `-2.431`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
