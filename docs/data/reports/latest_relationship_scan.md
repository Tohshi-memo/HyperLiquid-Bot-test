# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T11:52:10.573657+00:00`
- Price records: `547`
- Market context records: `643`
- Flow alert records: `1823`
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

- `market_context_high->crypto_major_24h` score `6.7931` n `146` status `ready` deltaP `18.3883` edge `0.4769` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.9351` n `146` status `ready` deltaP `8.8495` edge `0.4404` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1335` n `146` status `ready` deltaP `8.3141` edge `0.0146` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3366` n `146` status `ready` deltaP `1.7473` edge `0.003` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4658` n `146` status `ready` deltaP `2.1196` edge `0.0445` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6735` n `146` status `ready` deltaP `0.1055` edge `-0.0017` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1708` n `146` status `ready` deltaP `-4.4602` edge `-0.0075` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2108` n `146` status `ready` deltaP `5.6359` edge `-0.007` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2913` n `146` status `ready` deltaP `-2.3064` edge `-0.0112` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.6829` n `146` status `ready` deltaP `5.8137` edge `-0.0067` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.0767` n `146` status `ready` deltaP `3.9329` edge `0.0577` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2761` n `146` status `ready` deltaP `-0.5861` edge `-0.0335` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.4347` n `146` status `ready` deltaP `13.7257` edge `0.0762` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.9457` n `146` status `ready` deltaP `-8.6191` edge `0.0115` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.2913` n `146` status `ready` deltaP `-4.8426` edge `0.1081` maxDD `-13.0076`
- `market_context_high->equity_4h` score `-3.4254` n `146` status `ready` deltaP `-4.1915` edge `-0.0423` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4361` n `146` status `ready` deltaP `-5.0872` edge `-0.0565` maxDD `-9.0076`
- `market_context_high->fx_24h` score `-4.4431` n `146` status `ready` deltaP `-4.5662` edge `-0.022` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.6797` n `146` status `ready` deltaP `-11.2347` edge `-0.0546` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.8317` n `146` status `ready` deltaP `0.9867` edge `-0.2214` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
