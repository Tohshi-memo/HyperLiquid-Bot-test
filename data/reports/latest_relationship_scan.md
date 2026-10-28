# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T18:07:48.431696+00:00`
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

- `market_context_high->unknown_24h` score `1209.2643` n `148` status `ready` deltaP `-2.135` edge `100.879` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.8208` n `149` status `ready` deltaP `4.385` edge `1.8044` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.5143` n `148` status `ready` deltaP `24.5824` edge `0.0311` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1865` n `149` status `ready` deltaP `7.4187` edge `0.0019` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.0824` n `149` status `ready` deltaP `8.4767` edge `0.0076` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.1418` n `149` status `ready` deltaP `6.6193` edge `0.0039` maxDD `-0.4545`
- `market_context_high->crypto_major_1h` score `-0.3203` n `149` status `ready` deltaP `6.9797` edge `0.0407` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.3889` n `148` status `ready` deltaP `13.9687` edge `0.0317` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.4404` n `149` status `ready` deltaP `6.8966` edge `0.0392` maxDD `-1.0837`
- `market_context_high->commodity_1h` score `-0.6213` n `149` status `ready` deltaP `-0.0412` edge `0.0069` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7344` n `149` status `ready` deltaP `-3.4743` edge `-0.0027` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7419` n `149` status `ready` deltaP `9.0563` edge `-0.0014` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.3976` n `149` status `ready` deltaP `1.0891` edge `0.0048` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5081` n `149` status `ready` deltaP `3.3446` edge `0.0207` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.6566` n `148` status `ready` deltaP `7.1321` edge `0.0275` maxDD `-15.7143`
- `market_context_high->index_4h` score `-3.0772` n `149` status `ready` deltaP `-9.6364` edge `-0.03` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.1835` n `148` status `ready` deltaP `1.1965` edge `0.0696` maxDD `-29.1905`
- `market_context_high->metal_24h` score `-3.38` n `148` status `ready` deltaP `0.108` edge `0.0196` maxDD `-10.1587`
- `market_context_high->crypto_major_4h` score `-3.3868` n `149` status `ready` deltaP `3.8141` edge `-0.0277` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.37` n `149` status `ready` deltaP `-3.4774` edge `-0.1419` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
