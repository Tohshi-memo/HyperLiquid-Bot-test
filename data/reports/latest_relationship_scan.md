# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T16:07:32.138457+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `7312`

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

- `market_context_high->unknown_24h` score `1381.4502` n `40` status `ready` deltaP `-19.6181` edge `115.288` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `52.9852` n `76` status `ready` deltaP `-7.2769` edge `4.522` maxDD `-2.3109`
- `market_context_high->unknown_1h` score `12.2479` n `85` status `ready` deltaP `-4.3677` edge `1.0834` maxDD `-1.0231`
- `market_context_high->equity_24h` score `8.8634` n `40` status `ready` deltaP `28.0208` edge `0.5947` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.4146` n `40` status `ready` deltaP `52.7778` edge `0.1827` maxDD `0.0`
- `market_context_high->fx_24h` score `3.4157` n `40` status `ready` deltaP `38.5069` edge `0.0409` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.6645` n `40` status `ready` deltaP `-20.5903` edge `0.5908` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.8427` n `76` status `ready` deltaP `13.5431` edge `0.0083` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.5523` n `76` status `ready` deltaP `12.6685` edge `0.0149` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `0.3325` n `85` status `ready` deltaP `5.6587` edge `0.0934` maxDD `-4.9401`
- `market_context_high->commodity_1h` score `0.0296` n `85` status `ready` deltaP `3.7549` edge `0.0058` maxDD `-0.6025`
- `market_context_high->fx_1h` score `-0.0717` n `85` status `ready` deltaP `2.5573` edge `0.0012` maxDD `-0.271`
- `market_context_high->metal_4h` score `-0.2762` n `76` status `ready` deltaP `2.5754` edge `0.0197` maxDD `-1.1153`
- `market_context_high->crypto_major_1h` score `-0.2941` n `85` status `ready` deltaP `0.4174` edge `0.0484` maxDD `-3.7778`
- `market_context_high->metal_1h` score `-0.3362` n `85` status `ready` deltaP `4.2251` edge `0.0027` maxDD `-0.7107`
- `market_context_high->index_1h` score `-0.7454` n `85` status `ready` deltaP `-4.1388` edge `-0.0029` maxDD `-0.5392`
- `market_context_high->index_4h` score `-0.9026` n `76` status `ready` deltaP `-7.0925` edge `0.0016` maxDD `-0.9364`
- `market_context_high->crypto_major_4h` score `-1.0314` n `76` status `ready` deltaP `-4.541` edge `0.1086` maxDD `-11.1784`
- `market_context_high->equity_1h` score `-1.1515` n `85` status `ready` deltaP `-8.3515` edge `-0.005` maxDD `-2.2898`
- `market_context_high->crypto_alt_4h` score `-2.2767` n `76` status `ready` deltaP `-7.6621` edge `0.1172` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
