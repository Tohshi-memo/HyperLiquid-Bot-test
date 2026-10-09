# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T02:52:26.430313+00:00`
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

- `market_context_high->unknown_4h` score `39.862` n `91` status `ready` deltaP `-3.5965` edge `3.3997` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.3692` n `44` status `ready` deltaP `43.4451` edge `0.9078` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.5999` n `44` status `ready` deltaP `44.0825` edge `0.8462` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `11.0555` n `44` status `ready` deltaP `28.5827` edge `0.7407` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.6261` n `90` status `ready` deltaP `21.8402` edge `1.3859` maxDD `-16.7906`
- `market_context_high->equity_24h` score `8.7673` n `90` status `ready` deltaP `28.7847` edge `0.5816` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.8786` n `44` status `ready` deltaP `49.6528` edge `0.2422` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.1477` n `44` status `ready` deltaP `33.4257` edge `0.31` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5627` n `44` status `ready` deltaP `45.1358` edge `0.0838` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.5091` n `44` status `ready` deltaP `14.4393` edge `0.2317` maxDD `-1.5096`
- `market_context_high->crypto_alt_24h` score `3.3779` n `90` status `ready` deltaP `13.5417` edge `0.9366` maxDD `-34.5048`
- `news_risk_high->crypto_alt_1h` score `2.6657` n `44` status `ready` deltaP `5.7975` edge `0.2152` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4728` n `44` status `ready` deltaP `29.8721` edge `0.0161` maxDD `-0.0678`
- `news_risk_high->commodity_24h` score `2.2064` n `44` status `ready` deltaP `28.7878` edge `0.0004` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.7372` n `91` status `ready` deltaP `17.8588` edge `0.2367` maxDD `-6.9761`
- `news_risk_high->metal_4h` score `1.2582` n `44` status `ready` deltaP `19.8725` edge `0.0704` maxDD `-0.993`
- `market_context_high->metal_24h` score `1.161` n `90` status `ready` deltaP `20.4514` edge `0.161` maxDD `-3.5466`
- `news_risk_high->metal_1h` score `0.4818` n `44` status `ready` deltaP `10.7648` edge `0.0205` maxDD `-0.44`
- `market_context_high->fx_4h` score `0.4212` n `91` status `ready` deltaP `14.7715` edge `0.0113` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4164` n `91` status `ready` deltaP `8.4935` edge `0.0023` maxDD `-0.271`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
