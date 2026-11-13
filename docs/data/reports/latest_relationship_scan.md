# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T06:37:27.218020+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11824`

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

- `market_context_high->unknown_24h` score `268.2997` n `84` status `ready` deltaP `6.2996` edge `22.3304` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `56.6088` n `94` status `ready` deltaP `6.7333` edge `4.7173` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `31.7916` n `53` status `ready` deltaP `29.6744` edge `2.5221` maxDD `-3.6503`
- `market_context_high->equity_24h` score `23.7742` n `84` status `ready` deltaP `27.4057` edge `1.8691` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `13.2085` n `53` status `ready` deltaP `40.1337` edge `1.6224` maxDD `-12.7247`
- `market_context_high->crypto_alt_24h` score `10.2252` n `84` status `ready` deltaP `48.1647` edge `1.3994` maxDD `-25.4331`
- `news_risk_high->equity_4h` score `10.0012` n `53` status `ready` deltaP `33.9536` edge `0.7201` maxDD `-7.0416`
- `market_context_high->metal_24h` score `7.1328` n `84` status `ready` deltaP `43.7252` edge `0.3442` maxDD `-0.3044`
- `news_risk_high->commodity_24h` score `6.4322` n `53` status `ready` deltaP `40.2778` edge `0.2675` maxDD `0.0`
- `market_context_high->index_24h` score `4.5038` n `84` status `ready` deltaP `25.8929` edge `0.2122` maxDD `-0.0934`
- `news_risk_high->metal_4h` score `4.4095` n `53` status `ready` deltaP `42.4327` edge `0.1222` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.0955` n `53` status `ready` deltaP `24.0959` edge `0.211` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `3.3429` n `53` status `ready` deltaP `20.1335` edge `0.2931` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.2122` n `53` status `ready` deltaP `17.5658` edge `0.2136` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1885` n `53` status `ready` deltaP `29.3028` edge `0.0957` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `2.7875` n `53` status `ready` deltaP `18.2455` edge `0.6863` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.09` n `53` status `ready` deltaP `24.8418` edge `0.034` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.9679` n `53` status `ready` deltaP `26.4985` edge `0.2395` maxDD `-10.1088`
- `news_risk_high->index_4h` score `1.7998` n `53` status `ready` deltaP `18.9168` edge `0.0675` maxDD `-0.8235`
- `news_risk_high->index_1h` score `1.1735` n `53` status `ready` deltaP `16.2778` edge `0.0194` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
