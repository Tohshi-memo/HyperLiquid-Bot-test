# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T17:12:53.587338+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11757`

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

- `market_context_high->metal_24h` score `2.5915` n `101` status `ready` deltaP `11.0633` edge `0.1998` maxDD `-2.2743`
- `market_context_high->fx_24h` score `0.6752` n `101` status `ready` deltaP `22.7037` edge `0.0481` maxDD `-3.698`
- `market_context_high->commodity_4h` score `0.4349` n `109` status `ready` deltaP `10.2428` edge `0.0721` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.3762` n `121` status `ready` deltaP `9.5759` edge `0.026` maxDD `-1.3282`
- `market_context_high->index_24h` score `0.1127` n `101` status `ready` deltaP `4.9204` edge `0.1279` maxDD `-5.7715`
- `market_context_high->fx_4h` score `0.0974` n `109` status `ready` deltaP `9.3113` edge `0.0047` maxDD `-1.6928`
- `market_context_high->fx_1h` score `-0.2101` n `121` status `ready` deltaP `5.1443` edge `-0.0052` maxDD `-1.0616`
- `market_context_high->metal_1h` score `-0.569` n `121` status `ready` deltaP `-3.5507` edge `-0.0078` maxDD `-0.9852`
- `market_context_high->index_1h` score `-0.7959` n `121` status `ready` deltaP `-1.8978` edge `-0.011` maxDD `-1.4136`
- `market_context_high->metal_4h` score `-0.8263` n `109` status `ready` deltaP `2.9397` edge `0.0053` maxDD `-2.1669`
- `market_context_high->index_4h` score `-0.8322` n `109` status `ready` deltaP `-2.4349` edge `-0.0161` maxDD `-2.2826`
- `market_context_high->crypto_alt_1h` score `-0.842` n `121` status `ready` deltaP `-5.2098` edge `-0.0103` maxDD `-2.3669`
- `market_context_high->equity_1h` score `-1.2964` n `121` status `ready` deltaP `2.9173` edge `-0.0348` maxDD `-10.0678`
- `market_context_high->crypto_alt_4h` score `-1.8377` n `109` status `ready` deltaP `1.3874` edge `-0.0234` maxDD `-5.7857`
- `market_context_high->equity_24h` score `-1.9711` n `101` status `ready` deltaP `-6.7351` edge `0.3333` maxDD `-29.2127`
- `market_context_high->crypto_major_1h` score `-2.7017` n `121` status `ready` deltaP `-6.7254` edge `-0.0506` maxDD `-7.0428`
- `market_context_high->crypto_alt_24h` score `-4.1038` n `101` status `ready` deltaP `-13.4216` edge `-0.1082` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.1956` n `101` status `ready` deltaP `-1.8648` edge `-0.2167` maxDD `-17.7015`
- `market_context_high->crypto_major_4h` score `-4.5265` n `109` status `ready` deltaP `-7.6485` edge `-0.1814` maxDD `-21.5015`
- `market_context_high->equity_4h` score `-5.1191` n `109` status `ready` deltaP `3.9956` edge `-0.1587` maxDD `-20.2293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
