# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T01:37:27.205841+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8098`

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

- `news_risk_high->crypto_major_24h` score `62.6798` n `45` status `ready` deltaP `33.6458` edge `5.0882` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `57.342` n `45` status `ready` deltaP `35.4167` edge `4.6803` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.2399` n `149` status `ready` deltaP `-1.3781` edge `3.0525` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `15.3849` n `45` status `ready` deltaP `51.0417` edge `0.9418` maxDD `0.0`
- `risk_on_high->unknown_4h` score `10.1185` n `52` status `ready` deltaP `-8.6187` edge `0.9232` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `10.1185` n `52` status `ready` deltaP `-8.6187` edge `0.9232` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.96` n `72` status `ready` deltaP `28.6755` edge `0.6681` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.4195` n `52` status `ready` deltaP `46.3542` edge `0.3926` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.4195` n `52` status `ready` deltaP `46.3542` edge `0.3926` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.1204` n `149` status `ready` deltaP `39.6428` edge `0.3816` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `6.1673` n `72` status `ready` deltaP `25.5589` edge `0.461` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.8329` n `45` status `ready` deltaP `35.7639` edge `0.1801` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.2391` n `72` status `ready` deltaP `17.7728` edge `0.198` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.8977` n `72` status `ready` deltaP `22.2389` edge `0.1455` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.6595` n `52` status `ready` deltaP `31.3203` edge `0.0478` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6595` n `52` status `ready` deltaP `31.3203` edge `0.0478` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5593` n `149` status `ready` deltaP `27.8226` edge `0.0696` maxDD `-0.345`
- `news_risk_high->fx_24h` score `1.7935` n `45` status `ready` deltaP `8.8889` edge `0.0944` maxDD `-0.0029`
- `news_risk_high->equity_4h` score `1.5415` n `72` status `ready` deltaP `12.3984` edge `0.1358` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.5129` n `72` status `ready` deltaP `16.4634` edge `0.0382` maxDD `-0.084`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
