# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T02:52:28.766241+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4560`

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

- `market_context_high->unknown_1h` score `32379.4214` n `45` status `ready` deltaP `2.1656` edge `2698.2801` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22235.4446` n `45` status `ready` deltaP `3.1776` edge `1852.9464` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1169.892` n `31` status `ready` deltaP `2.3807` edge `97.4927` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1000.0914` n `31` status `ready` deltaP `4.3962` edge `83.3173` maxDD `-0.119`
- `news_risk_high->equity_24h` score `36.8506` n `31` status `ready` deltaP `42.8819` edge `2.785` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.8677` n `31` status `ready` deltaP `45.4861` edge `2.6024` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.78` n `31` status `ready` deltaP `45.6597` edge `2.2606` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.9134` n `31` status `ready` deltaP `42.6244` edge `0.7361` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.6628` n `31` status `ready` deltaP `23.864` edge `0.8165` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6539` n `31` status `ready` deltaP `30.8222` edge `0.5639` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.6291` n `31` status `ready` deltaP `56.4684` edge `0.1888` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.5804` n `31` status `ready` deltaP `14.0342` edge `0.8918` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.6697` n `31` status `ready` deltaP `40.4514` edge `0.2028` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.314` n `31` status `ready` deltaP `18.3407` edge `0.1726` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.2222` n `45` status `ready` deltaP `38.4722` edge `0.0405` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.8032` n `31` status `ready` deltaP `31.1271` edge `0.0521` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.5296` n `31` status `ready` deltaP `11.0585` edge `0.2967` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5021` n `31` status `ready` deltaP `29.8967` edge `0.0177` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.1397` n `31` status `ready` deltaP `10.31` edge `0.2413` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5991` n `31` status `ready` deltaP `30.6306` edge `0.0287` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
