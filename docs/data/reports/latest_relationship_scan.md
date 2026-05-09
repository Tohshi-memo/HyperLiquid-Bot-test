# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T11:37:16.891297+00:00`
- Price records: `672`
- Market context records: `862`
- Flow alert records: `2418`
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

- `market_context_high->crypto_major_24h` score `12.3426` n `165` status `ready` deltaP `27.5316` edge `0.8784` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.8517` n `165` status `ready` deltaP `7.2064` edge `0.4444` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.4626` n `32` status `ready` deltaP `8.1555` edge `0.2707` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.4626` n `32` status `ready` deltaP `8.1555` edge `0.2707` maxDD `-0.9217`
- `risk_on_high->crypto_major_4h` score `2.6382` n `32` status `ready` deltaP `19.2073` edge `0.129` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.6382` n `32` status `ready` deltaP `19.2073` edge `0.129` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `2.6374` n `32` status `ready` deltaP `21.1128` edge `0.0995` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.6374` n `32` status `ready` deltaP `21.1128` edge `0.0995` maxDD `-0.6377`
- `risk_on_high->index_4h` score `2.506` n `32` status `ready` deltaP `13.4909` edge `0.1277` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.506` n `32` status `ready` deltaP `13.4909` edge `0.1277` maxDD `-0.038`
- `risk_on_high->metal_1h` score `1.1432` n `32` status `ready` deltaP `13.2111` edge `0.0302` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.1432` n `32` status `ready` deltaP `13.2111` edge `0.0302` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.9171` n `32` status `ready` deltaP `5.8689` edge `0.1569` maxDD `-1.2759`
- `risk_on_and_context->commodity_4h` score `0.9171` n `32` status `ready` deltaP `5.8689` edge `0.1569` maxDD `-1.2759`
- `risk_on_high->commodity_1h` score `0.2846` n `32` status `ready` deltaP `7.7657` edge `0.0223` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.2846` n `32` status `ready` deltaP `7.7657` edge `0.0223` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.1435` n `32` status `ready` deltaP `6.0629` edge `0.0015` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.1435` n `32` status `ready` deltaP `6.0629` edge `0.0015` maxDD `-0.2147`
- `risk_on_high->crypto_major_1h` score `-0.0177` n `32` status `ready` deltaP `6.2313` edge `-0.0134` maxDD `-1.0995`
- `risk_on_and_context->crypto_major_1h` score `-0.0177` n `32` status `ready` deltaP `6.2313` edge `-0.0134` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
