# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T11:22:24.122617+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7870`

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

- `market_context_high->crypto_alt_24h` score `24.7766` n `42` status `ready` deltaP `25.9672` edge `2.0097` maxDD `-6.448`
- `market_context_high->crypto_major_24h` score `24.7162` n `42` status `ready` deltaP `37.5992` edge `1.896` maxDD `-3.9584`
- `market_context_high->unknown_4h` score `8.2942` n `108` status `ready` deltaP `-4.0481` edge `0.7828` maxDD `-1.8373`
- `risk_on_high->crypto_alt_4h` score `3.8232` n `48` status `ready` deltaP `18.1911` edge `0.2421` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `3.8232` n `48` status `ready` deltaP `18.1911` edge `0.2421` maxDD `-1.9151`
- `market_context_high->unknown_1h` score `3.5736` n `108` status `ready` deltaP `-3.7148` edge `0.3562` maxDD `-1.024`
- `risk_on_high->crypto_major_4h` score `3.4519` n `48` status `ready` deltaP `32.6728` edge `0.31` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.4519` n `48` status `ready` deltaP `32.6728` edge `0.31` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `2.2116` n `108` status `ready` deltaP `14.6172` edge `0.2664` maxDD `-8.6974`
- `market_context_high->metal_24h` score `2.0703` n `42` status `ready` deltaP `21.2797` edge `0.0784` maxDD `-1.1526`
- `market_context_high->equity_24h` score `1.8632` n `42` status `ready` deltaP `-2.2818` edge `0.4141` maxDD `-8.8011`
- `market_context_high->crypto_alt_4h` score `1.5901` n `108` status `ready` deltaP `8.2374` edge `0.2738` maxDD `-11.6965`
- `market_context_high->index_24h` score `1.4073` n `42` status `ready` deltaP `21.4038` edge `0.0999` maxDD `-0.6397`
- `market_context_high->crypto_alt_1h` score `1.2465` n `108` status `ready` deltaP `10.2684` edge `0.1305` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.8124` n `48` status `ready` deltaP `5.6387` edge `0.0898` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.8124` n `48` status `ready` deltaP `5.6387` edge `0.0898` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.4917` n `108` status `ready` deltaP `4.0031` edge `0.0906` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.3197` n `48` status `ready` deltaP `4.4661` edge `0.0765` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.3197` n `48` status `ready` deltaP `4.4661` edge `0.0765` maxDD `-3.2233`
- `market_context_high->index_1h` score `-0.0863` n `108` status `ready` deltaP `2.9552` edge `0.0023` maxDD `-0.3122`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
