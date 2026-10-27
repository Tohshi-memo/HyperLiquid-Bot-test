# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T16:38:00.682898+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8649`

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

- `market_context_high->unknown_4h` score `81.0298` n `135` status `ready` deltaP `4.5472` edge `6.7374` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `11.0733` n `138` status `ready` deltaP `0.8245` edge `0.9662` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.9939` n `135` status `ready` deltaP `27.1875` edge `0.0537` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4499` n `138` status `ready` deltaP `10.5159` edge `0.0032` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.3969` n `135` status `ready` deltaP `12.439` edge `0.01` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0513` n `138` status `ready` deltaP `9.0905` edge `0.0075` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.1976` n `138` status `ready` deltaP `3.1502` edge `0.0126` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.4278` n `135` status `ready` deltaP `6.0795` edge `0.0457` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.4826` n `138` status `ready` deltaP `6.0184` edge `0.0263` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5506` n `138` status `ready` deltaP `0.0` edge `-0.0023` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-0.5888` n `135` status `ready` deltaP `9.3056` edge `0.0197` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.8273` n `135` status `ready` deltaP `8.0137` edge `-0.0054` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-0.9501` n `135` status `ready` deltaP `16.0995` edge `0.0913` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.4041` n `138` status `ready` deltaP `2.2694` edge `-0.0039` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.8474` n `135` status `ready` deltaP `8.0671` edge `0.0887` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.9282` n `138` status `ready` deltaP `-0.6834` edge `-0.0063` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.8577` n `135` status `ready` deltaP `-6.6227` edge `-0.0318` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.8008` n `135` status `ready` deltaP `3.2024` edge `-0.0767` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-3.9124` n `135` status `ready` deltaP `0.544` edge `-0.0195` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.3438` n `135` status `ready` deltaP `0.5657` edge `-0.1655` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
