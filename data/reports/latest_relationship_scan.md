# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T23:22:27.698277+00:00`
- Price records: `672`
- Market context records: `8562`
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

- `news_risk_high->unknown_24h` score `5076.6984` n `61` status `ready` deltaP `40.3176` edge `422.8315` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.755` n `64` status `ready` deltaP `20.503` edge `0.4026` maxDD `-3.4427`
- `market_context_high->crypto_alt_4h` score `2.0662` n `62` status `ready` deltaP `14.4276` edge `0.1717` maxDD `-5.323`
- `news_risk_high->index_4h` score `2.0607` n `64` status `ready` deltaP `17.1113` edge `0.0767` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7337` n `64` status `ready` deltaP `16.2519` edge `0.0838` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.1193` n `64` status `ready` deltaP `7.6601` edge `0.17` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.752` n `64` status `ready` deltaP `14.0244` edge `0.1421` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.489` n `64` status `ready` deltaP `8.561` edge `0.0583` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3781` n `64` status `ready` deltaP `7.2137` edge `0.0516` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0909` n `64` status `ready` deltaP `5.2863` edge `0.0045` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0692` n `64` status `ready` deltaP `11.9284` edge `0.022` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0075` n `64` status `ready` deltaP `3.6209` edge `0.0085` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0365` n `64` status `ready` deltaP `1.7149` edge `0.0315` maxDD `-0.8085`
- `market_context_high->fx_4h` score `-0.099` n `62` status `ready` deltaP `8.753` edge `0.013` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.1227` n `64` status `ready` deltaP `3.4057` edge `0.0074` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2739` n `62` status `ready` deltaP `2.2117` edge `0.0004` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3286` n `62` status `ready` deltaP `3.8584` edge `-0.0053` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.4878` n `62` status `ready` deltaP `-2.4773` edge `0.0167` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7716` n `62` status `ready` deltaP `0.6471` edge `-0.0157` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9637` n `62` status `ready` deltaP `-2.8443` edge `-0.0119` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
