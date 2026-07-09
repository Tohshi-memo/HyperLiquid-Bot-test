# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T02:52:27.800190+00:00`
- Price records: `672`
- Market context records: `6150`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `11.9307` n `30` status `ready` deltaP `41.7708` edge `0.7305` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.6758` n `30` status `ready` deltaP `67.8819` edge `0.1871` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3055` n `32` status `ready` deltaP `44.8933` edge `0.0641` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4039` n `32` status `ready` deltaP `28.8922` edge `0.0216` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.4983` n `195` status `ready` deltaP `0.5052` edge `0.2223` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.2745` n `32` status `ready` deltaP `13.6789` edge `0.1189` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6697` n `32` status `ready` deltaP `8.7762` edge `0.0735` maxDD `-1.6923`
- `news_risk_high->crypto_major_24h` score `0.4839` n `30` status `ready` deltaP `12.4652` edge `0.0569` maxDD `-4.2368`
- `market_context_high->equity_4h` score `0.0752` n `195` status `ready` deltaP `2.6829` edge `0.0801` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.229` n `30` status `ready` deltaP `7.5` edge `0.0078` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2676` n `195` status `ready` deltaP `1.5845` edge `-0.0003` maxDD `-0.5659`
- `market_context_high->unknown_4h` score `-0.3339` n `195` status `ready` deltaP `-2.4594` edge `0.2418` maxDD `-11.925`
- `market_context_high->metal_24h` score `-0.422` n `195` status `ready` deltaP `17.946` edge `0.0831` maxDD `-11.8809`
- `market_context_high->metal_4h` score `-0.5769` n `195` status `ready` deltaP `4.1518` edge `0.0171` maxDD `-3.4996`
- `news_risk_high->commodity_24h` score `-0.6091` n `30` status `ready` deltaP `14.0973` edge `-0.1242` maxDD `-0.3101`
- `news_risk_high->metal_1h` score `-0.7458` n `32` status `ready` deltaP `-2.6946` edge `-0.0279` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.7763` n `195` status `ready` deltaP `-2.2885` edge `-0.0048` maxDD `-0.5708`
- `market_context_high->metal_1h` score `-0.7817` n `195` status `ready` deltaP `2.69` edge `-0.0032` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.8608` n `195` status `ready` deltaP `-1.4571` edge `0.0109` maxDD `-4.2573`
- `market_context_high->crypto_alt_1h` score `-0.9062` n `195` status `ready` deltaP `3.7602` edge `0.034` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
