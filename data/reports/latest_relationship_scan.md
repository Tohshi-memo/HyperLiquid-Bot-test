# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T12:52:31.228185+00:00`
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

- `market_context_high->unknown_4h` score `81.3235` n `135` status `ready` deltaP `5.3094` edge `6.7568` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `15.0036` n `135` status `ready` deltaP `1.069` edge `1.2921` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.9265` n `132` status `ready` deltaP `26.7055` edge `0.0513` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4955` n `135` status `ready` deltaP `11.0557` edge `0.0034` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4213` n `135` status `ready` deltaP `12.7439` edge `0.01` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.0452` n `135` status `ready` deltaP `10.4957` edge `0.0105` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.3405` n `135` status `ready` deltaP `1.6789` edge `0.0105` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.4576` n `135` status `ready` deltaP `6.1854` edge `0.0284` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5609` n `135` status `ready` deltaP `-0.2129` edge `-0.0022` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-0.6744` n `132` status `ready` deltaP `7.8856` edge `0.0182` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.6921` n `135` status `ready` deltaP `3.9453` edge `0.0379` maxDD `-1.0837`
- `market_context_high->metal_4h` score `-0.7503` n `135` status `ready` deltaP `8.6235` edge `0.0004` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-1.1557` n `132` status `ready` deltaP `14.1746` edge `0.087` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.3841` n `135` status `ready` deltaP `2.3397` edge `-0.0018` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.946` n `135` status `ready` deltaP `-1.0413` edge `-0.0062` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.4794` n `132` status `ready` deltaP `7.2015` edge `0.0418` maxDD `-15.7143`
- `market_context_high->index_4h` score `-2.6087` n `135` status `ready` deltaP `-4.3361` edge `-0.0263` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.5673` n `135` status `ready` deltaP `4.5743` edge `-0.0559` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.3808` n `132` status `ready` deltaP `-0.8443` edge `-0.0703` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-4.956` n `135` status `ready` deltaP `2.5474` edge `-0.129` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
