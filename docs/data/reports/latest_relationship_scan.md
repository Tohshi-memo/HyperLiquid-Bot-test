# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T12:46:06.399047+00:00`
- Price records: `672`
- Market context records: `4517`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9771`

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

- `risk_on_high->unknown_4h` score `140.4843` n `45` status `ready` deltaP `10.2879` edge `11.7617` maxDD `-7.5275`
- `risk_on_and_context->unknown_4h` score `140.4843` n `45` status `ready` deltaP `10.2879` edge `11.7617` maxDD `-7.5275`
- `market_context_high->unknown_1h` score `46.4309` n `192` status `ready` deltaP `5.5234` edge `3.8908` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `27.0829` n `192` status `ready` deltaP `6.8851` edge `2.3676` maxDD `-7.5275`
- `risk_on_high->unknown_24h` score `5.6626` n `45` status `ready` deltaP `17.1875` edge `0.3573` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5.6626` n `45` status `ready` deltaP `17.1875` edge `0.3573` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `5.4522` n `45` status `ready` deltaP `30.8502` edge `0.2839` maxDD `-1.4844`
- `risk_on_and_context->crypto_major_4h` score `5.4522` n `45` status `ready` deltaP `30.8502` edge `0.2839` maxDD `-1.4844`
- `risk_on_high->equity_4h` score `5.1451` n `45` status `ready` deltaP `41.7683` edge `0.1503` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.1451` n `45` status `ready` deltaP `41.7683` edge `0.1503` maxDD `0.0`
- `risk_on_high->metal_24h` score `3.0676` n `45` status `ready` deltaP `-10.7986` edge `0.5632` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `3.0676` n `45` status `ready` deltaP `-10.7986` edge `0.5632` maxDD `-4.834`
- `risk_on_high->metal_4h` score `2.1682` n `45` status `ready` deltaP `16.9716` edge `0.1011` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `2.1682` n `45` status `ready` deltaP `16.9716` edge `0.1011` maxDD `-1.3516`
- `risk_on_high->index_24h` score `1.3084` n `45` status `ready` deltaP `21.007` edge `0.0207` maxDD `-2.4702`
- `risk_on_and_context->index_24h` score `1.3084` n `45` status `ready` deltaP `21.007` edge `0.0207` maxDD `-2.4702`
- `risk_on_high->equity_1h` score `1.1199` n `45` status `ready` deltaP `13.9488` edge `0.0346` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.1199` n `45` status `ready` deltaP `13.9488` edge `0.0346` maxDD `-0.7415`
- `risk_on_high->crypto_alt_4h` score `0.7534` n `45` status `ready` deltaP `4.1836` edge `0.0961` maxDD `-2.2296`
- `risk_on_and_context->crypto_alt_4h` score `0.7534` n `45` status `ready` deltaP `4.1836` edge `0.0961` maxDD `-2.2296`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
