# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T02:52:27.815073+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9116`

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

- `news_risk_high->crypto_major_24h` score `41.8587` n `80` status `ready` deltaP `17.2917` edge `3.507` maxDD `-8.0574`
- `news_risk_high->crypto_alt_24h` score `38.4061` n `80` status `ready` deltaP `30.3472` edge `3.1361` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `25.2779` n `93` status `ready` deltaP `-3.2832` edge `2.1517` maxDD `-0.5326`
- `market_context_high->commodity_24h` score `7.6599` n `91` status `ready` deltaP `38.3166` edge `0.4354` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `6.9035` n `80` status `ready` deltaP `34.4792` edge `0.3515` maxDD `-0.1522`
- `news_risk_high->crypto_alt_4h` score `5.9704` n `98` status `ready` deltaP `22.9902` edge `0.4652` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6896` n `98` status `ready` deltaP `23.1427` edge `0.3623` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.9355` n `93` status `ready` deltaP `35.8773` edge `0.1021` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.3012` n `98` status `ready` deltaP `18.624` edge `0.1975` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.5841` n `98` status `ready` deltaP `21.1689` edge `0.1265` maxDD `-2.8494`
- `market_context_high->commodity_1h` score `1.9143` n `94` status `ready` deltaP `22.0888` edge `0.0333` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.588` n `80` status `ready` deltaP `23.3333` edge `0.0612` maxDD `-2.4203`
- `market_context_high->fx_4h` score `1.2051` n `93` status `ready` deltaP `21.6348` edge `0.003` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.8442` n `98` status `ready` deltaP `19.4344` edge `0.0462` maxDD `-2.0994`
- `market_context_high->fx_24h` score `0.7398` n `91` status `ready` deltaP `12.4428` edge `-0.0171` maxDD `-0.0027`
- `news_risk_high->metal_1h` score `0.7303` n `98` status `ready` deltaP `15.7552` edge `0.016` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.3994` n `94` status `ready` deltaP `8.4406` edge `0.0028` maxDD `-0.063`
- `news_risk_high->equity_1h` score `0.3779` n `98` status `ready` deltaP `6.2172` edge `0.0306` maxDD `-0.9112`
- `news_risk_high->commodity_24h` score `0.2149` n `80` status `ready` deltaP `16.8056` edge `0.0461` maxDD `-3.4467`
- `news_risk_high->fx_4h` score `-0.0671` n `98` status `ready` deltaP `5.3851` edge `0.0221` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
