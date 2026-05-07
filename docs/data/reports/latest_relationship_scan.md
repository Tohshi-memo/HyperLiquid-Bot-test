# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T12:52:15.676997+00:00`
- Price records: `551`
- Market context records: `647`
- Flow alert records: `1835`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `795`

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

- `market_context_high->crypto_major_24h` score `7.17` n `146` status `ready` deltaP `19.0335` edge `0.504` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.034` n `146` status `ready` deltaP `8.7656` edge `0.4492` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1782` n `146` status `ready` deltaP `7.5601` edge `0.0139` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3442` n `146` status `ready` deltaP `1.6007` edge `0.003` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4052` n `146` status `ready` deltaP `2.4572` edge `0.0473` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6774` n `146` status `ready` deltaP `0.0013` edge `-0.0015` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1674` n `146` status `ready` deltaP `-4.4326` edge `-0.0074` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2709` n `146` status `ready` deltaP `5.3342` edge `-0.01` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2787` n `146` status `ready` deltaP `-2.2087` edge `-0.0108` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.7244` n `146` status `ready` deltaP `5.4757` edge `-0.0079` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.0905` n `146` status `ready` deltaP `3.8804` edge `0.0569` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2114` n `146` status `ready` deltaP `-0.0916` edge `-0.0314` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.3675` n `146` status `ready` deltaP `14.1608` edge `0.0789` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.9187` n `146` status `ready` deltaP `-8.7917` edge `0.0149` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.2006` n `146` status `ready` deltaP `-4.5481` edge `0.1137` maxDD `-13.0076`
- `market_context_high->equity_4h` score `-3.412` n `146` status `ready` deltaP `-4.2347` edge `-0.0409` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.486` n `146` status `ready` deltaP `-5.3956` edge `-0.0586` maxDD `-9.0076`
- `market_context_high->fx_24h` score `-4.4871` n `146` status `ready` deltaP `-5.1575` edge `-0.0237` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.6412` n `146` status `ready` deltaP `-11.3537` edge `-0.0506` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.8408` n `146` status `ready` deltaP `0.7079` edge `-0.2203` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
