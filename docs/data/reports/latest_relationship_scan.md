# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T14:52:35.941801+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8489`

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

- `market_context_high->unknown_24h` score `1516.009` n `135` status `ready` deltaP `-3.7616` edge `126.4519` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `22.1412` n `149` status `ready` deltaP `4.385` edge `1.8311` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.4871` n `135` status `ready` deltaP `25.2778` edge `0.0242` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1889` n `149` status `ready` deltaP `7.4187` edge `0.0021` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0357` n `149` status `ready` deltaP `8.4486` edge `0.0065` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0707` n `149` status `ready` deltaP `8.6264` edge `0.0081` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.2689` n `149` status `ready` deltaP `7.7282` edge `0.0423` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.375` n `149` status `ready` deltaP `7.3539` edge `0.0416` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.5431` n `135` status `ready` deltaP `10.6945` edge `0.0163` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.7027` n `149` status `ready` deltaP `-0.9394` edge `0.0061` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.711` n `149` status `ready` deltaP `-3.0252` edge `-0.0027` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7237` n `149` status `ready` deltaP `9.3612` edge `-0.0011` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.375` n `149` status `ready` deltaP `1.3885` edge `0.0057` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5198` n `149` status `ready` deltaP `3.1949` edge `0.0202` maxDD `-12.2409`
- `market_context_high->metal_24h` score `-2.6015` n `135` status `ready` deltaP `3.9468` edge `0.0347` maxDD `-8.2244`
- `market_context_high->index_4h` score `-2.9592` n `149` status `ready` deltaP `-8.4169` edge `-0.0283` maxDD `-5.6417`
- `market_context_high->equity_24h` score `-3.0543` n `135` status `ready` deltaP `6.331` edge `-0.0003` maxDD `-15.7143`
- `market_context_high->crypto_major_24h` score `-3.2993` n `135` status `ready` deltaP `0.544` edge `0.0591` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.4288` n `149` status `ready` deltaP `3.9665` edge `-0.0341` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.3337` n `149` status `ready` deltaP `-3.0201` edge `-0.1403` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
