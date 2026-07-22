# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T16:22:34.196926+00:00`
- Price records: `672`
- Market context records: `7582`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14534`

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

- `market_context_high->commodity_4h` score `0.2334` n `160` status `ready` deltaP `9.7286` edge `0.0306` maxDD `-2.4139`
- `market_context_high->index_1h` score `-0.0077` n `160` status `ready` deltaP `5.5274` edge `0.011` maxDD `-0.9072`
- `market_context_high->commodity_1h` score `-0.1061` n `160` status `ready` deltaP `6.372` edge `0.0059` maxDD `-1.5775`
- `market_context_high->commodity_24h` score `-0.1083` n `152` status `ready` deltaP `12.2433` edge `0.0677` maxDD `-7.0012`
- `market_context_high->fx_1h` score `-0.4998` n `160` status `ready` deltaP `1.3026` edge `-0.0004` maxDD `-0.6615`
- `market_context_high->index_4h` score `-0.5019` n `160` status `ready` deltaP `10.9041` edge `0.0356` maxDD `-3.4775`
- `market_context_high->unknown_24h` score `-0.5708` n `153` status `ready` deltaP `8.752` edge `0.0966` maxDD `-8.9164`
- `market_context_high->crypto_alt_1h` score `-0.625` n `160` status `ready` deltaP `0.1497` edge `0.0047` maxDD `-4.5327`
- `market_context_high->metal_1h` score `-0.6629` n `160` status `ready` deltaP `0.8196` edge `0.0141` maxDD `-1.0307`
- `market_context_high->crypto_major_1h` score `-0.6928` n `160` status `ready` deltaP `5.6512` edge `0.004` maxDD `-6.7732`
- `market_context_high->equity_1h` score `-0.6993` n `160` status `ready` deltaP `5.0526` edge `0.0462` maxDD `-8.8965`
- `market_context_high->fx_24h` score `-0.8027` n `152` status `ready` deltaP `7.1842` edge `0.0147` maxDD `-3.6922`
- `market_context_high->unknown_1h` score `-0.9696` n `160` status `ready` deltaP `-0.0524` edge `-0.0616` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-1.3078` n `160` status `ready` deltaP `1.25` edge `0.0432` maxDD `-10.8698`
- `market_context_high->equity_4h` score `-1.5193` n `160` status `ready` deltaP `3.7099` edge `0.2172` maxDD `-21.9375`
- `market_context_high->metal_4h` score `-1.5381` n `160` status `ready` deltaP `-0.0457` edge `0.0513` maxDD `-4.8549`
- `market_context_high->crypto_major_4h` score `-1.9719` n `160` status `ready` deltaP `5.4573` edge `0.046` maxDD `-19.1488`
- `market_context_high->fx_4h` score `-2.201` n `160` status `ready` deltaP `-2.0623` edge `-0.0012` maxDD `-2.1439`
- `market_context_high->unknown_4h` score `-2.4172` n `160` status `ready` deltaP `9.8323` edge `-0.14` maxDD `-6.1692`
- `market_context_high->metal_24h` score `-3.2198` n `153` status `ready` deltaP `-4.5649` edge `0.0838` maxDD `-13.9601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
