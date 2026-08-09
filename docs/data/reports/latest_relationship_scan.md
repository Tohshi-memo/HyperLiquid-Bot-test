# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T23:07:25.682708+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10906`

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

- `market_context_high->commodity_4h` score `1.2073` n `147` status `ready` deltaP `14.9556` edge `0.0682` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8362` n `159` status `ready` deltaP `10.8274` edge `0.0318` maxDD `-0.7439`
- `market_context_high->metal_24h` score `0.6528` n `126` status `ready` deltaP `3.7946` edge `0.0867` maxDD `-2.2743`
- `market_context_high->fx_24h` score `0.4797` n `126` status `ready` deltaP `18.8492` edge `0.0225` maxDD `-1.9329`
- `market_context_high->equity_24h` score `0.2723` n `126` status `ready` deltaP `2.877` edge `0.3095` maxDD `-21.1456`
- `market_context_high->index_24h` score `-0.1682` n `126` status `ready` deltaP `3.5963` edge `0.1076` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.482` n `159` status `ready` deltaP `1.9621` edge `-0.0037` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.6509` n `159` status `ready` deltaP `-4.4759` edge `-0.0059` maxDD `-0.8168`
- `market_context_high->index_4h` score `-0.6673` n `147` status `ready` deltaP `-2.2855` edge `-0.0098` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.682` n `147` status `ready` deltaP `3.2842` edge `-0.0034` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.7236` n `159` status `ready` deltaP `-4.2358` edge `-0.0091` maxDD `-1.4345`
- `market_context_high->metal_4h` score `-1.0715` n `147` status `ready` deltaP `-2.4017` edge `-0.0191` maxDD `-2.8477`
- `market_context_high->equity_1h` score `-1.1162` n `159` status `ready` deltaP `-1.5686` edge `0.0003` maxDD `-4.6286`
- `market_context_high->crypto_alt_1h` score `-1.2126` n `159` status `ready` deltaP `-8.9076` edge `-0.0319` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.6764` n `147` status `ready` deltaP `-2.941` edge `-0.0697` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.3492` n `159` status `ready` deltaP `-11.2153` edge `-0.0596` maxDD `-8.2454`
- `market_context_high->crypto_major_24h` score `-4.0938` n `126` status `ready` deltaP `2.381` edge `-0.1076` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-4.1415` n `147` status `ready` deltaP `-9.2521` edge `-0.1178` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-4.7908` n `126` status `ready` deltaP `-13.8641` edge `-0.1625` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.7092` n `159` status `ready` deltaP `-5.9748` edge `-0.5569` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
