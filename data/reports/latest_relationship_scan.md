# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T17:22:26.125111+00:00`
- Price records: `672`
- Market context records: `5061`
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
- `market_context_high->unknown_4h` score `9.071` n `97` status `ready` deltaP `20.7207` edge `0.72` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `6.24` n `97` status `ready` deltaP `18.4546` edge `0.5189` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `5.5514` n `97` status `ready` deltaP `17.0025` edge `0.5077` maxDD `-8.3416`
- `market_context_high->crypto_major_1h` score `1.1467` n `97` status `ready` deltaP `8.3986` edge `0.1212` maxDD `-3.8637`
- `market_context_high->metal_4h` score `0.9848` n `97` status `ready` deltaP `10.5843` edge `0.1194` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8747` n `97` status `ready` deltaP `8.6302` edge `0.0727` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.7074` n `97` status `ready` deltaP `6.0112` edge `0.1721` maxDD `-6.3852`
- `market_context_high->crypto_alt_1h` score `0.6187` n `97` status `ready` deltaP `6.4356` edge `0.101` maxDD `-4.7207`
- `market_context_high->metal_1h` score `0.4567` n `97` status `ready` deltaP `7.5174` edge `0.0376` maxDD `-1.3057`
- `market_context_high->index_4h` score `0.0234` n `97` status `ready` deltaP `5.8147` edge `0.0393` maxDD `-1.0893`
- `market_context_high->fx_24h` score `-0.1154` n `74` status `ready` deltaP `8.0706` edge `0.0076` maxDD `-1.7626`
- `market_context_high->index_1h` score `-0.2743` n `97` status `ready` deltaP `1.9955` edge `0.0126` maxDD `-0.552`
- `market_context_high->commodity_1h` score `-0.5809` n `97` status `ready` deltaP `0.5494` edge `0.0139` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.8601` n `97` status `ready` deltaP `7.1426` edge `0.0056` maxDD `-4.9914`
- `market_context_high->fx_4h` score `-0.9409` n `97` status `ready` deltaP `-3.2232` edge `-0.0002` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.4699` n `97` status `ready` deltaP `-8.5792` edge `-0.0043` maxDD `-0.5464`
- `market_context_high->unknown_24h` score `-2.7638` n `74` status `ready` deltaP `27.0364` edge `-0.3763` maxDD `-1.4072`
- `market_context_high->metal_24h` score `-3.7366` n `74` status `ready` deltaP `4.4904` edge `0.0365` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-3.979` n `74` status `ready` deltaP `1.8252` edge `-0.0682` maxDD `-24.3277`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
