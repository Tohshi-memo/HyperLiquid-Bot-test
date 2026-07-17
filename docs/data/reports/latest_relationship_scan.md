# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T11:07:24.138439+00:00`
- Price records: `672`
- Market context records: `7022`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11529`

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

- `market_context_high->fx_1h` score `-0.2686` n `222` status `ready` deltaP `1.9447` edge `0.0011` maxDD `-0.5468`
- `market_context_high->unknown_24h` score `-0.6726` n `209` status `ready` deltaP `-6.4677` edge `0.4119` maxDD `-18.7342`
- `market_context_high->metal_1h` score `-0.6811` n `222` status `ready` deltaP `-1.671` edge `0.0006` maxDD `-2.1427`
- `market_context_high->crypto_alt_1h` score `-0.6827` n `222` status `ready` deltaP `0.6069` edge `0.0255` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.7459` n `222` status `ready` deltaP `-0.6164` edge `-0.0004` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.7652` n `222` status `ready` deltaP `2.255` edge `0.0221` maxDD `-7.1523`
- `market_context_high->fx_4h` score `-0.8693` n `222` status `ready` deltaP `10.4771` edge `0.0064` maxDD `-2.0155`
- `market_context_high->unknown_1h` score `-1.3189` n `222` status `ready` deltaP `-2.7162` edge `-0.0017` maxDD `-3.2083`
- `market_context_high->commodity_1h` score `-1.3386` n `222` status `ready` deltaP `-3.3002` edge `-0.0174` maxDD `-2.4388`
- `market_context_high->commodity_4h` score `-1.6312` n `222` status `ready` deltaP `-4.5869` edge `-0.0396` maxDD `-4.7827`
- `market_context_high->index_4h` score `-1.8392` n `222` status `ready` deltaP `6.9916` edge `-0.0125` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-1.9323` n `222` status `ready` deltaP `6.103` edge `0.0099` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.3199` n `222` status `ready` deltaP `-5.9478` edge `0.0751` maxDD `-9.6351`
- `market_context_high->crypto_alt_4h` score `-2.7955` n `222` status `ready` deltaP `0.651` edge `0.0158` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-2.8093` n `209` status `ready` deltaP `-3.8137` edge `-0.0778` maxDD `-4.4704`
- `market_context_high->equity_1h` score `-3.0635` n `222` status `ready` deltaP `2.5381` edge `-0.0168` maxDD `-15.7664`
- `market_context_high->crypto_major_4h` score `-3.1803` n `222` status `ready` deltaP `1.6836` edge `0.0095` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-4.026` n `209` status `ready` deltaP `-4.592` edge `-0.0146` maxDD `-4.5562`
- `market_context_high->equity_4h` score `-11.6061` n `222` status `ready` deltaP `3.8796` edge `-0.0756` maxDD `-66.3951`
- `market_context_high->metal_24h` score `-13.4778` n `209` status `ready` deltaP `-10.6675` edge `-0.0551` maxDD `-39.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
