# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T00:22:27.474247+00:00`
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

- `news_risk_high->unknown_1h` score `440.3224` n `82` status `ready` deltaP `-5.6996` edge `36.7737` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.0446` n `82` status `ready` deltaP `36.8923` edge `1.3899` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3484` n `82` status `ready` deltaP `38.0236` edge `1.4226` maxDD `-9.098`
- `news_risk_high->equity_24h` score `10.4788` n `82` status `ready` deltaP `31.2363` edge `0.843` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.6135` n `82` status `ready` deltaP `55.0084` edge `0.2854` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `5.6498` n `56` status `ready` deltaP `39.8276` edge `0.2053` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.0554` n `82` status `ready` deltaP `29.4155` edge `0.2706` maxDD `-0.6334`
- `market_context_high->fx_24h` score `2.4444` n `56` status `ready` deltaP `48.1774` edge `0.0416` maxDD `-0.9521`
- `risk_on_high->commodity_4h` score `1.8735` n `51` status `ready` deltaP `25.9505` edge `0.0181` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.8735` n `51` status `ready` deltaP `25.9505` edge `0.0181` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.6265` n `125` status `ready` deltaP `21.9976` edge `0.0307` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.4955` n `82` status `ready` deltaP `13.7195` edge `0.0349` maxDD `-0.6935`
- `market_context_high->commodity_1h` score `0.4636` n `137` status `ready` deltaP `9.724` edge `0.0115` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.1677` n `52` status `ready` deltaP `6.299` edge `0.0072` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.1677` n `52` status `ready` deltaP `6.299` edge `0.0072` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.1426` n `125` status `ready` deltaP `8.4012` edge `0.0099` maxDD `-0.1435`
- `risk_on_high->metal_1h` score `0.0454` n `52` status `ready` deltaP `4.7674` edge `0.0046` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.0454` n `52` status `ready` deltaP `4.7674` edge `0.0046` maxDD `-0.1115`
- `market_context_high->fx_1h` score `-0.0518` n `137` status `ready` deltaP `3.7709` edge `-0.0006` maxDD `-0.4945`
- `risk_on_high->fx_1h` score `-0.0782` n `52` status `ready` deltaP `1.9461` edge `0.0024` maxDD `-0.0318`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
