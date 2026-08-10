# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T02:22:28.775997+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10938`

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

- `market_context_high->commodity_4h` score `1.3886` n `159` status `ready` deltaP `15.4672` edge `0.0799` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8574` n `171` status `ready` deltaP `11.1978` edge `0.0311` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.5163` n `138` status `ready` deltaP `19.0444` edge `0.0227` maxDD `-1.678`
- `market_context_high->fx_1h` score `-0.1903` n `171` status `ready` deltaP `3.9229` edge `-0.001` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.2792` n `159` status `ready` deltaP `5.5175` edge `0.0027` maxDD `-1.6892`
- `market_context_high->index_24h` score `-0.5758` n `138` status `ready` deltaP `2.4985` edge `0.0885` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.5772` n `171` status `ready` deltaP `-3.1787` edge `-0.0051` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.8337` n `171` status `ready` deltaP `-4.7974` edge `-0.0113` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-0.8435` n `171` status `ready` deltaP `-2.3129` edge `-0.0057` maxDD `-4.6286`
- `market_context_high->index_4h` score `-0.8734` n `159` status `ready` deltaP `-3.4389` edge `-0.0108` maxDD `-1.26`
- `market_context_high->metal_24h` score `-1.1172` n `138` status `ready` deltaP `-3.3137` edge `0.0334` maxDD `-2.3529`
- `market_context_high->equity_24h` score `-1.3181` n `138` status `ready` deltaP `-1.253` edge `0.2045` maxDD `-21.1456`
- `market_context_high->crypto_alt_1h` score `-1.5488` n `171` status `ready` deltaP `-8.7973` edge `-0.0378` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.6726` n `159` status `ready` deltaP `-6.411` edge `-0.0333` maxDD `-5.4046`
- `market_context_high->equity_4h` score `-2.3469` n `159` status `ready` deltaP `-6.2586` edge `-0.0921` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-2.3696` n `171` status `ready` deltaP `-10.5613` edge `-0.06` maxDD `-10.5372`
- `market_context_high->crypto_alt_24h` score `-4.3504` n `138` status `ready` deltaP `-11.1036` edge `-0.1442` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.7344` n `138` status `ready` deltaP `-1.4719` edge `-0.1353` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-6.1241` n `159` status `ready` deltaP `-12.339` edge `-0.1635` maxDD `-14.5001`
- `market_context_high->unknown_1h` score `-7.5341` n `171` status `ready` deltaP `-4.6854` edge `-0.5509` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
