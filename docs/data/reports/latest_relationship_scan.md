# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T23:07:26.172533+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3911`

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

- `market_context_high->unknown_1h` score `32152.2902` n `45` status `ready` deltaP `1.5668` edge `2679.3565` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21820.8874` n `45` status `ready` deltaP `1.958` edge `1818.4081` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `917.3352` n `31` status `ready` deltaP `1.7819` edge `76.4503` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `567.9399` n `31` status `ready` deltaP `3.1766` edge `47.3128` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `272.3905` n `31` status `ready` deltaP `6.0764` edge `22.6587` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.8583` n `31` status `ready` deltaP `52.0833` edge `3.4743` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.0548` n `31` status `ready` deltaP `53.125` edge `3.1504` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `37.4615` n `31` status `ready` deltaP `52.6042` edge `2.7711` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.5593` n `31` status `ready` deltaP `38.9785` edge `0.7309` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.8843` n `31` status `ready` deltaP `26.3031` edge `0.8187` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.4639` n `31` status `ready` deltaP `37.9869` edge `0.6668` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.4595` n `31` status `ready` deltaP `53.2986` edge `0.2663` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.6994` n `31` status `ready` deltaP `17.3879` edge `0.8847` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.2563` n `31` status `ready` deltaP `44.6629` edge `0.1531` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6799` n `31` status `ready` deltaP `19.9874` edge `0.1921` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3512` n `31` status `ready` deltaP `36.4625` edge `0.0622` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6866` n `31` status `ready` deltaP `31.8428` edge `0.0201` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.475` n `31` status `ready` deltaP `10.31` edge `0.2947` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.3303` n `45` status `ready` deltaP `28.8685` edge `0.0302` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2799` n `31` status `ready` deltaP `13.0046` edge `0.2413` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
