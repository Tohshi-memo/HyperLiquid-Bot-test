# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T21:07:31.971511+00:00`
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

- `news_risk_high->unknown_24h` score `4816.3312` n `63` status `ready` deltaP `24.0327` edge `401.2428` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `16.1484` n `40` status `ready` deltaP `54.4097` edge `1.0227` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.0838` n `40` status `ready` deltaP `51.3194` edge `0.5943` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.4244` n `63` status `ready` deltaP `15.2947` edge `0.3431` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.4663` n `63` status `ready` deltaP `14.2277` edge `0.0654` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.0399` n `40` status `ready` deltaP `13.5976` edge `0.1273` maxDD `-2.7703`
- `market_context_high->crypto_alt_4h` score `0.742` n `40` status `ready` deltaP `8.3537` edge `0.13` maxDD `-4.9116`
- `market_context_high->fx_4h` score `0.6496` n `40` status `ready` deltaP `20.4573` edge `0.0265` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.6412` n `40` status `ready` deltaP `11.9461` edge `0.04` maxDD `-1.3282`
- `news_risk_high->equity_1h` score `0.4721` n `63` status `ready` deltaP `7.7132` edge `0.0702` maxDD `-2.916`
- `market_context_high->fx_1h` score `0.4279` n `40` status `ready` deltaP `13.5479` edge `0.0023` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.1216` n `63` status `ready` deltaP `12.1636` edge `0.0248` maxDD `-0.6604`
- `news_risk_high->fx_1h` score `0.049` n `63` status `ready` deltaP `5.0162` edge `0.0051` maxDD `-0.2475`
- `news_risk_high->crypto_alt_1h` score `0.0065` n `63` status `ready` deltaP `5.5556` edge `0.032` maxDD `-3.1233`
- `news_risk_high->index_1h` score `-0.0291` n `63` status `ready` deltaP `3.1604` edge `0.0075` maxDD `-0.5845`
- `news_risk_high->metal_4h` score `-0.0999` n `63` status `ready` deltaP `3.269` edge `0.013` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.2608` n `63` status `ready` deltaP `0.4349` edge `0.004` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.3334` n `63` status `ready` deltaP `1.3925` edge `0.02` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.4409` n `40` status `ready` deltaP `0.0` edge `0.0062` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.5666` n `63` status `ready` deltaP `4.3271` edge `-0.0263` maxDD `-2.6816`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
