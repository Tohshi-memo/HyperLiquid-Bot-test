# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T04:22:31.021635+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10952`

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

- `market_context_high->commodity_4h` score `1.4242` n `165` status `ready` deltaP `16.0162` edge `0.0792` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.8827` n `140` status `ready` deltaP `19.5189` edge `0.0242` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.7354` n `173` status `ready` deltaP `9.8828` edge `0.0297` maxDD `-0.7439`
- `market_context_high->fx_4h` score `-0.1131` n `165` status `ready` deltaP `7.1111` edge `0.0063` maxDD `-1.1228`
- `market_context_high->fx_1h` score `-0.1521` n `173` status `ready` deltaP `4.4642` edge `-0.0006` maxDD `-0.8933`
- `market_context_high->index_24h` score `-0.6164` n `140` status `ready` deltaP `2.3512` edge `0.0861` maxDD `-5.9181`
- `market_context_high->index_4h` score `-0.7638` n `165` status `ready` deltaP `-1.5558` edge `-0.0093` maxDD `-1.26`
- `market_context_high->metal_1h` score `-0.8334` n `173` status `ready` deltaP `-4.9712` edge `-0.0101` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-0.8342` n `173` status `ready` deltaP `-2.1183` edge `-0.0058` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.8582` n `173` status `ready` deltaP `-2.8962` edge `-0.0045` maxDD `-0.8168`
- `market_context_high->crypto_alt_1h` score `-1.5417` n `173` status `ready` deltaP `-8.7804` edge `-0.037` maxDD `-5.5029`
- `market_context_high->metal_24h` score `-1.5571` n `140` status `ready` deltaP `-4.38` edge `0.0276` maxDD `-2.9193`
- `market_context_high->equity_24h` score `-1.7627` n `140` status `ready` deltaP `-2.4107` edge `0.1835` maxDD `-21.1456`
- `market_context_high->metal_4h` score `-2.0699` n `165` status `ready` deltaP `-7.9472` edge `-0.036` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-2.7919` n `165` status `ready` deltaP `-8.2409` edge `-0.1026` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.5585` n `173` status `ready` deltaP `-9.8785` edge `-0.0573` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-3.9708` n `165` status `ready` deltaP `-11.7174` edge `-0.1552` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.345` n `140` status `ready` deltaP `-11.0367` edge `-0.1442` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.9291` n `140` status `ready` deltaP `-3.1696` edge `-0.1402` maxDD `-14.2873`
- `market_context_high->unknown_1h` score `-7.5152` n `173` status `ready` deltaP `-4.6139` edge `-0.5498` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
