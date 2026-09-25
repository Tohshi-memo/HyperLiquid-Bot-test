# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T03:37:26.047454+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11053`

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

- `market_context_high->unknown_1h` score `86.714` n `47` status `ready` deltaP `9.2178` edge `7.1718` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `48.4517` n `47` status `ready` deltaP `30.4226` edge `3.8741` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.708` n `47` status `ready` deltaP `24.782` edge `2.5151` maxDD `-2.7051`
- `market_context_high->equity_24h` score `26.0878` n `47` status `ready` deltaP `34.7628` edge `1.9778` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.2827` n `47` status `ready` deltaP `39.1031` edge `0.4425` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.611` n `47` status `ready` deltaP `38.8778` edge `0.1489` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.3321` n `57` status `ready` deltaP `30.6743` edge `0.108` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.9631` n `47` status `ready` deltaP `33.8739` edge `0.0365` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.5439` n `47` status `ready` deltaP `17.1445` edge `0.1395` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `0.9958` n `116` status `ready` deltaP `9.457` edge `0.111` maxDD `-4.2849`
- `news_risk_high->crypto_major_1h` score `0.9374` n `116` status `ready` deltaP `10.8404` edge `0.0704` maxDD `-3.164`
- `market_context_high->index_1h` score `0.9343` n `47` status `ready` deltaP `14.3107` edge `0.0103` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9259` n `47` status `ready` deltaP `11.3167` edge `0.042` maxDD `-1.5564`
- `news_risk_high->metal_1h` score `0.901` n `116` status `ready` deltaP `13.5247` edge `0.0176` maxDD `-0.6142`
- `market_context_high->crypto_alt_4h` score `0.7362` n `47` status `ready` deltaP `8.1636` edge `0.0737` maxDD `-3.3417`
- `market_context_high->fx_1h` score `0.3548` n `47` status `ready` deltaP `8.7622` edge `0.0068` maxDD `-0.1854`
- `market_context_high->metal_1h` score `-0.0077` n `47` status `ready` deltaP `2.9781` edge `0.0108` maxDD `-0.1976`
- `news_risk_high->equity_1h` score `-0.083` n `116` status `ready` deltaP `3.1179` edge `0.0303` maxDD `-2.6402`
- `news_risk_high->fx_4h` score `-0.1516` n `104` status `ready` deltaP `7.7392` edge `0.0119` maxDD `-1.301`
- `market_context_high->crypto_major_1h` score `-0.1924` n `47` status `ready` deltaP `1.9079` edge `0.053` maxDD `-4.5405`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
