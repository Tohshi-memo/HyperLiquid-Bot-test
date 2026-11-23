# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T15:37:30.264209+00:00`
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

- `market_context_high->unknown_1h` score `29560.2572` n `49` status `ready` deltaP `-0.1742` edge `2463.3721` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `20215.616` n `49` status `ready` deltaP `3.8452` edge `1684.6229` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1271.7178` n `31` status `ready` deltaP `3.5783` edge `105.9702` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1100.2522` n `31` status `ready` deltaP `4.701` edge `91.662` maxDD `-0.119`
- `news_risk_high->equity_24h` score `43.5828` n `31` status `ready` deltaP `48.0903` edge `3.3113` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `36.4785` n `31` status `ready` deltaP `48.6111` edge `2.7158` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.3356` n `31` status `ready` deltaP `48.7847` edge `2.3694` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.0475` n `31` status `ready` deltaP `48.7008` edge `0.7901` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `9.915` n `31` status `ready` deltaP `21.8823` edge `0.7674` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.5505` n `31` status `ready` deltaP `31.8893` edge `0.6315` maxDD `-2.1911`
- `news_risk_high->index_24h` score `6.8043` n `31` status `ready` deltaP `46.3542` edge `0.258` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.1021` n `31` status `ready` deltaP `51.2601` edge `0.1796` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `5.9151` n `31` status `ready` deltaP `11.2903` edge `0.8248` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.2205` n `31` status `ready` deltaP `18.0413` edge `0.1668` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.1473` n `31` status `ready` deltaP `33.7186` edge `0.0635` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.544` n `31` status `ready` deltaP `30.3458` edge `0.0182` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.5318` n `49` status `ready` deltaP `30.998` edge `0.0328` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.1312` n `31` status `ready` deltaP `8.813` edge `0.2606` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7953` n `31` status `ready` deltaP `7.7651` edge `0.2141` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4612` n `31` status `ready` deltaP `28.5348` edge `0.025` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
