# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T13:11:43.216841+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9825`

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

- `market_context_high->equity_24h` score `3.852` n `103` status `ready` deltaP `4.5729` edge `0.5965` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.4816` n `103` status `ready` deltaP `10.6493` edge `0.1934` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.1304` n `143` status `ready` deltaP `14.5947` edge `0.0642` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7654` n `143` status `ready` deltaP `10.5419` edge `0.0278` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7239` n `103` status `ready` deltaP `21.4013` edge `0.0368` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4818` n `103` status `ready` deltaP `7.7113` edge `0.1635` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.3505` n `143` status `ready` deltaP `-0.1957` edge `-0.0047` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.3588` n `143` status `ready` deltaP `3.5468` edge `-0.004` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.5321` n `143` status `ready` deltaP `5.2182` edge `-0.0038` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6488` n `143` status `ready` deltaP `-4.1392` edge `-0.006` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.76` n `143` status `ready` deltaP `0.7612` edge `-0.0079` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.8809` n `143` status `ready` deltaP `0.1121` edge `0.0087` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-0.9654` n `143` status `ready` deltaP `-0.8986` edge `-0.0169` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.8485` n `143` status `ready` deltaP `-9.6845` edge `-0.0253` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.3351` n `143` status `ready` deltaP `0.4105` edge `-0.0636` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.104` n `143` status `ready` deltaP `-10.388` edge `-0.0572` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-3.5851` n `143` status `ready` deltaP `-6.7521` edge `-0.0881` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-3.8461` n `103` status `ready` deltaP `2.7475` edge `-0.0894` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-5.9767` n `103` status `ready` deltaP `-16.6128` edge `-0.243` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.7646` n `143` status `ready` deltaP `-5.495` edge `-0.5657` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
