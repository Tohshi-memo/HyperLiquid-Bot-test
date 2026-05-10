# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T00:22:15.901698+00:00`
- Price records: `672`
- Market context records: `922`
- Flow alert records: `2582`
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

- `risk_on_high->crypto_major_24h` score `21.2601` n `32` status `ready` deltaP `31.0764` edge `1.5645` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `21.2601` n `32` status `ready` deltaP `31.0764` edge `1.5645` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.3867` n `169` status `ready` deltaP `28.1178` edge `0.9615` maxDD `-1.3382`
- `risk_on_high->equity_24h` score `12.8787` n `32` status `ready` deltaP `25.1736` edge `0.9054` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `12.8787` n `32` status `ready` deltaP `25.1736` edge `0.9054` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `12.2934` n `32` status `ready` deltaP `4.6875` edge `0.9932` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `12.2934` n `32` status `ready` deltaP `4.6875` edge `0.9932` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.2382` n `169` status `ready` deltaP `4.6875` edge `0.4886` maxDD `0.0`
- `risk_on_high->index_24h` score `4.1417` n `32` status `ready` deltaP `27.9514` edge `0.1588` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.1417` n `32` status `ready` deltaP `27.9514` edge `0.1588` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.3252` n `32` status `ready` deltaP `6.7835` edge `0.2684` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.3252` n `32` status `ready` deltaP `6.7835` edge `0.2684` maxDD `-0.9217`
- `risk_on_high->crypto_alt_4h` score `3.1791` n `32` status `ready` deltaP `23.3994` edge `0.1294` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.1791` n `32` status `ready` deltaP `23.3994` edge `0.1294` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `2.7696` n `32` status `ready` deltaP `20.5793` edge `0.1308` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.7696` n `32` status `ready` deltaP `20.5793` edge `0.1308` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.3258` n `32` status `ready` deltaP `11.5091` edge `0.1259` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.3258` n `32` status `ready` deltaP `11.5091` edge `0.1259` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `1.0598` n `32` status `ready` deltaP `-12.8472` edge `0.2961` maxDD `-1.9668`
- `risk_on_and_context->commodity_24h` score `1.0598` n `32` status `ready` deltaP `-12.8472` edge `0.2961` maxDD `-1.9668`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
