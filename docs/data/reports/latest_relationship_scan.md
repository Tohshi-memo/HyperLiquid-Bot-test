# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T16:07:30.039364+00:00`
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

- `market_context_high->unknown_4h` score `37.2825` n `90` status `ready` deltaP `-5.5707` edge `3.1979` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.7372` n `62` status `ready` deltaP `36.9888` edge `0.6685` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.5503` n `62` status `ready` deltaP `24.39` edge `0.601` maxDD `-6.4195`
- `news_risk_high->index_24h` score `4.0946` n `62` status `ready` deltaP `29.4627` edge `0.1448` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.8757` n `62` status `ready` deltaP `9.3196` edge `0.2708` maxDD `-0.1298`
- `news_risk_high->index_4h` score `3.1022` n `62` status `ready` deltaP `34.0674` edge `0.0576` maxDD `-0.4296`
- `market_context_high->crypto_major_24h` score `2.4051` n `90` status `ready` deltaP `7.3541` edge `0.5567` maxDD `-16.7906`
- `news_risk_high->crypto_major_1h` score `2.4024` n `62` status `ready` deltaP `9.8754` edge `0.1699` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.3647` n `62` status `ready` deltaP `19.8532` edge `0.1245` maxDD `-2.7837`
- `market_context_high->crypto_major_4h` score `2.2324` n `90` status `ready` deltaP `15.0533` edge `0.1821` maxDD `-4.047`
- `news_risk_high->index_1h` score `2.069` n `62` status `ready` deltaP `25.9224` edge `0.0146` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.4623` n `62` status `ready` deltaP `20.5577` edge `0.092` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.2761` n `62` status `ready` deltaP `3.9067` edge `0.1322` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.8642` n `90` status `ready` deltaP `19.6042` edge `0.016` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.7811` n `90` status `ready` deltaP `18.9659` edge `0.1222` maxDD `-3.5466`
- `market_context_high->fx_1h` score `0.7513` n `90` status `ready` deltaP `12.5449` edge `0.0032` maxDD `-0.271`
- `news_risk_high->metal_1h` score `0.1377` n `62` status `ready` deltaP `6.751` edge `0.0083` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `0.0965` n `90` status `ready` deltaP `9.8037` edge `0.0359` maxDD `-3.7778`
- `news_risk_high->unknown_4h` score `0.0621` n `62` status `ready` deltaP `-8.5457` edge `0.1867` maxDD `-5.6309`
- `market_context_high->crypto_alt_4h` score `0.0407` n `90` status `ready` deltaP `-4.6423` edge `0.2067` maxDD `-7.1222`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
