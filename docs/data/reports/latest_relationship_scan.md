# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T08:37:33.653892+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11206`

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

- `market_context_high->unknown_1h` score `84.8961` n `47` status `ready` deltaP `8.4693` edge `7.0253` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.1109` n `47` status `ready` deltaP `30.9434` edge `4.0089` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.3164` n `47` status `ready` deltaP `24.782` edge `2.5658` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.8435` n `47` status `ready` deltaP `34.5892` edge `1.9586` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `10.0789` n `112` status `ready` deltaP `3.796` edge `0.8285` maxDD `-0.4452`
- `market_context_high->index_24h` score `8.021` n `47` status `ready` deltaP `36.6726` edge `0.4369` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.7219` n `47` status `ready` deltaP `39.9195` edge `0.1512` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.6114` n `48` status `ready` deltaP `29.8611` edge `0.1367` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.7965` n `47` status `ready` deltaP `32.1971` edge `0.0338` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.3383` n `47` status `ready` deltaP `15.925` edge `0.1305` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.1258` n `47` status `ready` deltaP `9.688` edge `0.096` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9558` n `47` status `ready` deltaP `11.6161` edge `0.0425` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.9331` n `47` status `ready` deltaP `14.3107` edge `0.0102` maxDD `-0.2275`
- `news_risk_high->crypto_alt_1h` score `0.7978` n `112` status `ready` deltaP `8.287` edge `0.1023` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4458` n `47` status `ready` deltaP `9.8101` edge `0.0074` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.0539` n `47` status `ready` deltaP `3.8763` edge `0.0127` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.0079` n `112` status `ready` deltaP `8.5115` edge `0.0072` maxDD `-0.7016`
- `news_risk_high->index_1h` score `-0.0276` n `112` status `ready` deltaP `3.7104` edge `0.0064` maxDD `-0.4409`
- `market_context_high->crypto_major_1h` score `-0.0343` n `47` status `ready` deltaP `3.2552` edge `0.0572` maxDD `-4.5405`
- `news_risk_high->equity_1h` score `-0.1067` n `112` status `ready` deltaP `1.9087` edge `0.0276` maxDD `-2.3199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
