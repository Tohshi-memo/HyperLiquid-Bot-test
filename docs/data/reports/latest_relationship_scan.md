# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T00:37:32.058002+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12438`

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

- `news_risk_high->unknown_1h` score `440.1004` n `82` status `ready` deltaP `-5.6996` edge `36.7552` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.0662` n `82` status `ready` deltaP `36.8923` edge `1.3917` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3424` n `82` status `ready` deltaP `38.0236` edge `1.4221` maxDD `-9.098`
- `news_risk_high->equity_24h` score `10.5382` n `82` status `ready` deltaP `31.4088` edge `0.8468` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.6369` n `82` status `ready` deltaP `55.1808` edge `0.2862` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `5.7494` n `56` status `ready` deltaP `39.8276` edge `0.2136` maxDD `0.0`
- `risk_on_high->fx_24h` score `5.5851` n `30` status `ready` deltaP `62.5288` edge `0.0528` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.5851` n `30` status `ready` deltaP `62.5288` edge `0.0528` maxDD `-0.0054`
- `risk_on_high->commodity_24h` score `5.1182` n `30` status `ready` deltaP `39.8276` edge `0.161` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.1182` n `30` status `ready` deltaP `39.8276` edge `0.161` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.0752` n `82` status `ready` deltaP `29.5879` edge `0.2711` maxDD `-0.6334`
- `risk_on_high->crypto_alt_24h` score `2.7827` n `30` status `ready` deltaP `0.6322` edge `0.3549` maxDD `-6.5115`
- `risk_on_and_context->crypto_alt_24h` score `2.7827` n `30` status `ready` deltaP `0.6322` edge `0.3549` maxDD `-6.5115`
- `market_context_high->fx_24h` score `2.6138` n `56` status `ready` deltaP `49.7907` edge `0.0459` maxDD `-0.7524`
- `risk_on_high->commodity_4h` score `1.8663` n `51` status `ready` deltaP `25.9505` edge `0.0175` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.8663` n `51` status `ready` deltaP `25.9505` edge `0.0175` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.6589` n `125` status `ready` deltaP `21.9976` edge `0.0334` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.5196` n `137` status `ready` deltaP `10.3042` edge `0.0123` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5058` n `82` status `ready` deltaP `13.8719` edge `0.0352` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.1804` n `125` status `ready` deltaP `9.0488` edge `0.0104` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
