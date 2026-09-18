# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T18:37:36.445139+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8296`

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

- `market_context_high->unknown_4h` score `39.3892` n `149` status `ready` deltaP `-0.9208` edge `3.3119` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `27.2518` n `36` status `ready` deltaP `32.6389` edge `2.1913` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `15.7933` n `36` status `ready` deltaP `8.3333` edge `2.0878` maxDD `-6.8197`
- `risk_on_high->unknown_4h` score `13.2679` n `52` status `ready` deltaP `-8.1614` edge `1.1826` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.2679` n `52` status `ready` deltaP `-8.1614` edge `1.1826` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.6009` n `52` status `ready` deltaP `47.9167` edge `0.3973` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.6009` n `52` status `ready` deltaP `47.9167` edge `0.3973` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.5601` n `88` status `ready` deltaP `25.4019` edge `0.5816` maxDD `-7.675`
- `market_context_high->commodity_24h` score `7.3018` n `149` status `ready` deltaP `41.2053` edge `0.3863` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.8237` n `52` status `ready` deltaP `32.9972` edge `0.0503` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8237` n `52` status `ready` deltaP `32.9972` edge `0.0503` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7234` n `149` status `ready` deltaP `29.4995` edge `0.0721` maxDD `-0.345`
- `news_risk_high->crypto_major_4h` score `1.8928` n `88` status `ready` deltaP `16.6297` edge `0.3292` maxDD `-12.125`
- `news_risk_high->equity_4h` score `1.7418` n `88` status `ready` deltaP `16.117` edge `0.1277` maxDD `-4.1995`
- `news_risk_high->equity_24h` score `1.7086` n `36` status `ready` deltaP `11.4584` edge `0.263` maxDD `-4.294`
- `market_context_high->commodity_1h` score `1.1313` n `149` status `ready` deltaP `16.3606` edge `0.0229` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `0.8642` n `88` status `ready` deltaP `12.1734` edge `0.0349` maxDD `-1.1898`
- `news_risk_high->fx_4h` score `0.6306` n `88` status `ready` deltaP `9.6591` edge `0.0285` maxDD `-0.2274`
- `news_risk_high->crypto_alt_1h` score `0.5879` n `88` status `ready` deltaP `10.132` edge `0.1114` maxDD `-5.6192`
- `risk_on_high->commodity_1h` score `0.508` n `52` status `ready` deltaP `9.4427` edge `0.0146` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
