# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T21:07:26.029917+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8896`

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

- `market_context_high->unknown_4h` score `40.1178` n `91` status `ready` deltaP `-2.5295` edge `3.4139` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.5128` n `49` status `ready` deltaP `44.0549` edge `0.9157` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `14.0126` n `49` status `ready` deltaP `45.4611` edge `0.8714` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `9.5679` n `49` status `ready` deltaP `25.6322` edge `0.6364` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `8.8358` n `90` status `ready` deltaP `21.9122` edge `1.2841` maxDD `-16.7906`
- `market_context_high->equity_24h` score `6.8995` n `90` status `ready` deltaP `24.9066` edge `0.4518` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.3735` n `49` status `ready` deltaP `45.7539` edge `0.2261` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.9661` n `49` status `ready` deltaP `32.3855` edge `0.3018` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5939` n `49` status `ready` deltaP `45.8251` edge `0.0818` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.1157` n `49` status `ready` deltaP `12.4618` edge `0.2121` maxDD `-1.5096`
- `market_context_high->crypto_alt_24h` score `2.8607` n `90` status `ready` deltaP `13.6145` edge `0.8698` maxDD `-34.5048`
- `news_risk_high->crypto_alt_1h` score `2.6082` n `49` status `ready` deltaP `6.3394` edge `0.2068` maxDD `-1.2034`
- `news_risk_high->commodity_24h` score `2.4578` n `49` status `ready` deltaP `30.5804` edge `0.0094` maxDD `-0.0096`
- `news_risk_high->index_1h` score `2.4278` n `49` status `ready` deltaP `29.986` edge `0.0164` maxDD `-0.1194`
- `market_context_high->crypto_major_4h` score `1.9088` n `91` status `ready` deltaP `18.7735` edge `0.2526` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.4054` n `90` status `ready` deltaP `23.4719` edge `0.1722` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.2488` n `49` status `ready` deltaP `19.3629` edge `0.0726` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.6197` n `91` status `ready` deltaP `17.0581` edge `0.0126` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4524` n `91` status `ready` deltaP `8.9426` edge `0.0023` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.3137` n `91` status `ready` deltaP `10.892` edge `0.0565` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
