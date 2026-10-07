# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T14:37:35.533776+00:00`
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

- `market_context_high->unknown_4h` score `36.6028` n `90` status `ready` deltaP `-5.8468` edge `3.1431` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.7173` n `62` status `ready` deltaP `36.905` edge `0.6674` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.563` n `62` status `ready` deltaP `24.4591` edge `0.6016` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.9813` n `62` status `ready` deltaP `28.6458` edge `0.1408` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.648` n `62` status `ready` deltaP `9.1734` edge `0.2528` maxDD `-0.1298`
- `news_risk_high->index_4h` score `3.1345` n `62` status `ready` deltaP `34.4414` edge `0.0578` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.5163` n `62` status `ready` deltaP `10.1748` edge `0.1774` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.4237` n `62` status `ready` deltaP `20.2154` edge `0.127` maxDD `-2.7837`
- `market_context_high->crypto_major_4h` score `2.2125` n `90` status `ready` deltaP `14.9695` edge `0.181` maxDD `-4.047`
- `market_context_high->crypto_major_24h` score `2.1294` n `90` status `ready` deltaP `7.2569` edge `0.522` maxDD `-16.7906`
- `news_risk_high->index_1h` score `2.0846` n `62` status `ready` deltaP `26.0721` edge `0.0149` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.4632` n `62` status `ready` deltaP `20.4858` edge `0.0926` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.3721` n `62` status `ready` deltaP `4.2061` edge `0.1382` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.8078` n `90` status `ready` deltaP `18.9295` edge `0.0158` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.7501` n `90` status `ready` deltaP `12.5449` edge `0.0031` maxDD `-0.271`
- `market_context_high->metal_24h` score `0.742` n `90` status `ready` deltaP `18.8889` edge `0.1177` maxDD `-3.5466`
- `news_risk_high->metal_1h` score `0.2132` n `62` status `ready` deltaP `7.4995` edge `0.0096` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `0.1705` n `90` status `ready` deltaP `10.1031` edge `0.0434` maxDD `-3.7778`
- `market_context_high->crypto_alt_4h` score `0.0534` n `90` status `ready` deltaP `-4.5732` edge `0.2073` maxDD `-7.1222`
- `market_context_high->commodity_1h` score `-0.0443` n `90` status `ready` deltaP `4.2315` edge `0.0057` maxDD `-0.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
