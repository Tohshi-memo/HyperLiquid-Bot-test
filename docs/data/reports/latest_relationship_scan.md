# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T18:52:30.995066+00:00`
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

- `news_risk_high->crypto_major_24h` score `51.3404` n `72` status `ready` deltaP `28.2986` edge `4.1789` maxDD `-5.8019`
- `market_context_high->unknown_4h` score `47.4031` n `123` status `ready` deltaP `-3.3028` edge `3.9956` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `44.8659` n `72` status `ready` deltaP `33.6806` edge `3.6522` maxDD `-9.3661`
- `risk_on_high->unknown_4h` score `27.9049` n `33` status `ready` deltaP `-16.1631` edge `2.4557` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `27.9049` n `33` status `ready` deltaP `-16.1631` edge `2.4557` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `9.778` n `33` status `ready` deltaP `48.7847` edge `0.4896` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.778` n `33` status `ready` deltaP `48.7847` edge `0.4896` maxDD `0.0`
- `news_risk_high->equity_24h` score `9.1006` n `72` status `ready` deltaP `37.8472` edge `0.5103` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.7305` n `123` status `ready` deltaP `40.6546` edge `0.4257` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.6212` n `98` status `ready` deltaP `21.161` edge `0.4483` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.2361` n `98` status `ready` deltaP `21.3134` edge `0.3367` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.2903` n `98` status `ready` deltaP `19.0731` edge `0.1936` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.577` n `123` status `ready` deltaP `26.8293` edge `0.0777` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.3815` n `98` status `ready` deltaP `19.8216` edge `0.1186` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.1272` n `33` status `ready` deltaP `23.9468` edge `0.0526` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.1272` n `33` status `ready` deltaP `23.9468` edge `0.0526` maxDD `-0.1313`
- `news_risk_high->metal_24h` score `1.7297` n `72` status `ready` deltaP `22.5694` edge `0.0781` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.3632` n `123` status `ready` deltaP `17.0099` edge `0.0254` maxDD `-0.3491`
- `news_risk_high->metal_4h` score `0.8502` n `98` status `ready` deltaP `19.4344` edge `0.0467` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.7446` n `98` status `ready` deltaP `15.9049` edge `0.0162` maxDD `-0.8144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
