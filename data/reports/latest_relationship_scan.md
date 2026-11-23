# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T16:07:28.843937+00:00`
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

- `market_context_high->unknown_1h` score `30954.8529` n `47` status `ready` deltaP `-0.6084` edge `2579.5913` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `21224.4793` n `47` status `ready` deltaP `3.6715` edge `1768.696` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1269.9202` n `31` status `ready` deltaP `3.5783` edge `105.8204` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1094.5234` n `31` status `ready` deltaP `4.701` edge `91.1846` maxDD `-0.119`
- `news_risk_high->equity_24h` score `43.207` n `31` status `ready` deltaP `47.7431` edge `3.2823` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `36.3753` n `31` status `ready` deltaP `48.6111` edge `2.7072` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.2612` n `31` status `ready` deltaP `48.7847` edge `2.3632` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.0175` n `31` status `ready` deltaP `48.7008` edge `0.7876` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `9.8622` n `31` status `ready` deltaP `21.8823` edge `0.763` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.3715` n `31` status `ready` deltaP `31.7369` edge `0.6176` maxDD `-2.1911`
- `news_risk_high->index_24h` score `6.743` n `31` status `ready` deltaP `46.0069` edge `0.2552` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.1021` n `31` status `ready` deltaP `51.2601` edge `0.1796` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `5.8667` n `31` status `ready` deltaP `11.2903` edge `0.8186` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.2229` n `31` status `ready` deltaP `18.0413` edge `0.167` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.1037` n `31` status `ready` deltaP `33.4137` edge `0.0619` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.8225` n `47` status `ready` deltaP `34.2112` edge `0.0356` maxDD `-0.2774`
- `news_risk_high->index_1h` score `2.5584` n `31` status `ready` deltaP `30.4955` edge `0.0184` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.1788` n `31` status `ready` deltaP `9.1124` edge `0.2647` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8412` n `31` status `ready` deltaP `8.0645` edge `0.218` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4636` n `31` status `ready` deltaP `28.5348` edge `0.0253` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
