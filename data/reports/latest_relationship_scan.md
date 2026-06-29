# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T09:56:39.528249+00:00`
- Price records: `672`
- Market context records: `5133`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5568`

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

- `market_context_high->unknown_24h` score `29.9414` n `62` status `ready` deltaP `29.1107` edge `2.3353` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.0` n `129` status `ready` deltaP `8.642` edge `0.6732` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.2997` n `120` status `ready` deltaP `20.2845` edge `0.5753` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.0064` n `120` status `ready` deltaP `14.8069` edge `0.4784` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.5512` n `120` status `ready` deltaP `12.6118` edge `0.4411` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `1.6923` n `62` status `ready` deltaP `21.2365` edge `0.1612` maxDD `-4.1987`
- `market_context_high->equity_4h` score `0.8169` n `120` status `ready` deltaP `8.496` edge `0.1753` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.696` n `129` status `ready` deltaP `4.9587` edge `0.1211` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.6132` n `129` status `ready` deltaP `7.3272` edge `0.1268` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.5743` n `129` status `ready` deltaP `6.5358` edge `0.0636` maxDD `-2.745`
- `market_context_high->metal_24h` score `0.2171` n `62` status `ready` deltaP `1.5569` edge `0.2087` maxDD `-11.4122`
- `market_context_high->metal_1h` score `0.0036` n `129` status `ready` deltaP `5.178` edge `0.0174` maxDD `-1.4501`
- `market_context_high->index_1h` score `-0.1047` n `129` status `ready` deltaP `4.0872` edge `0.0144` maxDD `-1.0296`
- `market_context_high->crypto_alt_24h` score `-0.4493` n `62` status `ready` deltaP `15.0762` edge `0.5432` maxDD `-50.438`
- `market_context_high->index_4h` score `-0.4624` n `120` status `ready` deltaP `5.6402` edge `0.0356` maxDD `-2.9391`
- `market_context_high->commodity_1h` score `-0.4935` n `129` status `ready` deltaP `1.8846` edge `0.0011` maxDD `-2.155`
- `market_context_high->metal_4h` score `-0.5783` n `120` status `ready` deltaP `2.3984` edge `0.0509` maxDD `-4.6157`
- `market_context_high->fx_1h` score `-0.6919` n `129` status `ready` deltaP `-3.3921` edge `-0.002` maxDD `-0.7944`
- `market_context_high->fx_4h` score `-0.9781` n `120` status `ready` deltaP `-2.8049` edge `0.0006` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.1325` n `62` status `ready` deltaP `0.3976` edge `-0.0055` maxDD `-0.9885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
