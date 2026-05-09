# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T11:15:01.362064+00:00`
- Price records: `672`
- Market context records: `860`
- Flow alert records: `2413`
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

- `market_context_high->crypto_major_24h` score `12.237` n `165` status `ready` deltaP `27.5316` edge `0.8696` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.7413` n `165` status `ready` deltaP `7.2064` edge `0.4352` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.4772` n `32` status `ready` deltaP `8.3079` edge `0.2709` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.4772` n `32` status `ready` deltaP `8.3079` edge `0.2709` maxDD `-0.9217`
- `risk_on_high->crypto_major_4h` score `2.6212` n `32` status `ready` deltaP `19.0549` edge `0.1286` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.6212` n `32` status `ready` deltaP `19.0549` edge `0.1286` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `2.6096` n `32` status `ready` deltaP `20.9604` edge `0.0982` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.6096` n `32` status `ready` deltaP `20.9604` edge `0.0982` maxDD `-0.6377`
- `risk_on_high->index_4h` score `2.4914` n `32` status `ready` deltaP `13.3384` edge `0.1275` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.4914` n `32` status `ready` deltaP `13.3384` edge `0.1275` maxDD `-0.038`
- `risk_on_high->metal_1h` score `1.1444` n `32` status `ready` deltaP `13.2111` edge `0.0303` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.1444` n `32` status `ready` deltaP `13.2111` edge `0.0303` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.9163` n `32` status `ready` deltaP `5.8689` edge `0.1568` maxDD `-1.2759`
- `risk_on_and_context->commodity_4h` score `0.9163` n `32` status `ready` deltaP `5.8689` edge `0.1568` maxDD `-1.2759`
- `risk_on_high->commodity_1h` score `0.276` n `32` status `ready` deltaP `7.616` edge `0.0222` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.276` n `32` status `ready` deltaP `7.616` edge `0.0222` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.1513` n `32` status `ready` deltaP `6.2126` edge `0.0015` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.1513` n `32` status `ready` deltaP `6.2126` edge `0.0015` maxDD `-0.2147`
- `risk_on_high->crypto_major_1h` score `-0.0052` n `32` status `ready` deltaP `6.381` edge `-0.0128` maxDD `-1.0995`
- `risk_on_and_context->crypto_major_1h` score `-0.0052` n `32` status `ready` deltaP `6.381` edge `-0.0128` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
