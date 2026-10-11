# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T14:37:32.763543+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `7318`

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

- `market_context_high->unknown_24h` score `1090.7344` n `43` status `ready` deltaP `-17.7002` edge `91.0489` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `51.8339` n `75` status `ready` deltaP `-8.6037` edge `4.4349` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.8937` n `43` status `ready` deltaP `29.7642` edge `0.5856` maxDD `-1.0977`
- `market_context_high->unknown_1h` score `7.3911` n `82` status `ready` deltaP `-5.2285` edge `0.6844` maxDD `-1.0231`
- `market_context_high->index_24h` score `5.5411` n `43` status `ready` deltaP `45.9747` edge `0.1698` maxDD `-0.1632`
- `market_context_high->crypto_major_24h` score `3.041` n `43` status `ready` deltaP `-15.3545` edge `0.6706` maxDD `-17.8526`
- `market_context_high->fx_24h` score `2.8974` n `43` status `ready` deltaP `33.0951` edge `0.0353` maxDD `-0.1588`
- `market_context_high->fx_4h` score `1.0075` n `75` status `ready` deltaP `15.4838` edge `0.0091` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.53` n `75` status `ready` deltaP `12.435` edge `0.0146` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.0501` n `82` status `ready` deltaP `3.7243` edge `0.0052` maxDD `-0.4015`
- `market_context_high->fx_1h` score `-0.233` n `82` status `ready` deltaP `-0.9822` edge `0.0009` maxDD `-0.271`
- `market_context_high->crypto_alt_1h` score `-0.3202` n `82` status `ready` deltaP `3.4249` edge `0.0539` maxDD `-4.9401`
- `market_context_high->metal_1h` score `-0.4444` n `82` status `ready` deltaP `2.9319` edge `0.0024` maxDD `-0.7181`
- `market_context_high->metal_4h` score `-0.4748` n `75` status `ready` deltaP `-1.124` edge `0.0189` maxDD `-1.1153`
- `market_context_high->crypto_major_1h` score `-0.9829` n `82` status `ready` deltaP `-1.968` edge `0.0201` maxDD `-3.7778`
- `market_context_high->index_1h` score `-1.0522` n `82` status `ready` deltaP `-8.0656` edge `-0.0034` maxDD `-0.5514`
- `market_context_high->index_4h` score `-1.1198` n `75` status `ready` deltaP `-10.9146` edge `0.0001` maxDD `-1.0053`
- `market_context_high->equity_1h` score `-1.275` n `82` status `ready` deltaP `-10.0956` edge `-0.0092` maxDD `-2.2898`
- `market_context_high->crypto_major_4h` score `-1.3803` n `75` status `ready` deltaP `-6.4939` edge `0.0769` maxDD `-11.1784`
- `market_context_high->crypto_alt_4h` score `-2.034` n `75` status `ready` deltaP `-8.0589` edge `0.0488` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
