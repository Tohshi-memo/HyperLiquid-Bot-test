# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T00:06:01.002180+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10545`

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

- `risk_on_high->unknown_24h` score `339.8165` n `106` status `ready` deltaP `26.7361` edge `28.1398` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `339.8165` n `106` status `ready` deltaP `26.7361` edge `28.1398` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `19.4365` n `106` status `ready` deltaP `33.8705` edge `1.4456` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `19.4365` n `106` status `ready` deltaP `33.8705` edge `1.4456` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `13.5976` n `106` status `ready` deltaP `30.0347` edge `0.9329` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.5976` n `106` status `ready` deltaP `30.0347` edge `0.9329` maxDD `0.0`
- `market_context_high->unknown_1h` score `12.2774` n `250` status `ready` deltaP `-4.6096` edge `1.1263` maxDD `-2.4626`
- `market_context_high->crypto_alt_24h` score `8.7422` n `196` status `ready` deltaP `23.9123` edge `0.6266` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.6616` n `196` status `ready` deltaP `23.0903` edge `0.4012` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `6.3148` n `122` status `ready` deltaP `29.8581` edge `0.3328` maxDD `-0.116`
- `risk_on_and_context->crypto_alt_4h` score `6.3148` n `122` status `ready` deltaP `29.8581` edge `0.3328` maxDD `-0.116`
- `risk_on_high->equity_24h` score `5.8144` n `106` status `ready` deltaP `23.0903` edge `0.3306` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.8144` n `106` status `ready` deltaP `23.0903` edge `0.3306` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.2236` n `122` status `ready` deltaP `23.7355` edge `0.2796` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.2236` n `122` status `ready` deltaP `23.7355` edge `0.2796` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.7728` n `106` status `ready` deltaP `23.3851` edge `0.0794` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.7728` n `106` status `ready` deltaP `23.3851` edge `0.0794` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.6075` n `196` status `ready` deltaP `21.6235` edge `0.0946` maxDD `-0.0505`
- `risk_on_high->crypto_alt_1h` score `0.7446` n `130` status `ready` deltaP `3.7333` edge `0.0724` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.7446` n `130` status `ready` deltaP `3.7333` edge `0.0724` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
