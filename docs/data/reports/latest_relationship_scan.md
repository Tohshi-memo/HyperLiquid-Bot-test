# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T11:52:27.694039+00:00`
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

- `market_context_high->unknown_4h` score `82.0953` n `135` status `ready` deltaP `5.4619` edge `6.8201` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `15.072` n `135` status `ready` deltaP `1.069` edge `1.2978` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.9481` n `132` status `ready` deltaP `26.7055` edge `0.0531` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.5098` n `135` status `ready` deltaP `11.2054` edge `0.0036` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4615` n `135` status `ready` deltaP `13.2012` edge `0.0103` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.0468` n `135` status `ready` deltaP `10.4957` edge `0.0107` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.2986` n `135` status `ready` deltaP `2.128` edge `0.011` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.4607` n `135` status `ready` deltaP `6.0357` edge `0.029` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5609` n `135` status `ready` deltaP `-0.2129` edge `-0.0022` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7038` n `135` status `ready` deltaP `9.2333` edge `0.0023` maxDD `-4.6603`
- `market_context_high->fx_24h` score `-0.712` n `132` status `ready` deltaP `7.1924` edge `0.018` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.7429` n `135` status `ready` deltaP `3.6405` edge `0.0357` maxDD `-1.0837`
- `market_context_high->metal_24h` score `-1.2363` n `132` status `ready` deltaP `13.4814` edge `0.0849` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.3895` n `135` status `ready` deltaP `2.19` edge `-0.0015` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.9592` n `135` status `ready` deltaP `-1.191` edge `-0.0069` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.4722` n `132` status `ready` deltaP `7.2015` edge `0.0424` maxDD `-15.7143`
- `market_context_high->index_4h` score `-2.536` n `135` status `ready` deltaP `-3.7263` edge `-0.0243` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.5281` n `135` status `ready` deltaP `4.7267` edge `-0.0519` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.485` n `132` status `ready` deltaP `-1.0176` edge `-0.0825` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-4.8331` n `135` status `ready` deltaP `3.1572` edge `-0.1173` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
