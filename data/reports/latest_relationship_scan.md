# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T19:38:10.567286+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8636`

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

- `market_context_high->unknown_24h` score `1223.6403` n `148` status `ready` deltaP `-2.135` edge `102.077` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.6852` n `149` status `ready` deltaP `4.385` edge `1.7931` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.365` n `148` status `ready` deltaP `23.5407` edge `0.0256` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1482` n `149` status `ready` deltaP `6.9696` edge `0.0017` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.1019` n `149` status `ready` deltaP `8.1773` edge `0.0071` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.21` n `149` status `ready` deltaP `5.8571` edge `0.0033` maxDD `-0.4545`
- `market_context_high->crypto_major_1h` score `-0.3944` n `149` status `ready` deltaP `6.2312` edge `0.0362` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.4452` n `149` status `ready` deltaP `6.8966` edge `0.0388` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.507` n `148` status `ready` deltaP `12.927` edge `0.0288` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.6309` n `149` status `ready` deltaP `-0.1909` edge `0.0071` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7694` n `149` status `ready` deltaP `-4.0731` edge `-0.0032` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7822` n `149` status `ready` deltaP `8.4466` edge `-0.0025` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.4553` n `149` status `ready` deltaP `0.64` edge `0.0004` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6016` n `149` status `ready` deltaP `2.4464` edge `0.0147` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1356` n `149` status `ready` deltaP `-10.2462` edge `-0.0308` maxDD `-5.6417`
- `market_context_high->equity_24h` score `-3.1647` n `148` status `ready` deltaP `6.0904` edge `-0.0079` maxDD `-15.7143`
- `market_context_high->crypto_major_24h` score `-3.3195` n `148` status `ready` deltaP `0.1549` edge `0.0591` maxDD `-29.1905`
- `market_context_high->metal_24h` score `-3.4395` n `148` status `ready` deltaP `-0.0657` edge `0.0158` maxDD `-10.1587`
- `market_context_high->crypto_major_4h` score `-3.4401` n `149` status `ready` deltaP `3.5092` edge `-0.0325` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.4681` n `149` status `ready` deltaP `-4.2396` edge `-0.1494` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
