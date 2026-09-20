# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T01:22:29.532386+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9108`

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

- `news_risk_high->crypto_major_24h` score `48.718` n `74` status `ready` deltaP `24.1836` edge `3.9878` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `42.7014` n `74` status `ready` deltaP `31.9585` edge `3.4833` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `18.8899` n `99` status `ready` deltaP `-6.0621` edge `1.6379` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `7.9989` n `74` status `ready` deltaP `36.4958` edge `0.4275` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.8655` n `97` status `ready` deltaP `38.9963` edge `0.448` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.987` n `98` status `ready` deltaP `22.8378` edge `0.4676` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.679` n `98` status `ready` deltaP `23.2951` edge `0.3604` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.7574` n `99` status `ready` deltaP `34.0863` edge `0.0992` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.2424` n `98` status `ready` deltaP `18.4743` edge `0.1936` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.4738` n `98` status `ready` deltaP `20.4204` edge `0.1223` maxDD `-2.8494`
- `market_context_high->commodity_1h` score `1.7321` n `100` status `ready` deltaP `20.1557` edge `0.031` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.649` n `74` status `ready` deltaP `22.5507` edge `0.0715` maxDD `-2.4203`
- `market_context_high->fx_4h` score `1.1004` n `99` status `ready` deltaP `20.4607` edge `0.0021` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.8199` n `98` status `ready` deltaP `19.1295` edge `0.0462` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.7183` n `98` status `ready` deltaP `15.6055` edge `0.016` maxDD `-0.8144`
- `market_context_high->fx_24h` score `0.6331` n `97` status `ready` deltaP `11.4691` edge `-0.0195` maxDD `-0.0027`
- `news_risk_high->equity_1h` score `0.415` n `98` status `ready` deltaP `6.6663` edge `0.0307` maxDD `-0.9112`
- `news_risk_high->fx_24h` score `0.3616` n `74` status `ready` deltaP `3.0405` edge `0.0374` maxDD `-0.2031`
- `market_context_high->fx_1h` score `0.3402` n `100` status `ready` deltaP `7.7605` edge `0.0024` maxDD `-0.063`
- `news_risk_high->commodity_24h` score `-0.0251` n `74` status `ready` deltaP `14.1705` edge `0.0329` maxDD `-3.4467`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
