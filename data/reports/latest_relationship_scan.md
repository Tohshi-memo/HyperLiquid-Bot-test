# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T17:22:33.218254+00:00`
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

- `market_context_high->unknown_4h` score `81.049` n `135` status `ready` deltaP `4.5472` edge `6.739` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `7.1992` n `141` status `ready` deltaP `1.1637` edge `0.6411` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.9915` n `135` status `ready` deltaP `27.1875` edge `0.0535` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.5106` n `141` status `ready` deltaP `11.2604` edge `0.0033` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4237` n `135` status `ready` deltaP `12.7439` edge `0.0102` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0268` n `141` status `ready` deltaP `9.4715` edge `0.0081` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.3069` n `141` status `ready` deltaP `1.9939` edge `0.0112` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.4032` n `141` status `ready` deltaP `7.0051` edge `0.0299` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.4048` n `135` status `ready` deltaP `6.2319` edge `0.0466` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.5571` n `135` status `ready` deltaP `9.8264` edge `0.0203` maxDD `-1.2451`
- `market_context_high->index_1h` score `-0.5865` n `141` status `ready` deltaP `-0.6147` edge `-0.0028` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8327` n `135` status `ready` deltaP `8.0137` edge `-0.0061` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-0.9465` n `135` status `ready` deltaP `16.0995` edge `0.0916` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.3898` n `141` status `ready` deltaP `2.2296` edge `-0.0018` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.7718` n `135` status `ready` deltaP `8.0671` edge `0.095` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.8783` n `141` status `ready` deltaP `-0.0404` edge `-0.0042` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.9075` n `135` status `ready` deltaP `-7.08` edge `-0.0329` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.8164` n `135` status `ready` deltaP `3.2024` edge `-0.0787` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-3.8586` n `135` status `ready` deltaP `0.544` edge `-0.0126` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.4292` n `135` status `ready` deltaP `0.1084` edge `-0.1734` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
