# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T11:37:29.508215+00:00`
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

- `market_context_high->unknown_4h` score `82.2957` n `135` status `ready` deltaP `5.4619` edge `6.8368` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `15.1728` n `135` status `ready` deltaP `1.069` edge `1.3062` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.9541` n `132` status `ready` deltaP `26.7055` edge `0.0536` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.5098` n `135` status `ready` deltaP `11.2054` edge `0.0036` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4627` n `135` status `ready` deltaP `13.2012` edge `0.0104` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.0468` n `135` status `ready` deltaP `10.4957` edge `0.0107` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.2854` n `135` status `ready` deltaP `2.2777` edge `0.0111` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.4716` n `135` status `ready` deltaP `5.886` edge `0.0286` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5609` n `135` status `ready` deltaP `-0.2129` edge `-0.0022` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.6935` n `135` status `ready` deltaP `9.3857` edge `0.0026` maxDD `-4.6603`
- `market_context_high->fx_24h` score `-0.7226` n `132` status `ready` deltaP `7.0191` edge `0.0178` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.7489` n `135` status `ready` deltaP `3.6405` edge `0.0352` maxDD `-1.0837`
- `market_context_high->metal_24h` score `-1.2574` n `132` status `ready` deltaP `13.3081` edge `0.0843` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.3879` n `135` status `ready` deltaP `2.19` edge `-0.0013` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.9608` n `135` status `ready` deltaP `-1.191` edge `-0.0071` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.4542` n `132` status `ready` deltaP `7.2015` edge `0.0439` maxDD `-15.7143`
- `market_context_high->index_4h` score `-2.5178` n `135` status `ready` deltaP `-3.5739` edge `-0.0238` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.5266` n `135` status `ready` deltaP `4.7267` edge `-0.0517` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.5166` n `132` status `ready` deltaP `-1.1909` edge `-0.0854` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-4.8025` n `135` status `ready` deltaP `3.3096` edge `-0.1144` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
