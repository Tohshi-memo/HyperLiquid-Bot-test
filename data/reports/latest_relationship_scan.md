# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T00:52:26.159357+00:00`
- Price records: `672`
- Market context records: `6557`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9872`

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

- `market_context_high->unknown_24h` score `6.3883` n `144` status `ready` deltaP `11.8934` edge `0.7831` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.8035` n `209` status `ready` deltaP `-4.9358` edge `0.2733` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3653` n `144` status `ready` deltaP `13.304` edge `0.2119` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.2244` n `197` status `ready` deltaP `11.6712` edge `0.0252` maxDD `-0.939`
- `market_context_high->crypto_alt_4h` score `-0.1917` n `197` status `ready` deltaP `8.7308` edge `0.1024` maxDD `-8.4596`
- `market_context_high->fx_1h` score `-0.3534` n `209` status `ready` deltaP `0.9025` edge `-0.0006` maxDD `-0.7249`
- `market_context_high->equity_4h` score `-0.4276` n `197` status `ready` deltaP `9.5951` edge `0.0511` maxDD `-8.2573`
- `market_context_high->crypto_major_1h` score `-0.4606` n `209` status `ready` deltaP `6.8762` edge `0.0217` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.4987` n `209` status `ready` deltaP `6.609` edge `0.0233` maxDD `-5.8368`
- `market_context_high->crypto_major_4h` score `-0.5046` n `197` status `ready` deltaP `11.1683` edge `0.0899` maxDD `-12.6576`
- `market_context_high->commodity_1h` score `-0.5665` n `209` status `ready` deltaP `-0.0337` edge `-0.0041` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.6008` n `209` status `ready` deltaP `-1.1962` edge `0.0029` maxDD `-0.7564`
- `market_context_high->unknown_4h` score `-0.9302` n `197` status `ready` deltaP `-16.4928` edge `0.273` maxDD `-10.5788`
- `market_context_high->equity_1h` score `-1.1888` n `209` status `ready` deltaP `1.8831` edge `-0.0006` maxDD `-4.2147`
- `market_context_high->metal_1h` score `-1.2386` n `209` status `ready` deltaP `-3.2247` edge `-0.001` maxDD `-2.1239`
- `market_context_high->metal_4h` score `-1.2405` n `197` status `ready` deltaP `0.9232` edge `0.0348` maxDD `-2.6662`
- `market_context_high->metal_24h` score `-1.9769` n `144` status `ready` deltaP `5.966` edge `0.0885` maxDD `-5.7746`
- `market_context_high->commodity_4h` score `-2.0682` n `197` status `ready` deltaP `-1.6319` edge `-0.012` maxDD `-5.6246`
- `market_context_high->fx_4h` score `-2.9964` n `197` status `ready` deltaP `-3.0433` edge `-0.0082` maxDD `-3.3635`
- `market_context_high->fx_24h` score `-3.8447` n `144` status `ready` deltaP `-4.7877` edge `-0.0075` maxDD `-9.2795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
