# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T11:07:35.288536+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10695`

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

- `risk_on_high->crypto_major_24h` score `2.2307` n `107` status `ready` deltaP `15.7937` edge `0.9133` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `2.2307` n `107` status `ready` deltaP `15.7937` edge `0.9133` maxDD `-47.9416`
- `market_context_high->equity_24h` score `0.5853` n `193` status `ready` deltaP `11.8973` edge `0.3233` maxDD `-16.9737`
- `risk_on_high->metal_1h` score `-0.1052` n `145` status `ready` deltaP `8.6475` edge `0.0001` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.1052` n `145` status `ready` deltaP `8.6475` edge `0.0001` maxDD `-1.699`
- `risk_on_high->index_1h` score `-0.1084` n `145` status `ready` deltaP `5.0867` edge `-0.0031` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1084` n `145` status `ready` deltaP `5.0867` edge `-0.0031` maxDD `-0.5764`
- `risk_on_high->crypto_alt_1h` score `-0.4228` n `145` status `ready` deltaP `1.7933` edge `0.0545` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.4228` n `145` status `ready` deltaP `1.7933` edge `0.0545` maxDD `-5.4685`
- `risk_on_high->equity_1h` score `-0.4517` n `145` status `ready` deltaP `6.3535` edge `-0.0128` maxDD `-2.6638`
- `risk_on_and_context->equity_1h` score `-0.4517` n `145` status `ready` deltaP `6.3535` edge `-0.0128` maxDD `-2.6638`
- `risk_on_high->commodity_1h` score `-0.5758` n `145` status `ready` deltaP `0.3552` edge `0.0` maxDD `-1.0281`
- `risk_on_and_context->commodity_1h` score `-0.5758` n `145` status `ready` deltaP `0.3552` edge `0.0` maxDD `-1.0281`
- `market_context_high->commodity_1h` score `-0.7406` n `250` status `ready` deltaP `0.7138` edge `-0.0015` maxDD `-1.5315`
- `risk_on_high->crypto_major_1h` score `-0.7842` n `145` status `ready` deltaP `1.1305` edge `0.022` maxDD `-7.4065`
- `risk_on_and_context->crypto_major_1h` score `-0.7842` n `145` status `ready` deltaP `1.1305` edge `0.022` maxDD `-7.4065`
- `market_context_high->metal_1h` score `-0.8995` n `250` status `ready` deltaP `4.0958` edge `-0.0065` maxDD `-2.9947`
- `market_context_high->index_1h` score `-1.062` n `250` status `ready` deltaP `3.1557` edge `0.0009` maxDD `-3.1683`
- `market_context_high->index_4h` score `-1.1641` n `250` status `ready` deltaP `6.511` edge `0.001` maxDD `-5.825`
- `risk_on_high->metal_4h` score `-1.2425` n `145` status `ready` deltaP `3.4009` edge `-0.0004` maxDD `-5.1925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
