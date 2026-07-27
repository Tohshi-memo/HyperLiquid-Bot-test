# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T03:07:29.431047+00:00`
- Price records: `672`
- Market context records: `8051`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11848`

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

- `market_context_high->equity_24h` score `20.2204` n `74` status `ready` deltaP `35.2897` edge `1.5408` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.5401` n `87` status `ready` deltaP `33.3351` edge `0.5374` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.4056` n `74` status `ready` deltaP `35.8752` edge `0.4613` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.7155` n `74` status `ready` deltaP `37.0579` edge `0.3447` maxDD `-6.2367`
- `market_context_high->index_4h` score `3.2857` n `87` status `ready` deltaP `31.5881` edge `0.082` maxDD `-0.5022`
- `market_context_high->index_24h` score `2.5484` n `74` status `ready` deltaP `14.2934` edge `0.1841` maxDD `-1.3621`
- `market_context_high->equity_1h` score `2.5192` n `87` status `ready` deltaP `16.2227` edge `0.1451` maxDD `-2.1322`
- `market_context_high->metal_4h` score `2.301` n `87` status `ready` deltaP `21.1487` edge `0.113` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.4506` n `74` status `ready` deltaP `30.1701` edge `0.0552` maxDD `-0.6283`
- `market_context_high->index_1h` score `1.1362` n `87` status `ready` deltaP `14.9718` edge `0.0216` maxDD `-0.4716`
- `market_context_high->metal_1h` score `0.8338` n `87` status `ready` deltaP `11.6732` edge `0.0295` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.6406` n `87` status `ready` deltaP `9.9198` edge `0.0283` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.5066` n `87` status `ready` deltaP `7.9531` edge `0.161` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.391` n `87` status `ready` deltaP `4.2` edge `0.1163` maxDD `-3.9374`
- `market_context_high->fx_4h` score `0.0477` n `87` status `ready` deltaP `7.5747` edge `0.0059` maxDD `-0.3563`
- `market_context_high->crypto_alt_1h` score `-0.2783` n `87` status `ready` deltaP `0.1738` edge `0.0189` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.4001` n `87` status `ready` deltaP `1.879` edge `-0.0015` maxDD `-1.9855`
- `market_context_high->fx_1h` score `-0.4156` n `87` status `ready` deltaP `-2.6275` edge `0.0006` maxDD `-0.2428`
- `market_context_high->commodity_4h` score `-0.825` n `87` status `ready` deltaP `5.8067` edge `0.0057` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-2.2691` n `87` status `ready` deltaP `4.7181` edge `-0.1782` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
