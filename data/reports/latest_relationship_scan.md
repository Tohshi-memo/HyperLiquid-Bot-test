# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T21:37:30.560204+00:00`
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

- `market_context_high->unknown_4h` score `40.0586` n `91` status `ready` deltaP `-2.8343` edge `3.411` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.3708` n `49` status `ready` deltaP `43.75` edge `0.9059` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.8958` n `49` status `ready` deltaP `45.1562` edge `0.8637` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `9.7348` n `49` status `ready` deltaP `25.9788` edge `0.648` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `8.8912` n `90` status `ready` deltaP `21.9122` edge `1.2912` maxDD `-16.7906`
- `market_context_high->equity_24h` score `7.0664` n `90` status `ready` deltaP `25.2532` edge `0.4634` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.4276` n `49` status `ready` deltaP `46.1005` edge `0.2283` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.9397` n `49` status `ready` deltaP `32.3855` edge `0.2996` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5903` n `49` status `ready` deltaP `45.8251` edge `0.0815` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.0941` n `49` status `ready` deltaP `12.3121` edge `0.2113` maxDD `-1.5096`
- `market_context_high->crypto_alt_24h` score `2.8771` n `90` status `ready` deltaP `13.6145` edge `0.8719` maxDD `-34.5048`
- `news_risk_high->crypto_alt_1h` score `2.6082` n `49` status `ready` deltaP `6.3394` edge `0.2068` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4529` n `49` status `ready` deltaP `30.2854` edge `0.0165` maxDD `-0.1194`
- `news_risk_high->commodity_24h` score `2.3929` n `49` status `ready` deltaP `30.2338` edge `0.0063` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.8329` n `91` status `ready` deltaP `18.4686` edge `0.2449` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.3992` n `90` status `ready` deltaP `23.4719` edge `0.1714` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.2583` n `49` status `ready` deltaP `19.5153` edge `0.0728` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.6185` n `91` status `ready` deltaP `17.0581` edge `0.0125` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4763` n `91` status `ready` deltaP `9.242` edge `0.0023` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2997` n `91` status `ready` deltaP `10.7423` edge `0.0557` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
