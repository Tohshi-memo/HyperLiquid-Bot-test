# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T23:22:26.674867+00:00`
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

- `market_context_high->unknown_4h` score `38.3884` n `90` status `ready` deltaP `-4.9322` edge `3.2858` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.9791` n `62` status `ready` deltaP `38.8867` edge `0.676` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.0227` n `62` status `ready` deltaP `22.325` edge `0.5708` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `5.3222` n `62` status `ready` deltaP `12.9256` edge `0.3673` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.4902` n `62` status `ready` deltaP `32.3529` edge `0.1585` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `3.8648` n `90` status `ready` deltaP `10.0461` edge `0.7259` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.8268` n `62` status `ready` deltaP `31.2402` edge `0.0535` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.4742` n `90` status `ready` deltaP `16.9512` edge `0.1896` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `2.4671` n `62` status `ready` deltaP `10.1748` edge `0.1733` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.0274` n `62` status `ready` deltaP `17.1666` edge `0.1143` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.8846` n `62` status `ready` deltaP `23.8266` edge `0.0132` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.4919` n `62` status `ready` deltaP `21.248` edge `0.0912` maxDD `-0.993`
- `news_risk_high->unknown_4h` score `1.168` n `62` status `ready` deltaP `-7.9072` edge `0.2746` maxDD `-5.6309`
- `market_context_high->metal_24h` score `1.0777` n `90` status `ready` deltaP `20.0807` edge `0.1528` maxDD `-3.5466`
- `news_risk_high->crypto_alt_1h` score `1.0423` n `62` status `ready` deltaP `2.7091` edge `0.1207` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.9272` n `90` status `ready` deltaP `20.3015` edge `0.0166` maxDD `-0.3077`
- `market_context_high->equity_24h` score `0.8176` n `90` status `ready` deltaP `10.4883` edge `0.0411` maxDD `-1.0977`
- `market_context_high->fx_1h` score `0.6915` n `90` status `ready` deltaP `11.7964` edge `0.0032` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1386` n `90` status `ready` deltaP `10.1031` edge `0.0393` maxDD `-3.7778`
- `news_risk_high->metal_1h` score `0.1269` n `62` status `ready` deltaP `6.6013` edge `0.0084` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
