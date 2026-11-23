# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T21:07:32.468320+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4632`

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

- `market_context_high->unknown_1h` score `32438.6701` n `45` status `ready` deltaP `2.465` edge `2703.2155` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22277.361` n `45` status `ready` deltaP `3.4824` edge `1856.4374` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1229.1408` n `31` status `ready` deltaP `2.6801` edge `102.4281` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1042.0078` n `31` status `ready` deltaP `4.701` edge `86.8083` maxDD `-0.119`
- `news_risk_high->equity_24h` score `39.5189` n `31` status `ready` deltaP `44.2708` edge `2.9981` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `35.1026` n `31` status `ready` deltaP `46.0069` edge `2.6185` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.9782` n `31` status `ready` deltaP `46.0069` edge `2.2748` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.4874` n `31` status `ready` deltaP `45.7494` edge `0.7631` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.133` n `31` status `ready` deltaP `22.4921` edge `0.7815` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6333` n `31` status `ready` deltaP `30.6698` edge `0.5632` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.4092` n `31` status `ready` deltaP `54.5587` edge `0.1832` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.2397` n `31` status `ready` deltaP `12.3574` edge `0.8593` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.1196` n `31` status `ready` deltaP `42.5347` edge `0.2264` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.2397` n `31` status `ready` deltaP `18.0413` edge `0.1684` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.2392` n `45` status `ready` deltaP `38.6246` edge `0.0409` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.9137` n `31` status `ready` deltaP `32.1942` edge `0.0542` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5177` n `31` status `ready` deltaP `30.0464` edge `0.018` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4882` n `31` status `ready` deltaP `11.0585` edge `0.2914` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1031` n `31` status `ready` deltaP `10.1603` edge `0.2376` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5368` n `31` status `ready` deltaP `29.7324` edge `0.0267` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
