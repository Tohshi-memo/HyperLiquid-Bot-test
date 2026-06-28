# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T17:52:27.547672+00:00`
- Price records: `672`
- Market context records: `5064`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10310`

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

- `market_context_high->unknown_1h` score `13.1443` n `97` status `ready` deltaP `2.8428` edge `1.1265` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.0914` n `97` status `ready` deltaP `20.7207` edge `0.7217` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `6.2196` n `97` status `ready` deltaP `18.4546` edge `0.5172` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `5.555` n `97` status `ready` deltaP `17.0025` edge `0.508` maxDD `-8.3416`
- `market_context_high->crypto_major_1h` score `1.1659` n `97` status `ready` deltaP `8.5483` edge `0.1218` maxDD `-3.8637`
- `market_context_high->metal_4h` score `0.9812` n `97` status `ready` deltaP `10.5843` edge `0.1191` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8747` n `97` status `ready` deltaP `8.6302` edge `0.0727` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.7074` n `97` status `ready` deltaP `6.0112` edge `0.1721` maxDD `-6.3852`
- `market_context_high->crypto_alt_1h` score `0.6475` n `97` status `ready` deltaP `6.735` edge `0.1014` maxDD `-4.7207`
- `market_context_high->metal_1h` score `0.4292` n `97` status `ready` deltaP `7.218` edge `0.0373` maxDD `-1.3057`
- `market_context_high->index_4h` score `0.0234` n `97` status `ready` deltaP `5.8147` edge `0.0393` maxDD `-1.0893`
- `market_context_high->fx_24h` score `-0.1394` n `75` status `ready` deltaP `7.625` edge `0.0075` maxDD `-1.7626`
- `market_context_high->index_1h` score `-0.2821` n `97` status `ready` deltaP `1.8458` edge `0.0126` maxDD `-0.552`
- `market_context_high->commodity_1h` score `-0.551` n `97` status `ready` deltaP `0.8488` edge `0.0144` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.8407` n `97` status `ready` deltaP `7.2951` edge `0.0062` maxDD `-4.9914`
- `market_context_high->fx_4h` score `-0.9417` n `97` status `ready` deltaP `-3.2232` edge `-0.0003` maxDD `-1.2484`
- `market_context_high->unknown_24h` score `-1.1634` n `75` status `ready` deltaP `27.1805` edge `-0.2439` maxDD `-1.4072`
- `market_context_high->fx_1h` score `-1.4567` n `97` status `ready` deltaP `-8.4295` edge `-0.0042` maxDD `-0.5464`
- `market_context_high->metal_24h` score `-3.7198` n `75` status `ready` deltaP `4.2431` edge `0.0403` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-3.9316` n `75` status `ready` deltaP `2.2708` edge `-0.0651` maxDD `-24.3277`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
