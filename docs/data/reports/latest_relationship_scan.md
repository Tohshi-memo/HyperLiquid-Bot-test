# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T02:07:31.454465+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8126`

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

- `news_risk_high->crypto_major_24h` score `62.5788` n `46` status `ready` deltaP `33.839` edge `5.0785` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `57.1717` n `46` status `ready` deltaP `35.6582` edge `4.6645` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.0923` n `149` status `ready` deltaP `-1.3781` edge `3.0402` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `15.356` n `46` status `ready` deltaP `50.6944` edge `0.9417` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.9709` n `52` status `ready` deltaP `-8.6187` edge `0.9109` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.9709` n `52` status `ready` deltaP `-8.6187` edge `0.9109` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.9588` n `72` status `ready` deltaP `28.6755` edge `0.668` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.3858` n `52` status `ready` deltaP `46.0069` edge `0.3921` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.3858` n `52` status `ready` deltaP `46.0069` edge `0.3921` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.0866` n `149` status `ready` deltaP `39.2955` edge `0.3811` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `6.1479` n `72` status `ready` deltaP `25.4065` edge `0.4604` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.8282` n `46` status `ready` deltaP `36.0054` edge `0.1781` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.256` n `73` status `ready` deltaP `18.284` edge `0.196` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.9017` n `73` status `ready` deltaP `22.5433` edge `0.1438` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.6255` n `52` status `ready` deltaP `31.0155` edge `0.047` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6255` n `52` status `ready` deltaP `31.0155` edge `0.047` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5253` n `149` status `ready` deltaP `27.5178` edge `0.0688` maxDD `-0.345`
- `news_risk_high->fx_24h` score `1.7643` n `46` status `ready` deltaP `8.7636` edge `0.0928` maxDD `-0.0029`
- `news_risk_high->equity_4h` score `1.5463` n `72` status `ready` deltaP `12.3984` edge `0.1362` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.5385` n `72` status `ready` deltaP `16.7683` edge `0.0383` maxDD `-0.084`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
