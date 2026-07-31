# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T17:07:31.536485+00:00`
- Price records: `672`
- Market context records: `8533`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `6279.8745` n `52` status `ready` deltaP `43.523` edge `523.0748` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.7932` n `64` status `ready` deltaP `21.2652` edge `0.4007` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0483` n `64` status `ready` deltaP `16.8064` edge `0.0777` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7625` n `64` status `ready` deltaP `16.1022` edge `0.0872` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.9991` n `64` status `ready` deltaP `6.593` edge `0.1617` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.8252` n `64` status `ready` deltaP `14.7866` edge `0.1464` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.489` n `64` status `ready` deltaP `8.561` edge `0.0583` maxDD `-1.8813`
- `market_context_high->crypto_alt_4h` score `0.4505` n `49` status `ready` deltaP `7.3886` edge `0.1042` maxDD `-5.323`
- `news_risk_high->crypto_major_1h` score `0.3353` n `64` status `ready` deltaP `6.6149` edge `0.0501` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.08` n `64` status `ready` deltaP `5.1366` edge `0.0041` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0582` n `64` status `ready` deltaP `2.9345` edge `0.0355` maxDD `-0.8085`
- `news_risk_high->fx_4h` score `0.035` n `64` status `ready` deltaP `11.471` edge `0.0222` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0286` n `64` status `ready` deltaP `3.9203` edge `0.0092` maxDD `-0.5338`
- `news_risk_high->metal_1h` score `-0.0856` n `64` status `ready` deltaP `3.7051` edge `0.0085` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.3338` n `61` status `ready` deltaP `1.2688` edge `-0.001` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3706` n `61` status `ready` deltaP `2.9155` edge `-0.0044` maxDD `-2.0038`
- `market_context_high->index_1h` score `-0.8177` n `61` status `ready` deltaP `0.2062` edge `-0.0166` maxDD `-1.5667`
- `market_context_high->crypto_alt_1h` score `-0.8599` n `61` status `ready` deltaP `-3.3499` edge `0.0134` maxDD `-3.0178`
- `market_context_high->metal_1h` score `-0.9981` n `61` status `ready` deltaP `-3.3646` edge `-0.0113` maxDD `-1.6224`
- `market_context_high->commodity_4h` score `-1.0504` n `49` status `ready` deltaP `1.3346` edge `0.0079` maxDD `-5.4508`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
