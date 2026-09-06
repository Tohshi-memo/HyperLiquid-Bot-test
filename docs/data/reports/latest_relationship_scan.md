# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T04:37:24.575917+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10815`

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

- `risk_on_high->unknown_4h` score `21.8189` n `145` status `ready` deltaP `-3.4651` edge `2.0419` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `21.8189` n `145` status `ready` deltaP `-3.4651` edge `2.0419` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.3517` n `245` status `ready` deltaP `1.0951` edge `0.9355` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `4.2227` n `37` status `ready` deltaP `21.5325` edge `0.2353` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.9763` n `37` status `ready` deltaP `20.1389` edge `0.1971` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.1549` n `37` status `ready` deltaP `15.8084` edge `0.1988` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.5271` n `37` status `ready` deltaP `25.9806` edge `0.0595` maxDD `-0.7692`
- `market_context_high->equity_24h` score `1.729` n `167` status `ready` deltaP `13.6685` edge `0.4068` maxDD `-16.9737`
- `news_risk_high->equity_1h` score `1.5715` n `37` status `ready` deltaP `12.935` edge `0.0838` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.5454` n `37` status `ready` deltaP `7.4654` edge `0.0991` maxDD `-0.2737`
- `risk_on_high->crypto_major_24h` score `1.3484` n `84` status `ready` deltaP `11.6071` edge `0.8281` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `1.3484` n `84` status `ready` deltaP `11.6071` edge `0.8281` maxDD `-47.9416`
- `news_risk_high->metal_1h` score `1.3448` n `37` status `ready` deltaP `16.0625` edge `0.0243` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1634` n `37` status `ready` deltaP `14.5736` edge `0.0132` maxDD `-0.0724`
- `news_risk_high->fx_24h` score `1.1042` n `37` status `ready` deltaP `21.8656` edge `0.0478` maxDD `-3.1244`
- `news_risk_high->crypto_major_1h` score `1.0528` n `37` status `ready` deltaP `5.5673` edge `0.0689` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.8002` n `37` status `ready` deltaP `8.4278` edge `0.037` maxDD `-0.7867`
- `news_risk_high->commodity_1h` score `-0.0208` n `37` status `ready` deltaP `5.8748` edge `0.0028` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1154` n `145` status `ready` deltaP `4.937` edge `-0.003` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1154` n `145` status `ready` deltaP `4.937` edge `-0.003` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
