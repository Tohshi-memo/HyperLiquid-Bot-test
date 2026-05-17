# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T10:37:14.144600+00:00`
- Price records: `672`
- Market context records: `1004`
- Flow alert records: `4797`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8634`

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

- `market_context_high->crypto_major_24h` score `13.0096` n `208` status `ready` deltaP `31.9178` edge `0.9302` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.1746` n `208` status `ready` deltaP `10.9174` edge `0.3985` maxDD `-9.5387`
- `market_context_high->fx_1h` score `-0.5227` n `208` status `ready` deltaP `2.1764` edge `0.0` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.5835` n `208` status `ready` deltaP `2.2138` edge `0.0174` maxDD `-3.7959`
- `market_context_high->index_24h` score `-0.5838` n `208` status `ready` deltaP `3.5904` edge `0.1244` maxDD `-5.7586`
- `market_context_high->equity_1h` score `-0.6778` n `208` status `ready` deltaP `0.6276` edge `0.0162` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.6968` n `208` status `ready` deltaP `3.2675` edge `0.0055` maxDD `-2.8282`
- `market_context_high->fx_4h` score `-0.7352` n `208` status `ready` deltaP `0.6575` edge `0.001` maxDD `-1.6381`
- `market_context_high->equity_24h` score `-1.1596` n `208` status `ready` deltaP `4.5519` edge `0.1335` maxDD `-10.5047`
- `market_context_high->crypto_major_1h` score `-1.208` n `208` status `ready` deltaP `5.1791` edge `-0.0171` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.3649` n `208` status `ready` deltaP `-1.0536` edge `-0.024` maxDD `-8.1842`
- `market_context_high->equity_4h` score `-1.5059` n `208` status `ready` deltaP `1.7726` edge `0.0779` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.756` n `208` status `ready` deltaP `-1.7945` edge `0.0179` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.869` n `208` status `ready` deltaP `-0.7629` edge `-0.0386` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-2.8773` n `208` status `ready` deltaP `7.2334` edge `0.0826` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.203` n `208` status `ready` deltaP `-1.6133` edge `0.0606` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.276` n `208` status `ready` deltaP `-1.8135` edge `0.0169` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.5073` n `208` status `ready` deltaP `-1.5972` edge `-0.0226` maxDD `-19.9793`
- `market_context_high->metal_4h` score `-4.6346` n `208` status `ready` deltaP `-4.9933` edge `-0.1652` maxDD `-24.9891`
- `market_context_high->commodity_24h` score `-8.218` n `208` status `ready` deltaP `2.6245` edge `0.3937` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
