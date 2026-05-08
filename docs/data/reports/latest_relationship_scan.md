# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T09:58:44.829658+00:00`
- Price records: `635`
- Market context records: `743`
- Flow alert records: `2098`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1117`

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

- `market_context_high->crypto_major_24h` score `12.7473` n `146` status `ready` deltaP `30.3708` edge `0.8932` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6023` n `146` status `ready` deltaP `7.6639` edge `0.5039` maxDD `-0.0508`
- `market_context_high->index_24h` score `0.1801` n `146` status `ready` deltaP `1.6374` edge `0.2036` maxDD `-5.9609`
- `market_context_high->fx_1h` score `-0.344` n `161` status `ready` deltaP `3.9654` edge `0.0027` maxDD `-0.291`
- `market_context_high->fx_4h` score `-0.4279` n `156` status `ready` deltaP `6.2821` edge `0.0096` maxDD `-1.6381`
- `market_context_high->equity_24h` score `-0.4893` n `146` status `ready` deltaP `0.0154` edge `0.2196` maxDD `-10.5047`
- `market_context_high->commodity_1h` score `-0.5863` n `161` status `ready` deltaP `1.5741` edge `0.0381` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.8232` n `161` status `ready` deltaP `1.8079` edge `0.0047` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.0058` n `161` status `ready` deltaP `-0.5676` edge `0.001` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.0694` n `161` status `ready` deltaP `5.6245` edge `-0.0023` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.4026` n `161` status `ready` deltaP `4.5584` edge `-0.0158` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.5406` n `161` status `ready` deltaP `-4.4718` edge `-0.0214` maxDD `-3.5069`
- `market_context_high->crypto_major_4h` score `-1.5537` n `156` status `ready` deltaP `17.5241` edge `0.1243` maxDD `-22.648`
- `market_context_high->index_4h` score `-1.7558` n `156` status `ready` deltaP `1.8074` edge `-0.0061` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.1625` n `156` status `ready` deltaP `2.4999` edge `0.0601` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.5556` n `156` status `ready` deltaP `-1.1195` edge `0.0097` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.1296` n `161` status `ready` deltaP `-3.9403` edge `-0.0386` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6707` n `156` status `ready` deltaP `-5.3846` edge `0.0801` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.7457` n `156` status `ready` deltaP `5.1416` edge `-0.1586` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.376` n `146` status `ready` deltaP `-15.532` edge `-0.0685` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
