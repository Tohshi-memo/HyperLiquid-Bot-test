# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T16:37:30.165893+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5901`

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

- `news_risk_high->unknown_24h` score `4447.2587` n `67` status `ready` deltaP `26.3216` edge `370.4715` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.2552` n `40` status `ready` deltaP `57.5347` edge `1.0941` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.9206` n `40` status `ready` deltaP `51.3194` edge `0.5807` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.7904` n `68` status `ready` deltaP `18.3554` edge `0.3532` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.7703` n `68` status `ready` deltaP `17.5932` edge `0.0683` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.0381` n `40` status `ready` deltaP `13.2927` edge `0.1291` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.7402` n `68` status `ready` deltaP `10.6904` edge `0.0727` maxDD `-2.916`
- `market_context_high->crypto_alt_4h` score `0.72` n `40` status `ready` deltaP `9.1159` edge `0.1221` maxDD `-4.9116`
- `market_context_high->fx_4h` score `0.6273` n `40` status `ready` deltaP `20.0` edge `0.0267` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.603` n `40` status `ready` deltaP `11.3473` edge `0.0391` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.47` n `40` status `ready` deltaP `14.2964` edge `0.0027` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.2794` n `68` status `ready` deltaP `13.9706` edge `0.0259` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1988` n `68` status `ready` deltaP `6.6894` edge `0.0285` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1474` n `68` status `ready` deltaP `7.08` edge `0.0399` maxDD `-3.1233`
- `news_risk_high->index_1h` score `-0.0349` n `68` status `ready` deltaP `3.0645` edge `0.0074` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.042` n `68` status `ready` deltaP `3.267` edge `0.0051` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1069` n `68` status `ready` deltaP `3.0645` edge `0.0062` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1104` n `68` status `ready` deltaP `3.7161` edge `0.0331` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.3607` n `40` status `ready` deltaP `1.1976` edge `0.0085` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.6739` n `68` status `ready` deltaP `2.8179` edge `-0.0272` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
