# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T11:52:29.407549+00:00`
- Price records: `672`
- Market context records: `8618`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `5192.3346` n `60` status `ready` deltaP `34.2345` edge `432.5084` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.3215` n `44` status `ready` deltaP `52.9542` edge `1.2135` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.1591` n `60` status `ready` deltaP `20.7991` edge `0.4343` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.4556` n `60` status `ready` deltaP `21.1035` edge `0.083` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `1.8368` n `62` status `ready` deltaP `13.4359` edge `0.1592` maxDD `-5.323`
- `news_risk_high->equity_1h` score `1.6532` n `60` status `ready` deltaP `14.6308` edge `0.0879` maxDD `-2.4803`
- `market_context_high->fx_24h` score `1.1956` n `44` status `ready` deltaP `22.3491` edge `0.0618` maxDD `-1.2673`
- `news_risk_high->crypto_major_4h` score `1.0633` n `60` status `ready` deltaP `6.5982` edge `0.1699` maxDD `-3.5385`
- `news_risk_high->crypto_alt_1h` score `0.4374` n `60` status `ready` deltaP `8.3333` edge `0.0532` maxDD `-1.8813`
- `news_risk_high->crypto_alt_4h` score `0.3552` n `60` status `ready` deltaP `10.5327` edge `0.1145` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `0.3434` n `60` status `ready` deltaP `6.517` edge `0.0518` maxDD `-2.0972`
- `news_risk_high->fx_4h` score `0.3121` n `60` status `ready` deltaP `14.6651` edge `0.024` maxDD `-0.6604`
- `news_risk_high->fx_1h` score `0.1266` n `60` status `ready` deltaP `5.8982` edge `0.005` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0833` n `60` status `ready` deltaP `3.5388` edge `0.0347` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `0.0799` n `60` status `ready` deltaP `5.7884` edge `0.0084` maxDD `-0.5599`
- `news_risk_high->index_1h` score `-0.0232` n `60` status `ready` deltaP `2.9242` edge `0.0092` maxDD `-0.5338`
- `market_context_high->fx_4h` score `-0.1503` n `62` status `ready` deltaP `8.0522` edge `0.0134` maxDD `-1.3685`
- `market_context_high->fx_1h` score `-0.2568` n `62` status `ready` deltaP `2.5111` edge `0.0006` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3395` n `62` status `ready` deltaP `3.7087` edge `-0.0057` maxDD `-2.0038`
- `market_context_high->crypto_major_24h` score `-0.5265` n `44` status `ready` deltaP `1.9931` edge `0.3768` maxDD `-29.274`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
