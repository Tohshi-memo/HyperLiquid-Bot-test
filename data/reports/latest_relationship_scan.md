# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T10:22:28.037491+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9300`

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

- `news_risk_high->crypto_major_24h` score `30.1815` n `90` status `ready` deltaP `11.1459` edge `2.8743` maxDD `-28.6787`
- `news_risk_high->crypto_alt_24h` score `28.8704` n `90` status `ready` deltaP `20.0694` edge `2.5018` maxDD `-14.7118`
- `market_context_high->unknown_4h` score `15.7793` n `64` status `ready` deltaP `1.7149` edge `1.3185` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `6.3375` n `98` status `ready` deltaP `23.9049` edge `0.4897` maxDD `-7.675`
- `market_context_high->commodity_24h` score `6.1967` n `61` status `ready` deltaP `32.9122` edge `0.3495` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `4.6846` n `98` status `ready` deltaP `22.9902` edge `0.3629` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.0317` n `64` status `ready` deltaP `35.1753` edge `0.1148` maxDD `-0.0659`
- `news_risk_high->equity_24h` score `3.0758` n `90` status `ready` deltaP `23.6459` edge `0.1795` maxDD `-2.799`
- `news_risk_high->crypto_alt_1h` score `3.0186` n `101` status `ready` deltaP `16.3811` edge `0.1889` maxDD `-2.058`
- `market_context_high->fx_4h` score `2.2273` n `64` status `ready` deltaP `29.0777` edge `0.0091` maxDD `-0.0543`
- `news_risk_high->crypto_major_1h` score `2.2188` n `101` status `ready` deltaP `18.3272` edge `0.115` maxDD `-2.8494`
- `market_context_high->commodity_1h` score `1.5235` n `72` status `ready` deltaP `18.2884` edge `0.0344` maxDD `-0.3491`
- `market_context_high->fx_24h` score `1.3617` n `61` status `ready` deltaP `17.1107` edge `0.0036` maxDD `-0.0027`
- `news_risk_high->metal_24h` score `0.7744` n `90` status `ready` deltaP `21.9445` edge `0.0374` maxDD `-2.4203`
- `news_risk_high->commodity_24h` score `0.742` n `90` status `ready` deltaP `20.4167` edge `0.0896` maxDD `-3.4467`
- `news_risk_high->metal_4h` score `0.7335` n `98` status `ready` deltaP `18.2149` edge `0.0451` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6161` n `101` status `ready` deltaP `14.4483` edge `0.0152` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.3565` n `72` status `ready` deltaP `7.7096` edge `0.0041` maxDD `-0.063`
- `news_risk_high->equity_1h` score `0.2783` n `101` status `ready` deltaP `5.9628` edge `0.024` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `-0.0671` n `98` status `ready` deltaP `5.3851` edge `0.0221` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
