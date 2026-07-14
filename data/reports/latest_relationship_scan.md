# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T08:37:30.519637+00:00`
- Price records: `672`
- Market context records: `6692`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->commodity_24h` score `0.5122` n `190` status `ready` deltaP `10.4405` edge `0.1599` maxDD `-5.2791`
- `market_context_high->unknown_24h` score `0.4814` n `190` status `ready` deltaP `-1.0581` edge `0.444` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.4264` n `190` status `ready` deltaP `9.7825` edge `0.0563` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `0.2133` n `190` status `ready` deltaP `6.7791` edge `0.049` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3194` n `190` status `ready` deltaP `1.2559` edge `0.0009` maxDD `-0.6845`
- `market_context_high->unknown_1h` score `-0.4211` n `190` status `ready` deltaP `-5.2632` edge `0.0901` maxDD `-3.2083`
- `market_context_high->index_1h` score `-0.4737` n `190` status `ready` deltaP `0.8982` edge `0.0047` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.5102` n `190` status `ready` deltaP `-2.4141` edge `0.0032` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-0.5349` n `190` status `ready` deltaP `3.9931` edge `0.0075` maxDD `-3.8827`
- `market_context_high->commodity_1h` score `-0.5754` n `190` status `ready` deltaP `0.5452` edge `-0.0091` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.9497` n `190` status `ready` deltaP `9.9021` edge `0.0002` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.3889` n `190` status `ready` deltaP `6.5147` edge `-0.0013` maxDD `-3.2825`
- `market_context_high->crypto_major_4h` score `-1.5318` n `190` status `ready` deltaP `7.8257` edge `0.0829` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.6918` n `190` status `ready` deltaP `-4.1592` edge `-0.0397` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.7853` n `190` status `ready` deltaP `5.775` edge `0.0728` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.183` n `190` status `ready` deltaP `-2.0876` edge `0.0201` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-3.5113` n `190` status `ready` deltaP `-16.6865` edge `0.0592` maxDD `-10.5788`
- `market_context_high->fx_24h` score `-5.2527` n `190` status `ready` deltaP `-10.4294` edge `-0.006` maxDD `-8.6426`
- `market_context_high->equity_4h` score `-5.3334` n `190` status `ready` deltaP `6.4136` edge `-0.0603` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-7.0082` n `190` status `ready` deltaP `-6.1002` edge `-0.0093` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
