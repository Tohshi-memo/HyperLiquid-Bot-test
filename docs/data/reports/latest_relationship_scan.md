# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T15:22:12.781474+00:00`
- Price records: `672`
- Market context records: `878`
- Flow alert records: `2466`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1386`

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

- `risk_on_high->crypto_major_24h` score `21.712` n `32` status `ready` deltaP `32.4653` edge `1.5929` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `21.712` n `32` status `ready` deltaP `32.4653` edge `1.5929` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.6464` n `165` status `ready` deltaP `28.8289` edge `0.9784` maxDD `-1.3382`
- `risk_on_high->equity_24h` score `13.483` n `32` status `ready` deltaP `25.3472` edge `0.9546` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `13.483` n `32` status `ready` deltaP `25.3472` edge `0.9546` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `13.0174` n `32` status `ready` deltaP `7.8125` edge `1.0327` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.0174` n `32` status `ready` deltaP `7.8125` edge `1.0327` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.9473` n `165` status `ready` deltaP `7.2064` edge `0.5357` maxDD `-0.0508`
- `risk_on_high->index_24h` score `4.3649` n `32` status `ready` deltaP `27.9514` edge `0.1774` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.3649` n `32` status `ready` deltaP `27.9514` edge `0.1774` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4748` n `32` status `ready` deltaP `8.3079` edge `0.2707` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.4748` n `32` status `ready` deltaP `8.3079` edge `0.2707` maxDD `-0.9217`
- `risk_on_high->crypto_alt_4h` score `3.2787` n `32` status `ready` deltaP `23.3994` edge `0.1377` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.2787` n `32` status `ready` deltaP `23.3994` edge `0.1377` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `2.9711` n `32` status `ready` deltaP `21.4939` edge `0.1415` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.9711` n `32` status `ready` deltaP `21.4939` edge `0.1415` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.5655` n `32` status `ready` deltaP `14.1006` edge `0.1286` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.5655` n `32` status `ready` deltaP `14.1006` edge `0.1286` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `1.5245` n `32` status `ready` deltaP `-8.6806` edge `0.3279` maxDD `-1.9668`
- `risk_on_and_context->commodity_24h` score `1.5245` n `32` status `ready` deltaP `-8.6806` edge `0.3279` maxDD `-1.9668`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
