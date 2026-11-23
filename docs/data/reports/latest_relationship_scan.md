# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T20:37:25.410646+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4652`

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

- `market_context_high->unknown_1h` score `32449.0957` n `45` status `ready` deltaP `2.6147` edge `2704.0833` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22287.519` n `45` status `ready` deltaP `3.4824` edge `1857.2839` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1239.5663` n `31` status `ready` deltaP `2.8298` edge `103.2959` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1052.1658` n `31` status `ready` deltaP `4.701` edge `87.6548` maxDD `-0.119`
- `news_risk_high->equity_24h` score `39.8442` n `31` status `ready` deltaP `44.6181` edge `3.0229` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `35.1752` n `31` status `ready` deltaP `46.1806` edge `2.6234` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.0388` n `31` status `ready` deltaP `46.1806` edge `2.2787` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.5415` n `31` status `ready` deltaP `46.0966` edge `0.7653` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.0814` n `31` status `ready` deltaP `22.4921` edge `0.7772` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6139` n `31` status `ready` deltaP `30.5173` edge `0.5626` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.3766` n `31` status `ready` deltaP `54.2115` edge `0.1828` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.2038` n `31` status `ready` deltaP `12.3574` edge `0.8547` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.1774` n `31` status `ready` deltaP `42.8819` edge `0.2289` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.2672` n `31` status `ready` deltaP `18.191` edge `0.1697` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.2124` n `45` status `ready` deltaP `38.3198` edge `0.0407` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.9003` n `31` status `ready` deltaP `32.0417` edge `0.0541` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.544` n `31` status `ready` deltaP `30.3458` edge `0.0182` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4578` n `31` status `ready` deltaP `10.9088` edge `0.2885` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0688` n `31` status `ready` deltaP `9.8609` edge `0.2352` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5282` n `31` status `ready` deltaP `29.5827` edge `0.0266` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
