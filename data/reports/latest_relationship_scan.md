# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T04:22:24.403533+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9188`

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

- `news_risk_high->crypto_major_24h` score `40.5518` n `81` status `ready` deltaP `16.2423` edge `3.4378` maxDD `-10.3413`
- `news_risk_high->crypto_alt_24h` score `37.5119` n `81` status `ready` deltaP `29.2052` edge `3.0692` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `26.0026` n `88` status `ready` deltaP `0.0416` edge `2.1816` maxDD `-0.5326`
- `market_context_high->commodity_24h` score `7.4418` n `85` status `ready` deltaP `37.5409` edge `0.4224` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `6.4252` n `81` status `ready` deltaP `33.2755` edge `0.3272` maxDD `-0.4217`
- `news_risk_high->crypto_alt_4h` score `6.1642` n `98` status `ready` deltaP `23.4476` edge `0.4783` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.8252` n `98` status `ready` deltaP `23.1427` edge `0.3736` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.8828` n `88` status `ready` deltaP `35.1441` edge `0.1026` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.4092` n `98` status `ready` deltaP `18.9234` edge `0.2045` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6321` n `98` status `ready` deltaP `21.1689` edge `0.1305` maxDD `-2.8494`
- `market_context_high->commodity_1h` score `1.8886` n `88` status `ready` deltaP `21.5569` edge `0.0347` maxDD `-0.3491`
- `market_context_high->fx_4h` score `1.7799` n `88` status `ready` deltaP `25.485` edge `0.0041` maxDD `-0.0543`
- `news_risk_high->metal_24h` score `1.4803` n `81` status `ready` deltaP `22.3765` edge `0.0586` maxDD `-2.4203`
- `news_risk_high->metal_4h` score `0.8966` n `98` status `ready` deltaP `20.0441` edge `0.0465` maxDD `-2.0994`
- `market_context_high->fx_24h` score `0.8397` n `85` status `ready` deltaP `13.4068` edge `-0.0152` maxDD `-0.0027`
- `news_risk_high->metal_1h` score `0.7327` n `98` status `ready` deltaP `15.7552` edge `0.0162` maxDD `-0.8144`
- `news_risk_high->equity_1h` score `0.3839` n `98` status `ready` deltaP `6.0675` edge `0.0321` maxDD `-0.9112`
- `market_context_high->fx_1h` score `0.3421` n `88` status `ready` deltaP `7.7096` edge `0.0029` maxDD `-0.063`
- `news_risk_high->commodity_24h` score `0.2904` n `81` status `ready` deltaP `17.2068` edge `0.0531` maxDD `-3.4467`
- `news_risk_high->fx_4h` score `-0.1183` n `98` status `ready` deltaP `4.7754` edge `0.0219` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
