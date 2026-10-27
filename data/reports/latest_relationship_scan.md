# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T17:52:35.129314+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8651`

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

- `market_context_high->unknown_4h` score `81.1138` n `135` status `ready` deltaP `4.5472` edge `6.7444` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `4.7139` n `143` status `ready` deltaP `0.8323` edge `0.4362` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.9879` n `135` status `ready` deltaP `27.1875` edge `0.0532` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4699` n `143` status `ready` deltaP `10.7366` edge `0.0034` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4371` n `135` status `ready` deltaP `12.8963` edge `0.0103` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0202` n `143` status `ready` deltaP `9.5369` edge `0.0085` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.3448` n `143` status `ready` deltaP `1.5494` edge `0.011` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.3578` n `143` status `ready` deltaP `7.64` edge `0.0315` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.3696` n `135` status `ready` deltaP `6.5368` edge `0.0475` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.5351` n `135` status `ready` deltaP `10.1736` edge `0.0208` maxDD `-1.2451`
- `market_context_high->index_1h` score `-0.615` n `143` status `ready` deltaP `-1.1495` edge `-0.0029` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8548` n `135` status `ready` deltaP `7.7089` edge `-0.0069` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-0.9664` n `135` status `ready` deltaP `15.9259` edge `0.0911` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.3836` n `143` status `ready` deltaP `2.2444` edge `-0.0011` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.7334` n `135` status `ready` deltaP `8.0671` edge `0.0982` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.8173` n `143` status `ready` deltaP `0.7432` edge `-0.0016` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.9438` n `135` status `ready` deltaP `-7.3849` edge `-0.0339` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.8188` n `135` status `ready` deltaP `0.544` edge `-0.0075` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.8352` n `135` status `ready` deltaP `3.2024` edge `-0.0811` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.4903` n `135` status `ready` deltaP `-0.1965` edge `-0.1792` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
