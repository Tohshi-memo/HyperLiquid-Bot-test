# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T17:37:35.550166+00:00`
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

- `market_context_high->unknown_4h` score `81.1078` n `135` status `ready` deltaP `4.5472` edge `6.7439` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `5.9588` n `142` status `ready` deltaP `1.2735` edge `0.537` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.9903` n `135` status `ready` deltaP `27.1875` edge `0.0534` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4895` n `142` status `ready` deltaP `10.9956` edge `0.0033` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4237` n `135` status `ready` deltaP `12.7439` edge `0.0102` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0075` n `142` status `ready` deltaP `9.7811` edge `0.0085` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.3261` n `142` status `ready` deltaP `1.769` edge `0.0111` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.3788` n `142` status `ready` deltaP `7.3248` edge `0.0309` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.3866` n `135` status `ready` deltaP `6.3844` edge `0.0471` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.5457` n `135` status `ready` deltaP `10.0` edge `0.0206` maxDD `-1.2451`
- `market_context_high->index_1h` score `-0.5966` n `142` status `ready` deltaP `-0.8097` edge `-0.0028` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8438` n `135` status `ready` deltaP `7.8613` edge `-0.0065` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-0.9489` n `135` status `ready` deltaP `16.0995` edge `0.0914` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.396` n `142` status `ready` deltaP `2.0346` edge `-0.0013` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.7478` n `135` status `ready` deltaP `8.0671` edge `0.097` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.8469` n `142` status `ready` deltaP `0.3542` edge `-0.0028` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.9244` n `135` status `ready` deltaP `-7.2324` edge `-0.0333` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.825` n `135` status `ready` deltaP `3.2024` edge `-0.0798` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-3.8352` n `135` status `ready` deltaP `0.544` edge `-0.0096` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.4582` n `135` status `ready` deltaP `-0.044` edge `-0.1761` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
