# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T02:52:35.297932+00:00`
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

- `market_context_high->unknown_1h` score `85.6136` n `47` status `ready` deltaP `9.3675` edge `7.0791` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `48.1517` n `47` status `ready` deltaP `30.4226` edge `3.8491` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.5232` n `47` status `ready` deltaP `24.782` edge `2.4997` maxDD `-2.7051`
- `market_context_high->equity_24h` score `26.053` n `47` status `ready` deltaP `34.7628` edge `1.9749` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.2815` n `47` status `ready` deltaP `39.1031` edge `0.4424` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.5537` n `47` status `ready` deltaP `38.357` edge `0.1476` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.3327` n `60` status `ready` deltaP `30.9375` edge `0.1063` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.9619` n `47` status `ready` deltaP `33.8739` edge `0.0364` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.5223` n `47` status `ready` deltaP `17.1445` edge `0.1377` maxDD `-1.3444`
- `news_risk_high->unknown_1h` score `2.3362` n `116` status `ready` deltaP `-0.1703` edge `0.2177` maxDD `-0.7504`
- `news_risk_high->crypto_alt_1h` score `1.8305` n `116` status `ready` deltaP `10.8817` edge `0.1337` maxDD `-1.9626`
- `news_risk_high->crypto_major_1h` score `1.4363` n `116` status `ready` deltaP `12.9775` edge `0.0891` maxDD `-2.4737`
- `news_risk_high->metal_1h` score `1.1544` n `116` status `ready` deltaP `15.6618` edge `0.0203` maxDD `-0.6142`
- `market_context_high->index_1h` score `0.9331` n `47` status `ready` deltaP `14.3107` edge `0.0102` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9043` n `47` status `ready` deltaP `11.167` edge `0.0412` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `0.612` n `47` status `ready` deltaP `7.7063` edge `0.0664` maxDD `-3.3417`
- `market_context_high->fx_1h` score `0.3152` n `47` status `ready` deltaP `8.3131` edge `0.0065` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.0252` n `104` status `ready` deltaP `8.5483` edge `0.0153` maxDD `-0.8578`
- `news_risk_high->equity_1h` score `0.0184` n `116` status `ready` deltaP `3.8303` edge `0.034` maxDD `-2.6402`
- `market_context_high->metal_1h` score `-0.0349` n `47` status `ready` deltaP `2.529` edge `0.0103` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
