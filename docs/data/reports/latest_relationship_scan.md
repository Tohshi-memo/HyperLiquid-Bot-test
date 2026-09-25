# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T01:37:29.483801+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11041`

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

- `market_context_high->unknown_1h` score `83.762` n `47` status `ready` deltaP `9.0681` edge `6.9268` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.6429` n `47` status `ready` deltaP `30.4226` edge `3.8067` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.2688` n `47` status `ready` deltaP `24.782` edge `2.4785` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.9402` n `47` status `ready` deltaP `34.7628` edge `1.9655` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `10.6461` n `114` status `ready` deltaP `1.0427` edge `0.9021` maxDD `-0.7504`
- `market_context_high->index_24h` score `8.2417` n `47` status `ready` deltaP `38.7559` edge `0.4414` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.4905` n `47` status `ready` deltaP `37.8362` edge `0.1458` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.3518` n `63` status `ready` deltaP `31.1756` edge `0.1063` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.9547` n `47` status `ready` deltaP `33.8739` edge `0.0358` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.5131` n `114` status `ready` deltaP `13.9747` edge `0.1672` maxDD `-1.7416`
- `market_context_high->equity_4h` score `2.4647` n `47` status `ready` deltaP `17.1445` edge `0.1329` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `1.706` n `114` status `ready` deltaP `13.888` edge `0.1055` maxDD `-2.4737`
- `news_risk_high->metal_1h` score `1.3057` n `114` status `ready` deltaP `17.3285` edge `0.0218` maxDD `-0.6142`
- `market_context_high->index_1h` score `0.9176` n `47` status `ready` deltaP `14.161` edge `0.0099` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8551` n `47` status `ready` deltaP `10.8676` edge `0.0391` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `0.4483` n `47` status `ready` deltaP `7.2489` edge `0.0558` maxDD `-3.3417`
- `news_risk_high->fx_4h` score `0.4182` n `102` status `ready` deltaP `11.6511` edge `0.021` maxDD `-0.4395`
- `market_context_high->fx_1h` score `0.2565` n `47` status `ready` deltaP `7.7143` edge `0.0056` maxDD `-0.1854`
- `news_risk_high->equity_1h` score `0.1415` n `114` status `ready` deltaP `4.5593` edge `0.0394` maxDD `-2.6402`
- `market_context_high->metal_1h` score `-0.0528` n `47` status `ready` deltaP `2.2296` edge `0.01` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
