# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T04:52:21.018022+00:00`
- Price records: `615`
- Market context records: `720`
- Flow alert records: `2034`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `11.5248` n `146` status `ready` deltaP `28.0043` edge `0.8071` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.3304` n `146` status `ready` deltaP `7.9856` edge `0.4791` maxDD `-0.0508`
- `market_context_high->fx_1h` score `-0.2715` n `151` status `ready` deltaP `3.0886` edge `0.0024` maxDD `-0.291`
- `market_context_high->fx_4h` score `-0.2984` n `149` status `ready` deltaP `5.9534` edge `0.0092` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.3881` n `151` status `ready` deltaP `3.0462` edge `0.0448` maxDD `-3.7959`
- `market_context_high->index_24h` score `-0.5627` n `146` status `ready` deltaP `-1.0919` edge `0.1599` maxDD `-5.9609`
- `market_context_high->index_1h` score `-0.6393` n `151` status `ready` deltaP `0.1331` edge `0.0025` maxDD `-2.8282`
- `market_context_high->crypto_major_4h` score `-1.0119` n `149` status `ready` deltaP `17.3813` edge `0.125` maxDD `-22.648`
- `market_context_high->equity_1h` score `-1.1344` n `151` status `ready` deltaP `-1.3496` edge `-0.0045` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.2172` n `151` status `ready` deltaP `-4.2001` edge `-0.0131` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.4143` n `151` status `ready` deltaP `4.3214` edge `-0.0152` maxDD `-8.1842`
- `market_context_high->equity_24h` score `-1.4829` n `146` status `ready` deltaP `-2.9099` edge `0.1563` maxDD `-10.5047`
- `market_context_high->crypto_major_1h` score `-1.6664` n `151` status `ready` deltaP `5.5701` edge `-0.0037` maxDD `-11.4508`
- `market_context_high->index_4h` score `-1.824` n `149` status `ready` deltaP `1.4055` edge `-0.0091` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-1.9711` n `149` status `ready` deltaP `3.5282` edge `0.0692` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.7697` n `149` status `ready` deltaP `-1.6198` edge `-0.0048` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4511` n `151` status `ready` deltaP `-5.6351` edge `-0.0541` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6476` n `149` status `ready` deltaP `-5.606` edge `0.0835` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.101` n `149` status `ready` deltaP `3.9854` edge `-0.1805` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.1668` n `146` status `ready` deltaP `-13.3688` edge `-0.0561` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
