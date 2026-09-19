# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T17:07:26.476016+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8582`

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

- `news_risk_high->crypto_major_24h` score `51.7436` n `72` status `ready` deltaP `29.5138` edge `4.2044` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `45.3537` n `72` status `ready` deltaP `34.7223` edge `3.6859` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `44.6284` n `130` status `ready` deltaP `-3.3068` edge `3.7644` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `21.5441` n `40` status `ready` deltaP `-14.2683` edge `1.913` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `21.5441` n `40` status `ready` deltaP `-14.2683` edge `1.913` maxDD `-0.4694`
- `news_risk_high->equity_24h` score `9.487` n `72` status `ready` deltaP `39.0625` edge `0.5344` maxDD `-0.0053`
- `risk_on_high->commodity_24h` score `9.1709` n `40` status `ready` deltaP `47.9167` edge `0.4448` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.1709` n `40` status `ready` deltaP `47.9167` edge `0.4448` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5425` n `130` status `ready` deltaP `40.2244` edge `0.4129` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.73` n `98` status `ready` deltaP `21.7707` edge `0.4533` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.2929` n `98` status `ready` deltaP `21.6183` edge `0.3394` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3071` n `98` status `ready` deltaP `19.3725` edge `0.193` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.5499` n `130` status `ready` deltaP `27.0755` edge `0.0738` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.3983` n `98` status `ready` deltaP `20.121` edge `0.118` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.3601` n `40` status `ready` deltaP `27.6524` edge `0.0473` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.3601` n `40` status `ready` deltaP `27.6524` edge `0.0473` maxDD `-0.1313`
- `news_risk_high->metal_24h` score `1.7249` n `72` status `ready` deltaP `22.5694` edge `0.0777` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.4975` n `130` status `ready` deltaP `18.6734` edge `0.0255` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `1.4365` n `40` status `ready` deltaP `17.9042` edge `0.0189` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `1.4365` n `40` status `ready` deltaP `17.9042` edge `0.0189` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
