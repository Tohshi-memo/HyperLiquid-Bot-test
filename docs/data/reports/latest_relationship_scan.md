# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T20:37:34.550207+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11235`

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

- `news_risk_high->unknown_4h` score `369.66` n `83` status `ready` deltaP `-20.9007` edge `31.0338` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `18.6634` n `83` status `ready` deltaP `42.3444` edge `1.4109` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `17.1393` n `83` status `ready` deltaP `34.9314` edge `1.3949` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `13.4894` n `83` status `ready` deltaP `44.1642` edge `1.0071` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.0887` n `83` status `ready` deltaP `49.5942` edge `0.2777` maxDD `-0.075`
- `risk_on_high->commodity_24h` score `6.4272` n `52` status `ready` deltaP `38.7153` edge `0.2775` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.4272` n `52` status `ready` deltaP `38.7153` edge `0.2775` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.3218` n `83` status `ready` deltaP `32.6849` edge `0.271` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `5.1281` n `149` status `ready` deltaP `32.0039` edge `0.2665` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.436` n `52` status `ready` deltaP `30.1008` edge `0.0373` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.436` n `52` status `ready` deltaP `30.1008` edge `0.0373` maxDD `-0.1313`
- `risk_on_high->fx_24h` score `2.4132` n `52` status `ready` deltaP `32.1047` edge `-0.0087` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4132` n `52` status `ready` deltaP `32.1047` edge `-0.0087` maxDD `-0.0054`
- `market_context_high->commodity_4h` score `2.3357` n `149` status `ready` deltaP `26.6031` edge `0.0591` maxDD `-0.345`
- `market_context_high->fx_24h` score `2.2783` n `149` status `ready` deltaP `29.3298` edge `0.0159` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `0.9444` n `149` status `ready` deltaP `14.5642` edge `0.0193` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3982` n `83` status `ready` deltaP `12.1933` edge `0.0326` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3211` n `52` status `ready` deltaP `7.6463` edge `0.011` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3211` n `52` status `ready` deltaP `7.6463` edge `0.011` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1794` n `52` status `ready` deltaP `6.7135` edge `0.0088` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
