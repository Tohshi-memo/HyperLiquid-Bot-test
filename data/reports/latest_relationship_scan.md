# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T23:07:16.143715+00:00`
- Price records: `496`
- Market context records: `589`
- Flow alert records: `1666`
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

- `market_context_high->crypto_alt_24h` score `4.6356` n `146` status `ready` deltaP `7.0651` edge `0.344` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.3449` n `146` status `ready` deltaP `10.2808` edge `0.2436` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.1034` n `146` status `ready` deltaP `12.0007` edge `0.0204` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2842` n `146` status `ready` deltaP `2.546` edge `0.0044` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6007` n `146` status `ready` deltaP `1.6337` edge `0.0365` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6367` n `146` status `ready` deltaP `0.9179` edge `-0.0024` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1819` n `146` status `ready` deltaP `-4.3434` edge `-0.0092` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.227` n `146` status `ready` deltaP `5.2373` edge `-0.0057` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2297` n `146` status `ready` deltaP `-1.746` edge `-0.0098` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.8546` n `146` status `ready` deltaP `4.5077` edge `-0.0123` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.1462` n `146` status `ready` deltaP `2.9595` edge `0.0584` maxDD `-15.2248`
- `market_context_high->index_24h` score `-2.2709` n `146` status `ready` deltaP `-6.365` edge `0.0527` maxDD `-5.9609`
- `market_context_high->index_4h` score `-2.2758` n `146` status `ready` deltaP `-0.0576` edge `-0.037` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.8962` n `146` status `ready` deltaP `11.9178` edge `0.0498` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.3144` n `146` status `ready` deltaP `-4.7806` edge `-0.0484` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.3636` n `146` status `ready` deltaP `-3.8391` edge `-0.0395` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.7151` n `146` status `ready` deltaP `-6.7198` edge `0.0853` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-4.29` n `146` status `ready` deltaP `-10.2636` edge `-0.0286` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.4231` n `146` status `ready` deltaP `-4.0612` edge `-0.0228` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-5.0905` n `146` status `ready` deltaP `0.7819` edge `-0.2416` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
