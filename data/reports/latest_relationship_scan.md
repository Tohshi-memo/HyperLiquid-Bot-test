# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T07:07:30.889856+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11298`

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

- `market_context_high->unknown_1h` score `84.9201` n `47` status `ready` deltaP `8.4693` edge `7.0273` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `49.6452` n `47` status `ready` deltaP `30.5962` edge `3.9724` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.2276` n `47` status `ready` deltaP `24.782` edge `2.5584` maxDD `-2.7051`
- `market_context_high->equity_24h` score `26.005` n `47` status `ready` deltaP `34.7628` edge `1.9709` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.138` n `47` status `ready` deltaP `37.7142` edge `0.4397` maxDD `-0.3705`
- `news_risk_high->unknown_1h` score `5.7331` n `116` status `ready` deltaP `4.1039` edge `0.4643` maxDD `-0.4452`
- `market_context_high->metal_24h` score `4.7641` n `47` status `ready` deltaP `40.2667` edge `0.1524` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.7395` n `54` status `ready` deltaP `30.3819` edge `0.1439` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.8913` n `47` status `ready` deltaP `33.1117` edge `0.0356` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.5111` n `47` status `ready` deltaP `16.8396` edge `0.1388` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.216` n `47` status `ready` deltaP `9.8404` edge `0.1025` maxDD `-3.3417`
- `news_risk_high->crypto_alt_1h` score `1.0396` n `116` status `ready` deltaP `10.1693` edge `0.1099` maxDD `-4.2849`
- `market_context_high->equity_1h` score `0.9618` n `47` status `ready` deltaP `11.6161` edge `0.043` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.9595` n `47` status `ready` deltaP `14.6101` edge `0.0104` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.417` n `47` status `ready` deltaP `9.5107` edge `0.007` maxDD `-0.1854`
- `news_risk_high->crypto_major_1h` score `0.1076` n `116` status `ready` deltaP `5.1415` edge `0.0499` maxDD `-3.3501`
- `market_context_high->metal_1h` score `0.0632` n `47` status `ready` deltaP `4.026` edge `0.0129` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.0147` n `116` status `ready` deltaP `8.5381` edge `0.0079` maxDD `-0.7016`
- `market_context_high->crypto_major_1h` score `-0.045` n `47` status `ready` deltaP `3.1055` edge `0.0573` maxDD `-4.5405`
- `news_risk_high->equity_1h` score `-0.1678` n `116` status `ready` deltaP `1.6932` edge `0.0252` maxDD `-2.6402`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
