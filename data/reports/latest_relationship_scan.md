# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T15:07:37.181982+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4470`

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

- `market_context_high->unknown_1h` score `28272.2404` n `51` status `ready` deltaP `0.226` edge `2356.0347` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `19280.3584` n `51` status `ready` deltaP `4.0052` edge `1606.6837` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1271.6158` n `31` status `ready` deltaP `3.5783` edge `105.9617` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1100.4658` n `31` status `ready` deltaP `4.701` edge `91.6798` maxDD `-0.119`
- `news_risk_high->equity_24h` score `44.0006` n `31` status `ready` deltaP `48.4375` edge `3.3438` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `36.6777` n `31` status `ready` deltaP `48.6111` edge `2.7324` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.4868` n `31` status `ready` deltaP `48.7847` edge `2.382` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.1196` n `31` status `ready` deltaP `49.048` edge `0.7938` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.0388` n `31` status `ready` deltaP `22.0348` edge `0.7767` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.8005` n `31` status `ready` deltaP `32.1942` edge `0.6503` maxDD `-2.1911`
- `news_risk_high->index_24h` score `6.8705` n `31` status `ready` deltaP `46.7014` edge `0.2612` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.1323` n `31` status `ready` deltaP `51.6073` edge `0.1798` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.0205` n `31` status `ready` deltaP `11.4427` edge `0.8373` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.2301` n `31` status `ready` deltaP `18.0413` edge `0.1676` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.1969` n `31` status `ready` deltaP `34.0234` edge `0.0656` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5584` n `31` status `ready` deltaP `30.4955` edge `0.0184` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.2053` n `51` status `ready` deltaP `28.0368` edge `0.0295` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.1156` n `31` status `ready` deltaP `8.6633` edge `0.2596` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7789` n `31` status `ready` deltaP `7.6154` edge `0.213` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4644` n `31` status `ready` deltaP `28.5348` edge `0.0254` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
