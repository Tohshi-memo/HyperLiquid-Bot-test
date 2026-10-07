# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T21:52:33.096067+00:00`
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

- `market_context_high->unknown_4h` score `38.2978` n `90` status `ready` deltaP `-5.3895` edge `3.2813` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.9295` n `62` status `ready` deltaP `38.5818` edge `0.6739` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.0311` n `62` status `ready` deltaP `22.325` edge `0.5715` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `4.9439` n `62` status `ready` deltaP `11.8875` edge `0.3427` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.3544` n `62` status `ready` deltaP `31.3149` edge `0.1541` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `3.543` n `90` status `ready` deltaP `9.5271` edge `0.6881` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.8366` n `62` status `ready` deltaP `31.3926` edge `0.0533` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4575` n `62` status `ready` deltaP `10.1748` edge `0.1725` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.4247` n `90` status `ready` deltaP `16.6463` edge `0.1875` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.053` n `62` status `ready` deltaP `17.4715` edge `0.1144` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9373` n `62` status `ready` deltaP `24.4254` edge `0.0136` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.5038` n `62` status `ready` deltaP `21.4004` edge `0.0917` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.1274` n `62` status `ready` deltaP `3.1582` edge `0.1248` maxDD `-2.4854`
- `news_risk_high->unknown_4h` score `1.0774` n `62` status `ready` deltaP `-8.3645` edge `0.2701` maxDD `-5.6309`
- `market_context_high->metal_24h` score `1.0044` n `90` status `ready` deltaP `19.7347` edge `0.1457` maxDD `-3.5466`
- `market_context_high->fx_4h` score `0.9212` n `90` status `ready` deltaP `20.3015` edge `0.0161` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.6663` n `90` status `ready` deltaP `11.497` edge `0.0031` maxDD `-0.271`
- `market_context_high->equity_24h` score `0.4394` n `90` status `ready` deltaP `9.4502` edge `0.0165` maxDD `-1.0977`
- `market_context_high->crypto_major_1h` score `0.1323` n `90` status `ready` deltaP `10.1031` edge `0.0385` maxDD `-3.7778`
- `news_risk_high->metal_1h` score `0.1006` n `62` status `ready` deltaP `6.3019` edge `0.0082` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
