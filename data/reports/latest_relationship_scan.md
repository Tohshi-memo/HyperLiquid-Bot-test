# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T13:03:46.812988+00:00`
- Price records: `672`
- Market context records: `5042`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10202`

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

- `market_context_high->unknown_1h` score `11.8192` n `101` status `ready` deltaP `3.6491` edge `1.0107` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.0355` n `93` status `ready` deltaP `22.2118` edge `0.7071` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.5167` n `93` status `ready` deltaP `16.7946` edge `0.5062` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.3624` n `93` status `ready` deltaP `14.4834` edge `0.4897` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.2014` n `93` status `ready` deltaP `12.7819` edge `0.1228` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.7314` n `101` status `ready` deltaP `7.4835` edge `0.0684` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.6995` n `101` status `ready` deltaP `6.6668` edge `0.1056` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.3663` n `93` status `ready` deltaP `2.2063` edge `0.1704` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3226` n `101` status `ready` deltaP `6.1258` edge `0.0357` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1493` n `101` status `ready` deltaP `4.9623` edge `0.0883` maxDD `-5.5126`
- `market_context_high->fx_24h` score `0.0125` n `74` status `ready` deltaP `10.4261` edge `0.0083` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.2324` n `93` status `ready` deltaP `2.6472` edge `0.0391` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.3237` n `101` status `ready` deltaP `1.4511` edge `0.0148` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4197` n `101` status `ready` deltaP `1.2435` edge `0.012` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.761` n `93` status `ready` deltaP `4.1552` edge `0.0` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0252` n `93` status `ready` deltaP `-4.5256` edge `-0.0024` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.5115` n `101` status `ready` deltaP `-8.9909` edge `-0.005` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-3.5832` n `74` status `ready` deltaP `6.9444` edge `0.0398` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.7484` n `74` status `ready` deltaP `-0.6288` edge `-0.0937` maxDD `-27.5371`
- `market_context_high->crypto_major_24h` score `-6.0213` n `74` status `ready` deltaP `14.9822` edge `0.4077` maxDD `-90.3633`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
