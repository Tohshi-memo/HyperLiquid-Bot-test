# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T02:52:26.526703+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `risk_on_high->unknown_4h` score `7.6204` n `107` status `ready` deltaP `23.2691` edge `0.5417` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.6204` n `107` status `ready` deltaP `23.2691` edge `0.5417` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `6.0018` n `153` status `ready` deltaP `19.1765` edge `0.4418` maxDD `-2.5597`
- `market_context_high->unknown_1h` score `2.0342` n `153` status `ready` deltaP `4.5664` edge `0.2021` maxDD `-2.042`
- `risk_on_high->unknown_1h` score `2.017` n `107` status `ready` deltaP `4.7191` edge `0.1943` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.017` n `107` status `ready` deltaP `4.7191` edge `0.1943` maxDD `-1.9475`
- `risk_on_high->commodity_24h` score `1.613` n `104` status `ready` deltaP `13.742` edge `0.1416` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.613` n `104` status `ready` deltaP `13.742` edge `0.1416` maxDD `-0.5706`
- `risk_on_high->crypto_alt_24h` score `1.1245` n `104` status `ready` deltaP `14.3296` edge `0.739` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.1245` n `104` status `ready` deltaP `14.3296` edge `0.739` maxDD `-42.8959`
- `news_risk_high->unknown_1h` score `1.111` n `61` status `ready` deltaP `1.8234` edge `0.1151` maxDD `-1.1072`
- `market_context_high->commodity_24h` score `0.6667` n `150` status `ready` deltaP `12.2291` edge `0.1014` maxDD `-1.8565`
- `news_risk_high->commodity_4h` score `0.1388` n `61` status `ready` deltaP `5.6627` edge `0.0217` maxDD `-1.3325`
- `news_risk_high->fx_4h` score `0.1353` n `61` status `ready` deltaP `10.5008` edge `0.0006` maxDD `-0.7461`
- `risk_on_high->fx_24h` score `0.1226` n `104` status `ready` deltaP `37.2596` edge `0.0237` maxDD `-4.1767`
- `risk_on_and_context->fx_24h` score `0.1226` n `104` status `ready` deltaP `37.2596` edge `0.0237` maxDD `-4.1767`
- `market_context_high->commodity_1h` score `0.0586` n `153` status `ready` deltaP `8.1993` edge `0.0152` maxDD `-1.5315`
- `risk_on_high->commodity_1h` score `0.0185` n `107` status `ready` deltaP `5.9209` edge `0.0151` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `0.0185` n `107` status `ready` deltaP `5.9209` edge `0.0151` maxDD `-0.8428`
- `market_context_high->commodity_4h` score `-0.0231` n `153` status `ready` deltaP `6.1234` edge `0.047` maxDD `-2.1795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
