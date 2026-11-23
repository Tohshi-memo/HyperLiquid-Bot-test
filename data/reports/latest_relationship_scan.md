# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T15:22:29.812948+00:00`
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

- `market_context_high->unknown_1h` score `28904.2179` n `50` status `ready` deltaP `0.0299` edge `2408.7008` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `19739.4974` n `50` status `ready` deltaP `3.9268` edge `1644.9458` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1271.605` n `31` status `ready` deltaP `3.5783` edge `105.9608` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1100.287` n `31` status `ready` deltaP `4.701` edge `91.6649` maxDD `-0.119`
- `news_risk_high->equity_24h` score `43.7887` n `31` status `ready` deltaP `48.2639` edge `3.3273` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `36.5673` n `31` status `ready` deltaP `48.6111` edge `2.7232` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.4028` n `31` status `ready` deltaP `48.7847` edge `2.375` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.083` n `31` status `ready` deltaP `48.8744` edge `0.7919` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `9.9618` n `31` status `ready` deltaP `21.8823` edge `0.7713` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.6731` n `31` status `ready` deltaP `32.0417` edge `0.6407` maxDD `-2.1911`
- `news_risk_high->index_24h` score `6.8374` n `31` status `ready` deltaP `46.5278` edge `0.2596` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.1172` n `31` status `ready` deltaP `51.4337` edge `0.1797` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `5.9556` n `31` status `ready` deltaP `11.2903` edge `0.83` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.2229` n `31` status `ready` deltaP `18.0413` edge `0.167` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.1715` n `31` status `ready` deltaP `33.871` edge `0.0645` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5452` n `31` status `ready` deltaP `30.3458` edge `0.0183` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.3942` n `50` status `ready` deltaP `29.4878` edge `0.0314` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.1109` n `31` status `ready` deltaP `8.6633` edge `0.259` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7742` n `31` status `ready` deltaP `7.6154` edge `0.2124` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.462` n `31` status `ready` deltaP `28.5348` edge `0.0251` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
