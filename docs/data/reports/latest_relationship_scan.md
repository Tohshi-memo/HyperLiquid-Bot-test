# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T23:37:24.425958+00:00`
- Price records: `672`
- Market context records: `8563`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5919`

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

- `news_risk_high->unknown_24h` score `5076.6257` n `61` status `ready` deltaP `40.144` edge `422.8266` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.784` n `64` status `ready` deltaP `20.6555` edge `0.404` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0764` n `64` status `ready` deltaP `17.2637` edge `0.077` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.065` n `62` status `ready` deltaP `14.4276` edge `0.1716` maxDD `-5.323`
- `news_risk_high->equity_1h` score `1.7469` n `64` status `ready` deltaP `16.4016` edge `0.0839` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.1296` n `64` status `ready` deltaP `7.8125` edge `0.1703` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.7513` n `64` status `ready` deltaP `14.0244` edge `0.142` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4874` n `64` status `ready` deltaP `8.561` edge `0.0581` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3875` n `64` status `ready` deltaP `7.3634` edge `0.0518` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0986` n `64` status `ready` deltaP `5.436` edge `0.0045` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0704` n `64` status `ready` deltaP `11.9284` edge `0.0221` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0161` n `64` status `ready` deltaP `3.7706` edge `0.0086` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0365` n `64` status `ready` deltaP `1.7149` edge `0.0315` maxDD `-0.8085`
- `market_context_high->fx_4h` score `-0.0978` n `62` status `ready` deltaP `8.753` edge `0.0131` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.1215` n `64` status `ready` deltaP `3.4057` edge `0.0075` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2661` n `62` status `ready` deltaP `2.3614` edge `0.0004` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3379` n `62` status `ready` deltaP `3.7087` edge `-0.0055` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.4894` n `62` status `ready` deltaP `-2.4773` edge `0.0165` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7585` n `62` status `ready` deltaP `0.7968` edge `-0.0156` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9625` n `62` status `ready` deltaP `-2.8443` edge `-0.0118` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
