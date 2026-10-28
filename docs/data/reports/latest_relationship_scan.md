# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T18:37:35.149943+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8602`

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

- `market_context_high->unknown_24h` score `1214.1567` n `148` status `ready` deltaP `-2.135` edge `101.2867` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.822` n `149` status `ready` deltaP `4.385` edge `1.8045` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.4637` n `148` status `ready` deltaP `24.2352` edge `0.0292` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1733` n `149` status `ready` deltaP `7.269` edge `0.0018` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.0917` n `149` status `ready` deltaP `8.327` edge `0.0074` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.1698` n `149` status `ready` deltaP `6.3145` edge `0.0036` maxDD `-0.4545`
- `market_context_high->crypto_major_1h` score `-0.3523` n `149` status `ready` deltaP `6.6803` edge `0.0386` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.4286` n `148` status `ready` deltaP `13.6215` edge `0.0307` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.4404` n `149` status `ready` deltaP `6.8966` edge `0.0392` maxDD `-1.0837`
- `market_context_high->commodity_1h` score `-0.6189` n `149` status `ready` deltaP `-0.0412` edge `0.0071` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7445` n `149` status `ready` deltaP `-3.624` edge `-0.003` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7537` n `149` status `ready` deltaP `8.9039` edge `-0.0019` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.4187` n `149` status `ready` deltaP `0.9394` edge `0.0031` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5385` n `149` status `ready` deltaP `3.0452` edge `0.0188` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.8236` n `148` status `ready` deltaP `6.7849` edge `0.0159` maxDD `-15.7143`
- `market_context_high->index_4h` score `-3.0954` n `149` status `ready` deltaP `-9.7889` edge `-0.0305` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.2273` n `148` status `ready` deltaP `0.8493` edge `0.0663` maxDD `-29.1905`
- `market_context_high->metal_24h` score `-3.4071` n `148` status `ready` deltaP `-0.0657` edge `0.0185` maxDD `-10.1587`
- `market_context_high->crypto_major_4h` score `-3.4253` n `149` status `ready` deltaP `3.5092` edge `-0.0306` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.41` n `149` status `ready` deltaP `-3.7823` edge `-0.145` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
