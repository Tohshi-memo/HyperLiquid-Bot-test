# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T15:22:26.405294+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8594`

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

- `news_risk_high->crypto_major_24h` score `52.2896` n `72` status `ready` deltaP `30.7291` edge `4.2418` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `45.9014` n `72` status `ready` deltaP `35.7639` edge `3.7246` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `40.4839` n `137` status `ready` deltaP `-2.7172` edge `3.4151` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `12.0922` n `47` status `ready` deltaP `-10.9172` edge `1.103` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `12.0922` n `47` status `ready` deltaP `-10.9172` edge `1.103` maxDD `-0.4694`
- `news_risk_high->equity_24h` score `9.9262` n `72` status `ready` deltaP `40.2778` edge `0.5629` maxDD `-0.0053`
- `risk_on_high->commodity_24h` score `8.6609` n `47` status `ready` deltaP `46.7014` edge `0.4104` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.6609` n `47` status `ready` deltaP `46.7014` edge `0.4104` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.3087` n `137` status `ready` deltaP `39.4021` edge `0.3989` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.4049` n `94` status `ready` deltaP `24.747` edge `0.4897` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.5331` n `94` status `ready` deltaP `21.8604` edge `0.3578` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3047` n `98` status `ready` deltaP `19.2228` edge `0.1938` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.5524` n `47` status `ready` deltaP `29.9365` edge `0.0481` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.5524` n `47` status `ready` deltaP `29.9365` edge `0.0481` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5277` n `137` status `ready` deltaP `27.1876` edge `0.0712` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.4761` n `98` status `ready` deltaP `20.8695` edge `0.1195` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.7786` n `72` status `ready` deltaP `23.0903` edge `0.0787` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.3891` n `137` status `ready` deltaP `17.5281` edge `0.0241` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `1.227` n `47` status `ready` deltaP `15.5402` edge `0.0172` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `1.227` n `47` status `ready` deltaP `15.5402` edge `0.0172` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
