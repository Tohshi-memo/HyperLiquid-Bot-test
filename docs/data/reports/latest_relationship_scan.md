# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T21:22:32.458374+00:00`
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

- `market_context_high->unknown_4h` score `38.2246` n `90` status `ready` deltaP `-5.3895` edge `3.2752` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.8883` n `62` status `ready` deltaP `38.277` edge `0.6725` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.0275` n `62` status `ready` deltaP `22.325` edge `0.5712` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `4.8226` n `62` status `ready` deltaP `11.5415` edge `0.3349` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.3111` n `62` status `ready` deltaP `30.9689` edge `0.1528` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `3.4349` n `90` status `ready` deltaP `9.3541` edge `0.6754` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.8476` n `62` status `ready` deltaP `31.5451` edge `0.0532` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4156` n `62` status `ready` deltaP `9.8754` edge `0.171` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.3835` n `90` status `ready` deltaP `16.3415` edge `0.1861` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.0676` n `62` status `ready` deltaP `17.624` edge `0.1146` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9505` n `62` status `ready` deltaP `24.5751` edge `0.0137` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.503` n `62` status `ready` deltaP `21.4004` edge `0.0916` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.0831` n `62` status `ready` deltaP `2.8588` edge `0.1231` maxDD `-2.4854`
- `news_risk_high->unknown_4h` score `1.0042` n `62` status `ready` deltaP `-8.3645` edge `0.264` maxDD `-5.6309`
- `market_context_high->metal_24h` score `0.9864` n `90` status `ready` deltaP `19.7347` edge `0.1434` maxDD `-3.5466`
- `market_context_high->fx_4h` score `0.9212` n `90` status `ready` deltaP `20.3015` edge `0.0161` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.6663` n `90` status `ready` deltaP `11.497` edge `0.0031` maxDD `-0.271`
- `market_context_high->equity_24h` score `0.3181` n `90` status `ready` deltaP `9.1042` edge `0.0087` maxDD `-1.0977`
- `news_risk_high->metal_1h` score `0.1137` n `62` status `ready` deltaP `6.4516` edge `0.0083` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `0.1051` n `90` status `ready` deltaP `9.8037` edge `0.037` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
