# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T07:52:28.315565+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5234`

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

- `market_context_high->unknown_1h` score `17707.5078` n `77` status `ready` deltaP `2.088` edge `1475.6279` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `11659.9701` n `77` status `ready` deltaP `3.7259` edge `971.6532` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1317.0167` n `31` status `ready` deltaP `3.4286` edge `109.7461` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1169.3322` n `31` status `ready` deltaP `4.3962` edge `97.4207` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.0252` n `31` status `ready` deltaP `35.5478` edge `0.73` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.4066` n `31` status `ready` deltaP `23.4067` edge `0.7982` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.3123` n `31` status `ready` deltaP `12.5098` edge `0.8676` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.7807` n `31` status `ready` deltaP `18.9395` edge `0.2075` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4882` n `31` status `ready` deltaP `36.6149` edge `0.0726` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6783` n `31` status `ready` deltaP `31.3937` edge `0.0224` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4073` n `31` status `ready` deltaP `9.5615` edge `0.291` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9723` n `31` status `ready` deltaP `7.7651` edge `0.2368` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4987` n `31` status `ready` deltaP `28.6845` edge `0.0288` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4065` n `31` status `ready` deltaP `19.522` edge `0.1059` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.8359` n `31` status `ready` deltaP `18.1255` edge `0.0261` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.452` n `77` status `ready` deltaP `15.1549` edge `0.0157` maxDD `-0.3698`
- `news_risk_high->commodity_1h` score `-0.0166` n `31` status `ready` deltaP `1.6805` edge `0.0136` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.1862` n `77` status `ready` deltaP `2.5429` edge `0.011` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.2587` n `77` status `ready` deltaP `1.3979` edge `0.0031` maxDD `-0.9806`
- `market_context_high->metal_4h` score `-0.9334` n `77` status `ready` deltaP `7.5823` edge `0.0121` maxDD `-6.9009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
