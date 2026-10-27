# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T12:22:30.520729+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8856`

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

- `market_context_high->unknown_4h` score `81.6837` n `135` status `ready` deltaP `5.4619` edge `6.7858` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `15.0036` n `135` status `ready` deltaP `1.2187` edge `1.2911` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.9373` n `132` status `ready` deltaP `26.7055` edge `0.0522` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.5086` n `135` status `ready` deltaP `11.2054` edge `0.0035` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4359` n `135` status `ready` deltaP `12.8963` edge `0.0102` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.0631` n `135` status `ready` deltaP `10.7951` edge `0.0108` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.3285` n `135` status `ready` deltaP `1.8286` edge `0.0105` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.4474` n `135` status `ready` deltaP `6.1854` edge `0.0297` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5601` n `135` status `ready` deltaP `-0.2129` edge `-0.0021` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-0.6932` n `132` status `ready` deltaP `7.539` edge `0.0181` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.7243` n `135` status `ready` deltaP `8.9284` edge `0.0017` maxDD `-4.6603`
- `market_context_high->commodity_4h` score `-0.7333` n `135` status `ready` deltaP `3.6405` edge `0.0365` maxDD `-1.0837`
- `market_context_high->metal_24h` score `-1.1942` n `132` status `ready` deltaP `13.828` edge `0.0861` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.3778` n `135` status `ready` deltaP `2.3397` edge `-0.001` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.9421` n `135` status `ready` deltaP `-1.0413` edge `-0.0057` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.4782` n `132` status `ready` deltaP `7.2015` edge `0.0419` maxDD `-15.7143`
- `market_context_high->index_4h` score `-2.57` n `135` status `ready` deltaP `-4.0312` edge `-0.0251` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.5194` n `135` status `ready` deltaP `4.8792` edge `-0.0518` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.4198` n `132` status `ready` deltaP `-0.8443` edge `-0.0753` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-4.8864` n `135` status `ready` deltaP `2.8523` edge `-0.1221` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
