# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T08:22:37.655462+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5152`

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

- `market_context_high->unknown_1h` score `18266.966` n `75` status `ready` deltaP `1.8802` edge `1522.2508` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `12053.2032` n `75` status `ready` deltaP `3.7744` edge `1004.4223` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1317.0431` n `31` status `ready` deltaP `3.4286` edge `109.7483` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1171.1912` n `31` status `ready` deltaP `4.5486` edge `97.5746` maxDD `-0.119`
- `news_risk_high->equity_4h` score `10.972` n `31` status `ready` deltaP `35.243` edge `0.7276` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.3946` n `31` status `ready` deltaP `23.4067` edge `0.7972` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.3249` n `31` status `ready` deltaP `12.6623` edge `0.8682` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.7747` n `31` status `ready` deltaP `18.9395` edge `0.207` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.487` n `31` status `ready` deltaP `36.6149` edge `0.0725` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6783` n `31` status `ready` deltaP `31.3937` edge `0.0224` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4002` n `31` status `ready` deltaP `9.4118` edge `0.2911` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9622` n `31` status `ready` deltaP `7.6154` edge `0.2365` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5119` n `31` status `ready` deltaP `28.8342` edge `0.0295` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4072` n `31` status `ready` deltaP `19.522` edge `0.106` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.839` n `31` status `ready` deltaP `18.1255` edge `0.0265` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.5361` n `75` status `ready` deltaP `16.6301` edge `0.0166` maxDD `-0.3661`
- `news_risk_high->commodity_1h` score `-0.0285` n `31` status `ready` deltaP `1.5308` edge `0.0136` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.2691` n `75` status `ready` deltaP `2.6407` edge `0.0118` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.3365` n `75` status `ready` deltaP `0.0818` edge `0.0019` maxDD `-0.9806`
- `market_context_high->commodity_1h` score `-1.0594` n `75` status `ready` deltaP `-4.1896` edge `-0.0189` maxDD `-2.7863`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
