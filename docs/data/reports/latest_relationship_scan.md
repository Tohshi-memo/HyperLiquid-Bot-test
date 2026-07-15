# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T18:07:27.522175+00:00`
- Price records: `672`
- Market context records: `6840`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11802`

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

- `market_context_high->unknown_24h` score `0.9857` n `176` status `ready` deltaP `-1.5467` edge `0.5119` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `-0.0067` n `176` status `ready` deltaP `8.6648` edge `0.1285` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.2586` n `217` status `ready` deltaP `2.062` edge `0.0016` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5308` n `217` status `ready` deltaP `2.3525` edge `0.0165` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.5338` n `217` status `ready` deltaP `4.3455` edge `0.0167` maxDD `-4.2122`
- `market_context_high->index_1h` score `-0.887` n `217` status `ready` deltaP `-2.6843` edge `-0.0047` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-1.0214` n `217` status `ready` deltaP `-6.4295` edge `-0.0113` maxDD `-2.1427`
- `market_context_high->commodity_1h` score `-1.0351` n `217` status `ready` deltaP `-2.0385` edge `-0.0042` maxDD `-2.1443`
- `market_context_high->fx_4h` score `-1.0621` n `206` status `ready` deltaP `9.8567` edge `0.0045` maxDD `-2.1765`
- `market_context_high->unknown_1h` score `-1.6591` n `217` status `ready` deltaP `-3.5031` edge `-0.0248` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.985` n `217` status `ready` deltaP `-0.16` edge `-0.0354` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.2642` n `206` status `ready` deltaP `0.4337` edge `-0.0352` maxDD `-11.3047`
- `market_context_high->commodity_4h` score `-2.367` n `206` status `ready` deltaP `-4.81` edge `-0.0162` maxDD `-5.5853`
- `market_context_high->metal_4h` score `-2.7486` n `206` status `ready` deltaP `-3.8198` edge `-0.0286` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.9393` n `206` status `ready` deltaP `0.117` edge `-0.0449` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1286` n `206` status `ready` deltaP `0.1569` edge `-0.0438` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.2736` n `206` status `ready` deltaP `-9.9218` edge `0.0299` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4648` n `176` status `ready` deltaP `-9.7853` edge `-0.0032` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.9943` n `206` status `ready` deltaP `-1.773` edge `-0.2235` maxDD `-56.1671`
- `market_context_high->metal_24h` score `-9.2395` n `176` status `ready` deltaP `-18.8447` edge `-0.2104` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
