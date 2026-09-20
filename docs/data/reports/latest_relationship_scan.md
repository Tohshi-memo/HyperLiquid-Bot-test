# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T05:37:26.423841+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9286`

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

- `news_risk_high->crypto_major_24h` score `40.7855` n `81` status `ready` deltaP `16.7631` edge `3.4538` maxDD `-10.3413`
- `news_risk_high->crypto_alt_24h` score `37.4879` n `81` status `ready` deltaP `29.2052` edge `3.0672` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `9.7136` n `83` status `ready` deltaP `0.6832` edge `0.8199` maxDD `-0.5326`
- `market_context_high->commodity_24h` score `7.209` n `80` status `ready` deltaP `36.8056` edge `0.4079` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `6.304` n `81` status `ready` deltaP `33.2755` edge `0.3171` maxDD `-0.4217`
- `news_risk_high->crypto_alt_4h` score `6.2614` n `98` status `ready` deltaP `23.4476` edge `0.4864` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.8936` n `98` status `ready` deltaP `23.1427` edge `0.3793` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.8387` n `83` status `ready` deltaP `34.3227` edge `0.1044` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.4223` n `98` status `ready` deltaP `19.0731` edge `0.2046` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6465` n `98` status `ready` deltaP `21.3186` edge `0.1307` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.2744` n `83` status `ready` deltaP `30.1774` edge `0.0057` maxDD `-0.0543`
- `market_context_high->commodity_1h` score `1.8316` n `83` status `ready` deltaP `20.6497` edge `0.036` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.4659` n `81` status `ready` deltaP `22.3765` edge `0.0574` maxDD `-2.4203`
- `market_context_high->fx_24h` score `0.9441` n `80` status `ready` deltaP `14.2014` edge `-0.0118` maxDD `-0.0027`
- `news_risk_high->metal_4h` score `0.8978` n `98` status `ready` deltaP `20.0441` edge `0.0466` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.7566` n `98` status `ready` deltaP `16.0546` edge `0.0162` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.5434` n `83` status `ready` deltaP `10.1201` edge `0.0036` maxDD `-0.063`
- `news_risk_high->equity_1h` score `0.3695` n `98` status `ready` deltaP `5.9178` edge `0.0319` maxDD `-0.9112`
- `news_risk_high->commodity_24h` score `0.3239` n `81` status `ready` deltaP `17.2068` edge `0.0574` maxDD `-3.4467`
- `news_risk_high->fx_4h` score `-0.1427` n `98` status `ready` deltaP `4.4705` edge `0.0219` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
