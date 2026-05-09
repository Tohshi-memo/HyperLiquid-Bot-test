# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T12:06:23.834742+00:00`
- Price records: `672`
- Market context records: `864`
- Flow alert records: `2425`
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

- `risk_on_high->crypto_major_24h` score `22.5966` n `30` status `ready` deltaP `32.8125` edge `1.6643` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `22.5966` n `30` status `ready` deltaP `32.8125` edge `1.6643` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `13.8118` n `30` status `ready` deltaP `7.8125` edge `1.0989` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.8118` n `30` status `ready` deltaP `7.8125` edge `1.0989` maxDD `0.0`
- `risk_on_high->equity_24h` score `13.7854` n `30` status `ready` deltaP `25.3472` edge `0.9798` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `13.7854` n `30` status `ready` deltaP `25.3472` edge `0.9798` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `12.5812` n `165` status `ready` deltaP `27.964` edge `0.8954` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.0533` n `165` status `ready` deltaP `7.2064` edge `0.4612` maxDD `-0.0508`
- `risk_on_high->index_24h` score `4.5221` n `30` status `ready` deltaP `27.9514` edge `0.1905` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.5221` n `30` status `ready` deltaP `27.9514` edge `0.1905` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.459` n `32` status `ready` deltaP `8.1555` edge `0.2704` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.459` n `32` status `ready` deltaP `8.1555` edge `0.2704` maxDD `-0.9217`
- `risk_on_high->crypto_alt_4h` score `2.7122` n `32` status `ready` deltaP `21.4177` edge `0.1037` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.7122` n `32` status `ready` deltaP `21.4177` edge `0.1037` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `2.6782` n `32` status `ready` deltaP `19.5122` edge `0.1303` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.6782` n `32` status `ready` deltaP `19.5122` edge `0.1303` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.5206` n `32` status `ready` deltaP `13.6433` edge `0.1279` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.5206` n `32` status `ready` deltaP `13.6433` edge `0.1279` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `1.9113` n `30` status `ready` deltaP `-5.8333` edge `0.3458` maxDD `-1.6164`
- `risk_on_and_context->commodity_24h` score `1.9113` n `30` status `ready` deltaP `-5.8333` edge `0.3458` maxDD `-1.6164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
