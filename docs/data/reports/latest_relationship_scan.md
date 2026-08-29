# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T22:37:24.603924+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11432`

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

- `risk_on_high->crypto_alt_4h` score `8.6269` n `45` status `ready` deltaP `31.7649` edge `0.5253` maxDD `-0.4529`
- `risk_on_and_context->crypto_alt_4h` score `8.6269` n `45` status `ready` deltaP `31.7649` edge `0.5253` maxDD `-0.4529`
- `news_risk_high->crypto_alt_24h` score `7.8658` n `46` status `ready` deltaP `22.5166` edge `1.1959` maxDD `-22.3391`
- `risk_on_high->crypto_major_4h` score `6.9326` n `45` status `ready` deltaP `37.7574` edge `0.3536` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `6.9326` n `45` status `ready` deltaP `37.7574` edge `0.3536` maxDD `-1.208`
- `news_risk_high->unknown_4h` score `6.9238` n `55` status `ready` deltaP `1.2888` edge `0.6274` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6838` n `104` status `ready` deltaP `34.415` edge `0.2628` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `3.1751` n `55` status `ready` deltaP `-2.7463` edge `0.3186` maxDD `-0.8558`
- `risk_on_high->metal_4h` score `3.1028` n `45` status `ready` deltaP `34.6443` edge `0.0362` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.1028` n `45` status `ready` deltaP `34.6443` edge `0.0362` maxDD `-0.0208`
- `risk_on_high->equity_4h` score `2.104` n `45` status `ready` deltaP `16.6904` edge `0.089` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.104` n `45` status `ready` deltaP `16.6904` edge `0.089` maxDD `-0.3281`
- `market_context_high->unknown_4h` score `1.7422` n `147` status `ready` deltaP `17.9245` edge `0.0727` maxDD `-1.0945`
- `market_context_high->unknown_1h` score `1.4727` n `159` status `ready` deltaP `8.2543` edge `0.1158` maxDD `-1.5148`
- `risk_on_high->metal_1h` score `1.3539` n `57` status `ready` deltaP `18.9358` edge `0.008` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.3539` n `57` status `ready` deltaP `18.9358` edge `0.008` maxDD `-0.0463`
- `risk_on_high->index_4h` score `1.2585` n `45` status `ready` deltaP `19.065` edge `0.0087` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.2585` n `45` status `ready` deltaP `19.065` edge `0.0087` maxDD `-0.1405`
- `news_risk_high->fx_4h` score `1.2421` n `55` status `ready` deltaP `29.7727` edge `0.0157` maxDD `-0.3953`
- `risk_on_high->unknown_1h` score `0.8692` n `57` status `ready` deltaP `0.4754` edge `0.1132` maxDD `-1.5148`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
