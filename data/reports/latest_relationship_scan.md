# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T03:23:11.078857+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8150`

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

- `news_risk_high->crypto_major_24h` score `62.1833` n `50` status `ready` deltaP `34.5347` edge `5.0409` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `56.6665` n `50` status `ready` deltaP `36.5278` edge `4.6166` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.1859` n `149` status `ready` deltaP `-1.3781` edge `3.048` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `15.1305` n `50` status `ready` deltaP `49.8264` edge `0.9287` maxDD `0.0`
- `risk_on_high->unknown_4h` score `10.0645` n `52` status `ready` deltaP `-8.6187` edge `0.9187` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `10.0645` n `52` status `ready` deltaP `-8.6187` edge `0.9187` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.8684` n `72` status `ready` deltaP `28.3706` edge `0.6625` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.3285` n `52` status `ready` deltaP `45.4861` edge `0.3908` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.3285` n `52` status `ready` deltaP `45.4861` edge `0.3908` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.0293` n `149` status `ready` deltaP `38.7747` edge `0.3798` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `6.0476` n `72` status `ready` deltaP `24.7967` edge `0.4561` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.815` n `50` status `ready` deltaP `36.875` edge `0.1712` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.6511` n `78` status `ready` deltaP `19.8027` edge `0.2188` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.9955` n `78` status `ready` deltaP `22.5165` edge `0.1518` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.5418` n `52` status `ready` deltaP `30.2533` edge `0.0451` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.5418` n `52` status `ready` deltaP `30.2533` edge `0.0451` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.4415` n `149` status `ready` deltaP `26.7556` edge `0.0669` maxDD `-0.345`
- `news_risk_high->fx_24h` score `1.6271` n `50` status `ready` deltaP `8.0694` edge `0.086` maxDD `-0.0029`
- `news_risk_high->equity_4h` score `1.5463` n `72` status `ready` deltaP `12.3984` edge `0.1362` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.5385` n `72` status `ready` deltaP `16.7683` edge `0.0383` maxDD `-0.084`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
