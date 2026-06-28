# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T21:52:33.016907+00:00`
- Price records: `672`
- Market context records: `5081`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10338`

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

- `market_context_high->unknown_24h` score `11.8798` n `76` status `ready` deltaP `27.3209` edge `0.8421` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `11.1653` n `105` status `ready` deltaP `2.2854` edge `0.9767` maxDD `-2.5863`
- `market_context_high->unknown_4h` score `9.2997` n `93` status `ready` deltaP `21.4496` edge `0.7342` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `6.7494` n `93` status `ready` deltaP `19.7073` edge `0.553` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `5.968` n `93` status `ready` deltaP `18.1665` edge `0.5451` maxDD `-9.1768`
- `market_context_high->equity_4h` score `2.1094` n `93` status `ready` deltaP `10.52` edge `0.2188` maxDD `-6.3852`
- `market_context_high->equity_1h` score `1.024` n `105` status `ready` deltaP `9.4967` edge `0.0752` maxDD `-2.5875`
- `market_context_high->metal_1h` score `0.863` n `105` status `ready` deltaP `12.4907` edge `0.0383` maxDD `-1.3057`
- `market_context_high->crypto_major_1h` score `0.8208` n `105` status `ready` deltaP `6.8178` edge `0.1256` maxDD `-5.2121`
- `market_context_high->metal_4h` score `0.778` n `93` status `ready` deltaP `10.1741` edge `0.1049` maxDD `-1.9651`
- `market_context_high->crypto_alt_1h` score `0.7628` n `105` status `ready` deltaP `5.5788` edge `0.1074` maxDD `-3.8153`
- `market_context_high->index_4h` score `0.344` n `93` status `ready` deltaP `8.8021` edge `0.0461` maxDD `-1.0893`
- `market_context_high->index_1h` score `0.3176` n `105` status `ready` deltaP `6.0408` edge `0.016` maxDD `-0.3843`
- `market_context_high->commodity_1h` score `-0.43` n `105` status `ready` deltaP `0.8169` edge `0.0054` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.4798` n `93` status `ready` deltaP `8.9217` edge `0.0089` maxDD `-3.6686`
- `market_context_high->fx_24h` score `-0.5959` n `76` status `ready` deltaP `0.4203` edge `-0.003` maxDD `-1.7626`
- `market_context_high->fx_4h` score `-1.1574` n `93` status `ready` deltaP `-6.3713` edge `-0.0046` maxDD `-1.4377`
- `market_context_high->fx_1h` score `-1.8032` n `105` status `ready` deltaP `-12.217` edge `-0.0052` maxDD `-0.7561`
- `market_context_high->commodity_24h` score `-1.944` n `76` status `ready` deltaP `9.6491` edge `0.028` maxDD `-17.6575`
- `market_context_high->metal_24h` score `-4.2434` n `76` status `ready` deltaP `-2.8418` edge `0.0204` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
