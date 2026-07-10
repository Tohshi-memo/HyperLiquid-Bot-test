# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T22:13:35.966925+00:00`
- Price records: `672`
- Market context records: `6327`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.4806` n `32` status `ready` deltaP `43.2292` edge `1.0166` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.0608` n `32` status `ready` deltaP `50.6944` edge `0.1671` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.4269` n `32` status `ready` deltaP `16.6667` edge `0.5344` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.2045` n `32` status `ready` deltaP `43.8262` edge `0.0628` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.3827` n `32` status `ready` deltaP `30.0347` edge `0.1022` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.4374` n `32` status `ready` deltaP `29.3413` edge `0.0214` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5115` n `32` status `ready` deltaP `14.8765` edge `0.1413` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9353` n `32` status `ready` deltaP `11.7702` edge `0.0876` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.1469` n `196` status `ready` deltaP `10.4343` edge `0.039` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.0299` n `208` status `ready` deltaP `-7.5887` edge `0.1539` maxDD `-3.7317`
- `market_context_high->metal_24h` score `-0.3039` n `149` status `ready` deltaP `18.7931` edge `0.0926` maxDD `-11.8809`
- `market_context_high->index_4h` score `-0.3241` n `196` status `ready` deltaP `4.9807` edge `0.0203` maxDD `-0.9379`
- `market_context_high->metal_1h` score `-0.3504` n `208` status `ready` deltaP `4.5803` edge `0.0023` maxDD `-1.8877`
- `market_context_high->index_1h` score `-0.5861` n `208` status `ready` deltaP `-3.1207` edge `0.0023` maxDD `-0.8646`
- `news_risk_high->index_24h` score `-0.587` n `32` status `ready` deltaP `2.4306` edge `-0.0043` maxDD `-2.3058`
- `market_context_high->commodity_1h` score `-0.6273` n `208` status `ready` deltaP `-1.7417` edge `-0.0005` maxDD `-2.1314`
- `market_context_high->equity_4h` score `-0.737` n `196` status `ready` deltaP `4.6043` edge `0.0447` maxDD `-8.2573`
- `news_risk_high->metal_1h` score `-0.7714` n `32` status `ready` deltaP `-3.5928` edge `-0.0252` maxDD `-1.6464`
- `news_risk_high->unknown_1h` score `-0.7743` n `32` status `ready` deltaP `5.6325` edge `-0.0676` maxDD `-0.7581`
- `market_context_high->fx_1h` score `-0.8109` n `208` status `ready` deltaP `-1.9087` edge `-0.0021` maxDD `-0.8865`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
