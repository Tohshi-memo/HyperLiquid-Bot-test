# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T18:07:26.826122+00:00`
- Price records: `672`
- Market context records: `7904`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14745`

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

- `market_context_high->equity_24h` score `15.4341` n `96` status `ready` deltaP `29.5139` edge `1.2236` maxDD `-6.0681`
- `market_context_high->metal_24h` score `6.7172` n `96` status `ready` deltaP `33.0896` edge `0.3659` maxDD `-0.1383`
- `market_context_high->equity_4h` score `5.7635` n `102` status `ready` deltaP `20.3814` edge `0.4337` maxDD `-5.1426`
- `market_context_high->index_4h` score `2.0874` n `102` status `ready` deltaP `22.0363` edge `0.0672` maxDD `-0.8791`
- `market_context_high->commodity_24h` score `1.9723` n `96` status `ready` deltaP `21.1806` edge `0.1815` maxDD `-7.0012`
- `market_context_high->metal_4h` score `1.9395` n `102` status `ready` deltaP `16.8849` edge `0.1113` maxDD `-0.979`
- `market_context_high->crypto_alt_4h` score `1.5831` n `102` status `ready` deltaP `12.2011` edge `0.1623` maxDD `-3.9374`
- `market_context_high->equity_1h` score `1.4741` n `105` status `ready` deltaP `12.5096` edge `0.1212` maxDD `-4.2072`
- `market_context_high->crypto_major_4h` score `1.3732` n `102` status `ready` deltaP `14.0752` edge `0.1924` maxDD `-6.7444`
- `market_context_high->index_24h` score `1.2426` n `96` status `ready` deltaP `6.0764` edge `0.1384` maxDD `-1.3621`
- `market_context_high->fx_24h` score `1.2343` n `96` status `ready` deltaP `32.9861` edge `0.0471` maxDD `-3.0343`
- `market_context_high->crypto_major_1h` score `1.1744` n `105` status `ready` deltaP `13.714` edge `0.0473` maxDD `-1.6021`
- `market_context_high->index_1h` score `0.7512` n `105` status `ready` deltaP `12.8571` edge `0.0199` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.4016` n `105` status `ready` deltaP `6.7351` edge `0.0264` maxDD `-0.6936`
- `market_context_high->crypto_alt_1h` score `0.3469` n `105` status `ready` deltaP `5.0342` edge `0.0386` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.161` n `105` status `ready` deltaP `2.278` edge `0.0009` maxDD `-0.2715`
- `market_context_high->commodity_4h` score `-0.2082` n `102` status `ready` deltaP `5.7115` edge `0.019` maxDD `-2.2874`
- `market_context_high->fx_4h` score `-0.2559` n `102` status `ready` deltaP `5.3786` edge `0.0061` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.4687` n `105` status `ready` deltaP `2.2351` edge `0.0029` maxDD `-1.5486`
- `market_context_high->unknown_1h` score `-1.4825` n `105` status `ready` deltaP `5.5917` edge `-0.185` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
