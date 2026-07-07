# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T11:52:27.012007+00:00`
- Price records: `672`
- Market context records: `5978`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11220`

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

- `news_risk_high->fx_24h` score `7.2972` n `30` status `ready` deltaP `66.8403` edge `0.1625` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.8204` n `30` status `ready` deltaP `35.4514` edge `0.1859` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.9938` n `30` status `ready` deltaP `41.372` edge `0.0616` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1508` n `30` status `ready` deltaP `25.8782` edge `0.0206` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.3105` n `238` status `ready` deltaP `8.452` edge `0.1623` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.7741` n `30` status `ready` deltaP `9.8902` edge `0.08` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1101` n `30` status `ready` deltaP `4.8703` edge `0.0278` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0247` n `30` status `ready` deltaP `9.0625` edge `0.0299` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.4149` n `30` status `ready` deltaP `1.5369` edge `-0.0268` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.449` n `242` status `ready` deltaP `3.5817` edge `0.0314` maxDD `-4.3608`
- `market_context_high->commodity_1h` score `-0.4935` n `242` status `ready` deltaP `-1.4314` edge `0.002` maxDD `-1.4578`
- `market_context_high->metal_1h` score `-0.523` n `242` status `ready` deltaP `1.9226` edge `0.0` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.6895` n `242` status `ready` deltaP `-0.7609` edge `-0.0007` maxDD `-0.8015`
- `market_context_high->index_1h` score `-0.7067` n `242` status `ready` deltaP `-0.5629` edge `0.0045` maxDD `-1.3078`
- `market_context_high->equity_24h` score `-0.9613` n `214` status `ready` deltaP `21.2422` edge `0.3109` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.0882` n `30` status `ready` deltaP `-10.1497` edge `-0.0204` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.1247` n `238` status `ready` deltaP `0.7698` edge `0.0194` maxDD `-3.165`
- `market_context_high->crypto_major_1h` score `-1.1629` n `242` status `ready` deltaP `1.9288` edge `0.0148` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.1964` n `242` status `ready` deltaP `1.5094` edge `0.0118` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.422` n `238` status `ready` deltaP `-1.0453` edge `-0.004` maxDD `-6.3734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
