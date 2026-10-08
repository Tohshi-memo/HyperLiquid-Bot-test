# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T17:22:29.083477+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8914`

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

- `market_context_high->unknown_4h` score `40.1662` n `91` status `ready` deltaP `-2.2246` edge `3.4159` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.0216` n `49` status `ready` deltaP `43.75` edge `0.8768` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.6582` n `49` status `ready` deltaP `45.1562` edge `0.8439` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `8.0267` n `49` status `ready` deltaP `23.0325` edge `0.5253` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `7.7273` n `90` status `ready` deltaP `19.6591` edge `1.157` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.9135` n `49` status `ready` deltaP `43.1542` edge `0.2051` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.388` n `49` status `ready` deltaP `30.7087` edge `0.2648` maxDD `-0.6421`
- `market_context_high->equity_24h` score `5.3583` n `90` status `ready` deltaP `22.3069` edge `0.3407` maxDD `-1.0977`
- `news_risk_high->index_4h` score `4.3841` n `49` status `ready` deltaP `44.1482` edge `0.0755` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.2165` n `49` status `ready` deltaP `12.7612` edge `0.2185` maxDD `-1.5096`
- `news_risk_high->commodity_24h` score `3.0114` n `49` status `ready` deltaP `33.1801` edge `0.0382` maxDD `-0.0096`
- `news_risk_high->crypto_alt_1h` score `2.739` n `49` status `ready` deltaP `6.7885` edge `0.2147` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.3894` n `49` status `ready` deltaP `29.6866` edge `0.0152` maxDD `-0.1194`
- `market_context_high->crypto_alt_24h` score `1.7576` n `90` status `ready` deltaP `11.3615` edge `0.7434` maxDD `-34.5048`
- `market_context_high->crypto_major_4h` score `1.6785` n `91` status `ready` deltaP `18.4686` edge `0.2251` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.4993` n `90` status `ready` deltaP `24.5118` edge `0.1773` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.1983` n `49` status `ready` deltaP `18.6007` edge `0.0712` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5539` n `91` status `ready` deltaP `16.2959` edge `0.0122` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.5278` n `91` status `ready` deltaP `9.8408` edge `0.0026` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.3792` n `91` status `ready` deltaP `11.1914` edge `0.0629` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
