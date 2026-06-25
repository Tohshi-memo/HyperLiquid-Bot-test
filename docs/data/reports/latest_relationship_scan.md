# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T05:22:32.691834+00:00`
- Price records: `672`
- Market context records: `4693`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9760`

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

- `market_context_high->unknown_1h` score `77.8039` n `137` status `ready` deltaP `12.6623` edge `6.441` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.2144` n `135` status `ready` deltaP `10.9169` edge `0.4828` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.22` n `135` status `ready` deltaP `11.8403` edge `0.1984` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.5015` n `137` status `ready` deltaP `2.086` edge `0.0239` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.7804` n `135` status `ready` deltaP `3.7692` edge `-0.0129` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.8093` n `137` status `ready` deltaP `-2.2739` edge `0.0101` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.9362` n `135` status `ready` deltaP `-1.4826` edge `-0.0019` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-1.1016` n `137` status `ready` deltaP `-4.6702` edge `-0.0052` maxDD `-1.1038`
- `market_context_high->commodity_4h` score `-1.2359` n `135` status `ready` deltaP `5.5511` edge `0.0153` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.2607` n `135` status `ready` deltaP `1.3946` edge `0.006` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7369` n `137` status `ready` deltaP `-4.8188` edge `-0.0122` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.8308` n `137` status `ready` deltaP `-4.2026` edge `-0.0781` maxDD `-17.2107`
- `market_context_high->commodity_24h` score `-4.7539` n `135` status `ready` deltaP `14.5023` edge `0.0576` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-4.7654` n `135` status `ready` deltaP `-12.8704` edge `-0.0153` maxDD `-5.3476`
- `market_context_high->crypto_alt_1h` score `-5.327` n `137` status `ready` deltaP `-1.6937` edge `-0.1039` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.4478` n `137` status `ready` deltaP `-4.4451` edge `-0.1324` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.3927` n `135` status `ready` deltaP `-10.6366` edge `-0.091` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.6314` n `135` status `ready` deltaP `-3.1595` edge `-0.2198` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.1369` n `135` status `ready` deltaP `-0.5488` edge `-0.2824` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.6181` n `135` status `ready` deltaP `-3.5953` edge `-0.3755` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
