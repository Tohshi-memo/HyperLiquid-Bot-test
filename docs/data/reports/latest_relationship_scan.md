# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T19:07:25.674336+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8742`

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

- `market_context_high->unknown_4h` score `38.4971` n `90` status `ready` deltaP `-5.4185` edge `3.2981` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.8161` n `62` status `ready` deltaP `37.7498` edge `0.67` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.2139` n `62` status `ready` deltaP `23.0201` edge `0.5821` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `4.2865` n `62` status `ready` deltaP `9.9844` edge `0.3006` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.1416` n `62` status `ready` deltaP `29.5848` edge `0.1479` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `2.964` n `90` status `ready` deltaP `8.143` edge `0.6231` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.9274` n `62` status `ready` deltaP `32.3931` edge `0.0542` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.5043` n `62` status `ready` deltaP `10.3245` edge `0.1754` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.3113` n `90` status `ready` deltaP `15.8143` edge `0.1836` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.1493` n `62` status `ready` deltaP `18.3312` edge `0.1167` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9888` n `62` status `ready` deltaP `25.0242` edge `0.0139` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.427` n `62` status `ready` deltaP `20.2533` edge `0.0895` maxDD `-0.993`
- `news_risk_high->unknown_4h` score `1.2767` n `62` status `ready` deltaP `-8.3935` edge `0.2869` maxDD `-5.6309`
- `news_risk_high->crypto_alt_1h` score `1.2725` n `62` status `ready` deltaP `3.9067` edge `0.1319` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.8885` n `90` status `ready` deltaP `19.9087` edge `0.016` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.8646` n `90` status `ready` deltaP `19.0426` edge `0.1324` maxDD `-3.5466`
- `market_context_high->fx_1h` score `0.7286` n `90` status `ready` deltaP `12.2455` edge `0.0033` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1627` n `90` status `ready` deltaP `10.2528` edge `0.0414` maxDD `-3.7778`
- `news_risk_high->metal_1h` score `0.1077` n `62` status `ready` deltaP `6.4516` edge `0.0078` maxDD `-1.0132`
- `market_context_high->commodity_1h` score `-0.0443` n `90` status `ready` deltaP `4.0818` edge `0.0067` maxDD `-0.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
