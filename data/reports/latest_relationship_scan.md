# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T03:07:17.125097+00:00`
- Price records: `672`
- Market context records: `1180`
- Flow alert records: `5301`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `19.3945` n `144` status `ready` deltaP `44.4445` edge `1.4331` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `9.0602` n `144` status `ready` deltaP `22.2223` edge `0.8085` maxDD `-15.1306`
- `market_context_high->metal_24h` score `5.0408` n `144` status `ready` deltaP `-2.7778` edge `0.6053` maxDD `-6.3373`
- `market_context_high->equity_24h` score `4.4363` n `144` status `ready` deltaP `17.3611` edge `0.4346` maxDD `-11.4521`
- `market_context_high->index_24h` score `4.0326` n `144` status `ready` deltaP `17.0139` edge `0.2998` maxDD `-4.1741`
- `market_context_high->equity_4h` score `2.7385` n `148` status `ready` deltaP `14.2551` edge `0.1995` maxDD `-3.6396`
- `market_context_high->unknown_4h` score `1.2383` n `148` status `ready` deltaP `5.8422` edge `0.1859` maxDD `-6.7322`
- `market_context_high->index_4h` score `1.2305` n `148` status `ready` deltaP `10.2217` edge `0.1027` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.7266` n `148` status `ready` deltaP `9.7264` edge `0.0274` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.422` n `148` status `ready` deltaP `3.6494` edge `0.0486` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.0269` n `148` status `ready` deltaP `7.3677` edge `-0.0001` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.0262` n `148` status `ready` deltaP `7.8239` edge `0.1366` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.1457` n `148` status `ready` deltaP `7.829` edge `-0.0033` maxDD `-2.2164`
- `market_context_high->crypto_major_1h` score `-0.1553` n `148` status `ready` deltaP `5.2598` edge `0.0216` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.3547` n `148` status `ready` deltaP `0.9913` edge `0.0322` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.9533` n `148` status `ready` deltaP `-4.9563` edge `-0.0084` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-1.1237` n `148` status `ready` deltaP `-5.5537` edge `-0.0074` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.3935` n `148` status `ready` deltaP `3.3207` edge `0.0957` maxDD `-16.7194`
- `market_context_high->fx_24h` score `-1.4843` n `144` status `ready` deltaP `3.8195` edge `0.0073` maxDD `-11.1775`
- `market_context_high->unknown_24h` score `-1.6516` n `144` status `ready` deltaP `4.3403` edge `0.1064` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
