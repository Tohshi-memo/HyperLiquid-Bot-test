# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T18:14:45.498665+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8627`

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

- `market_context_high->unknown_4h` score `80.9854` n `135` status `ready` deltaP `4.5472` edge `6.7337` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `3.4804` n `144` status `ready` deltaP `0.3992` edge `0.3363` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.9867` n `135` status `ready` deltaP `27.1875` edge `0.0531` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4485` n `144` status `ready` deltaP `10.4832` edge `0.0033` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4383` n `135` status `ready` deltaP `12.8963` edge `0.0104` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0334` n `144` status `ready` deltaP `9.2981` edge `0.0084` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.3514` n `135` status `ready` deltaP `6.6892` edge `0.048` maxDD `-1.0837`
- `market_context_high->commodity_1h` score `-0.3632` n `144` status `ready` deltaP `1.3348` edge `0.0109` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.3691` n `144` status `ready` deltaP `7.406` edge `0.0316` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.5245` n `135` status `ready` deltaP `10.3472` edge `0.021` maxDD `-1.2451`
- `market_context_high->index_1h` score `-0.5956` n `144` status `ready` deltaP `-0.7901` edge `-0.0028` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8564` n `135` status `ready` deltaP `7.7089` edge `-0.0071` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-0.9839` n `135` status `ready` deltaP `15.7523` edge `0.0908` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.3966` n `144` status `ready` deltaP `2.0542` edge `-0.0015` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.7106` n `135` status `ready` deltaP `8.0671` edge `0.1001` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.788` n `144` status `ready` deltaP `1.1269` edge `-0.0004` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.9608` n `135` status `ready` deltaP `-7.5373` edge `-0.0343` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.8001` n `135` status `ready` deltaP `0.544` edge `-0.0051` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.8437` n `135` status `ready` deltaP `3.2024` edge `-0.0822` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.5169` n `135` status `ready` deltaP `-0.3489` edge `-0.1816` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
