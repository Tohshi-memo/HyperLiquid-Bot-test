# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T21:52:20.399698+00:00`
- Price records: `587`
- Market context records: `688`
- Flow alert records: `1947`
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

- `market_context_high->crypto_major_24h` score `9.8791` n `146` status `ready` deltaP `24.3674` edge `0.6942` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5812` n `146` status `ready` deltaP `8.4801` edge `0.4967` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1821` n `147` status `ready` deltaP `7.7097` edge `0.0124` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2649` n `149` status `ready` deltaP `3.1412` edge `0.0029` maxDD `-0.291`
- `market_context_high->index_1h` score `-0.5663` n `149` status `ready` deltaP `1.1626` edge `0.005` maxDD `-2.8282`
- `market_context_high->commodity_1h` score `-0.5707` n `149` status `ready` deltaP `1.843` edge `0.0376` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-1.1211` n `149` status `ready` deltaP `-1.4084` edge `-0.003` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.2395` n `149` status `ready` deltaP `-4.5081` edge `-0.0129` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3671` n `149` status `ready` deltaP `4.5966` edge `-0.0131` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.5246` n `147` status `ready` deltaP `3.603` edge `0.0012` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.662` n `149` status `ready` deltaP `5.7306` edge `-0.0044` maxDD `-11.4508`
- `market_context_high->crypto_major_4h` score `-1.7474` n `147` status `ready` deltaP `15.912` edge `0.1189` maxDD `-22.648`
- `market_context_high->index_24h` score `-1.7481` n `146` status `ready` deltaP `-5.2896` edge `0.0891` maxDD `-5.9609`
- `market_context_high->crypto_alt_4h` score `-1.8742` n `147` status `ready` deltaP `4.8584` edge `0.0684` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.5246` n `147` status `ready` deltaP `-0.8062` edge `0.0102` maxDD `-10.5498`
- `market_context_high->equity_24h` score `-3.146` n `146` status `ready` deltaP `-7.409` edge `0.0477` maxDD `-10.5047`
- `market_context_high->metal_1h` score `-3.2746` n `149` status `ready` deltaP `-4.5828` edge `-0.0464` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.8671` n `147` status `ready` deltaP `-6.3996` edge `0.0705` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.4206` n `147` status `ready` deltaP `2.4947` edge `-0.1972` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.8846` n `146` status `ready` deltaP `-10.0419` edge `-0.0421` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
