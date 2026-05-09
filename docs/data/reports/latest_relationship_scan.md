# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T22:22:16.225672+00:00`
- Price records: `672`
- Market context records: `912`
- Flow alert records: `2556`
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

- `risk_on_high->crypto_major_24h` score `21.2958` n `32` status `ready` deltaP `31.5972` edge `1.564` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `21.2958` n `32` status `ready` deltaP `31.5972` edge `1.564` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.4224` n `169` status `ready` deltaP `28.6386` edge `0.961` maxDD `-1.3382`
- `risk_on_high->equity_24h` score `12.9886` n `32` status `ready` deltaP `25.3472` edge `0.9134` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `12.9886` n `32` status `ready` deltaP `25.3472` edge `0.9134` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `12.2939` n `32` status `ready` deltaP `4.5139` edge `0.9944` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `12.2939` n `32` status `ready` deltaP `4.5139` edge `0.9944` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.2387` n `169` status `ready` deltaP `4.5139` edge `0.4898` maxDD `0.0`
- `risk_on_high->index_24h` score `4.1741` n `32` status `ready` deltaP `27.9514` edge `0.1615` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.1741` n `32` status `ready` deltaP `27.9514` edge `0.1615` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.484` n `32` status `ready` deltaP `8.003` edge `0.2735` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.484` n `32` status `ready` deltaP `8.003` edge `0.2735` maxDD `-0.9217`
- `risk_on_high->crypto_alt_4h` score `3.3401` n `32` status `ready` deltaP `23.5518` edge `0.1418` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.3401` n `32` status `ready` deltaP `23.5518` edge `0.1418` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `2.8742` n `32` status `ready` deltaP `20.7317` edge `0.1385` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.8742` n `32` status `ready` deltaP `20.7317` edge `0.1385` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.445` n `32` status `ready` deltaP `12.7287` edge `0.1277` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.445` n `32` status `ready` deltaP `12.7287` edge `0.1277` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `1.2017` n `32` status `ready` deltaP `-11.6319` edge `0.3062` maxDD `-1.9668`
- `risk_on_and_context->commodity_24h` score `1.2017` n `32` status `ready` deltaP `-11.6319` edge `0.3062` maxDD `-1.9668`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
