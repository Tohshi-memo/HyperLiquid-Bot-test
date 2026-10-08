# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T14:07:32.160165+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8459`

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

- `market_context_high->unknown_4h` score `40.6617` n `90` status `ready` deltaP `-2.6456` edge `3.46` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `13.2546` n `49` status `ready` deltaP `42.6829` edge `0.82` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.0242` n `49` status `ready` deltaP `43.9367` edge `0.7992` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `6.9157` n `49` status `ready` deltaP `21.025` edge `0.4461` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `6.641` n `90` status `ready` deltaP `17.5647` edge `1.0317` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.5852` n `49` status `ready` deltaP `41.1054` edge `0.1914` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.058` n `49` status `ready` deltaP `29.794` edge `0.2434` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.3537` n `49` status `ready` deltaP `43.8433` edge `0.075` maxDD `-0.025`
- `market_context_high->equity_24h` score `4.2473` n `90` status `ready` deltaP `20.2994` edge `0.2615` maxDD `-1.0977`
- `news_risk_high->commodity_24h` score `3.5023` n `49` status `ready` deltaP `35.2966` edge `0.065` maxDD `-0.0096`
- `news_risk_high->crypto_major_1h` score `3.0065` n `49` status `ready` deltaP `12.4618` edge `0.203` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.8968` n `90` status `ready` deltaP `18.0183` edge `0.2177` maxDD `-4.047`
- `news_risk_high->crypto_alt_1h` score `2.5205` n `49` status `ready` deltaP `7.0879` edge `0.1945` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4301` n `49` status `ready` deltaP `30.1357` edge `0.0156` maxDD `-0.1194`
- `market_context_high->metal_24h` score `1.4106` n `90` status `ready` deltaP `23.4369` edge `0.1731` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.1919` n `49` status `ready` deltaP `18.4482` edge `0.0714` maxDD `-0.993`
- `market_context_high->crypto_alt_24h` score `0.8388` n `90` status `ready` deltaP `9.787` edge `0.6361` maxDD `-34.5048`
- `market_context_high->fx_4h` score `0.6617` n `90` status `ready` deltaP `17.2527` edge `0.0148` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.5721` n `91` status `ready` deltaP `10.2899` edge `0.0033` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2428` n `91` status `ready` deltaP `10.892` edge `0.0474` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
