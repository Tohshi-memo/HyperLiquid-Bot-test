# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T21:22:28.714785+00:00`
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

- `market_context_high->unknown_4h` score `40.0912` n `91` status `ready` deltaP `-2.6819` edge `3.4127` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.4418` n `49` status `ready` deltaP `43.9024` edge `0.9108` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.9548` n `49` status `ready` deltaP `45.3086` edge `0.8676` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `9.6514` n `49` status `ready` deltaP `25.8055` edge `0.6422` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `8.8655` n `90` status `ready` deltaP `21.9122` edge `1.2879` maxDD `-16.7906`
- `market_context_high->equity_24h` score `6.9829` n `90` status `ready` deltaP `25.0799` edge `0.4576` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.4006` n `49` status `ready` deltaP `45.9272` edge `0.2272` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.9517` n `49` status `ready` deltaP `32.3855` edge `0.3006` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5915` n `49` status `ready` deltaP `45.8251` edge `0.0816` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.1109` n `49` status `ready` deltaP `12.4618` edge `0.2117` maxDD `-1.5096`
- `market_context_high->crypto_alt_24h` score `2.8716` n `90` status `ready` deltaP `13.6145` edge `0.8712` maxDD `-34.5048`
- `news_risk_high->crypto_alt_1h` score `2.6082` n `49` status `ready` deltaP `6.3394` edge `0.2068` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4409` n `49` status `ready` deltaP `30.1357` edge `0.0165` maxDD `-0.1194`
- `news_risk_high->commodity_24h` score `2.4259` n `49` status `ready` deltaP `30.4071` edge `0.0079` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.8713` n `91` status `ready` deltaP `18.621` edge `0.2488` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.4023` n `90` status `ready` deltaP `23.4719` edge `0.1718` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.2575` n `49` status `ready` deltaP `19.5153` edge `0.0727` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.6185` n `91` status `ready` deltaP `17.0581` edge `0.0125` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4643` n `91` status `ready` deltaP `9.0923` edge `0.0023` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.3106` n `91` status `ready` deltaP `10.892` edge `0.0561` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
