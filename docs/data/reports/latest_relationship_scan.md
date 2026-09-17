# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T11:22:29.067825+00:00`
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

- `news_risk_high->unknown_4h` score `384.6388` n `83` status `ready` deltaP `-21.5105` edge `32.2861` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `13.0737` n `83` status `ready` deltaP `32.6221` edge `1.0099` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `12.4103` n `83` status `ready` deltaP `24.6883` edge `1.0691` maxDD `-13.2931`
- `risk_on_high->commodity_24h` score `9.0827` n `52` status `ready` deltaP `48.9583` edge `0.4305` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.0827` n `52` status `ready` deltaP `48.9583` edge `0.4305` maxDD `0.0`
- `news_risk_high->equity_24h` score `8.9464` n `83` status `ready` deltaP `33.9211` edge `0.6968` maxDD `-6.5262`
- `market_context_high->commodity_24h` score `7.7835` n `149` status `ready` deltaP `42.2469` edge `0.4195` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.7964` n `83` status `ready` deltaP `39.3512` edge `0.2383` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.0006` n `83` status `ready` deltaP `31.4696` edge `0.169` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.6159` n `52` status `ready` deltaP `31.0155` edge `0.0462` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6159` n `52` status `ready` deltaP `31.0155` edge `0.0462` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5157` n `149` status `ready` deltaP `27.5178` edge `0.068` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.4805` n `52` status `ready` deltaP `32.4519` edge `-0.0054` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4805` n `52` status `ready` deltaP `32.4519` edge `-0.0054` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.3457` n `149` status `ready` deltaP `29.677` edge `0.0192` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.0546` n `149` status `ready` deltaP `15.7618` edge `0.0205` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.4313` n `52` status `ready` deltaP `8.8439` edge `0.0122` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4313` n `52` status `ready` deltaP `8.8439` edge `0.0122` maxDD `-0.1507`
- `news_risk_high->index_4h` score `0.2003` n `83` status `ready` deltaP `9.6018` edge `0.0245` maxDD `-0.6935`
- `market_context_high->fx_1h` score `0.0626` n `149` status `ready` deltaP `4.8015` edge `0.0018` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
