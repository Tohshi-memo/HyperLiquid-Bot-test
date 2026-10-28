# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T17:52:34.360259+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8580`

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

- `market_context_high->unknown_24h` score `1230.6907` n `147` status `ready` deltaP `-2.2499` edge `102.6653` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.8448` n `149` status `ready` deltaP `4.385` edge `1.8064` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.517` n `147` status `ready` deltaP `24.6457` edge `0.0309` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1865` n `149` status `ready` deltaP `7.4187` edge `0.0019` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.091` n `149` status `ready` deltaP `8.327` edge `0.0075` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.1272` n `149` status `ready` deltaP `6.7718` edge `0.0041` maxDD `-0.4545`
- `market_context_high->crypto_major_1h` score `-0.3079` n `149` status `ready` deltaP `7.1294` edge `0.0413` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.4136` n `147` status `ready` deltaP `13.8251` edge `0.0306` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.4258` n `149` status `ready` deltaP `7.049` edge `0.0394` maxDD `-1.0837`
- `market_context_high->commodity_1h` score `-0.6345` n `149` status `ready` deltaP `-0.1909` edge `0.0068` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7344` n `149` status `ready` deltaP `-3.4743` edge `-0.0027` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7419` n `149` status `ready` deltaP `9.0563` edge `-0.0014` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.3984` n `149` status `ready` deltaP `1.0891` edge `0.0047` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.4972` n `149` status `ready` deltaP `3.4943` edge `0.0211` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.6576` n `147` status `ready` deltaP `7.0897` edge `0.0277` maxDD `-15.7143`
- `market_context_high->index_4h` score `-3.076` n `149` status `ready` deltaP `-9.6364` edge `-0.0299` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.1903` n `147` status `ready` deltaP `1.0345` edge `0.0698` maxDD `-29.1905`
- `market_context_high->metal_24h` score `-3.3167` n `147` status `ready` deltaP `0.3792` edge `0.0208` maxDD `-9.9779`
- `market_context_high->crypto_major_4h` score `-3.3758` n `149` status `ready` deltaP `3.9665` edge `-0.0273` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.3581` n `149` status `ready` deltaP `-3.325` edge `-0.1414` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
