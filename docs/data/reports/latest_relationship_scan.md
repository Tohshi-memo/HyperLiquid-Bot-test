# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T21:52:12.013990+00:00`
- Price records: `672`
- Market context records: `910`
- Flow alert records: `2549`
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

- `risk_on_high->crypto_major_24h` score `21.297` n `32` status `ready` deltaP `31.5972` edge `1.5641` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `21.297` n `32` status `ready` deltaP `31.5972` edge `1.5641` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.4236` n `169` status `ready` deltaP `28.6386` edge `0.9611` maxDD `-1.3382`
- `risk_on_high->equity_24h` score `13.0066` n `32` status `ready` deltaP `25.3472` edge `0.9149` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `13.0066` n `32` status `ready` deltaP `25.3472` edge `0.9149` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `12.3234` n `32` status `ready` deltaP `4.6875` edge `0.9957` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `12.3234` n `32` status `ready` deltaP `4.6875` edge `0.9957` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.2682` n `169` status `ready` deltaP `4.6875` edge `0.4911` maxDD `0.0`
- `risk_on_high->index_24h` score `4.1825` n `32` status `ready` deltaP `27.9514` edge `0.1622` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.1825` n `32` status `ready` deltaP `27.9514` edge `0.1622` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.5228` n `32` status `ready` deltaP `8.3079` edge `0.2747` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.5228` n `32` status `ready` deltaP `8.3079` edge `0.2747` maxDD `-0.9217`
- `risk_on_high->crypto_alt_4h` score `3.3933` n `32` status `ready` deltaP `23.8567` edge `0.1442` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.3933` n `32` status `ready` deltaP `23.8567` edge `0.1442` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `2.9032` n `32` status `ready` deltaP `20.8841` edge `0.1399` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.9032` n `32` status `ready` deltaP `20.8841` edge `0.1399` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.4608` n `32` status `ready` deltaP `12.8811` edge `0.128` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.4608` n `32` status `ready` deltaP `12.8811` edge `0.128` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `1.2455` n `32` status `ready` deltaP `-11.2847` edge `0.3095` maxDD `-1.9668`
- `risk_on_and_context->commodity_24h` score `1.2455` n `32` status `ready` deltaP `-11.2847` edge `0.3095` maxDD `-1.9668`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
