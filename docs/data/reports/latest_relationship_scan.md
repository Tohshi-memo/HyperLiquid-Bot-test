# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T11:22:17.131077+00:00`
- Price records: `545`
- Market context records: `641`
- Flow alert records: `1816`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_major_24h` score `6.5846` n `146` status `ready` deltaP `18.0614` edge `0.4617` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.8367` n `146` status `ready` deltaP `8.6692` edge `0.4334` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1205` n `146` status `ready` deltaP `8.5049` edge `0.015` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3481` n `146` status `ready` deltaP `1.542` edge `0.0029` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5047` n `146` status `ready` deltaP `1.9489` edge `0.0424` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6772` n `146` status `ready` deltaP `0.065` edge `-0.0019` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1548` n `146` status `ready` deltaP `-4.2893` edge `-0.0073` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.1902` n `146` status `ready` deltaP `5.7884` edge `-0.0063` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2977` n `146` status `ready` deltaP `-2.3558` edge `-0.0114` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.6633` n `146` status `ready` deltaP `5.9846` edge `-0.0062` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.1165` n `146` status `ready` deltaP `3.6758` edge `0.0561` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.3105` n `146` status `ready` deltaP `-0.8363` edge `-0.0347` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.4871` n `146` status `ready` deltaP `13.5057` edge `0.0733` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.9986` n `146` status `ready` deltaP `-8.7564` edge `0.008` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.3165` n `146` status `ready` deltaP `-4.9915` edge `0.107` maxDD `-13.0076`
- `market_context_high->metal_1h` score `-3.4176` n `146` status `ready` deltaP `-4.9313` edge `-0.056` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.4645` n `146` status `ready` deltaP `-4.4553` edge `-0.0438` maxDD `-10.5498`
- `market_context_high->fx_24h` score `-4.4181` n `146` status `ready` deltaP `-4.2666` edge `-0.0208` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.7528` n `146` status `ready` deltaP `-11.3991` edge `-0.0596` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.824` n `146` status `ready` deltaP `1.1277` edge `-0.2217` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
