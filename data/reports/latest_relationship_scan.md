# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T09:52:28.511239+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

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

- `market_context_high->unknown_4h` score `40.2235` n `90` status `ready` deltaP `-2.7981` edge `3.4245` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `11.1039` n `61` status `ready` deltaP `38.6021` edge `0.6883` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `7.6673` n `61` status `ready` deltaP `19.6948` edge `0.5176` maxDD `-0.1298`
- `news_risk_high->crypto_alt_4h` score `7.4409` n `61` status `ready` deltaP `23.6206` edge `0.5823` maxDD `-5.5756`
- `market_context_high->crypto_major_24h` score `5.5453` n `90` status `ready` deltaP `14.6286` edge `0.9108` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.2735` n `61` status `ready` deltaP `38.1693` edge `0.185` maxDD `0.0`
- `news_risk_high->index_4h` score `3.2816` n `61` status `ready` deltaP `35.5907` edge `0.0624` maxDD `-0.4296`
- `market_context_high->equity_24h` score `3.1688` n `90` status `ready` deltaP `17.3633` edge `0.1912` maxDD `-1.0977`
- `news_risk_high->equity_4h` score `2.8316` n `61` status `ready` deltaP `20.6493` edge `0.1581` maxDD `-2.7837`
- `news_risk_high->crypto_major_1h` score `2.6777` n `61` status `ready` deltaP `11.3822` edge `0.1828` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.5041` n `90` status `ready` deltaP `16.7988` edge `0.1931` maxDD `-4.047`
- `news_risk_high->index_1h` score `2.203` n `61` status `ready` deltaP `27.0418` edge `0.0173` maxDD `-0.1194`
- `news_risk_high->unknown_4h` score `1.9952` n `61` status `ready` deltaP `-6.2226` edge `0.3323` maxDD `-5.6309`
- `news_risk_high->metal_4h` score `1.5106` n `61` status `ready` deltaP `22.2062` edge `0.0872` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.348` n `61` status `ready` deltaP `4.383` edge `0.1333` maxDD `-2.3482`
- `market_context_high->metal_24h` score `1.2748` n `90` status `ready` deltaP `21.7098` edge `0.1672` maxDD `-3.5466`
- `market_context_high->fx_4h` score `0.8868` n `90` status `ready` deltaP `19.6917` edge `0.0173` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.6124` n `90` status `ready` deltaP `10.7485` edge `0.0036` maxDD `-0.271`
- `market_context_high->crypto_alt_24h` score `0.4659` n `90` status `ready` deltaP `9.0962` edge `0.5929` maxDD `-34.5048`
- `news_risk_high->metal_1h` score `0.2429` n `61` status `ready` deltaP `7.8261` edge `0.0099` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
