# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T00:07:21.647675+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3540`

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

- `news_risk_high->unknown_1h` score `3209.3796` n `31` status `ready` deltaP `2.0813` edge `267.452` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3182.5098` n `31` status `ready` deltaP `4.3962` edge `265.1855` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `27.055` n `31` status `ready` deltaP `35.9375` edge `2.015` maxDD `0.0`
- `news_risk_high->equity_24h` score `24.0864` n `31` status `ready` deltaP `35.0694` edge `1.7734` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.9238` n `31` status `ready` deltaP `35.2431` edge `1.5087` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.698` n `31` status `ready` deltaP `23.864` edge `0.7361` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.3615` n `31` status `ready` deltaP `35.243` edge `0.5099` maxDD `-2.178`
- `news_risk_high->metal_24h` score `6.3141` n `31` status `ready` deltaP `22.6591` edge `0.4026` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.3003` n `31` status `ready` deltaP `16.7781` edge `0.8376` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.9767` n `31` status `ready` deltaP `42.2323` edge `0.146` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.2439` n `31` status `ready` deltaP `36.4583` edge `0.1106` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.1677` n `31` status `ready` deltaP `18.6401` edge `0.1584` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.9511` n `31` status `ready` deltaP `33.2612` edge `0.0502` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5572` n `31` status `ready` deltaP `30.6452` edge `0.0173` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3177` n `31` status `ready` deltaP `8.3639` edge `0.2875` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0928` n `31` status `ready` deltaP `11.3579` edge `0.2283` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.3475` n `31` status `ready` deltaP `27.3372` edge `0.0184` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.6516` n `31` status `ready` deltaP `13.1196` edge `0.0518` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.2234` n `31` status `ready` deltaP `9.4365` edge `0.0055` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4718` n `31` status `ready` deltaP `-2.9602` edge `0.0066` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
