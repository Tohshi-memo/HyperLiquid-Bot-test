# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T13:32:18.629900+00:00`
- Price records: `456`
- Market context records: `546`
- Flow alert records: `1542`
- Minimum samples: `30`
- Pattern count: `96`

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

- `market_context_high->crypto_alt_24h` score `4.9206` n `135` status `ready` deltaP `7.8228` edge `0.3627` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.059` n `135` status `ready` deltaP `10.1719` edge `0.2205` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0655` n `146` status `ready` deltaP `10.9715` edge `0.0224` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.315` n `146` status `ready` deltaP `1.9386` edge `0.0045` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5742` n `146` status `ready` deltaP `1.7398` edge `0.038` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5849` n `146` status `ready` deltaP `1.5839` edge `-0.0002` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-0.7293` n `146` status `ready` deltaP `-2.6761` edge `0.0174` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.1716` n `146` status `ready` deltaP `-1.0947` edge `-0.0093` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.482` n `146` status `ready` deltaP `3.9854` edge `-0.0186` maxDD `-8.1842`
- `market_context_high->index_24h` score `-2.062` n `135` status `ready` deltaP `-6.3481` edge `0.07` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-2.2296` n `146` status `ready` deltaP `2.7306` edge `-0.0317` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.3095` n `146` status `ready` deltaP `-0.2985` edge `-0.0382` maxDD `-6.5149`
- `market_context_high->unknown_4h` score `-2.9369` n `146` status `ready` deltaP `0.9713` edge `-0.0634` maxDD `-8.3588`
- `market_context_high->crypto_alt_4h` score `-3.0002` n `146` status `ready` deltaP `0.0996` edge `0.0063` maxDD `-15.2248`
- `market_context_high->commodity_4h` score `-3.2111` n `146` status `ready` deltaP `-4.5149` edge `0.1126` maxDD `-13.0076`
- `market_context_high->metal_1h` score `-3.307` n `146` status `ready` deltaP `-5.0037` edge `-0.0463` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.5342` n `146` status `ready` deltaP `-4.4269` edge `-0.0498` maxDD `-10.5498`
- `market_context_high->equity_24h` score `-3.9865` n `135` status `ready` deltaP `-10.7449` edge `-0.0001` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.0376` n `135` status `ready` deltaP `-5.2017` edge `-0.0356` maxDD `-15.4555`
- `market_context_high->crypto_major_4h` score `-4.0718` n `146` status `ready` deltaP `7.8269` edge `-0.0209` maxDD `-22.648`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
