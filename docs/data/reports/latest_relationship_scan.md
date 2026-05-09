# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T14:52:14.466596+00:00`
- Price records: `672`
- Market context records: `876`
- Flow alert records: `2460`
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

- `risk_on_high->crypto_major_24h` score `21.7564` n `32` status `ready` deltaP `32.4653` edge `1.5966` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `21.7564` n `32` status `ready` deltaP `32.4653` edge `1.5966` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.536` n `165` status `ready` deltaP `28.8289` edge `0.9692` maxDD `-1.3382`
- `risk_on_high->equity_24h` score `13.5358` n `32` status `ready` deltaP `25.3472` edge `0.959` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `13.5358` n `32` status `ready` deltaP `25.3472` edge `0.959` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `13.0594` n `32` status `ready` deltaP `7.8125` edge `1.0362` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.0594` n `32` status `ready` deltaP `7.8125` edge `1.0362` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.8453` n `165` status `ready` deltaP `7.2064` edge `0.5272` maxDD `-0.0508`
- `risk_on_high->index_24h` score `4.3913` n `32` status `ready` deltaP `27.9514` edge `0.1796` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.3913` n `32` status `ready` deltaP `27.9514` edge `0.1796` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4566` n `32` status `ready` deltaP `8.1555` edge `0.2702` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.4566` n `32` status `ready` deltaP `8.1555` edge `0.2702` maxDD `-0.9217`
- `risk_on_high->crypto_alt_4h` score `3.1931` n `32` status `ready` deltaP `23.0945` edge `0.1326` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.1931` n `32` status `ready` deltaP `23.0945` edge `0.1326` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `2.9204` n `32` status `ready` deltaP `21.189` edge `0.1393` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.9204` n `32` status `ready` deltaP `21.189` edge `0.1393` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.5643` n `32` status `ready` deltaP `14.1006` edge `0.1285` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.5643` n `32` status `ready` deltaP `14.1006` edge `0.1285` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `1.5284` n `32` status `ready` deltaP `-8.6806` edge `0.3284` maxDD `-1.9668`
- `risk_on_and_context->commodity_24h` score `1.5284` n `32` status `ready` deltaP `-8.6806` edge `0.3284` maxDD `-1.9668`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
