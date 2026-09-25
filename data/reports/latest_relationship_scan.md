# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T01:52:25.664821+00:00`
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

- `market_context_high->unknown_1h` score `83.8016` n `47` status `ready` deltaP `9.0681` edge `6.9301` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.7401` n `47` status `ready` deltaP `30.4226` edge `3.8148` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.3048` n `47` status `ready` deltaP `24.782` edge `2.4815` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.9654` n `47` status `ready` deltaP `34.7628` edge `1.9676` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `9.4162` n `115` status `ready` deltaP `1.1495` edge `0.7989` maxDD `-0.7504`
- `market_context_high->index_24h` score `8.2441` n `47` status `ready` deltaP `38.7559` edge `0.4416` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.5092` n `47` status `ready` deltaP `38.0098` edge `0.1462` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.3458` n `63` status `ready` deltaP `31.1756` edge `0.1058` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.9559` n `47` status `ready` deltaP `33.8739` edge `0.0359` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.4755` n `47` status `ready` deltaP `17.1445` edge `0.1338` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `2.4553` n `115` status `ready` deltaP `13.4913` edge `0.1656` maxDD `-1.7416`
- `news_risk_high->crypto_major_1h` score `1.7171` n `115` status `ready` deltaP `14.1474` edge `0.1047` maxDD `-2.4737`
- `news_risk_high->metal_1h` score `1.3356` n `115` status `ready` deltaP `17.6412` edge `0.0222` maxDD `-0.6142`
- `market_context_high->index_1h` score `0.9176` n `47` status `ready` deltaP `14.161` edge `0.0099` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8551` n `47` status `ready` deltaP `10.8676` edge `0.0391` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `0.4917` n `47` status `ready` deltaP `7.4014` edge `0.0584` maxDD `-3.3417`
- `news_risk_high->fx_4h` score `0.3767` n `103` status `ready` deltaP `11.3086` edge `0.0205` maxDD `-0.4933`
- `market_context_high->fx_1h` score `0.2565` n `47` status `ready` deltaP `7.7143` edge `0.0056` maxDD `-0.1854`
- `news_risk_high->equity_1h` score `0.1924` n `115` status `ready` deltaP `4.9102` edge `0.0413` maxDD `-2.6402`
- `market_context_high->metal_1h` score `-0.0528` n `47` status `ready` deltaP `2.2296` edge `0.01` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
